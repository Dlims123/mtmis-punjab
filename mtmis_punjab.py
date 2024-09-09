# mtmis_punjab.py

# Sample data representing vehicles in the system
vehicles = {
    "ABC123": {
        "owner": "John Doe",
        "model": "Toyota Corolla",
        "year": 2015,
        "registration_status": "Registered"
    },
    "XYZ789": {
        "owner": "Jane Smith",
        "model": "Honda Civic",
        "year": 2018,
        "registration_status": "Registered"
    },
    "DEF456": {
        "owner": "Ali Ahmed",
        "model": "Suzuki Mehran",
        "year": 2012,
        "registration_status": "Pending"
    }
}

# Function to verify vehicle registration
def verify_vehicle(registration_number):
    vehicle = vehicles.get(registration_number.upper())
    
    if vehicle:
        print(f"Vehicle Found: {registration_number}")
        print(f"Owner: {vehicle['owner']}")
        print(f"Model: {vehicle['model']}")
        print(f"Year: {vehicle['year']}")
        print(f"Registration Status: {vehicle['registration_status']}")
    else:
        print(f"No vehicle found with registration number: {registration_number}")

# Main program to simulate MTMIS Punjab
def main():
    print("Welcome to MTMIS Punjab Vehicle Verification System!")
    reg_num = input("Enter vehicle registration number to verify: ")
    verify_vehicle(reg_num)

if __name__ == "__main__":
    main()
