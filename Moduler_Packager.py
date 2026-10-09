import datetime
import time
import math
import random
import string
import uuid


# 1. DateTime and Time Operations
def datetime_operations():

    while True:
        print("\nDateTime and Time Operations:")
        print("1. Display Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            current = datetime.datetime.now()
            print("Current Date and Time:",
                  current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            d1 = input("Enter First Date (YYYY-MM-DD): ")
            d2 = input("Enter Second Date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            print("Difference:", abs((d2 - d1).days), "days")

        elif choice == "3":
            date = input("Enter Date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            print("Formatted Date:", date.strftime("%d-%m-%Y"))

        elif choice == "4":
            print("Stopwatch Started...")
            start = time.time()
            input("Press Enter to Stop: ")
            elapsed = time.time() - start
            print("Elapsed:", round(elapsed, 2), "seconds")

        elif choice == "5":
            seconds = int(input("Enter seconds: "))

            while seconds > 0:
                print("Time remaining:", seconds)
                time.sleep(1)
                seconds -= 1

            print("Time's Up!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


# 2. Mathematical Operations
def mathematical_operations():

    while True:
        print("\nMathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Logarithms Calculation")
        print("4. Trigonometric Calculation")
        print("5. Area of Shapes")
        print("6. Back to Main Menu")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter number: "))
            fact = 1
            for i in range(1,num +1):
                fact = fact *i
            else:
                print("Factorial:",fact)

        elif choice == "2":
            p = float(input("Enter principal: "))
            r = float(input("Enter rate (%): "))
            t = float(input("Enter time in years: "))

            amount = p * (1 + r / 100) ** t
            print("Compound Interest:",amount - p)

        elif choice == "3":
            num = float(input("Enter number: "))
            print("Logarithm (base 10):", math.log10(num))
            print("Natural Logarithm:", math.log(num))

        elif choice == "4":
            angle = float(input("Enter angle in degrees: "))
            
            print("Sin:", math.sin(math.radians(angle)))
            print("Cos:",math.cos(math.radians(angle)))
            print("Tan:", math.tan(math.radians(angle)))


        elif choice == "5":
            print("\nArea of Shapes:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Square")
            print("4. Triangle")

            shape = input("Enter choice: ")

            if shape == "1":
                r = float(input("Enter radius: "))
                print("Area of Circle:", math.pi * r * r)

            elif shape == "2":
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print("Area of Rectangle:", l * w)

            elif shape == "3":
                s = float(input("Enter side: "))
                print("Area of Square:", s * s)

            elif shape == "4":
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                print("Area of Triangle:", 0.5 * b * h)

            else:
                print("Invalid Shape!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

# 3. Random Data Generation
def random_operations():

    while True:
        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back to Main Menu")
        print("===============================")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            numbers = [random.randint(1, 100) for i in range(5)]
            print("Random List:", numbers)

        elif choice == "3":
            password = ""
            for i in range(8):
                password += random.choice(string.ascii_letters+string.digits)
            print("Password:",password)
            

        elif choice == "4":
            print("OTP:", random.randint(100000, 999999))

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# 4. UUID Operations
def uuid_operations():

    while True:
        print("\nGenerate Unique Identifier (UUID)")
        print("1. Generate UUID")
        print("2. Back to Main Menu")
        print("===============================")

        choice = input("Enter choice: ")

        if choice == "1":
            unique_id = uuid.uuid4()
            print("UUID:", unique_id)

        elif choice == "2":
            break

        else:
            print("Invalid choice!")


# 5. File Operations (Custom Package)
from mypackage import file_operations


def file_operation():

    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("===============================")

        choice = input("Enter choice: ")

        if choice == "1":
            file_operations.create_file()

        elif choice == "2":
            file_operations.write_file()

        elif choice == "3":
            file_operations.read_file()

        elif choice == "4":
            file_operations.append_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# 6. Explore Module Attributes
def explore_modules():
        print("\nExplore Module Attributes:")

        module = input("Enter module name and Explore: ").strip()

        if module == "":
            return

        elif module.lower() == "math":
            print("\nAvailable Math Attributes in math module:")
            print(dir(math))

        elif module.lower() == "random":
            print("\nAvailable Random Attributes in random module:")
            print(dir(random))

        elif module.lower() == "datetime":
            print("\nAvailable DateTime Attributes in datetime module:")
            print(dir(datetime))

        elif module.lower() == "time":
            print("\nAvailable Time Attributes in time module:")
            print(dir(time))

        else:
            print("Invalid module name!")
# 7. Main Menu
def main():

    while True:
        print("\n===============================")
        print("   MODULAR AND PACKAGES TOOLKIT")
        print("===============================")

        print("1. DateTime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")
        print("===============================")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            datetime_operations()

        elif choice == "2":
            mathematical_operations()

        elif choice == "3":
            random_operations()

        elif choice == "4":
            uuid_operations()

        elif choice == "5":
            file_operation()

        elif choice == "6":
            explore_modules()

        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start Program
if __name__ == "__main__":
    main()
