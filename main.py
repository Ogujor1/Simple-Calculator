print("TWO NUMBERS SIMPLE CALCULATOR")

response1 = float(input(" Type any number;\n"))
response2 = float(input("Type another number;\n"))

response3 = input("Pick an operator;\n + \n- \n* \n/ \n")
operators = ["+", "-", "*", "/"]


def add_no(n1, n2):
    return n1 + n2


def sub_no(n1, n2):
    return n1 - n2


def multiply_no(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

need_to_operate =  True

while need_to_operate:

    if response3 == "+":
        answer = add_no(response1, response2)
        print(f"Your result is: {answer}")
    elif response3 == "-":
        answer = sub_no(response1, response2)
        print(f"Your result is: {answer}")
    elif response3 == "*":
        answer = multiply_no(response1, response2)
        print(f"Your result is: {answer}")
    elif response3 == "/":
        answer = divide(response1, response2)
        print(f"Your result is: {answer}")

    else:
        if response3 not in operators:
            print("Wrong Operator Chosen")
            check_again = input("You need to try? Type 'Yes' or 'No' ")
            if check_again.lower() == "yes":
                response1 = float(input(" Type any number;\n"))
                response2 = float(input("Type another number;\n"))
                response3 = input("Pick an operator;\n + \n- \n* \n/ \n")
            else:
                print("Goodbye")
    need_to_operate = False