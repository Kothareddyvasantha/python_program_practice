
lst_a = ["v", "a", 1, 2 ]
emp_lst = [ ] # one kind of empty list
print("One kind of empty list is {}".format(emp_lst))
empt_lst = list()      # Another kind of empty list
print("Another kind of defining empty list is {}".format(empt_lst))
#

lst_x =["v", "s", "c", 0, 1]
len_lstx = len(lst_x)
print("Length of list x is {}".format(len_lstx))

''''''
print("The of the variable is {}".format(type(lst_x)))

lst_y =["0", "1","vasantha", 123]
len_lsty = len(lst_y)
print("The length of list is {}".format(len_lsty))

ind0_lsty = lst_y[0]
print("The zeroeth index of lst_y is {}".format(ind0_lsty))
ind1_lsty = lst_y[1]
print("The first index of lst_y is {}".format(ind1_lsty))
ind2_lsty = lst_y[2]
print("The second index of lst_y is {}".format(ind2_lsty))
ind3_lsty = lst_y[3]
print("the third index of lst_y is {}".format(ind3_lsty))

lst_y = ["1", "2", "vasantha", 123, "@abc"]
lst_vasantha = lst_y[2]
print("the value is {}".format(lst_vasantha))
lsty_s = lst_vasantha[3]
print("the value is {}",format(lsty_s))

lst_y =[999]
print("The lst_y value after changing the value is {}".format(lst_y))
lst_y.append(123)
print("the value of lst_y after appending is {}".format(lst_y))
lst_y.extend(["a", "b"])
print("The lst_y after extending is {}".format(lst_y))
lst_y.extend(["11","22"])
print(" The list of lst_y after extending is {}".format(lst_y))

''''''''
lst_z =["0","1","vasu", 456]
ind0_to_ind3 =lst_z[0:3]
print("The value of list from zero to fourth index is {}".format(ind0_to_ind3))
ind1_to_in5d =lst_z[1:5]
print("The value of list from first to fifth index is {}".format(ind1_to_in5d))

""""""
lst_w =["1", "2", "nayana", 123]
len_lst_w =len(lst_w)
print(len_lst_w)
slc_with_stp2 =lst_w[0:7:2]
print("The value of slicing str w with step size 2 is {}".format(slc_with_stp2))
slc_with_stp3 =lst_w[0:7:3]
print("The value of slicing str w with step size 3 is {}".format(slc_with_stp3))

#slicing all from right or left
ind2_to_all =lst_w[2]
print("value from 2 index to all is {}".format(ind2_to_all))
till_ind4 =lst_w[:4]
print("value till 4 index is {}".format(till_ind4))


#list concatination
lst_a = ["1", "2", "welcome","a","b"]
lst_b = ["1", "2", "python"]
lst_res = lst_a+lst_b
print("value after concatinating is {}".format(lst_res))

lst_a = ["1","2","3","a"]
lst_a.append(4)
print("value of lst_a after appending is {}".format(lst_a))

lst_a = ["1","2","3","4"]
lst_a.append(5)
print("value of lst_a after appending is {}".format(lst_a))


# item reversing in list
lst_a ="welcome to class"
lst_a_split =lst_a.split(" ")
print(" the list after splitting the string is {}",format(lst_a_split))


lst_y = [1,2,["a","b", "python"],3,4]
lst_y[2][2] = lst_y[2][2][::-1]
print(lst_y)

#assignment

lst_z = ["a", "b", ["john", "class", "Alex"], 4, 5, 7]
lst_z[2][1] = lst_z[2][1][::-1]
print(lst_z)
#deleting methods

#clear - it clears all the elements in the lists
lst_a =[2,3,4]
lst_a.clear()
print("the list after clearing is {}".format(lst_a))

# pop - it deletes last index value
lst_b.pop()
print("the list after pop is {}".format(lst_b))

#remove - we can specify which item to be delted from the list
lstc = ["John", "Bob", "Alex", "xyz"]
lstc.remove("Bob")
print(" the value after deleting the bob from list is {}".format(lstc))

# reverse
lst_d =[1,2,3,4]
lst_d.reverse()
print("the value after reversing is {}".format(lst_d))

#insert and index
lst_x =["a","b","c","d","e"]
ind_value =lst_x.index("b")
print("the value after indexing is {}".format(ind_value))

# insert
lst_x.insert(1,"x")
print("the list after inserting is {}".format(lst_x))

# sort max min
lst_z = [3, 2, 6, 1, 5, 4]
lst_z.sort()
print("the list after sorting is {}".format(lst_z))

max_val =lst_z[-1]
print("the one way of getting maximum value is {}".format(max_val))
min_val =lst_z[0]
print("the one way of getting minimum value is {}".format(min_val))
sec_max_val = lst_z[-2]
print("the second highest value is {}".format(sec_max_val))

lst_c =[30,10,50,100,60]
lst_c_max = max(lst_c)
print("the other way of getting maximum value is {}".format(lst_c_max))

lst_min = min(lst_c)
print("the other way of getting minimum value is {}".format(lst_min))

lstm =["a","b","c","a","d"]
cnt_a =lstm.count("a")
print("the count of a is {}".format(cnt_a))
cnt_b =lstm.count("b")
print("the count of b is {}".format(cnt_b))






