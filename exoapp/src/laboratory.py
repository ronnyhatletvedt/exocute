print('-------------------------')

def my_function():
  print("Hello from a function")

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))

my_function()

print('-------------------------')

# Sample
for i in range(1, 12):
    switch_demo(i)

print('-------------------------')

# Sample
def one():
    return "January"

def two():
    return "February"

def three():
    return "March"

def four():
    return "April"

def five():
    return "May"

def six():
    return "June"

def seven():
    return "July"

def eight():
    return "August"

def nine():
    return "September"

def ten():
    return "October"

def eleven():
    return "November"

def twelve():
    return "December"

def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print(func())

numbers_to_months(1)