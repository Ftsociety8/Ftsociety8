# # a=int(input("Enter The Number :"))
# # b=int(input("Enter The Second Number :"))
# # c=input("Enter The Symbols :")

# # if c=='+':
# #     print(a+b)
# # elif c=='*':
# #     print(a*b)
# # elif c=='-':
# #     print(a-b)
# # elif c=='/':
# #     print(a/b)

# # for i in range(5):
# #     for j in range(5):
# #         if i == 0 or i == 4:
# #              print('*',end=' ')
# #         else:
# #             if j == 0 or j == 4:
# #                print('*',end=' ')         
# #             else :
# #                  print(' ',end=' ')   
# #     print()    


# # for i in range(4):
# #     for j in range(i+2):
# #         print(' ',end='')
# #     for j in range(3-i):
# #         print('*',end='')
# #     print()  
# # n = int(input("enter the starter number :"))
# # x = int(input("enter the range :"))
# # for  i in range(n,x+1):  
# #     if i%2==1:
# #         print(i)

# # number = int(input("Enter The Number :"))
# # factorial = 1
# # for i in range(1,number+1):
# #     factorial = factorial*i
    
# # print("the factorial of this number {} is {}".format(number,factorial))


# students =[]

# def F(l1):
#     students.append(l1)
    
    
# flag = True

# f = open ('The Student .List .txt','a')
# while flag:
#     id = input("Enter Your ID :")  
#     fname = input("Enter Your First Name :")  
#     lname = input("Enter Your Last Name :")  
#     age = int(input("Enter Your Age :"))  
#     city = input("Enter Your City's Name :")  
#     l1 = [id,fname,lname,age,city]
#     F(l1)
        



#     while True:
#         Ask = input(' Do you want to continue?(y/n):').capitalize()
#         if Ask == 'Y':
#             f.write(f'ID={id}\nFirst Name:{fname}\nLast Name:{lname}\nAge = {age}\ncity = {city}\n=============')
#             break    
#         elif Ask == 'N':
#             f.write(f'ID={id}\nFirst Name:{fname}\nLast Name:{lname}\nAge = {age}\ncity = {city}\n=============')
#             flag = False
#             break
#         else:
#             print("\t\t\t\t\t\t Please Try Again.")  
#     print("=======================================")            

 
# from mysql.connector import connect,Error

# try:
#     with connect(host = 'localhost',
#                 username = 'root',
#                 password ='12345678',
#                 port = 3306
#     )as connection:
#         create_db = 'CREATE DATABASE IF NOT EXISTS bigsmoke'
#         create_table = '''CREATE TABLE users(
#             username VARCHAR(20)NOT NULL,
#             passwd VARCHAR(20)NOT NULL
#         )'''
#         with connection.cursor() as crsr:
#             crsr.execute(create_db)
#             connection.connect(database ='bigsmoke')
#             crsr.execute(create_table)
# except Error as e:
#     print(e) 


