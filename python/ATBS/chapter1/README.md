# Chapter 1 - Python Basics

**Expression**: The most basic kind of programming instruction, made up of values and operators. These expressions always **evaluate** down to a single value.

## Integer, Floating-point, and String Data Types
Data Type | Examples
---|---
Integers | -2, 0, 1, 5
Floating-point numbers | -1.25, 0.0, 1.2
Strings | 'a', 'abcde', 'Ray'

## Concatenation
For integers or floating-point numbers, '+' will perform addition. However, on strings, it will concatenate, or combine the strings.

Example | Output
--- | ---
'Ray' + 'Laura' | RayLaura

**Note:** This operator cannot combine strings and integers.

## Variables
A **variable** is a place in the computer's memory where you can store a single value that can be used later. An **assignment statement** is used to store a value to a variable.

> someVariable = 12

The equals sign in the assignment statement is called an **assignment operator**. The process of storing a value within a variable for the first time is called **initialization**. Variables can be overwritten with new values.

### Allowed Variable Names
- One word with no spaces
- Only contains letters, numbers, or underscore (_)
- It cannot begin with a number

**Note:** Variable names are *case-sensitive*! (it's Python convention to start variable names with a lowercase)

## Functions

### print() Function
This function is used to display the string value within the parentheses. Example:

> print('this string will print')

This function is **called** and the string value is being **passed** to the function as an **argument**.

### input() Function
This function waits for a user to type a value and press enter. The value of this input can be saved as a variable, such as:

> someVariable = input()

### len() Function
This function is passed a string which it then responds with the integer value of the number of characters in that string.

### str(), int(), float()
These functions will change any arguments passed to them into a string, integer, or float, respectively.
