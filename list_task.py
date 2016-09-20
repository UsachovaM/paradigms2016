# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    for i in range(len(lst)-1):
        lst1=lst[i]
	while lst[i+1]==lst[i]:
	    i=i+1
    return lst1
 
# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    j1=0
    j2=0
    for i in range(len(lst1)+len(lst2)-1):
        if lst1[j1]>lst2[j2]:
	    lst=lst+lst2[j2]
            j2=j2+1
	else
	    lst=lst+lst1[j1]
            j1=j1+1
    return lst
