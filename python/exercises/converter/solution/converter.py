def dir_q():
    print("What is the direction of conversion?")

def temp_c_to_f(temp_val):
    return ((temp_val * (9/5)) + 32)

def temp_f_to_c(temp_val):
    return ((temp_val - 32) * (5/9))

def temp():
    dir_q()
    conv_dir = int(input("1) C to F\n2) F to C\n"))
    temp_val = float(input("Type in the value: "))
    if conv_dir == 1:
        print("Answer: " + str(temp_c_to_f(temp_val)))
    elif conv_dir == 2:
        print("Answer: " + str(temp_f_to_c(temp_val)))
    else:
        print("Error: wrong choice")

def speed():
    dir_q()
    return 0

def weight():
    dir_q()
    return 0

print("This program converts values")
print("What is the type of conversion you'd like to do? (type a number 1, 2 or 3)")
print("1) Temperature (C <-> F)\n2) Speed (MPH <-> KPH)\n3) Weight (kg <-> stone <-> lbs)")

user_choice = int(input())

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



