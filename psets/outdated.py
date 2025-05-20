months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        # Handle numeric format: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        # Handle text format: Month DD, YYYY
        elif "," in date:
            month_name, rest = date.split(" ", 1)
            day, year = rest.split(",")
            month = months.index(month_name) + 1
            day = int(day.strip())
            year = int(year.strip())

        else:
            raise ValueError  # Force reprompt for bad format

        # Validate day/month values
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        continue  # If any parsing fails, re-prompt the user
