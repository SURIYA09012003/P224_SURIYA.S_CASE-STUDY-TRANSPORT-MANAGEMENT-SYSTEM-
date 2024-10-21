class Vehicle:  # Changed from vehicles to Vehicle
    def __init__(self, vehicle_id=None, model=None, capacity=None, vehicle_type=None, status=None):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.__capacity = capacity
        self.__vehicle_type = vehicle_type
        self.__status = status

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_status(self):
        return self.__status

    # Setters
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Vehicle[ID={self.__vehicle_id}, Model={self.__model}, Capacity={self.__capacity}, Type={self.__vehicle_type}, Status={self.__status}]"
