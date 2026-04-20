# Task : A program using a for loop that processes a 
# list of African city populations and finds the top 3 largest.  

cities = [
    ['Lagos', 20],
    ['Cairo', 15],
    ['Accra', 10],
    ['Cape_town', 12],
    ['Ibadan', 10], 
    ['Nairobi', 5]
] 

def africa_pop():
    
    print("Highest Africa City Population in our Library")
    cities.sort(key=lambda city: city[1], reverse=True) 
    for i in range(3):
        city_name = cities[i][0] 
        city_population = cities[i][1]
        print(f" {i+1}.{city_name} has {city_population} million people") 
        
africa_pop()
