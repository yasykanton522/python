import numpy as np


def main():
    rng = np.random.default_rng(42)

    students = np.array([f"Студент_{i}" for i in range(1, 23)])
    subjects = np.array(["Математика", "Физика", "Программирование", "Алгоритмы", "Английский"])

    grades = rng.integers(0, 11, size=(len(students), len(subjects)))

    student_avg = np.round(np.mean(grades, axis=1), 2)

    best_students = students[student_avg == np.max(student_avg)]
    worst_students = students[student_avg == np.min(student_avg)]

    subject_avg = np.round(np.mean(grades, axis=0), 2)

    easiest_subject = subjects[np.argmax(subject_avg)]
    hardest_subject = subjects[np.argmin(subject_avg)]

    fund = 10000.0
    eligible = student_avg >= 4.0
    scholarships = np.zeros(len(students))
    if np.any(eligible):
        scholarships[eligible] = np.round(fund / np.sum(eligible), 2)

    for name, avg, money in zip(students, student_avg, scholarships):
        print(f"{name}: ср. балл = {avg}, стипендия = {money}")

    print("\nЛучшие:", best_students.tolist(), "| Худшие:", worst_students.tolist())
    for subj, avg in zip(subjects, subject_avg):
        print(f"{subj}: ср. балл = {avg}")
    print("\nСамый простой предмет:", easiest_subject)
    print("Самый сложный предмет:", hardest_subject)


if __name__ == "__main__":
    main()