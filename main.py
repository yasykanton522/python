
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px


def load_data(file_path: Path) -> pd.DataFrame:
    if file_path.exists():
        return pd.read_csv(file_path)

    rng = np.random.default_rng(42)
    n = 150
    df = pd.DataFrame({
        "product_name": [f"Товар_{i}" for i in range(n)],
        "category": rng.choice(["Электроника", "Одежда", "Дом", "Спорт"], size=n),
        "region": rng.choice(["Минск", "Брест", "Гомель", "Гродно"], size=n),
        "price": np.round(rng.uniform(15.0, 400.0, size=n), 2),
        "rating": np.round(rng.uniform(1.0, 5.0, size=n), 1),
        "quantity": rng.integers(1, 100, size=n),
    })
    df.loc[[2, 14, 37, 88], "price"] = np.nan
    df.loc[[5, 21, 63], "rating"] = np.nan
    df.loc[[9, 44, 102], "category"] = np.nan
    return pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True)


def main() -> None:
    df = load_data(Path("data.csv"))

    print(df.info())
    print(df.describe(include="all"))
    print(df.isna().sum())

    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    for col in cat_cols:
        mode_val = df[col].mode()
        if not mode_val.empty:
            df[col] = df[col].fillna(mode_val.iloc[0])

    df = df.drop_duplicates().reset_index(drop=True)
    print(df[num_cols].corr(numeric_only=True).round(3))

    col_price = "price" if "price" in df.columns else num_cols[0]
    col_qty = "quantity" if "quantity" in df.columns else num_cols[min(1, len(num_cols) - 1)]
    col_rating = "rating" if "rating" in df.columns else num_cols[-1]
    main_cat = "category" if "category" in df.columns else cat_cols[0]
    sub_cat = "region" if "region" in df.columns else (cat_cols[1] if len(cat_cols) > 1 else main_cat)
    item_col = "product_name" if "product_name" in df.columns else df.columns[0]

    df["total_amount"] = np.round(df[col_price] * df[col_qty], 2)
    target = "total_amount"

    print(df.groupby(main_cat, observed=False)[target].agg(["count", "mean", "median"]).round(2))

    pivot = df.pivot_table(
        index=main_cat,
        columns=sub_cat,
        values=target,
        aggfunc="mean",
        fill_value=0,
        observed=False,
    ).round(2)
    print(pivot)

    top5 = (
        df[df[target] >= df[target].median()]
        .sort_values(by=target, ascending=False)
        .head(5)[[item_col, main_cat, target]]
    )
    print(top5.to_string(index=False))

    tpl = "plotly_white"
    bar_df = pivot.mean(axis=1).reset_index(name="mean_value")

    px.bar(
        bar_df,
        x=main_cat,
        y="mean_value",
        text_auto=".2f",
        title=f"Среднее значение ({target}) по категориям",
        labels={main_cat: "Категория", "mean_value": f"Среднее ({target})"},
        template=tpl,
    ).show()

    px.box(
        df,
        x=main_cat,
        y=target,
        title=f"Распределение {target} по категориям",
        labels={main_cat: "Категория", target: target},
        template=tpl,
    ).show()

    px.scatter(
        df,
        x=col_price,
        y=col_rating,
        color=main_cat,
        trendline="ols",
        title=f"Связь {col_rating} и {col_price} с линией тренда",
        labels={col_price: col_price, col_rating: col_rating, main_cat: "Категория"},
        template=tpl,
    ).show()

    px.imshow(
        pivot,
        text_auto=".2f",
        aspect="auto",
        title=f"Тепловая карта сводной таблицы ({target})",
        labels={"x": sub_cat, "y": main_cat, "color": target},
        template=tpl,
    ).show()


if __name__ == "__main__":
    main()

