import time # You don't need to know this now
# If you're still curious, there are code out there that people have written for others to use, these collections of code are called 'libraries', and this library 'time' is a set of code to allow us to manipulate time in Python.

secs = int(input("How many seconds should it count from? "))

while secs > 0:
    print(secs)
    time.sleep(1) # Now we are using something within the 'time' library

print("Timer finished")