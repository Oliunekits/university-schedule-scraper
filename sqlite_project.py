import sqlite3

# --- функції ---
def create_table():
    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        group_name TEXT
    )
    """)
    conn.commit()

def add_student(name, age, group_name):
    c.execute("INSERT INTO students (name, age, group_name) VALUES (?, ?, ?)", (name, age, group_name))
    conn.commit()

def show_students():
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    for row in rows:
        print(row)

def find_by_group(group):
    c.execute("SELECT * FROM students WHERE group_name = ?", (group,))
    rows = c.fetchall()
    for row in rows:
        print(row)

def update_student(student_id, new_name, new_age, new_group):
    c.execute("UPDATE students SET name=?, age=?, group_name=? WHERE id=?", (new_name, new_age, new_group, student_id))
    conn.commit()

def delete_student(student_id):
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

# --- головна програма ---
conn = sqlite3.connect("students.db")
c = conn.cursor()
create_table()

while True:
    print("\n=== Меню ===")
    print("1. Додати студента")
    print("2. Показати всіх студентів")
    print("3. Знайти студента за групою")
    print("4. Оновити студента")
    print("5. Видалити студента")
    print("6. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Ім'я: ")
        age = int(input("Вік: "))
        group = input("Група: ")
        add_student(name, age, group)

    elif choice == "2":
        show_students()

    elif choice == "3":
        group = input("Введіть групу: ")
        find_by_group(group)

    elif choice == "4":
        student_id = int(input("ID студента для оновлення: "))
        new_name = input("Нове ім'я: ")
        new_age = int(input("Новий вік: "))
        new_group = input("Нова група: ")
        update_student(student_id, new_name, new_age, new_group)

    elif choice == "5":
        student_id = int(input("ID студента для видалення: "))
        delete_student(student_id)

    elif choice == "6":
        print("Вихід...")
        break

    else:
        print("Невірний вибір! Спробуйте ще раз.")

conn.close()