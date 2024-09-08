numbers = []
for iter in range(1, 11):
    user_input = int(input(f'Enter number {iter} => '))
    numbers.append(user_input)

result = sum(numbers)
print(f'\nThe total is {result}.')