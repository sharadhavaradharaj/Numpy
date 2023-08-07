'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

	
# A short way to remember LC is:

#result  = [*transform/expression*    *iteration*         *filter/condition*     ]


#Exercise 1
list1 = list(range(1,11)) # ranges from 0 to 10

list2 = []
for x in list1:
    if x>5:
        list2.append(x*2)
print(list2)

#List comprehension method

list2 = [x*2 for x in list1 if x>5]
print(list2)

# **********************************************# 

#Exercise 2
list3 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

# **********************************************#  

#Exercise 3                 

listOfWords = ["this" , "is" , "a" , "list" , "of" , "words"]

#Index value should be mentioned if its a string to obtain each letter of a word
items = [word[0] for word in listOfWords] 
print(items)

# When index value is not mentioned, it gives the whole word which inturn is the list
items = [word for word in listOfWords]
print(items)

# **********************************************# 

#Exercise 4
lower = [x.lower() for x in ["A", "B", "C"]]
print(lower)

# **********************************************# 
#Exercise 5

listA = list(range(1,11))

# To get a list of only even numbers
listB = [x for x in listA if x %2 == 0]
print(listB)

# **********************************************# 

#Exercie 6

string = "Hello 12345 world"

# Use isdigit function to extract only numbers from the string,the output is in string format
number = [x for x in string if x.isdigit()]
print(number)

# Convert it into integer
number = [int(x) for x in string if x.isdigit()]
print(number)

# using list comprehension
print([int(x) for x in string if x.isdigit()])

# To extract only words use .isalpha
words = [x for x in string if x.isalpha()]
print(words)

# Convert the string to uppercase
words = [x.upper() for x in string if x.isalpha()]
print(words)

# Convert the string to uppercase
words = [x.lower() for x in string if x.isalpha()]
print(words)

# **********************************************# 

#Exercise 7 (from text.txt file)

# To generate only the line 3 from the file and rstrip is used in the expression part of the code
infile = open("text.txt" , "r")
result= [i.rstrip("\n") for i in infile if "line3" in i]
print(result)

# **********************************************# 


#Exercise 8

# To get the values double of x if x ranges from 1 to 10
def double(x):
    return x*2
result = [double(x) for x in range (1,11)]
for x in range(1,11):
    print (x)
print("Hello",result)

# **********************************************# 

#Exercise 9 
# using 2 arguments 
result = [x+y for x in [10,30,50] for y in [20,40,60]]
print(result)




