
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

lst_y =999
print("The lst_y value after changing the value is {}".format(lst_y))
lst_y.append(123)
print("the value of lst_y after appending is {}".format(lst_y))
lst_y.extend(["a", "b"])
print("The lst_y after extending is {}".format(lst_y))
lst_y.extend(["11","22"])
print(" The list of lst_y after extending is {}".format(lst_y))