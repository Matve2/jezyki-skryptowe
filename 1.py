list_to_sort=[[3,2,3], [2,0,2], [3,0,1], [3,1,0]]
list_to_sort2=[[3,2,3], [2,0,2], [3,0,1], [3,1,0]]

sorted_list=sorted(list_to_sort, key=lambda list_element:(list_element[1], list_element[2]))
print("Lista 1 przed sortowaniem: ", list_to_sort)
print("Lista 1 po sortowaniu: ", sorted_list)


sorted_list_2=sorted(list_to_sort2, key=lambda list_element2:(list_element2[1], list_element2[2]))
print("Lista 2 przed sortowaniem: ", list_to_sort2)
print("Lista 2 po sortowaniu: ", sorted_list_2)