
# Type casting
# a = "10" # type string
# b = 20.25 # type float
# # sum = a + b # TypeError: can only concatenate str (not "float") to str
# c = float(a)
# sum = c + b # Type casting string to float
# print(sum)
#----------------------------------
# Program to take two inputs from the user and print thier sum
# print ("Sum of two numbers : ")
# a = int (input ("Enter first number : "))
# b = int (input ("Enter the second number : "))
# sum = a + b
# print ("Sum of two numbers is : ", sum)
#--------------------------------------------
#program to take the side of a square from the user and print the area of the square
# print ("Area of square : ")
# side = float (input ("Enter the side of square : "))
# area = side * side
# print ("Area of square is : ", area)
#---------------------------------------------
#program to take two floating point numbers and print thier average
# print ("Average of two numbers : ")
# a = float (input ("Enter the first number :"))
# b = float (input ("Enter the second number :"))
# avg = (a + b) / 2   
# print ("Average of two numbers is : ", avg)
# ---------------------------------------------
# strings in python :
# str = "Python is a programming language"
# str1 = 'Python is a programming language'
# str2 = """Python is a programming language"""
# print (str)
# print (str1)
# print (str2)
# Strings are immutable in python, we cannot change the value of a string once it is created.
# #   \n is used to print the next string in new line
# print ("Hello\nWorld")
# # \t is used to print the next string after a tab space
# print ("Hello\tWorld")  
# # CONCATINATION OF STRINGS
# str3 = str + str1
# print (str3) # Python is a programming languagePython is a programming language
# # length of string
# print (len(str3)) # 56
# print (len(str1)) # 34
# str4 = str + " " + str1
# print (str4) # Python is a programming language Python is a programming language
# print (len(str4)) # 70
# # indexing of string
# print (str4[0]) # P
# print (str4[1]) # y
# print (str4[6]) # space 
# # Slicing of string
# # str4[start:end] # start index is inclusive and end index is exclusive
# print (str4[0:6]) # Python
# print (str4[7:17]) # is a programming
# print (str4[0:len(str4)]) # Python is a programming language Python is a programming language
# print (str4[0:]) # Python is a programming language Python is a programming language
# print (str4[:len(str4)]) # Python is a programming language Python is a programming
# # in python we can do negative indexing also
# print (str4[-1]) # g
# print (str4[-2]) # n
# # slicing with negative indexing
# print (str4[-10:-1]) # language
# # string methods
# str5 = "python is a programming language"
# print (str5.upper()) # PYTHON IS A PROGRAMMING LANGUAGE
# print (str5.lower()) # python is a programming language
# print (str5.capitalize()) # Python is a programming language
# print (str5.title()) # Python Is A Programming Language
# #string comparison
# print (str5 == "python is a programming language") # True   
# print (str5.startswith("python")) # True
# print (str5.endswith("language")) # True
# #string searching
# print (str5.find("programming")) # 14   
# # string replacement
# str6 = str5.replace("programming", "coding")
# print (str6) # python is a coding language
# # string split
# str7 = str5.split(" ")  
# print (str7) # ['python', 'is', 'a', 'programming', 'language']
# # string join
# str8 = "-".join(str7)
# print (str8) # python-is-a-programming-language
# # find function returns the index of the first occurrence of the substring, if found. If not found, it returns -1.
# print (str5.find("python")) # 0
# print (str5.find("Java")) # -1
# print (str5.find("is")) # 7
# # count function returns the number of occurrences of the substring in the string.
# print (str5.count("is")) # 1    
# print (str5.count("a")) # 4

# Some programs to practice string methods
# # 1. Program to take input user's first name and print its length
# print ("Hello, welcome to string methods practice programs")
# first_name = input("Enter your first name : ")
# print ("Length of your first name is : ", len(first_name))

# # 2. program to find the occurrence of $ in the a string
# str9 = input("Enter a string : ")
# print ("Occurrence of $ in the string is : ", str9.count("$"))
