# If don't want have new line at use print function time
# Default : print function will default create a new line after "Hello"


def default_print_function():
    print("Hello")
    print("New Line")


default_print_function()


# Parameterized : parameter of print function 'end' , it statement what is end of the this print


def parameterized_print_function():
    print("parameterized Hello", end="")
    print("Without a new line")


parameterized_print_function()

