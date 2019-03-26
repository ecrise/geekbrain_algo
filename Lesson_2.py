from random import randint

def calculate()->None:
    """ simple calculator """
    continue_calc = True
    while continue_calc:
        first_val = float(input("Please enter a first number: "))
        second_val = float(input("Please enter a second number: "))
        operation = input("Please enter a required operation (+, -, *, /) or 0 for exit: ")
        if operation == "0":
            continue_calc = False
        elif operation == "+":
            print("Your result is", first_val + second_val)
        elif operation == "-":
            print("Your result is", first_val - second_val)
        elif operation == "*":
            print("Your result is", first_val * second_val)
        elif operation == "/":
            if second_val == 0:
                print("You enter incorrect second number - division by zero")
            else:
                print("Your result is", first_val / second_val)
        else:
            print("You enter incorrect data")
    return 0

def num_count()->int:
    even_count = 0
    odd_count = 0
    num = input("Please enter a number: ")
    for ch in num:
        if int(ch) % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
    print("In the number you enter there is", even_count, "even digigts and", odd_count, "odd digits!")
    return 0

def num_reverse()->int:
    num = input("Please enter a number: ")
    print("The inverse number is", num[-1::-1])
    return 0


def geometr_sum()->int:
    num = int(input("Please enter a number: "))
    sum = (1-(-0.5)**num)/1.5
    print("The of", num, "first members of geometrical progression is", sum) 
    return 0

def ascii_table()->int:
    num = 32
    for i in range(10):
        for j in range(10):
            print(num, "-", chr(num), sep="", end=" | ")
            if num == 127:
                return 0
            num += 1
        print()

def random_game()->int:
    continue_game = True
    while continue_game:
        random_num = randint(0,100)
        end_game = False
        attempt_num = 0
        while not(end_game):
            user_num = int(input("Please enter a number: "))
            if random_num == user_num:
                end_game = True
                print("You WIN!!!")
                continue_game = True if input("Do you want to repeat? (y/n)?") == "y" else False
            elif random_num < user_num:
                print("The number you enter is greater than it shall be")
            else:
                print("The number you enter is lower than it shall be")
            attempt_num += 1
            if attempt_num == 11:
                end_game = True
                print("You lose. The namber was", random_num)
                continue_game = True if input("Do you want to repeat? (y/n)?") == "y" else False
    return 0

def expression()->int:
    n = int(input("Please enter a number: "))
    sum = 0
    for i in range(1,n+1):
        sum += i
        calc_exp = n*(n+1)/2
    if sum == calc_exp:
        print("Summary is", sum, "and calculates value is", calc_exp, "It prooved!!!")
    else:
        print("Mathematics lowes are over!")
        
def digit_calc()->int:
    num = int(input("Please enter a number of numbers you want to enter: "))
    digit = int(input("Please enter a digit you want to calculate: "))
    print("Plese enter all", num, "numbers!")
    num_str = ""
    for i in range(1,num+1):
        print("enter", i, "number: ", end="")
        current_num = input()
        num_str += current_num
    digit_count = 0
    for ch in num_str:
        if int(ch) == digit:
            digit_count += 1
    print("In the sequens of numbers you enter, the digin", digit, "meets", digit_count, "times")
    return 0


def max_sum_number()->int:
    num = int(input("Please enter a number of numbers you want to enter: "))
    print("Plese enter all", num, "numbers!")
    max_digit_sum = 0
    for i in range(1,num+1):
        print("enter", i, "number: ", end="")
        digit_sum = 0
        current_num = input()
        for ch in current_num:
            digit_sum += int(ch)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            max_num = current_num
    print("In the sequens of numbers you enter, the number with max summary of digits is", max_num)
    return 0


menu = {
    "Simple calculator" : calculate,
    "Calculate even & odd" : num_count,
    "Reverse number": num_reverse,
    "Cakculate geometric progressive" : geometr_sum,
    "Show ASCII table" : ascii_table,
    "Play game" : random_game,
    "Mathematics expression" : expression,
    "Count a digit in sequense of numbers" : digit_calc,
    "Fidn max number" : max_sum_number,
    "Exit" : exit
    }
        
while True:
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")
    command = int(input("Enter a command: "))
    if 1 <= command <= len(menu):
        key = list(menu.keys())[command - 1]
        print("______________________________")
        menu[key]()
        print("______________________________")
    else:
        print("You enter wrong command!")       
