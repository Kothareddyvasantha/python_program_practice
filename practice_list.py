
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
lst_z ="welcome to List"
ind0_to_ind3 =lst_z[0:3]
print("The value of list from zero to fourth index is {}".format(ind0_to_ind3))
ind1_to_ind8 =lst_z[1:8]
print("The value of list from first to eigth index is {}".format(ind1_to_ind8))

""""""
lst_w ="welcome"
len_lst_w =len(lst_w)
print(len_lst_w)
slc_with_stp2 =lst_w[0:7:2]
print("The value of slicing str w with step size 2 is {}".format(slc_with_stp2))
slc_with_stp3 =lst_w[0:7:3]
print("The value of slicing str w with step size 3 is {}".format(slc_with_stp3))
