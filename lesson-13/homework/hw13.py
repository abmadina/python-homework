# age_calculator.py
from datetime import date
import calendar

def calculate_age(birth: date, today: date):
    # start with naive difference
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    if days < 0:
        # borrow days from previous month
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days

# Input
raw = input("Enter your birthdate (YYYY-MM-DD): ").strip()
y, m, d = map(int, raw.split('-'))
birth = date(y, m, d)
today = date.today()

years, months, days = calculate_age(birth, today)
print(f"You are {years} years, {months} months, and {days} days old.")

# days_until_birthday.py
from datetime import date, datetime, timedelta

raw = input("Enter your birthdate (YYYY-MM-DD): ").strip()
y, mo, d = map(int, raw.split('-'))
today = date.today()

this_year_bday = date(today.year, mo, d)
if this_year_bday <= today:
    next_bday = date(today.year + 1, mo, d)
else:
    next_bday = this_year_bday

days_remaining = (next_bday - today).days
print(f"{days_remaining} day(s) until your next birthday ({next_bday.isoformat()}).")

# meeting_scheduler.py
from datetime import datetime, timedelta

raw_dt = input("Enter current date and time (YYYY-MM-DD HH:MM): ").strip()
start = datetime.strptime(raw_dt, "%Y-%m-%d %H:%M")

dur_hours = int(input("Meeting duration hours: ").strip())
dur_minutes = int(input("Meeting duration minutes: ").strip())

end = start + timedelta(hours=dur_hours, minutes=dur_minutes)
print("Meeting ends at:", end.strftime("%Y-%m-%d %H:%M"))

# tz_converter.py
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None

if ZoneInfo is None:
    raise SystemExit("This script requires Python 3.9+ (zoneinfo).")

raw = input("Enter date and time (YYYY-MM-DD HH:MM): ").strip()
dt = datetime.strptime(raw, "%Y-%m-%d %H:%M")

src = input("Enter source timezone (e.g. Europe/London): ").strip()
dst = input("Enter destination timezone (e.g. Asia/Tokyo): ").strip()

try:
    aware_src = dt.replace(tzinfo=ZoneInfo(src))
except Exception as e:
    raise SystemExit(f"Invalid source timezone: {e}")

try:
    converted = aware_src.astimezone(ZoneInfo(dst))
except Exception as e:
    raise SystemExit(f"Invalid destination timezone: {e}")

print(f"{aware_src.isoformat()} in {src} is {converted.isoformat()} in {dst}.")

# countdown_timer.py
from datetime import datetime, timedelta
import time

raw = input("Enter future date/time (YYYY-MM-DD HH:MM:SS): ").strip()
target = datetime.strptime(raw, "%Y-%m-%d %H:%M:%S")

try:
    while True:
        now = datetime.now()
        diff = target - now
        if diff.total_seconds() <= 0:
            print("Countdown finished!")
            break
        # break into days, hours, minutes, seconds
        days = diff.days
        hours, rem = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"\rTime remaining: {days}d {hours:02}h:{minutes:02}m:{seconds:02}s", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user.")

# email_validator.py
import re

pattern = re.compile(
    r"^[A-Za-z0-9._%+-]+@"        # local part
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"  # domain
)

email = input("Enter email: ").strip()
if pattern.match(email):
    print("Valid email format.")
else:
    print("Invalid email format.")

# phone_formatter.py
import re

raw = input("Enter phone number digits (e.g. 1234567890): ").strip()
digits = re.sub(r"\D", "", raw)  # remove non-digits

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted:", formatted)
elif len(digits) == 11 and digits[0] == "1":
    # US with leading country code 1
    formatted = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:11]}"
    print("Formatted:", formatted)
else:
    print("Unsupported phone format / length. Digits found:", len(digits))

# phone_formatter.py
import re

raw = input("Enter phone number digits (e.g. 1234567890): ").strip()
digits = re.sub(r"\D", "", raw)  # remove non-digits

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted:", formatted)
elif len(digits) == 11 and digits[0] == "1":
    # US with leading country code 1
    formatted = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:11]}"
    print("Formatted:", formatted)
else:
    print("Unsupported phone format / length. Digits found:", len(digits))

# password_strength.py
import re

pwd = input("Enter password: ")

criteria = [
    (len(pwd) >= 8, "At least 8 characters"),
    (re.search(r"[A-Z]", pwd), "At least one uppercase letter"),
    (re.search(r"[a-z]", pwd), "At least one lowercase letter"),
    (re.search(r"\d", pwd), "At least one digit"),
    (re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\",.<>/?\\|`~]", pwd), "At least one special character"),
]

passed = [msg for ok, msg in criteria if ok]
failed = [msg for ok, msg in criteria if not ok]

print(f"Passed: {len(passed)}/{len(criteria)} checks.")
if failed:
    print("Missing:")
    for f in failed:
        print(" -", f)
else:
    print("Strong password (by these rules).")

# word_finder.py
import re

text = input("Enter the text (or paste):\n")
word = input("Enter the word to find: ").strip()

# case-insensitive search, word boundaries
pattern = re.compile(rf"\b{re.escape(word)}\b", flags=re.IGNORECASE)

matches = list(pattern.finditer(text))
if not matches:
    print("No occurrences found.")
else:
    print(f"Found {len(matches)} occurrence(s):")
    for i, m in enumerate(matches, 1):
        start, end = m.start(), m.end()
        snippet = text[max(0, start-20):min(len(text), end+20)]
        print(f"{i}. Indices [{start}:{end}] -> ...{snippet}...")

# date_extractor.py
import re

text = input("Enter text to search for dates:\n")

patterns = [
    # YYYY-MM-DD
    r"\b(20\d{2}|19\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b",
    # DD/MM/YYYY or D/M/YYYY
    r"\b(0?[1-9]|[12]\d|3[01])[/-](0?[1-9]|1[0-2])[/-](20\d{2}|19\d{2})\b",
    # Month name DD, YYYY  (e.g., January 5, 2020)
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s*(20\d{2}|19\d{2})\b",
    # Abbreviated month Jan/Feb 5 2020 or Jan 5, 2020
    r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\.?\s+\d{1,2},?\s*(20\d{2}|19\d{2})\b",
]

found = set()
for p in patterns:
    for m in re.finditer(p, text, flags=re.IGNORECASE):
        found.add(m.group(0))

if not found:
    print("No dates found.")
else:
    print("Dates found:")
    for d in sorted(found):
        print(" -", d)

