import unittest
from unittest.mock import MagicMock
from dao.transport_management_service_impl import TransportManagementServiceImpl

class TestDriverMappedToVehicle(unittest.TestCase):

    def setUp(self):
        self.db_connection = MagicMock()
        self.service = TransportManagementServiceImpl(self.db_connection)

    def test_driver_mapped_to_vehicle_successfully(self):
        # Mock cursor and its behavior for allocate_driver method
        cursor = MagicMock()
        self.db_connection.cursor.return_value = cursor

        # Simulate a successful driver allocation
        cursor.rowcount = 1

        result = self.service.allocate_driver(trip_id=1, driver_id=101)
        
        self.assertTrue(result, "Driver should be mapped to the vehicle successfully.")

        # Check both queries were called as expected
        cursor.execute.assert_any_call("UPDATE trips SET driver_id=? WHERE trip_id=?", (101, 1))
        cursor.execute.assert_any_call("UPDATE drivers SET status='Unavailable' WHERE driver_id=?", (101,))

if __name__ == '__main__':
    unittest.main()
