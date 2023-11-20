list = [17,38,10,25,72]
list.sort()
print(f'sorted list: {list}')
list.append(12)
print(f'after adding 12: {list}')
list.reverse()
print(f'reversed list: {list}')
index_17 = list.index(17)
print(f'index of 17: {index_17}')
list.remove(38)
print(f'after removing 38: {list}')
sublistof2_3 = list[1:3]
print(f'sublist of 2 and 3 elmt: {sublistof2_3}')
sublistto_2 = list[:2]
print(f'sublist from beginning to 2 element: {sublistto_2}')
sublistfrom_3 = list[2:]
print(f'sublist from 3 elmt to last: {sublistfrom_3}')
complete_sublist = list[:]
print(f'complete sublist: {complete_sublist}')
last_element = list[-1]
print(f'last element: {last_element}') 