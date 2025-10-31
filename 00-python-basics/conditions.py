# def main():
#         x = int(input("What is x? "))
#         if isEven(x):
#             print("Even")
#         else:
#             print("Odd")

# def isEven(num):
#     return num % 2 == 0

# main()



from email.policy import default


name = input("Enter the name ")
match name:
    case "Peter" | "Jake":
        print("Bake")
    case "Jane":
        print("Blue")
    case _:
        print("Who?")
