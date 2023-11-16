
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

#Reverse indexing
lst_g = ["a", "b", "vasantha", 123]
ind1_neg =lst_g[-1]
print("value of negative index one is {}".format(ind1_neg))
ind2_neg =lst_g[-2]
print("value of negative index two is {}".format(ind2_neg))
ind3_neg =lst_g[-3]
print("value of negative index three is {}".format(ind3_neg))
ind4_neg =lst_g[-4]
print("value of negative index four is {}".format(ind4_neg))
ind5_neg =lst_g[-5]
print("value of negative index five is {}".format(ind5_neg))
ind6_neg =lst_g[-6]
print("value of negative index six is {}".format(ind6_neg))
ind7_neg =lst_g[-7]
print("value of negative index seven is {}".format(ind7_neg))

#Reverse slicing
lst_g_slc =lst_g[3:1:-1]
print("value of slicing from one to three in reverse format is {}".format(lst_g_slc))
lst_g_slc =lst_g[4:3:-1]
print("value of slicing from three to four in reverse format is{}".format(lst_g_slc))

#list concatination
lst_a =["1", "2", "welcome","a","b"]
lst_b =["1", "2", "python"]
lst_res =lst_a+lst_b
print("value after concatinating is {}".format(lst_res))

#capitalize -it will capitalizes first character of string
lst_a =["a","b","vAsu",112]
a =lst_a.capitalize()
print("value after capitalizing is {}".format(a))

#upper case
upp_case =lst_a.upper()
print("upper case values are {}".format(upp_case))

#lower case
low_case =lst_a.lower()
print("lower case values are {}".format(low_case))

#Title
lst_x =["a","b","welcome to class",321]
tit_lst =lst_x.title()
print("the list is title {}".format(tit_lst))

#to check whether title or not
print("the list is title {}".format(lst_x.istitle()))
print("the list is title {}".format(tit_lst.istitle()))

#count
lst_a =["x","y","program",123]
print("the count of p in list is {}".format(lst_a.count("p")))
print("the count of g in list is {}".format(lst_a.count("g")))

#index
print("the index value of p in list a is {}".format(lst_a.index("p")))
print("the index value of m in list a is {}".format(lst_a.index("m")))

#starts with
lst_a =["c","d","welcome",456]
print("the list is starting with h is {}".format(lst_a.startswith("h")))
print("the list is starting with w is {}".format(lst_a.startswith("w")))

#ends with
lst_b =["a","b","python",123]
print("the list is ends with n is {}".format(lst_b.endswith("n")))
print("the list is ends with p is {}".format(lst_b.endswith("p")))


lst_a =["1","2","3","a"]
lst_a.append(4)
print("value of lst_a after appending is {}".format(lst_a))
lst_a.extend["4","5"]
print("value of lst_a after extending is {}".format(lst_a))

lst_a = ["1","2","3","4"]
lst_a.append(5)
print("value of lst_a after appending is {}".format(lst_a))


# item reversing in list
lst_a ="welcome to class"
lst_a_split =lst_a.split(" ")
print(" the list after splitting the string is {}",format(lst_a_split))


list_x =[1,2,["a","b", "python"],3,4]
lst_x[2][2][::-1]
print(lst_x)
lst_z = ["a", "b", ["john", "class", "Alex"], 4, 5, 7]
lst_z[1][2][::-1]
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
print(" the value after deleting the bob is {}")






