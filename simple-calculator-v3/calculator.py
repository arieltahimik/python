# 1. Input functions

def get_number(prompt='Enter a number: '):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print('Invalid input! Please enter a number.\n')


def get_operator():
  while True:
    operator = input('Enter operator (+, -, *, /): ').strip()

    if operator in ['+', '-', '*', '/']:
      return operator

    print('Invalid operator! Please choose again.\n')


def get_continue():
  while True:
    again = input('\nAgain (y/n)? ').strip().lower()
    if again == 'y':
      return True
    if again == 'n':
      return False
    print('Invalid input! Please enter y or n.')


# 2. Arithmetic functions

def addition(a, b):
  return a + b


def subtraction(a, b):
  return a - b


def multiplication(a, b):
  return a * b


def division(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return None


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
    else:
      result = division(first_number, second_number)

    if result is None:
      print('Error: Cannot divide by zero!')
    else:
      print(f'Result: {result}')

    if not get_continue():
      break
    print()

  print('Goodbye!')


# 4. Program entry point

if __name__ == "__main__":
  main()
