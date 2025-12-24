# Import the time module
# This allows us to pause the program for 1 second using time.sleep()
import time


# Ask the user to enter time in seconds
# input() returns a string, so we convert it to an integer
my_time = int(input("Enter the time in seconds: "))


# Loop from my_time down to 1
# range(start, stop, step)
# start = my_time
# stop = 0 (not included)
# step = -1 (counting backwards)
for x in range(my_time, 0, -1):

    # Get remaining seconds
    # % 60 gives the remainder after dividing by 60
    seconds = x % 60

    # Get remaining minutes
    # First divide by 60 to convert seconds to minutes
    # % 60 ensures minutes stay between 0–59
    minutes = int(x / 60) % 60

    # Get hours
    # Divide by 3600 (60 seconds × 60 minutes)
    hours = int(x / 3600)

    # Print time in HH:MM:SS format
    # :02 ensures each value has 2 digits (e.g., 04 instead of 4)
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end ="\r", flush =True)

    # Pause the program for 1 second
    time.sleep(1)


# This runs after the loop finishes
print("Time's Up!!!")
