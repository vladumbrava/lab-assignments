class MyPoint:
    def __init__(self, coord_x, coord_y, color):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.color = color

    def create_point_by_coordinates(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def get_coord_x(self):
        return self.coord_x

    def set_coord_x(self, x):
        self.coord_x = x

    def get_coord_y(self):
        return self.coord_y

    def set_coord_y(self, y):
        self.coord_y = y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return f"Point [{self.coord_x},{self.coord_y}] of color {self.color}"
