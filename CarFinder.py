AllowedVehiclesList = [ 'Ford F-150',
                        'Chevrolet Silverado',
                        'Tesla CyberTruck',
                        'Toyota Tundra',
                        'Nissan Titan' ]

while True:
    print("""********************************
AutoCountry Vehicle Finder v0.2
********************************""")
    
    menu = print("""Please Enter the following number below from the following menu: 

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
********************************""")



    answer = input("Enter Number: ")

    if answer == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for x in AllowedVehiclesList:
            print(x)
    elif answer == "2":
        answer2 = input("Please Enter the full vehicle name: ")
        if answer2 in AllowedVehiclesList:
            print(f'{answer2} is an authorized vehicle')
        else:
            print(f'{answer2} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    elif answer == "3":
        exit("Thank you for using the AutoCountry Vehicle Finder, good-bye!")