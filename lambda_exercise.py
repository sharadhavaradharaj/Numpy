''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, list1))
odd_numbers = list(filter(lambda x: x % 2 != 0, list1))
print(even_numbers)
print(odd_numbers)




''' 2)
find which days of the week have exactly 6 characters.
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = [day for day in weekdays if len(day) == 6]
print("Days with 6 characters:", days)







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

list2 = ['orange', 'red', 'green', 'blue', 'white', 'black']

list3= ['orange', 'black']

result = list(filter(lambda word: word not in list3, list2))

print(result)








''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

result = list(filter(lambda word: word not in list3, list2))








''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
colors =['red', 'black', 'white', 'green', 'orange']
string = "ack"

result = list(filter(lambda x :string in x, colors))

print(result)


# 6)
#Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


list1 = [5,3,7,2,9]
list2 = sorted(list1)
print(list2)

original_scores.sort()
print(original_scores)

# To get the output in an acending order of marks along with the subjects
original_scores.sort(key=lambda x: x[1])
print(original_scores)


''' 7)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful). Use all three of the below
varaitions (str1, str2, str3) to check if your program works. It should FAIL for str1 and str2 and PASS for str3.
'''

str1 = "HELLO"
str2 = "hello"
str3= "Hello8world"


# Whenever the lambda is used its output is a function
result = lambda somestring: any(
    [x.isupper for x in somestring]
    and [x.islower() for x in somestring]
    and [x.isdigit() for x in somestring]
    and [len(somestring) > 7]
)
if result(str1):
    print("pass")
else:
    print("fail")

if result(str2):
    print("pass")
else:
    print("fail")

if result(str3):
    print("pass")
else:
    print("fail")