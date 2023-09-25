# You don't need to understand how code in this file works
# This serves as an entry to each individual task
import os
import time

# Parameters
lessons = ["L1", "L2", "L3", "L4", "L5"]
root = '/home/runner/GHS-Y9-Python/'
sleep = 1

# Intro
print("Glenthorne Python Work Directory - Y9")
print("Last updated 24/09/2023")

# Lesson selection
time.sleep(sleep)
print("")
print("The following lessons are available to view:")
print(lessons)
lesson = input("Choose from the above: ")

# Task selection (calc)
res = []
for file_path in os.listdir(root + lesson):
  if os.path.isfile(os.path.join(root + lesson, file_path)):
    res.append(file_path)

# Task selection
time.sleep(sleep)
print("")
print("The following tasks/challenges are available to view:")
print(res)
task = input(
    "Choose one task/challenge (you need to input the name in full): ")

# Opening task
path = lesson + "/" + task
print(
    "Opening ",
    path,
)

# Run task
time.sleep(sleep)
print("")
print("Would you like to try this program?")
option = input("enter True or False: ")
if option == True:
  print("")
  with open(path) as f:
    exec(f.read())

# Show task code
time.sleep(sleep)
print("")
print("Would you like to see the code?")
option = input("enter True or False: ")
if option == True:
  print("")
  with open(path) as f:
    print(f.read())