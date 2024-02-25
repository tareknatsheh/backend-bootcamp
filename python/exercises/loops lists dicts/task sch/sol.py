import pandas as pd

def generate_empty_hours():
    eight_hrs_list = []
    for i in range(8):
        eight_hrs_list.append(None)

    return eight_hrs_list

def generate_empty_week():
    work_week = []
    for i in range(5):
        hours_list = generate_empty_hours()
        work_week.append(hours_list)
    
    return work_week

def add_task(work_days, task_name, task_duration, task_day = None, task_start_hr = None):
    # TODO: handle when only one of them is not None
    if task_day != None and task_start_hr != None:

        # Let's check if any of the time hours is taken:
        for i in range(task_start_hr, len(work_days[task_day])):
            # print("it is: ", work_days[task_day][i])
            if work_days[task_day][i] != None:
                want_to_overwrite = input("OOps! this time slot is occupied. Want to overwrite? [y, n]")
                if want_to_overwrite.lower() == "y":
                    break
                else:
                    return
        # Now we are sure that the whole time range is empty, let's add:
        for hr in range(task_start_hr, task_start_hr + task_duration):
            work_days[task_day][hr] = task_name
    else:
        for day in work_days:
            for hr_index, task_value in enumerate(day):
                if task_value is None:
                    day[hr_index] = task_name
                    task_duration -= 1
                    if task_duration == 0: return
        # TODO: check if the whole required range is not taken, not just the first hour.

##------------------------------------------
##------------------------------------------

work_days = generate_empty_week()

active = True

while active:
    task_name = input("What's the task name: ")
    task_duration = int(input("How many hours this task requires: "))
    task_day = int(input("On what day [0 to 4], or -1 to auto add: "))

    if task_day not in [0,1, 2, 3, 4]:
        task_day = None
        task_start_hr = None
    else:
        task_start_hr = int(input("At what hour [0 to 7] or -1 to auto add: "))

    add_task(work_days, task_name, task_duration, task_day, task_start_hr)

    user_input = input("Would you like to add another task? ")
    if user_input.lower() == "n":
        active = False
    elif user_input.lower() == "y":
        active = True

print("\n")

df = pd.DataFrame(work_days, columns = ['1', '2', '3', '4', '5', '6', '7', '8'], index=['Sun', 'Mon', 'Tue', 'Wed', 'Th'])
print(df)