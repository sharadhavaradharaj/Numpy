# # # # lista = list(range(1,11))
# # # # print(lista)
# # # # listb = [x for x in lista if x%2 ==0]
# # # # print(listb)
# # # # listA = list(range(1,11))
# # # # # To get a list of only even numbers
# # # # #listB = [x for x in listA if x %2 == 0]
# # # # print([x for x in listA if x %2 == 0])
# # # # infile = open("text.txt" , "r")
# # # # print([i.rstrip("\n") for i in infile if "line3" in i])
# # # # # def double(x):
# # # # #     return x*2
# # # # # result = [double(x) for x in range (1,11)]
# # # # print([(x*x) for x in range (1,11)])
# # # # def double(x):
# # # #     return x*2
# # # result = [x*2 for x in range (1,11)]
# # # # # for x in range(1,11):
# # # # #     print(double(x))
# # # print("This is ",result)
# # numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# # print([int(x) for x in numbers if x >=0])

# ## 2 create a list of integers which specify the length of each word in
# ## a sentence except for the word 'the'
# # sentence = "the quick brown fox jumps over the lazy dog"

# # print([len(x) for x in sentence.split() if x.lower() != "the"])

# ## 3 Given dictionary is consisted of vehicles and their weights in kilograms. 
# ## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
# ## In the same list comprehension make the key names all upper case.
# dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
# "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# #print(dict[0])
# print([i.upper() for i in dict if dict[i] < 5000])


nummbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

print([x for x in nummbers_list if x>7])

