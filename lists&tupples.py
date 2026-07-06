#List :
#   A built-in data structure in python which is used to store multiple items in a single variable.
#   Lists are mutable, ordered and allows duplicate elements.    
#   e.g. list1 = [1, 2, 3, 4, 5]
# print ("List : ")
# list1 = [1, 2, 3, 4, 5]
# print (list1)
# print ("First element of list1 is : ", list1[0])
# print ("Last element of list1 is : ", list1[-1])
# print ("Length of list1 is : ", len(list1))
# print (type(list1)) # <class 'list'>
# #   Lists can contain elements of different data types.
# list2 = [1, "Hello", 3.14, True]
# print ("List with different data types : ", list2)
# # lists are mutable, we can change the value of an element in a list.
# list1[0] = 10
# print ("List after changing the first element : ", list1)
# # List slicing
# print ("List slicing : ", list1[1:4]) # [2, 3, 4]
# # List methods
# list1.append(6)
# print ("List after appending an element : ", list1)
# list1.remove(3)
# print ("List after removing an element : ", list1)   
# list2 = [7, 8, 9]
# list2.insert(2, 3)
# print ("List after inserting an element : ", list2) 
# list2.sort()
# print ("List after sorting : ", list2  )
# list2.reverse()
# print ("List after reversing : ", list2)
# list2.pop(1)
# print ("List after popping an element : ", list2)
# # -----------------------------------------------
# # Tuples :
# #   A built-in data structure in python which is used to store multiple items in a single variable.
# #   Tuples are immutable, ordered and allows duplicate elements.
# tuple1 = (1, 2, 3, 4, 5)
# print ("Tuple : ", tuple1)
# print ("First element of tuple1 is : ", tuple1[0])
# print ("Last element of tuple1 is : ", tuple1[-1])
# print ("Length of tuple1 is : ", len(tuple1))
# print (type(tuple1)) # <class 'tuple'>
# # slicing of tuple
# print ("Tuple slicing : ", tuple1[1:4]) # (2, 3, 4)
# # tuple methods
# tuple2 = (1, "Hello", 3.14, True)
# print ("Tuple with different data types : ", tuple2)
# tuple2.count(1) # 1
# tuple2.index("Hello") # 1
# # ------------------------------------------------
# # practice programs on lists and tuples
# # ------------------------------------------------
# # Program to take input of three movie names from user and store them in a list.
# print ("Enter three movie names : ")
# movies = []
# movie1 = input("Enter your first movie name : ")
# movie2 = input("Enter your second movie name : ")  
# movies.append(movie1)
# movies.append(movie2)   
# movies.append(input("Enter your third movie name : "))
# print ("List of movies : ", movies) 
# #  -------------------------------------------------
# # Program to check if a list contains a palindrome of elements or not.
# list3 = [1,2,3,4,1]
# list4 = list3.copy()
# list4.reverse()
# if (list3 == list4):
#     print ("List is a palindrome ")
# else:
#     print ("List is not a palindrome")    
# -------------------------------------------------
# Program to cont number of grade A in a marks tuple.
marks = ("A", "B", "C", "A", "D", "A", "B")
print ("Number of grade A in marks tuple is : ", marks.count("A"))
# Now store this tuple  in a list and sort them from "A" to "D"
marks_list = list(marks)#explict type casting
marks_list.sort()
print ("Sorted marks list : ", marks_list) 