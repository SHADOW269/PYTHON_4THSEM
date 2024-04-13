import random
class valueOutRange(Exception):
    pass
flag = 0
while flag == 0:
    try:
        minimum = int (input("ENTER THE MIN VALUE: "))
        maximum = int (input("ENTER THE MAX VALUE: "))
        if maximum < minimum:
            print("Max value can't be less than Min Value")
    except:
        print("Enter the Value no:")
    else:
        flag = 1
    rand_no = random.randint (minimum,maximum)
    user_guess = minimum-1
    count = 0
    while rand_no!=user_guess:
        try:
            user_guess = int(input(f"Enter your guess ({minimum}-{maximum}):"))
            if user_guess not in range(minimum,maximum):
                raise valueOutRange
            count = count+1
        except valueOutRange:
            print("Please enter number within {minimum} and {maximum}")
        except:
            print("Please enter the valid number")
        else:
            if user_guess > rand_no:
                print(f"{user_guess} is Higher than Actual value")
            elif user_guess < rand_no:
                print(f"{user_guess} is Lower than the Actual value")
            if count>=5:
                print("your Attempts is over")
                print(quit())
    print(f"You Gussed the correct value in {count} Attempts")