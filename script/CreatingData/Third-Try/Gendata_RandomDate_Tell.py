import json
import random
import os
from datetime import datetime
from pathlib import Path

random.seed(69)

base_dir = Path(__file__).resolve().parent.parent

# load title template
with open(os.path.join(base_dir, 'Component', 'Title.json'), 'r', encoding='utf-8') as f:
    data_title = json.load(f)

with open(os.path.join(base_dir, 'Component', 'TimeDic_mostly.json'), 'r', encoding='utf-8') as f:
    data_time = json.load(f)

with open(os.path.join(base_dir, 'Component', 'Mounth.json'), 'r', encoding='utf-8') as f:
    data_mounth = json.load(f)

# text template

with open(os.path.join(base_dir, 'action', 'add_event.json'), 'r', encoding='utf-8') as f:
    data_add = json.load(f)

with open(os.path.join(base_dir, 'action', 'delete_event.json'), 'r', encoding='utf-8') as f:
    data_delete = json.load(f)

with open(os.path.join(base_dir, 'action', 'update_event.json'), 'r', encoding='utf-8') as f:
    data_update = json.load(f)

with open(os.path.join(base_dir, 'action', 'view_event.json'), 'r', encoding='utf-8') as f:
    data_view = json.load(f)

# function

def add_event_data(day, mounth ,year ,current_date):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"
    current_day = datetime.strptime(current_date, "%Y-%m-%d").strftime("%A")
    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_add)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": current_date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "add_event_date",
        "date": actual_date,
        "time": actual_time,
        "title": title
        }
    }

def delete_event_data(day, mounth ,year ,current_date):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"
    current_day = datetime.strptime(current_date, "%Y-%m-%d").strftime("%A")
    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_delete)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": current_date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "delete_event_date",
        "date": actual_date,
        "title": title
        }
    }

def update_event_data(day, mounth ,year ,current_date):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"
    current_day = datetime.strptime(current_date, "%Y-%m-%d").strftime("%A")
    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_update)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": current_date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "update_event",
        "date": actual_date,
        "time": actual_time,
        "title": title
        }
    }

def view_event_data(day, mounth ,year ,current_date):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"
    current_day = datetime.strptime(current_date, "%Y-%m-%d").strftime("%A")
    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_view)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": current_date,
        "current_day" : current_day,
        "input": text,
        "output": {
        "action": "view_event_date",
        "date": actual_date
        }
    }

data = []

for m in range(1, 13):
    for d in range(1, 32):
        for i in range(4):
            current_date = datetime.strptime(f"2025-{random.randint(1,12):02}-{random.randint(1,28):02}", "%Y-%m-%d")
            current_date_str = current_date.strftime("%Y-%m-%d")
            
            if m == 2 and d > 28:
                continue
            elif m in [4, 6, 9, 11] and d > 30:
                continue

            event_date = datetime(current_date.year, m, d)
            
            if event_date < current_date:
                year = current_date.year + 1
            else:
                year = current_date.year

            if i == 0:
                data.append(add_event_data(d, m, year, current_date_str))
            elif i == 1:             
                data.append(delete_event_data(d, m, year, current_date_str))
            elif i == 2:
                data.append(update_event_data(d, m, year, current_date_str))
            elif i == 3:
                data.append(view_event_data(d, m, year, current_date_str))

name = "data-RandomCurrentDate-Tell"

with open(name+".json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data generated and saved to", name+".json")