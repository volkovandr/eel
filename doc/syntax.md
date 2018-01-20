# General

* The language uses identations just like Python.
* Comments are not supported. If you want to comment something it means your code is not expressive enough and you need to change the code
* There are no global variables. All the functions should be pure functions
* [Keywords](keywords.md)
* keywords are case insensitive. Identifiers are case sensitive.
* Parenthesis, braces and brackets should be avoided.

# Ignored words

The keywords `a` and `the` are ignored by the compliler in case they are not the part of a bigger keyword combination. You can use them wherever you want to make your code more expressive.

# Variables

You don't need to define variables explicitly. To create a variable and assign a value to the following:

```
let the dividend be 10
let then divisor be 5
```

# Operators

We don't want to use operators because we believe they are not epressive enough.  Although sometimes it is necessary. Do it like that:

```
perform dividend / divisor and let the outcome be that
```

# Functions

To create a function use the keywords `to` followed by the function name and the parameters separated by `and`, `with`, `for`, `by` etc. and finally followed by `performed` when the function is a oneliner. To return from the function assign any value to the special variable `the result`. 

```
to divide dividend by divisor perform dividend / divisor and let the result be that 
```

and then to use the function use its name with the parameters. To use the return value in subsequent calls you may use the constract `and then ... that` where `that` refers to the return value. To assign the result of the function to a variable use `and let <vairable> be that`.

```
let dividend be 10
let divisor be 2
divide dividend by divisor and then print that
```

# Blocks of code

To define and use a block of code use the construce `do the following:` and a block of code in the following lines that shoule be indented. As follows

```
to add x to y do the following:
    perform x + y and let the outcome be that
    let the result be outcome
```

# Exceptions

To raise an exception use the syntax "unfortunately it is" followed by the name of the exception. 

```
to divide a dividend by a divisor do the following:
    if the divisor is equal to 0 then unfortunately it is a division_by_zero
    perform x / y and let the result be that

```

To catch an exception use the keyword `please` with `when <exception name> happens then` as follows:

```
please divide 10 by 0 and then print that
when a division_by_zero happens print "Could not divide by zero"
```
