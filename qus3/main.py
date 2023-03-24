#3. Write a function called interleave which accepts two iterables of any type and
#returns a new iterable with each of the given items "interleaved" (item 0 from
#iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on). An
#assumption here that both iterables contain the same number of elements.
def interleave(a, b):
    result=[]                       
    if len(a) < len(b):            
        for i in range (len(a)):   
            result.append(a[i])
            result.append(b[i])
    else:                          
        for i in range (len(b)):
            result.append(a[i])
            result.append(b[i])            
    return result
a = [1,2,3,4]
b = ['a', 'b', 'c','d','e']
result = interleave(a, b)
print(result)  