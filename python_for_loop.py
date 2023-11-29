
# squares of elements in list
lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqr_lst = []
for i in lst_to_sqr:
    sqr_lst.append(i*i)
print("the squared values is {}".format(sqr_lst))

# squares with list comprehension
lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqrd_lst = [i**2 for i in lst_to_sqr]
print("The squared value of list items is {}".format(sqrd_lst))

for i in range(0, 5):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(1, 10, 2):
    print(i)

# square the numbers from 1 to 9
lst_sqr = [i**2 for i in range(1, 10)]
print("The square from range 1 to 10 is {}".format(lst_sqr))
# print([i**2 for i in range(1, 10)])

# sum from 1 to 10
lst_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summation = 0
for i in lst_to_sum:
    summation = summation+i
print("The sum of all items in list is {}".format(summation))

# using range function
sum_of_items = 0
for i in range(1, 11):
    sum_of_items = sum_of_items+i
print("The sum of range of items from 1 to 11 is {}".format(sum_of_items))

# find the sum from range 1, 100
sum_of_items = 0
for i in range(1, 101):
    sum_of_items = sum_of_items+i
print("the sum of range of items from 1 to 101 is {}".format(sum_of_items))

# find the cubes from the number 1 to 9
list_cube =[i**3 for i in range(1, 10)]
print("the cube from range 1 to 10 is {}".format(list_cube))
print([i**3 for i in range(1, 10)])







