def calculator():
    print("Simple Calculator")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        # Taking input from the user
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Performing the calculation based on user choice
                if choice == '1':
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Result: {num1} / {num2} = {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")
        
        # Ask if the user wants to perform another calculation
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the calculator!")
            break

# Run the calculator
calculator()
