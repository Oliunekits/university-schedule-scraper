import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import quote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

group = input("Введіть назву групи (наприклад, КІ-106): ")
group_encoded = quote(group.upper())

url = f"https://student.lpnu.ua/students_schedule?studygroup_abbrname={group_encoded}&semestr=1&semestrduration=1"
print(f"Завантажую розклад з: {url}")

response = requests.get(url, verify=False)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

lessons = soup.find_all("div", class_="group_content")

if not lessons:
    print("❌ Пари не знайдені")
else:
    current_day = None
    for lesson in lessons:
        parent = lesson.find_parent("div")
        parent_classes = parent.get("class", [])


        if "week_color" not in parent_classes:
            continue

        day_header = lesson.find_previous("span", class_="view-grouping-header")
        if day_header:
            day_name = day_header.text.strip()
            if day_name != current_day:
                current_day = day_name


                print(f"\n📅 {current_day}")

        text = lesson.get_text(" ", strip=True)
        print("   🔹", text)
