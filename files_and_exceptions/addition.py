# adding two input numbers together
print("Let's add two numbers together.")
print("Type 'q' when done entering numbers.")

while True:
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number!")
    else:
        print(f"The answer to these numbers are: {answer}")