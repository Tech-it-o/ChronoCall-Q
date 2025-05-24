from datetime import datetime, timedelta

date = "2025-05-24"

day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")

print(day)