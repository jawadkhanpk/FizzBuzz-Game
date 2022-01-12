# if the number is divisible by 3 then it will be a fizz
# if the number is divisible by 5 then it will be a buzz
# if the number is divisible bt both 3 & 5 then it will be a fizzbuzz

for num in range(0, 101):
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)