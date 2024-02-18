##-------- Functions ---------##

def dir_q():
    print("What is the direction of conversion?")

def temp_c_to_f(temp_val):
    return ((temp_val * (9/5)) + 32)

def temp_f_to_c(temp_val):
    return ((temp_val - 32) * (5/9))

def temp():
    dir_q()
    conv_dir = int(input("1) C to F\n2) F to C\n"))
    temp_val = float(input("Type the value: "))
    if conv_dir == 1:
        print("Answer: " + str(temp_c_to_f(temp_val)))
    elif conv_dir == 2:
        print("Answer: " + str(temp_f_to_c(temp_val)))
    else:
        print("Error: wrong choice")

def speed_mph_kph(speed_val, factor):
    return (speed_val * factor)


def speed():
    dir_q()
    conv_dir = int(input("1) MPH to KPH\n2) KPH to MPH\n"))
    speed_val = float(input("Type the value: "))
    factor = 1.60934
    if conv_dir == 1:
        print("Answer: " + str(speed_mph_kph(speed_val, factor)))
    elif conv_dir == 2:
        print("Answer: " + str(speed_mph_kph(speed_val, 1/factor)))
    else:
        print("Error: wrong choice")


def weight_converter(weight_val, factor):
    return (weight_val * factor)


def weight():
    dir_q()
    conv_dir = int(input("1) kg to stone\n2) stone to kg\n3) kg to lbs\n4) lbs to kg\n5) stone to lbs\n6) lbs to stone\n"))
    weight_val = float(input("Type the value: "))
    stone_kg_factor = 6.35029
    stone_lbs_factor = 14
    kg_lbs_factor = 2.20462
    if conv_dir == 1:
        print("Answer: " + str(weight_converter(weight_val, 1/stone_kg_factor)))
    elif conv_dir == 2:
        print("Answer: " + str(weight_converter(weight_val, stone_kg_factor)))
    elif conv_dir == 3:
        print("Answer: " + str(weight_converter(weight_val, kg_lbs_factor)))
    elif conv_dir == 4:
        print("Answer: " + str(weight_converter(weight_val, 1/kg_lbs_factor)))
    elif conv_dir == 5:
        print("Answer: " + str(weight_converter(weight_val, stone_lbs_factor)))
    elif conv_dir == 6:
        print("Answer: " + str(weight_converter(weight_val, 1/stone_lbs_factor)))
    else:
        print("Error: wrong choice")


##-------------- Main ---------------##

print("This program converts values")
print("What is the type of conversion you'd like to do? (type a number 1, 2 or 3)")
print("1) Temperature (C <-> F)\n2) Speed (MPH <-> KPH)\n3) Weight (kg <-> stone <-> lbs)")

user_choice = int(input())

print(type(user_choice))

print("You have chosen " + str(user_choice))

if user_choice > 3 or user_choice < 1:
    print("Error: value should be 1, 2 or 3")
elif user_choice == 1:
    temp()
elif user_choice == 2:
    speed()
elif user_choice == 3:
    weight()
else:
    print("Hmmm, something went wrong!")



