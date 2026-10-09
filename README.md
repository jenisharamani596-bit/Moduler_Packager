# 🚀 Modular & Package – Multi-Utility Toolkit

**Author:** Jenisha Ramani

**Project Name:** Modular & Package – Multi-Utility Toolkit

## 📌 Project Overview

**Modular & Package – Multi-Utility Toolkit** is a Python-based console application that provides multiple useful operations through a menu-driven program.

The project uses Python built-in modules and a custom package named `mypage` to organize file-handling operations. It demonstrates how modules and packages make code reusable, structured, and easy to understand.

## 🛠️ Technology Used

- **Python**
- **GitHub**
- **Visual Studio Code (VS Code)**

## 🎯 Project Objectives

The main objectives of this project are to implement and demonstrate:

- **Python Modules and Packages**
- **Importing Built-in Modules**
- **Date and Time Operations**
- **Mathematical Calculations**
- **Random Data Generation**
- **Unique Identifier Generation**
- **File Operations**
- **Module Attribute Exploration using dir()**
- **Menu-Driven Programming**
- **Functions and Variables**
- **Input and Output**
- **Conditional Statements**
- **Loops**
- **File Handling**

## 📂 Project Structure

```text
Moduler & Packager/
│
├── mypackage/
│   ├── __init__.py
│   └── file_operations.py
│
├── example.txt
├── Moduler_Packager.py
└── README.md
```
## 📄 Project Files

## 1. Moduler_Packager.py
- **Purpose:** The main execution file of the project.
- **Usage:** Displays the main menu and allows users to access date and time operations, mathematical calculations, random data generation, UUID generation, file operations, and module exploration.

## 2. mypackage/file_operations.py
- **Purpose:** Contains the functions used for file handling.
- **Functions:**
  - `create_file()` – Creates a new file using "x" mode.
  - `write_file()` – Writes data to a file using "w" mode.
  - `read_file()` – Reads file contents using "r" mode.
  - `append_file()` – Adds new data to a file using "a" mode.

## 3. mypackage/__init__.py
- **Purpose:** Marks the mypage directory as a Python package.
- **Usage:** Allows the package's modules and functions to be imported and organized for reuse.

## 4. example.txt
- **Purpose:** A sample text file used to test file-handling operations such as creating, writing, reading, and appending data.

## 5. README.md
- **Purpose:** Provides project documentation, including the overview, objectives, project structure, features, and sample output.## ✨ Features

## 🕒 Date and Time Operations
- Displays the current date and time, calculates the difference between two dates, formats dates, runs a stopwatch, and provides a countdown timer.

## 🧮 Mathematical Operations
- Calculates factorials, compound interest, logarithms, and trigonometric values.

## 📐 Area of Shapes
- Calculates the area of a circle, rectangle, square, and triangle.

## 🎲 Random Data Generation
- Generates random numbers, random lists, passwords, and six-digit OTPs.

## 🆔 UUID Generation
- Generates unique identifiers using Python's uuid module.

## 📁 File Operations
- Creates, writes, reads, and appends files using a custom Python package.

## 🔍 Module Exploration
- Displays available attributes of the math, random, datetime, and time modules using dir().

## 🔄 Menu-Driven Interface
- Provides a simple menu for accessing different operations.

## 📦 Modules and Packages
- Demonstrates importing and using built-in modules and a custom package.

## ⚡ Interactive Console Application
- Accepts user input and displays the corresponding results.



🖥️ Sample Output
```
===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 1

DateTime and Time Operations:
1. Display Current Date and Time
​2. Difference Between Two Dates
3. Format Date
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
===============================
Enter your choice: 1
Current Date and Time: 2026-10-09 14:31:24

Enter your choice: 2
Enter First Date (YYYY-MM-DD): 2026-09-05
Enter Second Date (YYYY-MM-DD): 2026-07-16
Difference: 51 days

Enter your choice: 3
Enter Date (YYYY-MM-DD): 2026-10-27
Formatted Date: 27-10-2026

Enter your choice: 4
Stopwatch Started...
Press Enter to Stop:
Elapsed: 0.49 seconds

Enter your choice: 5
Enter seconds: 5
Time remaining: 5
Time remaining: 4
Time remaining: 3
Time remaining: 2
Time remaining: 1
Time's Up!

Enter your choice: 6

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 2

Mathematical Operations:
1. Factorial
​2. Compound Interest
3. Logarithms Calculation
4. Trigonometric Calculation
5. Area of Shapes
6. Back to Main Menu
===============================
Enter your choice: 1
Enter number: 5
Factorial: 120

Enter your choice: 2
Enter principal: 23
Enter rate (%): 2
Enter time in years: 3
Compound Interest: 1.407784000000003

Enter your choice: 3
Enter number: 23
Logarithm (base 10): 1.3617278360175928
Natural Logarithm: 3.1354942159291497

Enter your choice: 4
Enter angle in degrees: 34
Sin: 0.5591929034707469
Cos: 0.8290375725550417
Tan: 0.6745085168424266

Enter your choice: 5
Area of Shapes:
1. Circle
​2. Rectangle
3. Square
4. Triangle
Enter choice: 1
Enter radius: 2
Area of Circle: 12.566370614359172

Enter your choice: 6

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 3

Random Data Generation:
1. Random Number
​2. Random List
3. Random Password
4. Random OTP
5. Back to Main Menu
===============================
Enter choice: 1
Random Number: 55

Enter choice: 2
Random List: [9, 8, 66, 44, 93]

Enter choice: 3
Password: pxQqI0aa

Enter choice: 4
OTP: 500435

Enter choice: 5

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 4

Generate Unique Identifier (UUID)
1. Generate UUID
​2. Back to Main Menu
===============================
Enter choice: 1
UUID: c1bd3108-6968-41f4-b111-d4a96a500fbb

Enter choice: 2

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 5

File Operations:
1. Create a new file
​2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
===============================
Enter choice: 1
Enter file name: example.txt
File Created Successfully!

Enter choice: 2
Enter file name: example.txt
Enter data to write: hello python
Data Written Successfully!

Enter choice: 3
Enter file name: example.txt
Content: hello python
Data Read Successfully!

Enter choice: 4
Enter file name: example.txt
Enter data to append: python is programming language..
Data Appended Successfully!

Enter choice: 5

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 6

Explore Module Attributes:
Enter module name and Explore: math

Available Math Attributes in math module:
['__doc__', '__loader__', '__name__', '__package__',
'__spec__', 'acos', 'acosh', 'asin', 'asinh',
'atan', 'atan2', 'atanh', 'ceil', 'comb',
'cos', 'cosh', 'degrees', 'dist', 'e',
'exp', 'factorial', 'floor', 'fmod', 'fsum',
'gcd', 'hypot', 'isclose', 'isfinite', 'isinf',
'isnan', 'isqrt', 'lcm', 'log', 'log10',
'log2', 'pi', 'pow', 'prod', 'radians',
'sin', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

===============================
   MODULAR AND PACKAGES TOOLKIT
===============================
1. DateTime and Time Operations
​2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
===============================
Enter Your Choice: 7
Thank you for using the Multi-Utility Toolkit!
```
