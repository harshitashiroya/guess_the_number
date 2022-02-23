n=18
number_of_guessing=1

while(number_of_guessing<=5):
    print("Enter your number:")
    num=int(input())
    if num<n:
        print("your guessing number is low")
    elif num>n:
        print("your guessing number is high")
    else:
        print("Congratulation you guess the right number")
        print(number_of_guessing,"times you guess the number")
        break
    print(5-number_of_guessing,"try remaining")
    number_of_guessing=number_of_guessing+1

if number_of_guessing>5:
    print("Sorry,Game Over!")



