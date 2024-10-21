import unittest
from unittest.mock import MagicMock
from dao.transport_management_service_impl import TransportManagementServiceImpl

class TestBookingOperations(unittest.TestCase):

    def setUp(self):
        self.db_connection = MagicMock()
        self.service = TransportManagementServiceImpl(self.db_connection)

    def test_booking_operations(self):
        cursor = MagicMock()
        self.db_connection.cursor.return_value = cursor

        # Simulate successful booking
        cursor.rowcount = 1  
        result = self.service.book_trip(trip_id=1, passenger_id=101, booking_date='2024-10-20')
        self.assertTrue(result, "Trip booking should be successful.")

if __name__ == '__main__':
    unittest.main()
