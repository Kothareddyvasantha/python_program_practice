tpl_a = ("M", "N", 1, "vasantha")
print("The items of tuple is {}".format(tpl_a))

len_tpl_a =len(tpl_a)
print("The length of tuple is {}".format(len_tpl_a))

typ_tpl_a =type(tpl_a)
print("The type is {}".format(typ_tpl_a))

ind0_tpl_a =tpl_a[0]
print("The zeroeth element of tuple is {}".format(ind0_tpl_a))
ind1_tpl_a =tpl_a[1]
print("The first element of tuple is {}".format(ind1_tpl_a))
ind2_tpl_a =tpl_a[2]
print("The second element of tuple is {}".format(ind2_tpl_a))
ind3_tpl_a =tpl_a[3]
print("The third element of tuple is {}".format(ind3_tpl_a))

""""""
tpl_x ="welcome to tuple"
ind0_to_ind6 =tpl_x[0:6]
print(" The value of tuple from zero to sixth index is".format(ind0_to_ind6))
ind2_to_ind8 =tpl_x[2:8]
print("The value of tuple from second to eigth index is {}".format(ind2_to_ind8))

""""""
tpl_y ="Tuple"
len_tpl_y =len(tpl_y)
print(len_tpl_y)
slc_with_stp2 =tpl_y[0:5:2]
print("The value of slicing tpl_y with stp size 2 {}".format(slc_with_stp2))
slc_with_stp3 =tpl_y[0:5:3]
print("The value of slicing str y with step size 3 is {}".format(slc_with_stp3))
