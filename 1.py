list_to_sort=[[3,2,3], [2,0,2], [3,0,1], [3,1,0]]
sorted_list=sorted(list_to_sort, key=lambda list_element:(list_element[1], list_element[2]))
print(list_to_sort)
print(sorted_list)