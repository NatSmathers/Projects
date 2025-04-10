AllowedVehiclesList = [ 'Ford F-150',
                        'Chevrolet Silverado',
                        'Tesla CyberTruck',
                        'Toyota Tundra',
                        'Nissan Titan' ]

while True:
    print("""********************************
AutoCountry Vehicle Finder v0.4
********************************""")
    
    menu = print("""Please Enter the following number below from the following menu: 

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
********************************""")

    answer = input("Enter Number: ")

    if answer == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in AllowedVehiclesList:
            print(vehicle)
    elif answer == "2":
        answer2 = input("Please Enter the full vehicle name: ")
        if answer2 in AllowedVehiclesList:
            print(f'{answer2} is an authorized vehicle')
        else:
            print(f'{answer2} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    elif answer == "3":
        add = input("Please Enter the full Vehicle name you would like to add: ")
        list1 = AllowedVehiclesList.append(add)
        print(f'You have added {add} as an authorized vehicle')
    elif answer == "4":
        remove = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        sure = input(f'Are you sure you want to remove {remove} from the Authorized Vehicles List? ')
        if sure == "yes":
            list2 = AllowedVehiclesList.remove(remove)
            print(f'You have REMOVED {remove} as an authorized vehicle')
    elif answer == "5":
        exit("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
