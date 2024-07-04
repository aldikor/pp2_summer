from datetime import datetime

# Define two dates
date1 = datetime(2024, 7, 1, 12, 0, 0)
date2 = datetime(2024, 7, 4, 12, 0, 0)

# Calculate the difference in seconds
difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)