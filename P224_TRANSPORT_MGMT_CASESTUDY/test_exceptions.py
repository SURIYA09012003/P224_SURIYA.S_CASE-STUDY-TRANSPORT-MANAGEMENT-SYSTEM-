import unittest
from unittest.mock import MagicMock
from dao.transport_management_service_impl import TransportManagementServiceImpl
from entity.vehicles import Vehicle
from myexceptions.vehicle_not_found_exception import VehicleNotFoundException
from myexceptions.booking_not_found_exception import BookingNotFoundException

class TestExceptions(unittest.TestCase):

    def setUp(self):
        self.db_connection = MagicMock()
        self.service = TransportManagementServiceImpl(self.db_connection)

    def test_vehicle_not_found_exception(self):
        cursor = MagicMock()
        self.db_connection.cursor.return_value = cursor

        cursor.rowcount = 0  # Simulate no vehicle found for update
        
        with self.assertRaises(VehicleNotFoundException):
            self.service.update_vehicle(Vehicle(vehicle_id=99, model="Unknown", capacity=4, vehicle_type="Gas", status="Unavailable"))

    def test_booking_not_found_exception(self):
        cursor = MagicMock()
        self.db_connection.cursor.return_value = cursor

        cursor.fetchall.return_value = []  # Simulate no bookings found
        
        with self.assertRaises(BookingNotFoundException):
            self.service.get_bookings_by_passenger(passenger_id=999)

if __name__ == '__main__':
    unittest.main()
