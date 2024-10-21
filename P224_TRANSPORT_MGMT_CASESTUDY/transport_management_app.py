import pyodbc
from dao.transport_management_service_impl import TransportManagementServiceImpl
from myexceptions.vehicle_not_found_exception import VehicleNotFoundException
from myexceptions.booking_not_found_exception import BookingNotFoundException
from entity.vehicles import Vehicle 
from entity.booking import Booking
from entity.driver import Driver

def main_menu():
    print("Welcome to the Transport Management System")
    print("1. Add Vehicle")
    print("2. Update Vehicle")
    print("3. Delete Vehicle")
    print("4. Schedule Trip")
    print("5. Cancel Trip")
    print("6. Book Trip")
    print("7. Cancel Booking")
    print("8. Allocate Driver")
    print("9. Deallocate Driver")
    print("10. Get Bookings by Passenger")
    print("11. Get Bookings by Trip")
    print("12. Get Available Drivers")
    print("0. Exit")

def main():
    # Establishing a database connection
    try:
        db_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                        'SERVER=LUFFY\SQLEXPRESS;'
                                        'DATABASE=cs_transport_management;'
                                        'Trusted_Connection=yes;')
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return

    service = TransportManagementServiceImpl(db_connection)

    while True:
        main_menu()
        choice = int(input("Select an option: "))

        if choice == 1:
            # Add Vehicle
            try:
                vehicle_id = int(input("Enter vehicle ID: "))
                model = input("Enter vehicle model: ")
                capacity = int(input("Enter vehicle capacity: "))
                vehicle_type = input("Enter vehicle type: ")
                status = input("Enter vehicle status: ")

                vehicle = Vehicle(vehicle_id, model, capacity, vehicle_type, status)
                if service.add_vehicle(vehicle):
                    print("Vehicle added successfully!")
            except VehicleNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 2:
            # Update Vehicle
            try:
                vehicle_id = int(input("Enter vehicle ID to update: "))
                model = input("Enter new vehicle model: ")
                capacity = int(input("Enter new vehicle capacity: "))
                vehicle_type = input("Enter new vehicle type: ")
                status = input("Enter new vehicle status: ")

                vehicle = Vehicle(vehicle_id, model, capacity, vehicle_type, status)
                if service.update_vehicle(vehicle):
                    print("Vehicle updated successfully!")
            except VehicleNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 3:
            # Delete Vehicle
            try:
                vehicle_id = int(input("Enter vehicle ID to delete: "))
                if service.delete_vehicle(vehicle_id):
                    print("Vehicle deleted successfully!")
            except VehicleNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 4:
            # Schedule Trip
            try:
                vehicle_id = int(input("Enter vehicle ID for the trip: "))
                route_id = int(input("Enter route ID: "))
                departure_date = input("Enter departure date (YYYY-MM-DD): ")
                arrival_date = input("Enter arrival date (YYYY-MM-DD): ")

                if service.schedule_trip(vehicle_id, route_id, departure_date, arrival_date):
                    print("Trip scheduled successfully!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 5:
            # Cancel Trip
            try:
                trip_id = int(input("Enter trip ID to cancel: "))
                if service.cancel_trip(trip_id):
                    print("Trip cancelled successfully!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 6:
            # Book Trip
            try:
                trip_id = int(input("Enter trip ID: "))
                passenger_id = int(input("Enter passenger ID: "))
                booking_date = input("Enter booking date (YYYY-MM-DD): ")

                if service.book_trip(trip_id, passenger_id, booking_date):
                    print("Trip booked successfully!")
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 7:
            # Cancel Booking
            try:
                booking_id = int(input("Enter booking ID to cancel: "))
                if service.cancel_booking(booking_id):
                    print("Booking cancelled successfully!")
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 8:
            # Allocate Driver
            try:
                trip_id = int(input("Enter trip ID: "))
                driver_id = int(input("Enter driver ID: "))

                if service.allocate_driver(trip_id, driver_id):
                    print("Driver allocated successfully!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 9:  # Deallocate Driver
            try:
                trip_id = int(input("Enter trip ID to deallocate driver: "))
                if service.deallocate_driver(trip_id):
                    print("Driver deallocated successfully and status updated.")
            except Exception as e:
                print(f"Error: {e}")


        elif choice == 10:
            # Get Bookings by Passenger
            try:
                passenger_id = int(input("Enter passenger ID: "))
                bookings = service.get_bookings_by_passenger(passenger_id)
                print(f"Bookings for Passenger ID {passenger_id}: {bookings}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 11:
            # Get Bookings by Trip
            try:
                trip_id = int(input("Enter trip ID: "))
                bookings = service.get_bookings_by_trip(trip_id)
                print(f"Bookings for Trip ID {trip_id}: {bookings}")
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == 12:
            # Get Available Drivers
            try:
                drivers = service.get_available_drivers()
                print(f"Available Drivers: {drivers}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 0:
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

