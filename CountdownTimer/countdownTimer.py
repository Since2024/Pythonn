# Import the time module
# This allows us to pause the program for a specific amount of time (sleep)
import time


# Define a function called countdown
# It takes one parameter 't' which represents time in seconds
def countdown(t):

    # This loop will run as long as 't' is not 0
    # When t becomes 0, the loop stops
    while t:

        # divmod(t, 60) splits time into:
        # mins → total minutes
        # secs → remaining seconds
        mins, secs = divmod(t, 60)

        # Format minutes and seconds so they always show 2 digits
        # Example: 1:5 becomes 01:05
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Print the timer on the same line
        # '\r' moves the cursor back to the start of the line
        print(timer, end="\r")

        # Pause the program for 1 second
        # This makes the countdown realistic
        time.sleep(1)

        # Decrease time by 1 second
        t -= 1

    # This line runs after the countdown finishes
    print('Time is Up!')


# Ask the user to enter time in seconds
# input() always returns a string
t = input('Enter the time in seconds: ')

# Convert the input string to an integer
# Then call the countdown function
countdown(int(t))
