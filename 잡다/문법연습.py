students = [("김철수", 85, 90), ("이영희", 90, 85), ("박민수", 75, 95), ("정다운", 95, 75)]
students.sort(key=lambda x : x[1], reverse=True)

students.sort(key=lambda x : x[2], reverse=False)

students.sort(key=lambda x : (x[1]+x[2])//2, reverse=True)

print(students)

orders = [
    ("A123", 150000, 4.5, "2024-01-15"),
    ("B435", 89000, 4.8, "2024-01-20"),
    ("C678", 230000, 3.9, "2024-01-18"),
    ("D901", 95000, 4.8, "2024-01-15"),
    ("E234", 178000, 4.2, "2024-01-20")
]

orders.sort(key=lambda x : (-x[2], -x[1]))