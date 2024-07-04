from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Remove microseconds
datetime_no_microseconds = current_datetime.replace(microsecond=0)

print("Current datetime:", current_datetime)
print("Datetime without microseconds:", datetime_no_microseconds)