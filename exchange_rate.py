# Task: A program that calculates exchange rates between 3 African currencies using variables and operators 

# Solution: 

# Step 1:  
# 1 Ghana Cedi = 125 Naira 
# 1 Kenyan shilling = 11 Naira 

# Step 2: 
# user enter value for exchange 

user_choice = int(input('Enter the value you want to exchange? ')) 
ghana_to_naira = user_choice * 125 
kenyan_to_naira = user_choice * 11 

print(f"Your value equivalent to naira is #{ghana_to_naira}")

