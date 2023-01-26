year = 2022
first_name = "Eilio"
address = "London 55"

number = 5
age = 55
correct = False
#print(type(correct))

#print(20)
#print("age")

result = age + number

#print(result)

age = age + number  # gae 55
age += number  # the same: age += number
#print(age)
#print(result)
input()
result -= 30  # the same as : result = result - 30
#print(result)

result *= 6  # the same result * 6
#print(result)

side_lenght = 5
#area_square= 5*5*5*5*5*5*5*5 # 8**8 nor correct cause no scalability escalabit
area_squeare = side_lenght**2
#print(area_squeare)
print()

#use floor division //
#use module operator 
dyas = 15450 
days_in_aone_year = 365 
days_in_a_month = 30

year  = dyas// days_in_aone_year
month = (dyas - (year + days_in_aone_year) //days_in_a_month)
daysod_of_the_year = (dyas - (year + days_in_aone_year)) - (month + days_in_a_month)

#print(f"Years : {year}, Months: {month}, Days of the Year: {daysod_of_the_year}")
#print(dyas == days_in_aone_year) 
