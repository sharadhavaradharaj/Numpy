

'''
remainder = lambda num: num % 2
print(type(remainder)) # Its a function
print(remainder(5)) # Its  a value


product = lambda x,y : x+y
print(product(2,3))

def testfunc(num):
    print(num)
    return lambda x: x*num
result10 = testfunc(10)

# Passing the above cde in Lambda expression directly
result10 = lambda x: x*10
print(result10)
result100 = lambda x: x*100
print(result100)
'''

nummbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

# General use of function
def filter_list(num):
    if num >7:
        return num
    
result = list( filter(filter_list, nummbers_list))
print(result)

# using lambda 
result = list( filter(lambda num: (num>7), nummbers_list)) # filter ==>produces True or false
print(result)

#using mapp function

mapped_list = list(map(lambda num: num % 2, nummbers_list))# itterates every object the elements
print(mapped_list)