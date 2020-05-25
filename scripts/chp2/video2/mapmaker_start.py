class Point():
    def __init__(self, name, lat, lon):
        self.name = name
        self.latitude = lat
        self.longitude = lon
    
    def get_lat_lon(self):
        return (self.latitude, self.longitude)
