import json
import re
from collections import Counter
from pathlib import Path
from bs4 import BeautifulSoup
import requests

HTML = """
<div class="event">
  <div class="title">Рок-концерт</div>
  <div class="date">25.11.2026 19:00</div>
  <div class="place">Дворец спорта</div>
  <div class="price">40 руб.</div>
  <div class="age">16+</div>
</div>
<div class="event">
  <div class="title">Симфонический вечер</div>
  <div class="date">26.11.2026 18:30</div>
  <div class="place">Филармония</div>
  <div class="price">60 руб.</div>
  <div class="age">6+</div>
</div>
<div class="event">
  <div class="title">Джаз у сцены</div>
  <div class="date">27.11.2026 20:00</div>
  <div class="place">Дворец спорта</div>
  <div class="price">25 руб.</div>
  <div class="age">18+</div>
</div>
<div class="event">
  <div class="title">Стендап шоу</div>
  <div class="date">28.11.2026 21:00</div>
  <div class="place">Клуб 10</div>
  <div class="price">35 руб.</div>
  <div class="age">18+</div>
</div>
"""


def get_html(url: str) -> str:
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        return r.text
    except requests.RequestException:
        return HTML


def parse_price(text: str) -> float:
    m = re.search(r"\d+(?:[.,]\d+)?", text)
    return float(m.group(0).replace(",", ".")) if m else 0.0


def main():
    html = get_html("https://example.com/afisha")
    soup = BeautifulSoup(html, "html.parser")

    events = []
    for item in soup.select(".event"):
        events.append({
            "title": item.select_one(".title").get_text(strip=True),
            "date": item.select_one(".date").get_text(strip=True),
            "place": item.select_one(".place").get_text(strip=True),
            "price": parse_price(item.select_one(".price").get_text(strip=True)),
            "age": item.select_one(".age").get_text(strip=True),
        })

    prices = [e["price"] for e in events]
    top_place, top_count = Counter(e["place"] for e in events).most_common(1)[0]
    cheapest = min(events, key=lambda e: e["price"])
    expensive = max(events, key=lambda e: e["price"])

    result = {
        "events": events,
        "min_price": min(prices),
        "max_price": max(prices),
        "avg_price": round(sum(prices) / len(prices), 2),
        "top_place": top_place,
        "top_place_count": top_count,
        "cheapest": cheapest,
        "expensive": expensive,
    }

    out_file = Path(__file__).resolve().parent / "result.json"
    out_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Мин. цена:", result["min_price"])
    print("Макс. цена:", result["max_price"])
    print("Средняя цена:", result["avg_price"])
    print(f"Больше всего событий: {top_place} ({top_count})")
    print("Самый дешёвый:", cheapest["title"], cheapest["price"])
    print("Самый дорогой:", expensive["title"], expensive["price"])
    print("Сохранено в:", out_file)


if __name__ == "__main__":
    main()