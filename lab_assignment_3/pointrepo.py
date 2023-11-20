from math import sqrt
import matplotlib.pyplot as plt


class PointRepository:
    def __init__(self):
        self.points_list = []

    def get_list_of_points(self):
        return self.points_list

    def set_list_of_points(self, points_list):
        self.points_list = points_list

    def add_new_point(self, new_point):
        self.points_list.append(new_point)

    def get_point_given_index(self, index):
        return self.points_list[index]

    def get_points_given_color(self, color):
        color_list = []
        for i in range(len(self.points_list)):
            if self.points_list[i].color == color:
                color_list.append(self.points_list[i])
        return color_list

    def get_points_inside_square(self, corner, length):
        list = []
        for point in self.points_list:
            if corner.coord_x <= point.coord_x <= corner.coord_x + length \
                    and corner.coord_y - length <= point.coord_y <= corner.coord_y:
                list.append(point)
        return list

    def update_point_given_index(self, index, x, y, color):
        self.points_list[index].coord_x = x
        self.points_list[index].coord_y = y
        self.points_list[index].color = color
        return self.points_list[index]

    def delete_point_by_index(self, index):
        self.points_list.pop(index)

    def delete_points_inside_square(self, corner, length):
        points_to_remove = [point for point in self.points_list
                            if corner.coord_x <= point.coord_x <= corner.coord_x + length
                            and corner.coord_y - length <= point.coord_y <= corner.coord_y]

        for point in points_to_remove:
            self.points_list.remove(point)

    def extra_delete_points_within_distance_from_point(self, given_point, distance):
        points_to_remove = [point for point in self.points_list
                            if sqrt(pow(given_point.coord_x - point.coord_x, 2) +
                                    pow(given_point.coord_y - point.coord_y, 2)) <= distance]
        for point in points_to_remove:
            self.points_list.remove(point)

    def extra_maximum_distance_2_points(self):
        max_distance = sqrt(pow(self.points_list[1].coord_x - self.points_list[0].coord_x, 2) +
                            pow(self.points_list[1].coord_y - self.points_list[0].coord_y, 2))
        for point1 in self.points_list:
            for point2 in self.points_list:
                if point1 != point2:
                    dist = sqrt(pow(point2.coord_x - point1.coord_x, 2) + pow(point2.coord_y - point1.coord_y, 2))
                    if dist > max_distance:
                        max_distance = dist
        return max_distance

    def extra_shift_on_x(self, x_value):
        for point in self.points_list:
            point.coord_x += x_value









    def get_min_dist_between_points(self):
        min_distance = sqrt(pow(self.points_list[1].coord_x - self.points_list[0].coord_x, 2) +
                            pow(self.points_list[1].coord_y - self.points_list[0].coord_y, 2))
        for point1 in self.points_list:
            for point2 in self.points_list:
                if point1 != point2:
                    dist = sqrt(pow(point2.coord_x - point1.coord_x, 2) + pow(point2.coord_y - point1.coord_y, 2))
                    if dist < min_distance:
                        min_distance = dist
        return min_distance

    def plot_all_points(self):
        colors = {'red': 'r', 'blue': 'b', 'black': 'k', 'green': 'g', 'yellow': 'y', 'purple': 'm', 'cyan': 'c',
                  'white': 'w'}

        for point in self.points_list:
            x = point.coord_x
            y = point.coord_y
            color = colors.get(point.get_color(), 'b')  # Default to blue if color is not recognized

            plt.scatter(x, y, c=color, marker='o', label=f'Point ({x},{y})')

        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Plot of Points')
        plt.legend()
        plt.show()
    def __str__(self):
        result = "The points list is: "
        for i in range(len(self.points_list)):
            result += f"\n{self.points_list[i]}"
        return result
