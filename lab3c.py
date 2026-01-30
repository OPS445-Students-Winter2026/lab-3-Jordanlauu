#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: jlau103

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        results = number1 + number2
    elif operator == 'subtract':
        results = number1 - number2
    elif operator == 'multiply':
        results = number1 * number2
    else:
         results = 'Error: function operator can be "add", "subtract", or "multiply"'

    return results

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
