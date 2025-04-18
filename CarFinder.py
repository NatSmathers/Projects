FILENAME = "vehicles.txt"

def load_vehicles():
    with open(FILENAME, 'r') as file:
        return [line.strip() for line in file.readlines()]
        
def save_vehicles(vehicle_list):
    with open(FILENAME, 'w') as file:
        for vehicle in vehicle_list:
            file.write(vehicle + '\n')

def print_vehicles(vehicle_list):
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in vehicle_list:
            print(vehicle)

def search_vehicles(vehicle_list):
    answer2 = input("Please Enter the full vehicle name: ")
    if answer2 in vehicle_list:
        print(f'{answer2} is an authorized vehicle')
    else:
        print(f'{answer2} is not an authorized vehicle, if you received this in error please check the spelling and try again')

def add_vehicles(vehicle_list):
    add = input("Please Enter the full Vehicle name you would like to add: ")
    list1 = vehicle_list.append(add)
    print(f'You have added {add} as an authorized vehicle')

def delete_vehicles(vehicle_list):
    remove = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    sure = input(f'Are you sure you want to remove {remove} from the Authorized Vehicles List? ')
    if sure == "yes":
        list2 = vehicle_list.remove(remove)
        print(f'You have REMOVED {remove} as an authorized vehicle')

def exit_program(vehicle_list):
    exit("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    

AllowedVehiclesList = load_vehicles()

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
        print_vehicles(AllowedVehiclesList)
    elif answer == "2":
        search_vehicles(AllowedVehiclesList)
    elif answer == "3":
        add_vehicles(AllowedVehiclesList)
    elif answer == "4":
        delete_vehicles(AllowedVehiclesList)
    elif answer == "5":
        exit_program(AllowedVehiclesList)
