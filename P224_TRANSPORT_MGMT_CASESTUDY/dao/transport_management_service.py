from abc import ABC, abstractmethod

class TransportManagementService(ABC):
    @abstractmethod
    def add_vehicle(self, vehicle):
        """Add a new vehicle to the system."""
        pass

    @abstractmethod
    def update_vehicle(self, vehicle):
        """Update the details of an existing vehicle."""
        pass

    @abstractmethod
    def delete_vehicle(self, vehicle_id):
        """Delete a vehicle by its ID."""
        pass

    @abstractmethod
    def schedule_trip(self, vehicle_id, route_id, departure_date, arrival_date):
        """Schedule a trip for a vehicle on a specific route."""
        pass

    @abstractmethod
    def cancel_trip(self, trip_id):
        """Cancel a trip by its ID."""
        pass

    @abstractmethod
    def book_trip(self, trip_id, passenger_id, booking_date):
        """Book a trip for a passenger."""
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        """Cancel a booking by its ID."""
        pass

    @abstractmethod
    def allocate_driver(self, trip_id, driver_id):
        """Allocate a driver to a specific trip."""
        pass

    @abstractmethod
    def deallocate_driver(self, trip_id):
        """Deallocate a driver from a trip."""
        pass

    @abstractmethod
    def get_bookings_by_passenger(self, passenger_id):
        """Retrieve bookings by a passenger's ID."""
        pass

    @abstractmethod
    def get_bookings_by_trip(self, trip_id):
        """Retrieve bookings by a trip's ID."""
        pass

    @abstractmethod
    def get_available_drivers(self):
        """Retrieve a list of available drivers."""
        pass
