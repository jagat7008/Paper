#13. Write a function that accepts a string containing lines of numbers and returns a
#list of lists of numbers.
#Ex. matrix_from_string("3 4 5")
#[[3.0, 4.0, 5.0]]

def matrix_from_string(input_string):
    lines = input_string.strip().split(',')    
    matrix = []
    for line in lines:
        numbers = [float(x) for x in line.strip().split()]
        matrix.append(numbers)
    return matrix

input_string = "3 4 5"
print(matrix_from_string(input_string))
