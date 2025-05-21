import json
import random
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

random.seed(69)

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

def add_event_data(day, mounth ,year):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"

    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_add)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": "2025-05-06",
        "input": text,
        "output": {
        "action": "add_event_date",
        "date": actual_date,
        "time": actual_time,
        "title": title
        }
    }

def delete_event_data(day, mounth ,year):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"

    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_delete)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": "2025-05-06",
        "input": text,
        "output": {
        "action": "delete_event_date",
        "date": actual_date,
        "title": title
        }
    }

def update_event_data(day, mounth ,year):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"

    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_update)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": "2025-05-06",
        "input": text,
        "output": {
        "action": "update_event",
        "date": actual_date,
        "time": actual_time,
        "title": title
        }
    }

def view_event_data(day, mounth ,year):
    actual_time = (random.choice(list(data_time.keys())))
    title = (random.choice(data_title["เพิ่มนัด"]))
    actual_date = str(year)+"-"+f"{mounth:02}"+"-"+f"{day:02}"

    date = (str(day) + " " + random.choice(data_mounth[str(mounth)]))
    time = random.choice(data_time[actual_time])
    text = (random.choice(data_view)).replace("[date]", date).replace("[time]", time).replace("[title]", title)

    return {
        "current_date": "2025-05-06",
        "input": text,
        "output": {
        "action": "view_event_date",
        "date": actual_date
        }
    }

data = []

for m in range(1, 13):
    for d in range(1, 32):
        
        if m == 2 and d > 28:
            continue
        elif m in [4, 6, 9, 11] and d > 30:
            continue

        if (m > 5) or (m == 5 and d >= 6):
            year = 2025
        else:
            year = 2026

        data.append(add_event_data(d, m, year))
        data.append(delete_event_data(d, m, year))
        data.append(update_event_data(d, m, year))
        data.append(view_event_data(d, m, year))


with open("data-2025-05-06.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data generated and saved to data-2025-05-06.json")