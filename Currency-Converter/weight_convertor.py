def determine(user_weight, unit):
    if unit == 'k':
        ans = user_weight * 2.20462
        print("Weight in kg:",ans)
    elif unit == 'l':
        ans = user_weight * 0.453592
        print("Weight in lbs:",ans)
    else:
        print("Wrong Input!")

user_weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ").lower()
determine(user_weight, unit)
