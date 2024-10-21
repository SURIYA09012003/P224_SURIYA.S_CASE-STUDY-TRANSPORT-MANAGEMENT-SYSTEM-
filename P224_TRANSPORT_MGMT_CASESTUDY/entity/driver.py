class Driver:
    def __init__(self, driver_id=None, name=None, status="Available"):
        self.__driver_id = driver_id  # Can be None initially if it's auto-generated
        self.__name = name
        self.__status = status  # Default status can be set to "Available"

    # Getters
    def get_driver_id(self):
        return self.__driver_id

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    # Setters
    def set_driver_id(self, driver_id):
        self.__driver_id = driver_id

    def set_name(self, name):
        self.__name = name

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Driver[ID={self.__driver_id}, Name={self.__name}, Status={self.__status}]"
