str_a = "hello"
for i in str_a:
    print(i)

lst_a = ["a","b","c","d"]
for i in lst_a:
    print(i)

tpl_a = ("e", "f","g")
for i in tpl_a:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    print(i)
for i in str_y:
    print(i)

str_x ="xyz"
str_y ="abc"
for i in str_x:
    for j in str_y:
        print((i,j))

str_a = "John is clever"
res =[]
split_stra = str_a.split(" ")
for i in split_stra:
      res.append(i[::-1])
rev_str =" ".join(res)
print("the reverse string is {}".format(rev_str))

# squares with list comprehension
lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqrd_lst = [i**2 for i in lst_to_sqr]
print("the sqared value of list items is {}".format(sqrd_lst))

for i in range(0, 5):
    print(i)
for i in range(0,10):
    print(i)
#square the number from 1 to 9
lst_sqr = [i**2 for i in range (1,10)]
print("the square from range 1 to 10 is {}".format(lst_sqr))
print([i**2 for i in range (1,10)])

# sum from 1 to 10
lst_to_sum = [1,2,3,4,5,6,7,8,9,10]
summation =0
for i in lst_to_sum:
    summation = summation+i
print("the sum of all items in list is {}".format(summation))

# using range function
sum_of_items = 0
for i in range (1,11):
    sum_of_items = sum_of_items+i
print("the sum of items from range 1 to 11 is {}".format(sum_of_items))

#assignment
# find cubes
lst_cube = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_to_cube = [i**3 for i in range (1,10)]
print("the cube from range 1 to 10 is {}".format(lst_cube))
print([i**3 for i in range(1,10)])

# sum of range 1,100
sum_of_items =0
for i in range (1,101):
    sum_of_items = sum_of_items+i
print("the sum of range from 1 to 101 is {}".format(sum_of_items))

str_x = "Python"
len_str_x = len(str_x)
for i in range(0,len_str_x):
    print("the value of {} index is {}".format(i, str_x[i]))

lst_x =[1,2,3,4]
lst_y =[5,6,7,8]
len_lst_x =len(lst_x)
sum_lst_x_y = []
for i in range (0,len_lst_x):
    summation = lst_x[i]+lst_y[i]
    sum_lst_x_y.append(summation)
print("the sum of two lists are {}".format(sum_lst_x_y))

lst_x = [1,2,3,4]
lst_y = [5,6,7,8]
summation = [lst_x[i]+lst_y[i] for i in range(0, len(lst_y))]
print("the sum of two lists is {}".format(summation))

# count of characters
str_y = "Alex is in class"
for i in str_y:
    cnt =str_y.count(i)
    print("the character {} occured {} time".format(i,cnt))

# reverse string without string

str_y ="hello"
rev_str =""
for i in str_y:
    rev_str = i+rev_str
print("the value after reversing string is {}".format(rev_str))



















