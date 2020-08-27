"""Write a function called remove_if_in_list that takes two arguments. The first argument is a list and the second argument is the element to be removed. This function should return a list with the element removed.

Note:

    The element may not be in the list, so first you need to check to see if it is. If it is in the list, then remove the element

For example:

remove_if_in_list(['cat', 'dog', 'fish', 'bird'], 'bird')

should return:

['cat', 'dog', 'fish']

"""


lst1 = ['cat', 'dog', 'fish', 'bird']
elmt1 = 'bird'

def remove_if_in_list(lst,elmt):
  if elmt in lst:
    lst.remove(elmt)
    return lst
  else:
    return False

print(remove_if_in_list(lst1, elmt1))