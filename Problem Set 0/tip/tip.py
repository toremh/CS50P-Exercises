def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # print(float(d[1:]))
    return float(d[1:])


def percent_to_float(p):
    # print(float(p[:2]))
    return float(p[:2])/100

main()
