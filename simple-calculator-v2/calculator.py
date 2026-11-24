# 1. Input functions

def get_number(prompt='Enter a number: '):
  return float(input(prompt))

def get_operator():
  # strip will remove accidental spaces
  return input('Choose an operation (+, -, *, /): ').strip()


# 2. Arithmetic functions

def addition(a, b):
  return a + b

def subtraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  if b == 0:
    return None
  return a / b


# 3. Main function
def main():
  while True:
    first_number = get_number('Enter first number: ')
    second_number = get_number('Enter second number: ')
    operator = get_operator()

    if operator == '+':
      result = addition(first_number, second_number)
    elif operator == '-':
      result = subtraction(first_number, second_number)
    elif operator == '*':
      result = multiplication(first_number, second_number)
    elif operator == '/':
      result = division(first_number, second_number)
    else:
      result = 'Invalid operator!'

    if result is None:
      print('Error: Cannot divide by zero!')
    else:
      print(f'Result: {result}')

    again = input('\nAgain (y/n)? ')

    if again.strip().lower() != 'y':
      break
    print()

  print('Goodbye!')


# 4. Program entry point
if __name__ == "__main__":
  main()
