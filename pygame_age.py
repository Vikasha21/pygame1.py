def math_trick():
    print("Welcome to the Magic Age Guessing Game!")
    print("Think of your age (but don't tell me). Now follow these steps:")

    print("\nStep 1: Multiply your age by 2.")
    print("Step 2: Add 5 to the result.")
    print("Step 3: Multiply the result by 50.")
    print("Step 4: If you have already had your birthday this year, add 1773.")
    print("If not, add 1772.")
    print("Step 5: Subtract the year you were born from the result.")

    print("\nEnter the final result:")

    final_result = int(input())
    
    age = (final_result - 250) // 100

    print(f"\nTa-da! Your age is {age}! Was I right?")

if __name__ == "__main__":
    math_trick()
