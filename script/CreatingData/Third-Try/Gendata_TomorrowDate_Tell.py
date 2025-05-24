from datetime import datetime, timedelta
import random
import json
import os
from pathlib import Path

random.seed(69)

base_dir = Path(__file__).resolve().parent.parent

# load title template
with open(os.path.join(base_dir, 'Component_datetext', 'Title.json'), 'r', encoding='utf-8') as f:
    data_title = json.load(f)

with open(os.path.join(base_dir, 'Component_datetext', 'TimeDic_mostly.json'), 'r', encoding='utf-8') as f:
    data_time = json.load(f)

with open(os.path.join(base_dir, 'Component_datetext', 'DayWord.json'), 'r', encoding='utf-8') as f:
    data_date = json.load(f)

# text template

with open(os.path.join(base_dir, 'action_datetext', 'add_event.json'), 'r', encoding='utf-8') as f:
    data_add = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'delete_event.json'), 'r', encoding='utf-8') as f:
    data_delete = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'update_event.json'), 'r', encoding='utf-8') as f:
    data_update = json.load(f)

with open(os.path.join(base_dir, 'action_datetext', 'view_event.json'), 'r', encoding='utf-8') as f:
    data_view = json.load(f)

def resolve_date_only(base_date_str, day_word):
    base_date = datetime.strptime(base_date_str, "%Y-%m-%d")
    day_word = day_word.strip()

    weekdays_th = {
        'จันทร์': 0,
        'อังคาร': 1,
        'พุธ': 2,
        'พฤหัส': 3,
        'ศุกร์': 4,
        'เสาร์': 5,
        'อาทิตย์': 6
    }

    if day_word == "วันนี้":
        return base_date.strftime("%Y-%m-%d")
    elif day_word == "พรุ่งนี้":
        return (base_date + timedelta(days=1)).strftime("%Y-%m-%d")
    elif day_word == "มะรืน":
        return (base_date + timedelta(days=2)).strftime("%Y-%m-%d")
    else:
        for wd in weekdays_th.keys():
            if day_word.startswith(wd):
                weekday_target = weekdays_th[wd]
                suffix = day_word[len(wd):].strip()

                base_weekday = base_date.weekday()

                if suffix == "นี้" or suffix == "ที่จะถึงนี้":
                    days_ahead = (weekday_target - base_weekday) % 7
                    if days_ahead == 0:
                        target_date = base_date
                    else:
                        target_date = base_date + timedelta(days=days_ahead)
                elif suffix == "หน้า":
                    days_ahead = (weekday_target - base_weekday) % 7
                    if days_ahead == 0:
                        days_ahead = 7
                    else:
                        days_ahead += 7
                    target_date = base_date + timedelta(days=days_ahead)
                else:
                    return None

                return target_date.strftime("%Y-%m-%d")

        return None

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
    random_day_class = random.choice(data_date)
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    current_day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_add)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "add_event_date",
        "date": answer_date,
        "time": actual_time,
        "title": title
        }
    }

def delete_event_data(date):
    random_day_class = random.choice(data_date)
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    current_day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_delete)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "delete_event_date",
        "date": answer_date,
        "title": title
        }
    }

def update_event_data(date):
    random_day_class = random.choice(data_date)
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    current_day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_update)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "update_event",
        "date": answer_date,
        "time": actual_time,
        "title": title
        }
    }

def view_event_data(date):
    random_day_class = random.choice(data_date)
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    answer_date =  resolve_date_only(date, random_day_class)
    current_day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_view)).replace("[date]", random_day_class).replace("[time]", time).replace("[title]", title)

    return {
        "current_date" : date,
        "current_day" : current_day,
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

name = "data-dateBytime-Tell"

with open(name+".json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data generated and saved to", name+".json")