# Email Slicer Program (Python)

This is a simple Python program that extracts the username and domain from an email address.  
It helps beginners understand string slicing and basic input handling.

## What the Program Does
- Takes an email address as input
- Extracts the username (before `@`)
- Extracts the domain (after `@`)
- Displays both parts separately

## Concepts Used
- User input
- String indexing
- String slicing
- Basic string manipulation

## How It Works
The program finds the position of the `@` symbol in the email using the `index()` method.  
Using string slicing, it separates:
- Username → text before `@`
- Domain → text after `@`

## Sample Input
Enter your email: example@gmail.com

## Sample Output
Your username is: example  
Your domain is: gmail.com

## How to Run
1. Make sure Python is installed on your system.
2. Save the file as `email-slicer.py`
3. Run the program using:
python email_slicer.py

