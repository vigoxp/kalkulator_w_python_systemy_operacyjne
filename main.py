#!/usr/bin/env python3


num1 = float(input("Podaj pierwszą liczbe: "))
operator = input("operacja (+, -, *, /): ")
num2 = float(input("Podaj druga liczbę: "))

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
        print("Błąd: dzielenie przez zero.")
        exit()
else:
    print("Błąd: inny.")
    exit()

print("Wynik:", result)