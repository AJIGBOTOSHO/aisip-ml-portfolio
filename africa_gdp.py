# Task: A program using if/elif/else that categories African countries 
# by GDP per capital into 'Low', 'Middle', 'High' income  

country = (input("Enter the name of your country? ")) 
gdp = float(input("Enter your country gdp rate? ")) 


print("\n --- Analyzing " + country + "----") 

if gdp > 200: 
    print(f"High Income rate.")
elif gdp <= 200:
    print(f"Middle Income rate.") 
else:
    print(f"Low Income rate.") 
    
    

# africa_gdp = { 
#     "south_africa": 410.34, 
#     "egypt": 347.34,
#     "algeria": 268.89,
#     "nigeria": 188.27,
#     "morocco": 165.84,
#     "kenya": 131.67,
#     "ethiopia": 117.46,
#     "angola": 113.34,
#     "ivory_coast": 94.48,
#     "tanzania": 85.98
# } 

# africa_gdp['algeria']
# # for keys in africa_gdp:
# #     print(keys)
#     # if rate > 200:
#     #     print("High income") 
#     # elif rate <= 100:
#     #     print("Middle income") 
#     # else:
#     #     print("Low income")