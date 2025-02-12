# FutureTime.py
# Name:abbas 
# Date:02/03/2025
# Assignment: lab 2

import datetime

def main():
    # Get current time from the system
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    # Print current time (for debugging, can be removed later)
    print(f"Current Time: {current_hour:02d}:{current_minute:02d}")

    # Ask user for hours and minutes to add
    hours_to_add = int(input("Enter the number of hours to add: "))
    minutes_to_add = int(input("Enter the number of minutes to add: "))

    # Compute the future time using modular arithmetic
    future_hour = (current_hour + hours_to_add) % 24
    future_minute = (current_minute + minutes_to_add) % 60
    extra_hours = (current_minute + minutes_to_add) // 60

    # Adjust hours based on extra minutes
    future_hour = (future_hour + extra_hours) % 24

    # Convert 24-hour format to 12-hour format
    display_hour = (future_hour % 12)
    display_hour = 12 if display_hour == 0 else display_hour  # Convert 0 to 12
    meridian = "AM" if future_hour < 12 else "PM"

    # Display the result in HH:MM AM/PM format
    print(f"Future Time: {display_hour:02d}:{future_minute:02d} {meridian}")

if __name__ == '__main__':
    main()
