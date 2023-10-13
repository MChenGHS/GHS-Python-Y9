# Initialise values
total = 0
mark = int(input("Enter first exam mark: "))
maxMark = mark
minMark = mark
numberOfMarks = 0

# Main loop, continue running (asking for new mark) until user enters -1
while mark != -1:
    total = total + mark
    if mark < minMark:
        minMark = mark

    if mark > maxMark
        maxMark = mark
    mark = int(input("Enter next exam mark, -1 to end: "))

    numberOfMarks = numberOfMarks + 1

# Calculate average
averageMark = total / numberOfMarks

# Print results
print ("Maximum mark =",maxMark)
print ("Minimum mark =",minMark)
print("Average mark =",averageMark) 
input("Press Enter to exit ")
