from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date five days ago:", new_date)