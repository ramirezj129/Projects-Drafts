while True:
 
    fuel = (input("Fraction: "))
    try:
       
        numerator,denominator = fuel.split("/")

        new_n = int(numerator)
        new_d = int(denominator)

        f = new_n / new_d

        if f <= 1:
            break
    except(ValueError,ZeroDivisionError):
            pass

p = f * 100

if p < 1:
    print("E")
elif p > 99:
    print("F")
else:
    print(f"{p}%")
