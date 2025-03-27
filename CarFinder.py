AllowedVehiclesList = [ 'Ford F-150',
                        'Chevrolet Silverado',
                        'Tesla CyberTruck',
                        'Toyota Tundra',
                        'Nissan Titan' ]

print("""********************************
AutoCountry Vehicle Finder v0.1
********************************""")

menu = print("""Please Enter the following number below from the following menu: 

1. PRINT all Authorized Vehicles
2. Exit""")

answer = input("Enter Number: ")

if answer == "1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for x in AllowedVehiclesList:
        print(x)
elif answer == "2":
    exit("Thank you for using the AutoCountry Vehicle Finder, good-bye!")