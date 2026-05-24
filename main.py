#!/usr/bin/env python3


num1 = float(input("Podaj pierwszą liczbę: "))
operator = input("Podaj działanie (+, -, *, /): ")
num2 = float(input("Podaj drugą liczbę: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Błąd: nie można dzielić przez zero.")
        exit()
else:
    print("Błąd: nieznane działanie.")
    exit()

print("Wynik:", result)