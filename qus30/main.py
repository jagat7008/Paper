
test_list = [2323, 82, 129388, 234, 95]
print("The original list is : " + str(test_list))
res = dict()
for ele in test_list:
	mid_idx = len(str(ele)) // 2
	key = int(str(ele)[:mid_idx])
	val = int(str(ele)[mid_idx:])
	res[key] = val
print("Constructed Dictionary : " + str(res))
