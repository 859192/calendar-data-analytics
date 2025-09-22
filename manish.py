from ics import Calendar

with open('my_calendar.ics', 'r', encoding='utf-8') as f:
    c = Calendar(f.read())

for event in c.events:
    print("Title:", event.name)
    print("Start:", event.begin)
    print("End:", event.end)
    print("Description:", event.description)
    print("Location:", event.location)
    print("="*40)
# This script reads an .ics calendar file and prints out the details of each event.