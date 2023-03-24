#4. Write to_celsius function that accepts a temperature in Fahrenheit as input and
#returns a temperature in Celsius.
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return celsius
temp_f=55
temp_c=to_celsius(temp_f)
print(temp_c)
