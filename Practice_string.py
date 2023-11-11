
str_a ="Python"
str_n ="1234"
str_an ="python 3.9"
str_s =" "

len_str = len(str_an)
print("The length of string is {}".format(len_str))
type_str =type(str_an)
print("The type of variable str_an is {}".format(type_str))


#indexing
str_x ="python"
strx_zeroeth_ind =str_x[0]
print("zeroeth index value of strx is {}".format(strx_zeroeth_ind))
strx_fst_index =str_x[1]
print("Fist index value of str is {}".format(strx_fst_index))
strx_sec_index =str_x[2]
print(" Sec index value of str is {}".format(strx_sec_index))
strx_Thr_index =str_x[3]
print("Thr index value of str is {}".format(strx_Thr_index))
strx_Four_index =str_x[4]
print("Four index value of str is {}". format(strx_Four_index))
strx_Five_index =str_x[5]
print("Five index value of str is {}".format(strx_Five_index))

str_v ="Welcome to class"
strv_zeroeth_index =str_v[0]
print("Zeroeth index value of str is {}".format(strv_zeroeth_index))
strv_fst_index =str_v[1]
print("fst index value of str is {}".format(strv_fst_index))
strv_sec_index =str_v[2]
print("sec index value of str is {}".format(strv_sec_index))
strv_thr_index =str_v[3]
print("thr index value of str is {}".format(strv_thr_index))
strv_four_index =str_v[4]
print("four index value of str is {}".format(strv_four_index))
strv_five_index =str_v[5]
print("five index value of str is {}".format(strv_five_index))
strv_six_index =str_v[6]
print("six index value of str is {}".format(strv_six_index))
strv_seven_index =str_v[7]
print("seven index value of str is {}".format(strv_seven_index))
strv_eight_index =str_v[8]
print("eight index value of str is {}".format(strv_eight_index))
strv_nine_index =str_v[9]
print("nine index value of str is {}".format(strv_nine_index))
strv_ten_index =str_v[10]
print("ten index value of str is {}".format(strv_ten_index))
strv_eleven_index =str_v[11]
print("eleven index value of str is {}".format(strv_eleven_index))
strv_Twelve_index =str_v[12]
print("Twelve index value of str is {}".format(strv_Twelve_index))
strv_Thirteen_index =str_v[13]
print("Thirteen index value of str is {}".format(strv_Thirteen_index))
strv_fourteen_index =str_v[14]
print("Fourteen index value of str is {}".format(strv_fourteen_index))
strv_Fifteen_index =str_v[15]
print("Fifteen index value of str is {}".format(strv_Fifteen_index))

""""""
str_c ="welcome to Git"
ind0_to_ind4 = str_c[0:4]
print("The value of string from zero to fourth index is {}".format(ind0_to_ind4))
ind1_to_ind5 =str_c[1:5]
print("The value of string from first to fifth index is {}".format(ind1_to_ind5))
ind3_to_ind6 =str_c[3:6]
print("The value of string from third to sixth index is {}".format(ind3_to_ind6))

""""""
str_d ="Github"
len_str_d =len(str_d)
print(len_str_d)
slc_with_stp2 =str_d [0:6:2]
print("The value of slicing str with step size 2 is {}".format(slc_with_stp2))
slc_with_stp3 =str_d[0:6:3]
print("The value of slicing str with step size 3 is {}".format(slc_with_stp3))

# slicing all from right or left
ind3_to_all =str_d[3:]
print("Value from 3 rd index to all is {}".format(ind3_to_all))
till_ind5 =str_d[:5]
print("value till 5th index is {}".format(till_ind5))

#Reverse Indexing
str_e ="github"
ind1_neg =str_e[-1]
print("Value of negative index one is {}".format(ind1_neg))
ind2_neg =str_e[-2]
print("value of negative index two is {}".format(ind2_neg))
ind3_neg =str_e[-3]
print("value of negative index three is {}".format(ind3_neg))
ind4_neg =str_e[-4]
print("value of negative index four is {}".format(ind4_neg))
ind5_neg =str_e[-5]
print("value of negative index five is {}".format(ind5_neg))
ind6_neg =str_e[-6]
print("value of negative index six is {}".format(ind6_neg))

#Reverse slicing
str_e_slc =str_e[5:3:-1]
print("Value of slicing from 3 to 5 in reverse format{}".format(str_e_slc))

str_f ="Python"
str_f_slc =str_f[5:2:-1]
print("value of slicing from 2 to 5 in reverse format{}".format(str_f_slc))

# string concatination
str1 ="welcome"
str2 ="vasu"
str_res =str1 +str2
print("value after concatinating is {}".format(str_res))

#capitalize -capitalize first character of string
str_a ="vasantha"
a =str_a.capitalize()
print("value after capitalizing string is {}".format(a))
#upper case-coverts string into upper case
upp_case =str_a.upper()
print("upper case values are {}".format(upp_case))
str_b ="PyChArM"
str_b = "pYcHaRm"
low_case = str_b.lower()
print("Lower case values are {}".format(low_case))

str_c="program"
res =str_c[0:2]+str_c[1:4].upper()+str_c[-1]
print("value after capitalizing only 1 is {}".format(res))

# check whether given string is upper
print("The string is upper {}".format(res.isupper()))
str_upp ="VASU"
print("The string is upper {}".format(str_upp.isupper()))
# check whether given string is lower
print("the string is lower {}".format(res.islower()))
str_low ="vasu"
print("the string is lower {}".format(str_low.islower()))

#Title
str_x ="welcome to Github"
tit_str =str_x.title()
print("the value converting into title {}".format(tit_str))

# to check whether title or not
print("the string is title {}".format(str_x.istitle()))
print("the string is title {}".format(tit_str.istitle()))

#count
str_a ="vasantha"
print(" the count of v in string is {}".format(str_a.count("v")))
print("the count of h in string is {}".format(str_a.count("h")))

str_x ="welcome to class"
print("the count of 2 in string is {}".format(str_x.count("2")))
print("the count of 1 in string is {}".format(str_x.count("1")))

#index
print("index value of s in str x is {}".format(str_x.index("s")))
print("index value of l in str x is {}".format(str_x.index("l")))

#starts with
str_a ="github"
print("the string is starting with g is {}".format(str_a.startswith("g")))
print("the string is starting with i is {}".format(str_a.startswith("i")))

#ends with
str_b ="welcome"
print("the string is ends with e is {}".format(str_b.endswith("e")))
print("the string is ends with l is {}".format(str_b.endswith("l")))







