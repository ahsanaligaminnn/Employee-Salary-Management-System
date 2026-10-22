print("\n=======================================")
print("|  Employee Salary Management System  |")
print("=======================================")
print("_______________________________________\n")

#Employee information
employee_name = input("Enter Employee Name : ")
while True:
    employee_age = input("Employee age : ")
    if employee_age.isdigit():
        employee_age = int(employee_age)
        salary = input("Basic Salary : ")
        if salary.isdigit():
            salary = int(salary)
            break
        else:
            print("Enter salary in a number validation.\n")
    else:
        print("Enter age in a number validation.\n") 

employee_id = input("Employee ID : ")
department = input("Department : ") 



monthly_performance = []

print("\n----- Monthly performance -----")
print("_______________________________\n")

for i in range(1,6):
    while True:
        performance = input(f"{i} Monthly sale RS.  ")
        if performance.isdigit():
            performance = int(performance)
            monthly_performance.append(performance)
            break
        else:
            print("Invalid input")

def calculate_salary(employee_name , employee_age , employee_id , department , salary):
    employee_data = {}
    total_sales = sum(monthly_performance)
    highest_sale = max(monthly_performance)
    lowest_sale = min(monthly_performance)
    average_sales = sum(monthly_performance)/len(monthly_performance)

    #Calculate Bonus
    if average_sales >= 100000:
        bonus_apply = "20%"
        bonus = salary*0.20
        final_salary = salary+bonus
        performance_status = "Excellient"

    elif average_sales >= 50000:
        bonus_apply = "10%"
        bonus = salary*0.10
        final_salary = salary+bonus
        performance_status = "Good"

    else:
        bonus_apply = "Not Apply"
        bonus = 0
        performance_status = "Needs Improvement"
        final_salary = salary+bonus

    employee_data['employee name'] = employee_name
    employee_data['age'] = employee_age
    employee_data['employee id'] = employee_id
    employee_data['department'] = department
    employee_data['salary'] = salary
    employee_data['average sales'] = average_sales
    employee_data['final salary'] = final_salary
    employee_data['total sales'] = total_sales
    employee_data['highest sale'] = highest_sale
    employee_data['lowest sale'] = lowest_sale
    employee_data['bonus apply'] = bonus_apply
    employee_data['bonus'] = bonus
    employee_data['performance'] = performance_status
    return employee_data

data = calculate_salary(employee_name , employee_age , employee_id , department , salary)

def department_message(department):
    return(f"{department} Department Report.")
report = department_message(department)

print("\n=====================")
print("|  Employee Report  |")
print("=====================")
print("_____________________\n")

print(f"Employee Name : {data['employee name']}")
print(f"Age : {data['age']}")
print(f"Employee ID : {data['employee id']}")
print(f"Department : {data['department']}")
print(f"Salary : {data['salary']}\n")

print(f"Total Sales : {data['total sales']}")
print(f"Average Sales : {data['average sales']}")
print(f"Highest Sale : {data['highest sale']}")
print(f"Lowest Sale : {data['lowest sale']}")
print(f"Bonus Apply : {data['bonus apply']}")
print(f"Bonus : {data['bonus']}")
print(f"Final Salary : {data['final salary']}")
print(f"Performance : {data['performance']}\n")

print(report)

