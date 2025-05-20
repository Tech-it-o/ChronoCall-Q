from datetime import datetime, timedelta
import random
import json

# load title template
with open('Component/Title.json', 'r', encoding='utf-8') as f:
    data_title = json.load(f)

with open('Component_datetext/TimeDic_mostly.json', 'r', encoding='utf-8') as f:
    data_time = json.load(f)

# text template

with open('action_datetext/add_event.json', 'r', encoding='utf-8') as f:
    data_add = json.load(f)

with open('action_datetext/delete_event.json', 'r', encoding='utf-8') as f:
    data_delete = json.load(f)

with open('action_datetext/update_event.json', 'r', encoding='utf-8') as f:
    data_update = json.load(f)

with open('action_datetext/view_event.json', 'r', encoding='utf-8') as f:
    data_view = json.load(f)

thai_weekdays = {
    "จันทร์": 0,
    "อังคาร": 1,
    "พุธ": 2,
    "พฤหัส": 3,
    "ศุกร์": 4,
    "เสาร์": 5,
    "อาทิตย์": 6
}

def resolve_date_only(input_date_str, keyword):
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

    if keyword == "พรุ่งนี้":
        target_date = input_date + timedelta(days=1)
    elif keyword == "มะรืน":
        target_date = input_date + timedelta(days=2)
    elif "หน้า" in keyword:
        for day_name in thai_weekdays:
            if day_name in keyword:
                target_weekday = thai_weekdays[day_name]
                current_weekday = input_date.weekday()
                delta_days = (target_weekday - current_weekday + 7) % 7
                if delta_days == 0:
                    delta_days = 7
                target_date = input_date + timedelta(days=delta_days)
                break
    else:
        raise ValueError("Unknown keyword")

    return target_date.strftime("%Y-%m-%d")

def list_dates_only(year=None):
    if year is None:
        year = datetime.today().year
    
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    current_date = start_date
    result = []

    while current_date <= end_date:
        result.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
    return result

for date in list_dates_only(2025):
    print(date)
    break



def add_event_data(date):
    random_day_class = random.choice(["พรุ่งนี้", "มะรืน", "จันทร์หน้า", "อังคารหน้า", "พุธหน้า", "พฤหัสหน้า", "ศุกร์หน้า", "เสาร์หน้า", "อาทิตย์หน้า"])
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_add)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "input": text,
        "output": {
        "action": "add_event_date",
        "date": answer_date,
        "time": actual_time,
        "title": title
        }
    }

# print(resolve_date_only("2025-05-20", "พรุ่งนี้"))      # 2025-05-21
# print(resolve_date_only("2025-05-20", "มะรืน"))        # 2025-05-22
# print(resolve_date_only("2025-05-20", "จันทร์หน้า"))  # 2025-05-26