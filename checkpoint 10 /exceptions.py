# # SyntaxError
# # print ("Hello, world")
# # Value Error
# try: 
#     x = int(input("What's x?"))
#     print(f"x is equal to  {x}")
# except ValueError:
#     print("x is not a number")
# ZeroDivision Error 
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print ("error invalid argument" )

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))
while True:
    try: 
        x = int(input( "What's? " ))
    except ValueError:
        print("x is not a number ")
    else:
        break
print (f"x is equal to {x}")

def read_small_integer():
    while True:
        input_string = input("please type an integer: ")
        number =  int (input_string)
        if number < 100 and number >=0:
            return number
    except ValueError:
pass
    print("this input is invalid")

        number = read_small_integer()
        print("number," to the power of three is", number **3)