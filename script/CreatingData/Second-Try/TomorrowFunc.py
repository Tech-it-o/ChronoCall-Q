from datetime import datetime, timedelta

def parse_future_date(base_date_str, day_word):
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


base = "2025-05-21"

print("ทดสอบคำว่า 'วันนี้':")
print(parse_future_date(base, "วันนี้"))        # 2025-05-21

print("\nทดสอบคำว่า 'พรุ่งนี้':")
print(parse_future_date(base, "พรุ่งนี้"))      # 2025-05-22

print("\nทดสอบคำว่า 'มะรืน':")
print(parse_future_date(base, "มะรืน"))         # 2025-05-23

print("\nทดสอบคำว่า 'จันทร์นี้':")
print(parse_future_date(base, "จันทร์นี้"))     # 2025-05-26

print("\nทดสอบคำว่า 'จันทร์ที่จะถึงนี้':")
print(parse_future_date(base, "จันทร์ที่จะถึงนี้"))  # 2025-05-26

print("\nทดสอบคำว่า 'จันทร์หน้า':")
print(parse_future_date(base, "จันทร์หน้า"))    # 2025-06-02

print("\nทดสอบคำว่า 'ศุกร์นี้':")
print(parse_future_date(base, "ศุกร์นี้"))      # 2025-05-23

print("\nทดสอบคำว่า 'ศุกร์ที่จะถึงนี้':")
print(parse_future_date(base, "ศุกร์ที่จะถึงนี้"))   # 2025-05-23

print("\nทดสอบคำว่า 'ศุกร์หน้า':")
print(parse_future_date(base, "ศุกร์หน้า"))     # 2025-05-30

print("\nทดสอบคำว่า 'อาทิตย์นี้':")
print(parse_future_date(base, "อาทิตย์นี้"))    # 2025-05-25

print("\nทดสอบคำว่า 'อาทิตย์ที่จะถึงนี้':")
print(parse_future_date(base, "อาทิตย์ที่จะถึงนี้"))  # 2025-05-25

print("\nทดสอบคำว่า 'อาทิตย์หน้า':")
print(parse_future_date(base, "อาทิตย์หน้า"))   # 2025-06-01

print("\nทดสอบคำที่ไม่รองรับ เช่น 'วันก่อน':")
print(parse_future_date(base, "วันก่อน"))       # None
