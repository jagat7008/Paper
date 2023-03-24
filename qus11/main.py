from this import s


def last_lines(filename,n):
    with open(filename,'r') as f:
        lines = f.readlines()
        return lines[::-1]
lines=last_lines('test.txt', 3)
for i in lines:
    
    print(i)