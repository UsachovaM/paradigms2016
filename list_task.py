# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    for i in range(len(lst)-1):
	while lst[i+1]==lst[i]:
	    i=i+1
    return lst
 
# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    for i in range(len(lst1)+len(lst2)):
        if lst1[1]>lst2[1]:
	    lst.append(lst2.pop([1]))
	else
	    lst.append(lst1.pop([1]))
    return lst
