import unittest
from unittest.mock import MagicMock
from dao.transport_management_service_impl import TransportManagementServiceImpl
from entity.vehicles import Vehicle

class TestVehicleOperations(unittest.TestCase):

    def setUp(self):
        self.db_connection = MagicMock()
        self.service = TransportManagementServiceImpl(self.db_connection)

    def test_vehicle_operations(self):
        vehicle = Vehicle(1, "Tesla", 5, "Electric", "Available")
        cursor = MagicMock()
        self.db_connection.cursor.return_value = cursor

        # Test adding vehicle
        cursor.rowcount = 1
        result = self.service.add_vehicle(vehicle)
        self.assertTrue(result, "Vehicle should be added successfully.")

        # Test updating vehicle
        cursor.rowcount = 1  # Simulate a successful update
        result = self.service.update_vehicle(vehicle)
        self.assertTrue(result, "Vehicle should be updated successfully.")
        
        # Test deleting vehicle
        cursor.rowcount = 1  # Simulate successful deletion
        result = self.service.delete_vehicle(vehicle_id=1)
        self.assertTrue(result, "Vehicle should be deleted successfully.")

if __name__ == '__main__':
    unittest.main()
