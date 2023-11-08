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
tpl_x =("c", "d","nayana", 567)
ind0_to_ind6 =tpl_x[0:6]
print(" The value of tuple from zero to sixth index is".format(ind0_to_ind6))
ind2_to_ind8 =tpl_x[2:8]
print("The value of tuple from second to eigth index is {}".format(ind2_to_ind8))

""""""
tpl_y =("x", "y", "python", 789)
len_tpl_y =len(tpl_y)
print(len_tpl_y)
slc_with_stp2 =tpl_y[0:5:2]
print("The value of slicing tpl_y with stp size 2 {}".format(slc_with_stp2))
slc_with_stp3 =tpl_y[0:5:3]
print("The value of slicing str y with step size 3 is {}".format(slc_with_stp3))

# slicing all from right or left
ind4_to_all =tpl_y[4]
print("value from 4th index to all is{}".format(ind4_to_all))
till_ind5 =tpl_y[:5]
print("value of fifth index to all is {}".format(till_ind5))

#reverse indexing
tpl_l ="welcome"
ind1_neg =tpl_a[-1]
print("value of negative index one is {}".format(ind1_neg))
ind2_neg =tpl_a[-2]
print("value of negative index two is {}".format(ind2_neg))
ind3_neg =tpl_a[-3]
print("value of negative index three is {}".format(ind3_neg))
ind4_neg =tpl_a[-4]
print("value of negative index four is {}".format(ind4_neg))
ind5_neg =tpl_a[-5]
print("value of negative index five is {}".format(ind5_neg))
ind6_neg =tpl_a[-6]
print("value of negative index six is {}".format(ind6_neg))

#Reverse Slicing
tpl_a_slc =tpl_a[3:2:-1]
print("value of slicing from 2 to 3 in reverse format {}".format(tpl_a_slc))
tpl_a_slc =tpl_a[5:2:-1]
print("value of slicing from 2 to 5 in reverse format {}".format(tpl_a_slc))