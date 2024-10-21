from dao.transport_management_service import TransportManagementService
from myexceptions.vehicle_not_found_exception import VehicleNotFoundException
from myexceptions.booking_not_found_exception import BookingNotFoundException
from entity.vehicles import Vehicle  # Correcting the import for Vehicle
from entity.booking import Booking
from entity.driver import Driver
import pyodbc

class TransportManagementServiceImpl(TransportManagementService):

    def __init__(self, db_connection):
        self.db_connection = db_connection 

    def add_vehicle(self, vehicle: Vehicle) -> bool: 
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO vehicles (model, capacity, vehicle_type, status) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (vehicle.get_model(), vehicle.get_capacity(), vehicle.get_vehicle_type(), vehicle.get_status()))
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while adding vehicle: {e}")
            return False

    def update_vehicle(self, vehicle: Vehicle) -> bool:  
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE vehicles SET model=?, capacity=?, vehicle_type=?, status=? WHERE vehicle_id=?"
            cursor.execute(query, (vehicle.get_model(), vehicle.get_capacity(), vehicle.get_vehicle_type(), vehicle.get_status(), vehicle.get_vehicle_id()))
            
            if cursor.rowcount == 0:
                raise VehicleNotFoundException("Vehicle not found for update.")
            
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while updating vehicle: {e}")
            return False

    def delete_vehicle(self, vehicle_id: int) -> bool:
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM vehicles WHERE vehicle_id=?"
            cursor.execute(query, (vehicle_id,))
            if cursor.rowcount == 0:
                raise VehicleNotFoundException("Vehicle not found for deletion.")
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while deleting vehicle: {e}")
            return False

    def schedule_trip(self, vehicle_id: int, route_id: int, departure_date: str, arrival_date: str) -> bool:
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO trips (vehicle_id, route_id, departure_date, arrival_date, status) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (vehicle_id, route_id, departure_date, arrival_date, 'scheduled'))
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while scheduling trip: {e}")
            return False

    def cancel_trip(self, trip_id: int) -> bool:
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE trips SET status=? WHERE trip_id=?"
            cursor.execute(query, ('cancelled', trip_id))
            if cursor.rowcount == 0:
                print("Trip not found for cancellation.")
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while cancelling trip: {e}")
            return False

    def book_trip(self, trip_id: int, passenger_id: int, booking_date: str) -> bool:
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO bookings (trip_id, passenger_id, booking_date, status) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (trip_id, passenger_id, booking_date, 'confirmed'))
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while booking trip: {e}")
            return False

    def cancel_booking(self, booking_id: int) -> bool:
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM bookings WHERE booking_id=?"
            cursor.execute(query, (booking_id,))
            if cursor.rowcount == 0:
                raise BookingNotFoundException("Booking not found for cancellation.")
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while cancelling booking: {e}")
            return False

    def allocate_driver(self, trip_id, driver_id):
        try:
            # Update the trip with the driver ID
            cursor = self.db_connection.cursor()
            query = "UPDATE trips SET driver_id=? WHERE trip_id=?"
            cursor.execute(query, (driver_id, trip_id))

            if cursor.rowcount == 0:
                print("Trip not found for driver allocation.")
                return False

            # Change the driver's status to 'Unavailable'
            update_driver_status_query = "UPDATE drivers SET status='Unavailable' WHERE driver_id=?"
            cursor.execute(update_driver_status_query, (driver_id,))
            
            # Commit the changes to the database
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while allocating driver: {e}")
            return False


    def deallocate_driver(self, trip_id):
        try:
            cursor = self.db_connection.cursor()
            
            # Fetch the driver ID associated with the trip
            select_query = "SELECT driver_id FROM trips WHERE trip_id=?"
            cursor.execute(select_query, (trip_id,))
            driver_id = cursor.fetchone()
            
            if driver_id is None:
                print(f"No trip found with ID: {trip_id}")
                return False
            
            driver_id = driver_id[0]  # Extract the driver ID

            # Check if the driver is already available
            check_query = "SELECT status FROM drivers WHERE driver_id=?"
            cursor.execute(check_query, (driver_id,))
            status = cursor.fetchone()
            
            if status is None or status[0] != 'Unavailable':
                print(f"No driver found with ID: {driver_id} or status was already 'Available'.")
                return False

            # Update the trip to deallocate the driver
            update_trip_query = "UPDATE trips SET driver_id=NULL WHERE trip_id=?"
            cursor.execute(update_trip_query, (trip_id,))
            
            # Update the driver's status back to 'Available'
            update_driver_query = "UPDATE drivers SET status='Available' WHERE driver_id=?"
            cursor.execute(update_driver_query, (driver_id,))
            
            if cursor.rowcount == 0:
                print(f"No driver found with ID: {driver_id} or status was already 'Available'.")
                return False

            self.db_connection.commit()
            print("Driver deallocated successfully and status updated.")
            return True
            
        except Exception as e:
            print(f"Error while deallocating driver: {e}")
            return False




    def get_bookings_by_passenger(self, passenger_id: int):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM bookings WHERE passenger_id=?"
            cursor.execute(query, (passenger_id,))
            bookings = cursor.fetchall()
            
            if not bookings:  # Check if bookings is empty
                raise BookingNotFoundException("No bookings found for this passenger.")
            
            return bookings
        except Exception as e:
            print(f"Error while retrieving bookings by passenger: {e}")
            return []

    def get_bookings_by_trip(self, trip_id: int):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM bookings WHERE trip_id=?"
            cursor.execute(query, (trip_id,))
            bookings = cursor.fetchall()
            if bookings:
                return bookings
            raise BookingNotFoundException("No bookings found for this trip.")
        except Exception as e:
            print(f"Error while retrieving bookings by trip: {e}")
            return []

    def get_available_drivers(self):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM drivers WHERE status=?"
            cursor.execute(query, ('Available',))
            drivers = cursor.fetchall()
            return drivers
        except Exception as e:
            print(f"Error while retrieving available drivers: {e}")
            return []