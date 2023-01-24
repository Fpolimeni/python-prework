# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):
#        print("Hello," + user_name.title() + "!" )

# hello_name('Frank') 

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds():
#   first_odds = [str(x) for x in range(100) if x%2 == 1]
#   print(first_odds)

#   Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# def max_num_in_list(a_list):
#    max = a_list[ 3 ]
#    for a in a_list:
#         if a > max:
#             max = [a]
#         return max
# print(max_num_in_list([1, 13, 25, 100000000, 2]))

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

# def is_leap_year (a_year):
#     if a_year % 400 == 0:
#         if a_year % 400 == 0:
#             print(a_year, "is a leap year.")
#     elif a_year % 4 != 0:
#         print(a_year, "is not a leap year.")
# (is_leap_year(2000))

# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list =[1,3, 4,8]
    a_list = list(filter(None,a_list))
    a_list = sorted(a_list)
    if len(a_list) > 1:
        maximum = a_list[-1]
        minimum = a_list[0] - 1
        if minimum == 0:
            if sum(a_list) == (maximum * (maximum+1) /2):
                return True
            else:
                return False
        else:
            if sum(a_list) == (maximum * (maximum+1) /2) - (minimum * (minimum+1)/2):
                return True
            else:
                return False
    else:
            return True
print(is_consecutive(list))