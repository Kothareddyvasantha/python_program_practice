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
print("the sum of two tuples are {}".format(sum_lst_x_y))

