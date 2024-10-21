class Booking:
    def __init__(self, trip_id=None, passenger_id=None, booking_date=None, booking_id=None):
        self.__booking_id = booking_id  # Booking ID can be None initially and set when added to the database
        self.__trip_id = trip_id
        self.__passenger_id = passenger_id
        self.__booking_date = booking_date

    # Getters
    def get_booking_id(self):
        return self.__booking_id

    def get_trip_id(self):
        return self.__trip_id

    def get_passenger_id(self):
        return self.__passenger_id

    def get_booking_date(self):
        return self.__booking_date

    # Setters
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id

    def set_trip_id(self, trip_id):
        self.__trip_id = trip_id

    def set_passenger_id(self, passenger_id):
        self.__passenger_id = passenger_id

    def set_booking_date(self, booking_date):
        self.__booking_date = booking_date

    def __str__(self):
        return f"Booking[ID={self.__booking_id}, TripID={self.__trip_id}, PassengerID={self.__passenger_id}, Date={self.__booking_date}]"
