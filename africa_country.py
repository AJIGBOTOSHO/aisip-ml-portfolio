# Task : A program using a dictionary that stores 10 African 
# countries with their capitals and lets a user look up any country.  


while True:
    capitals = {
        "Algeria": "Algiers",
        "Angola": "Luanda",
        "Benin": "Port-Novo",
        "Botswana": "Gaborone",
        "Burkina_Faso": "Ouagadougou",
        "Burundi": "Bujumbura",
        "Cameroon": "Yaounde",
        "Cap Verde": "Praia",
        "Central_Africa_Republic": "Bengui",
        "Chad": "N'Djamena",
        "Comoros": "Moroni",
        "Congo": "Brazzavaille",
        "Cote_d'viore": "Yamoussoukro",
        "Democratic_Republic_of_the_Congo": "Kinshasa",
        "Djibouti": "Djibouti_City",
        "Egypt": "Cairo",
        "Equatorial_Guineas": "Malabo",
        "Eritrea": "Asmara",
        "Ethiopia": "Addis_Ababa",
        "Gabon": "Libreville",
        "Gambia": "Banjul",
        "Ghana": "Accra",
        "Guinea": "Conakry",
        "Guinea_Bissau": "Bissau",
        "Kenya": "Nairobi",
        "Lesotho": "Maseru",
        "Liberia": "Monrovia",
        "Libya": "Tripoli",
        "Madagascar": "Antananarivo",
        "Malawi": "Lilongwe",
        "Mali": "Bamako",
        "Mauritania": "Nouakchott",
        "Mauritius": "Port_Louis",
        "Morocco": "Rabat",
        "Mozambique": "Maputo",
        "Namibia": "Windhoek",
        "Niger": "Niamey",
        "Nigeria": "Abuja",
        "Rwanda": "Kigali",
        "Sahrawi_Arab_Democratic_Republic": "El_Auluna",
        "Sao_Tome_and_Principe": "Sao_Tome",
        "Senegal": "Dakar",
        "Seychelles": "Victoria",
        "Sierra_Leone": "Freetown",
        "Somalia": "Mogadishu",
        "Somaliland": "Hargeisa",
        "South_Africa": "Pretoria",
        "South_Sudan": "Juba",
        "Sudan": "Khartoum",
        "Swaziland": "Mbabane",
        "Tanzania": "Dodoma",
        "Togo": "Lome",
        "Tunisia": "Tunis",
        "Uganda": "Kampala",
        "Zambia": "Lusaka",
        "Zimbabwe": "Harare"
    }

    # print(len(capitals))
    user_input = (input("Enter a capital of any Africa nation? ")) 

    if user_input in capitals:
        print(f"The capital of {user_input} is {capitals[user_input]}") 
    else:
        print(f"The country entered is not Africa Country")