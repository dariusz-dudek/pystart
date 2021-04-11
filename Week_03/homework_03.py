def get_factorial(number: int) -> int:
    result = 1
    while not number == 1:
        result *= number
        number -= 1
    return result


end = True
while end:
    num = input("Enter the number and program will calculate the strengths: ")
    if num.isdecimal():
        print(f'The strengths for number {num} is {get_factorial(int(num)):,} ')
        end = False
    else:
        print('Wrong answer')


