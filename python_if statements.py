a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a>b:
    diff =a-b
    print(diff)
elif a<b:
    summation =a+b
    print(summation)
# the other way of writing above code
if a>b:
    diff =a-b
    print(diff)
else:
    summation =a+b
    print(summation)
lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_y)
sum_lst_x_y = []
for i in range (0, len_lst_x):
    summation =lst_x[i]+lst_y[i]
    sum_lst_x_y.append(summation)
print("the sum of two lists are {}".format(sum_lst_x_y))

# using list comprehension
lst_a = [1, 2, 3, 4]
lst_b = [5, 6, 7, 8]
summation = [lst_a[i]+lst_b[i] for i in range (0,len(lst_b)) if len(lst_a)==len(lst_b)]
print("the sum of two lists using list comprehension is {}".format(summation))

# if list lenghts are not same
lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_x)
sum_lst_x_y = []
if len (lst_x)==len(lst_y):
    for i in range(0, len_lst_x):
        summation = lst_x[i]+lst_y[i]
        sum_lst_x_y.append(summation)
print("the sum of two lists are {}".format(sum_lst_x_y))

# check given string is palindrome or not
str_to_check = input("Enter the value: ")
str_rev = str_to_check [::-1]
if str_to_check ==str_rev:
    print("the given string is palindrome")
elif str_to_check != str_rev:
    print("the given string is not a palindrome")

str_a ="python"
# str_to_check = input("Enter the value:")
if str_a == str_a [::-1]:
    print("the given string is palindrome")
else:
    print("the given string is not a palindrome")

# check whether given number is even or odd
num_to_check =  int(input("Enter the value: "))
if num_to_check % 2 == 0:
    print("the given number is even")
else:
    print("the given number is odd")
# make a list of even numbers and make a list of odd numbers
# even_lst = []  odd_lst = []

# find the largest among a,b,c numbers
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
if a > b and a > c:
    print("a is greater")
elif b >a and b > a:
    print("b ia greater")
else:
    print("c is greater")





