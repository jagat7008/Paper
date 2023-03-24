#6. Write a function to_percent which accepts a number representing a ratio and
#returns a string representing the percentage representation of the number to one
#decimal place.

def to_percent(ratio):
    percent = round(ratio * 100, 1)
    return f"{percent}%"

percentage = float(input("Enter the number: "))
print(to_percent(percentage))     