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
ind4_to_all =tpl_y[3]
print("value from 3th index to all is{}".format(ind4_to_all))
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


#Reverse Slicing
tpl_a_slc =tpl_a[3:2:-1]
print("value of slicing from 2 to 3 in reverse format {}".format(tpl_a_slc))
tpl_a_slc =tpl_a[5:2:-1]
print("value of slicing from 2 to 5 in reverse format {}".format(tpl_a_slc))

#tuple concatination
tpl_a ="welcome"
tpl_b ="to class"
tpl_res =tpl_a+tpl_b
print("value after concatinating is {}".format(tpl_res))

#capitalizing
tpl_a ="pycHarm"
a=tpl_a.capitalize()
print("Value after capitalizing tuple is {}".format(a))

#upper case
upp_case =tpl_a.upper()
print("the upper case values are {}".format(upp_case))
#lower case
tpl_b ="Hello"
low_case =tpl_b.lower()
print("the lower case values are {}".format(low_case))

#to check given tpl is lower
tpl_low ="hello"
print("The tuple is lower {}".format(tpl_low.islower()))

#title
tpl_x ="welcome to class"
tit_tpl =tpl_x.title()
print("value converting into title is {}".format(tit_tpl))

# to check whether it is title or not
print("The tuple is title {}".format(tpl_x.istitle()))
print("The tuple is title {}".format(tit_tpl.istitle()))

#count
tpl_a ="vasantha"
print("count of tuple v is {}".format(tpl_a.count("v")))
print("count of tuple a is {}".format(tpl_a.count("a")))

#index
print("index value of v in tuple is {}".format(tpl_a.index("v")))
print("index value of a in tuple is {}".format(tpl_a.index("a")))

#starts with
tpl_c ="github"
print("the tuple is starting with g is {}".format(tpl_c.startswith("g")))
print("the tuple is starting with h is {}".format(tpl_c.startswith("h")))
#ends with
tpl_d ="welcome"
print("The tuple is ends with e is {}".format(tpl_d.endswith("e")))
print("The tuple is ends with l is {}".format(tpl_d.endswith("l")))




