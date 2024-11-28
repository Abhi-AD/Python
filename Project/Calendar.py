import calendar


def print_calendar(year, month):
    # Print the calendar for the specified year and month
    print(calendar.month(year, month))


# User input for year and month
year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (1-12): "))

print_calendar(year, month)
