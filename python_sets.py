"""
what is sets
set is mutable,but items inside set is unchangeable, unordered, unindexed collection of item.
set is enclosed between {}.set does not allow duplicates
Note: internally items of set is mapped to hash key
"""
empty_Set = set()
print("the value of set is {}".format(empty_Set))
"""
Difference between Lists and sets
lists:
*list is a ordered collections
*list can have duplicates
exisiting items of lists can be changed
list is slow compared to set(if we fetch an element from the list it iterates through all the index)

sets:
*sets are unordered collections
*sets does not have duplicates
existing of items of sets cannot be changed
sets is faster compared to list (internally set is mapped to hash key)
"""
# add -we can add single item to the set
set_a = {"a", 1, "b", 2}
set_a.add("c")
print("the value of set after adding c is {}".format(set_a))

#update -we can add multiple items to set
set_a.update ({8,7})
print("the value after updating is {}".format(set_a))

# remove -it throws an error if element is not present
set_b ={"a","b","c","d","e","f"}
set_b.remove("c")
print("the value after removing is {}".format(set_b))

#discard -it returns none if the element is not present
set_b.discard("e")
print("the value after discarding is {}".format(set_b))

#pop -it will delete random item in the set
set_b.pop()
print("the value of set b after pop is {}".format(set_b))

#clear -it will delete all the elements of items
set_b.clear()
print("the value after clear is {}".format(set_b))

#uinon of sets
set_x ={1,2,3}
set_y ={3,4,5}
union_set = set_x.union(set_y)
print("the value of union set is {}".format(union_set))

# intersection of sets
intersection_set = set_x.intersection(set_y)
print("the value of intersection sets is {}".format(intersection_set))

set_z = {1,2,3,4,1}
set_c = frozenset (set_z)
print("the value after freezing is {}".format(set_c))

#removing duplicates in the list
lst_a = [1,2,1,4,6,3,8,2]
lst_b =list(set(lst_a))
print("the value after removing duplicates is {}".format(lst_b))




