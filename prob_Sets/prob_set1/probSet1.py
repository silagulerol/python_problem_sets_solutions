############ PART A
# Inputs:FLOAT: yearly_salary, portion_saved(decimal), ost_of_dream_home)
# # Output: months, down_payment = total_cost * downPay_perc

# yearly_salary = float(input("Enter your salary: "))
# portion_saved = float(input("Enter your portion save:"))
# cost_of_dream_home = float(input("Enter your cost of dream home: "))

# downPay_perc = 0.25
# amount_saved = 0.0
# r = 0.05
# months = 0

# while amount_saved < cost_of_dream_home*downPay_perc:
#     amount_saved += (yearly_salary/12)*portion_saved + amount_saved * (r/12) 
#     months +=1
    
# print("Number of months:", months)



############ PART B
# yearly_salary = float(input("Enter your salary: "))
# portion_saved = float(input("Enter your portion save:"))
# cost_of_dream_home = float(input("Enter your cost of dream home: "))
# semi_annual_raise = float(input("Enter your semi annual raise : "))

# downPay_perc = 0.25
# amount_saved = 0.0
# r = 0.05
# months = 0

# while amount_saved < cost_of_dream_home*downPay_perc:
#     amount_saved += (yearly_salary/12)*portion_saved + amount_saved * (r/12) 
#     months +=1
#     if months%6 == 0:
#         yearly_salary += yearly_salary*semi_annual_raise
    
# print("Number of months:", months)



############ PART C
initial_deposit = float(input("Enter your  initial deposit: "))
years = 3
cost_of_hose = 800000
down_payment =800000*0.25
steps=0

epsilon = 100
low = 0.0
high = 1.0
r = (low+high)/2.0

amount_saved = lambda r,years: initial_deposit*((1+ r/12)**(years*12))

while abs(amount_saved(r,3) - down_payment) >= epsilon:
    if amount_saved(r,3) > down_payment:
        high = r
    if amount_saved(r,3) < down_payment:
        low = r
    r = (low+high)/2.0
    steps+=1
    if (0>=r or r>=1):
        break

if (0.0<r<1.0):
    print("Best savings rate:", r,"[or very close to this number]")
    print("Steps in bisection search: ",steps,"[or very close to this number]")
else:
    print("Best savings rate: None")       
    print("Steps in bisection search: 0 [May vary based on how you implemented your bisection search]")    

    
    





























































