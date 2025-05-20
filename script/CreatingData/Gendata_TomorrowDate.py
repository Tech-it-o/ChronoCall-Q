from datetime import datetime, timedelta
import random
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

# load title template
with open(os.path.join(base_dir, 'Component_datetext', 'Title.json'), 'r', encoding='utf-8') as f:
    data_title = json.load(f)

with open(os.path.join(base_dir, 'Component_datetext', 'TimeDic_mostly.json'), 'r', encoding='utf-8') as f:
    data_time = json.load(f)

# text template

with open(os.path.join(base_dir, 'action_datetext', 'add_event.json'), 'r', encoding='utf-8') as f:
    data_add = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'delete_event.json'), 'r', encoding='utf-8') as f:
    data_delete = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'update_event.json'), 'r', encoding='utf-8') as f:
    data_update = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'view_event.json'), 'r', encoding='utf-8') as f:
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

def delete_event_data(date):
    random_day_class = random.choice(["พรุ่งนี้", "มะรืน", "จันทร์หน้า", "อังคารหน้า", "พุธหน้า", "พฤหัสหน้า", "ศุกร์หน้า", "เสาร์หน้า", "อาทิตย์หน้า"])
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_delete)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "input": text,
        "output": {
        "action": "delete_event_date",
        "date": answer_date,
        "title": title
        }
    }

def update_event_data(date):
    random_day_class = random.choice(["พรุ่งนี้", "มะรืน", "จันทร์หน้า", "อังคารหน้า", "พุธหน้า", "พฤหัสหน้า", "ศุกร์หน้า", "เสาร์หน้า", "อาทิตย์หน้า"])
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_update)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "input": text,
        "output": {
        "action": "update_event",
        "date": answer_date,
        "time": actual_time,
        "title": title
        }
    }

def view_event_data(date):
    random_day_class = random.choice(["พรุ่งนี้", "มะรืน", "จันทร์หน้า", "อังคารหน้า", "พุธหน้า", "พฤหัสหน้า", "ศุกร์หน้า", "เสาร์หน้า", "อาทิตย์หน้า"])
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_view)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "input": text,
        "output": {
        "action": "view_event_date",
        "date": answer_date
        }
    }

# print(add_event_data("2025-05-21"))
# print(delete_event_data("2025-05-21"))
# print(update_event_data("2025-05-21"))
# print(view_event_data("2025-05-21"))

data = []

for date in list_dates_only(2025):
    data.append(add_event_data(date))
    data.append(delete_event_data(date))
    data.append(update_event_data(date))
    data.append(view_event_data(date))

name = "data-dateBytime"

with open(name+".json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data generated and saved to", name+".json")