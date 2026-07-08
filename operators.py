# data = (1, 2, 3, 4, 5)
# data[0] = 10  # This will raise an error because tuples are immutable
# print(data)
######

# x = (1, 2, 3)
# print(x.count(2))  # Output: 1
#######
# X=('vinay','dhoni','rohit','virat','dhoni','dhoni')
# print(X.count('dhoni'))
######
# num=(1, 2, 3, 4, 5)
# print(num[1:4])  # Output: (2, 3, 4)
######
#sets
# set is a collection of unique elements, meaning it does not allow duplicate values. Sets are unordered, which means that the items do not have a defined order, and they cannot be accessed by index. 
#sets
# set is a collection of unique elements, meaning it does not allow duplicate values. Sets are unordered, which means that the items do not have a defined order, and they cannot be accessed by index. 
# x={1, 2, 3, 4, 5}
# print(x)
#######
# a={1, 2, 3, }
# b={1, 2, 3, 4, 5}
# print(a & b)  
# print(a | b) 
# print(a - b)
# print(a ^ b)
####
# def add(a, b):
#     print(a + b)
# add(10, 5)
######
# def add(numbers):
#      total =0
#      for i in numbers:
#          total += i
#          print("Sum:", total)
#          add(10, 20, 30, 40)
#####
# def squareroot(num):
#     return num ** 0.5
# print(squareroot(16))
#####
# def square(num):
#      return num ** 2
# print(square(6))
#####
# square=lambda x:x*x
# print(square(12))
#####
# check_num = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(check_num(7))   
# print(check_num(12))
######
# to_upper = lambda x: x.upper()
# to_lower = lambda x: x.lower()

# print(to_upper("hello"))  
# print(to_lower("WORLD"))
######
# file = open("student.txt")
# file.write("hello")
# file.close()
# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close()
#######
# file = open("test.txt", "w")
# file.write("hello")
# file.close()
# print("file created successfully")

# file = open("test.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("test.txt", "a")
# file.write("\nworld")
# print("data appended successfully")
# file.close()

# file = open("test.txt", "r")
# print(file.read())
# file.close()
######
# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("only numbers are allowed")
######
# try:   
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")
#####
try:
    print(10/2)
except:
    print("error")
else:
    print("no error")