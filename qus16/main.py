
#16. Write a function split_in_half that splits a list in half and returns both halves.
#>>> split_in_half([1, 2, 3, 4])
#([1, 2], [3, 4])
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5,6]
B, C = split_list(A)
print(B,C)
 