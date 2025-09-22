from ics import Calendar
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# STEP 1: Load calendar data
# ------------------------------
with open('my_calendar.ics', 'r', encoding='utf-8') as f:
    c = Calendar(f.read())

data = []
for event in c.events:
    data.append({
        "Title": event.name,
        "Start": event.begin.datetime,
        "End": event.end.datetime,
        "Duration (hours)": (event.end.datetime - event.begin.datetime).total_seconds() / 3600,
        "Location": event.location,
        "Description": event.description
    })

df = pd.DataFrame(data)

# ------------------------------
# STEP 2: Add extra columns
# ------------------------------
df["Year"] = df["Start"].dt.year
df["Month"] = df["Start"].dt.month_name()
df["Weekday"] = df["Start"].dt.day_name()

# ------------------------------
# STEP 3: Summary Analysis
# ------------------------------
print("\n📊 Calendar Summary")
print("="*40)
print(f"Total Events: {len(df)}")
print(f"Total Hours in Events: {df['Duration (hours)'].sum():.2f}")
print("\nEvents per Month:")
print(df["Month"].value_counts())
print("\nEvents per Weekday:")
print(df["Weekday"].value_counts())

# ------------------------------
# STEP 4: Visualizations
# ------------------------------

# Events per Month
df["Month"].value_counts().plot(kind="bar", figsize=(8,5))
plt.title("Number of Events per Month")
plt.xlabel("Month")
plt.ylabel("Events")
plt.show()

# Hours spent per Month
df.groupby("Month")["Duration (hours)"].sum().plot(kind="line", marker="o", figsize=(8,5))
plt.title("Total Hours Spent in Events per Month")
plt.xlabel("Month")
plt.ylabel("Hours")
plt.show()

# Events by Weekday
df["Weekday"].value_counts().plot(kind="bar", color="orange", figsize=(8,5))
plt.title("Events Distribution by Weekday")
plt.xlabel("Day of the Week")
plt.ylabel("Events")
plt.show()
