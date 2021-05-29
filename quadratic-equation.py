from math import sqrt
print("Enter 3 coefficients :")
co_a = float(input("A = "))
co_b = float(input("B = "))
co_c = float(input("C = "))

if co_a != 0:
    sub_calc = (co_b*co_b)-(4*co_a*co_c)
    if sub_calc == 0:
        zero_calc = (-sub_calc/(2*co_a))
        print(f"A = {co_a}, B = {co_b}, C = {co_c}\nx = {zero_calc}")
    elif sub_calc > 0:
        add_calc = (-co_b+sqrt(sub_calc))/(2*co_a)
        less_calc = (-co_b-sqrt(sub_calc))/(2*co_a)
        print(f"A = {co_a}, B = {co_b}, C = {co_c}")
        print(f"x1 = {add_calc}\nx2 = {less_calc}")
    else:
        print("x are imaginary")
else:
    print("Input Error")
