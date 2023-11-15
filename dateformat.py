from datetime import datetime

# Get the current date and time
now = datetime.now()

# Define the format as per your requirement
formatted_date = now.strftime("%A %B %d %H:%M:%S %Z %Y")

# Print the formatted date
print(formatted_date)

