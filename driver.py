class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0       
        self.__total_trips = 0  

    def add_rating(self, new_rating):
        if new_rating <= 5.0 and new_rating >= 1.0:
            total_points = self.__rating * self.__total_trips + new_rating
            self.__total_trips += 1
            self.__rating = total_points / self.__total_trips
        else:
            raise ValueError("Invalid rating!")

    def get_rating_info(self):
        return f"Average Rating: {self.__rating}, Total Trips: {self.__total_trips}"

# test = DriverAccount("Tung", "NEJ 9802")

# test.add_rating(4.5)
# print(test.get_rating_info())
# test.add_rating(5.0)
# print(test.get_rating_info())
# test.add_rating(5.1)
# print(test.get_rating_info())