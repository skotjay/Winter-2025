from datetime import datetime, timedelta

# Define the dates for the Sabbats
sabbats = {
    "Samhain": {"month": 10, "day": 31},
    "Yule": {"month": 12, "day": 21},
    "Imbolc": {"month": 2, "day": 2},
    "Ostara": {"month": 3, "day": 21},
    "Beltane": {"month": 5, "day": 1},
    "Litha": {"month": 6, "day": 21},
    "Lammas": {"month": 8, "day": 1},
    "Mabon": {"month": 9, "day": 21},
}

#Print The last sabbat was (last Sabbat name), and was on (last Sabbat date).
def get_last_sabbat():
    today = datetime.today()
    current_year = today.year
    sabbat_dates = []

    for sabbat, date in sabbats.items():
        sabbat_date = datetime(current_year, date["month"], date["day"])
        # Check if the sabbat date is in the past
        if sabbat_date < today:
            sabbat_dates.append((sabbat_date, sabbat))
    
    # Sort the dates and return the last one
    sabbat_dates.sort()
    if sabbat_dates:
        return sabbat_dates[-1][1], sabbat_dates[-1][0]
    else:
        # If no past sabbats in the current year, return the last sabbat of the previous year
        last_sabbat_last_year = max(sabbats.keys(), key=lambda sabbat: (sabbats[sabbat]["month"], sabbats[sabbat]["day"]))
        last_sabbat_date = datetime(current_year - 1, sabbats[last_sabbat_last_year]["month"], sabbats[last_sabbat_last_year]["day"])
        return last_sabbat_last_year, last_sabbat_date

def get_next_sabbat():
    today = datetime.today()
    current_year = today.year
    sabbat_dates = []

    for sabbat, date in sabbats.items():
        sabbat_date = datetime(current_year, date["month"], date["day"])
        # Check if the sabbat date is in the future
        if sabbat_date >= today:
            sabbat_dates.append((sabbat_date, sabbat))
    
    # Sort the dates and return the next one
    sabbat_dates.sort()
    if sabbat_dates:
        return sabbat_dates[0][1], sabbat_dates[0][0]
    else:
        # If no future sabbats in the current year, return the first sabbat of the next year
        first_sabbat_next_year = min(sabbats.keys(), key=lambda sabbat: (sabbats[sabbat]["month"], sabbats[sabbat]["day"]))
        first_sabbat_date = datetime(current_year + 1, sabbats[first_sabbat_next_year]["month"], sabbats[first_sabbat_next_year]["day"])
        return first_sabbat_next_year, first_sabbat_date

print ()  
#Print today's date
print(f"Today's date is {datetime.today().strftime('%B %d, %Y')}.")

print ()
# Get the last Sabbat
last_sabbat, last_sabbat_date = get_last_sabbat()
print(f"The last Sabbat was {last_sabbat} on {last_sabbat_date.strftime('%B %d, %Y')}.")

#Print how many days since the last Sabbat.
days_since_last_sabbat = (datetime.today() - last_sabbat_date).days
print(f"It has been {days_since_last_sabbat} days since the last Sabbat.")

print()
# Get the next Sabbat
next_sabbat, next_sabbat_date = get_next_sabbat()
print(f"The next Sabbat is {next_sabbat} on {next_sabbat_date.strftime('%B %d, %Y')}.")

#Print how many days until the next Sabbat.
days_until_next_sabbat = (next_sabbat_date - datetime.today()).days
print(f"It is {days_until_next_sabbat} days until the next Sabbat.")

