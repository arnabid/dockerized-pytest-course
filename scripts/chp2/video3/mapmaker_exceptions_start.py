
class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name, str):
            raise TypeError("City name provided must be string type")
        self.name = name

        if not ((-90 <= latitude <= 90) and (-180 <= longitude <= 180)):
            raise ValueError("Invalid latitude, longitude combination")
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        return (self.latitude, self.longitude)
