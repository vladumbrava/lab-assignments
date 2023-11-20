from mypoint import MyPoint
from pointrepo import PointRepository
'''
sa nu uit pt minimum si maximum distance sa fac sa se afiseze numarul si doar 2 zecimale (aproximand)
'''

def main():
    '''
        Initializare cateva puncte
    '''
    new_point = MyPoint(-1, 4, "blue")
    new_point1 = MyPoint(-6, 6, "red")
    new_point3 = MyPoint(-10, 5, "red")
    new_point4 = MyPoint(5, 4, "red")
    new_point5 = MyPoint(1,2,"red")
    new_point6 = MyPoint(1,1,"red")

    new_list = [new_point, new_point1, new_point3, new_point4, new_point5, new_point6]

    '''
            Initializare repository
    '''
    repository = PointRepository()
    '''
                Setare lista puncte si afisare
    '''
    repository.set_list_of_points(new_list)

    '''
                Am creat punct nou, l-am adaugat la 
                repository si afisare
    '''
    new_point_to_add = MyPoint(-2, 25, "black")
    repository.add_new_point(new_point_to_add)

    list_of_points_of_given_color = repository.get_points_given_color("red")
    print("List of points of given color: ")
    for point in list_of_points_of_given_color:
        print(point)

    list_of_points_inside_square = repository.get_points_inside_square(MyPoint(4, 5, None), 3)
    print("List of points in the square: ")
    for point in list_of_points_inside_square:
        print(point)

    print(repository.get_min_dist_between_points())

    print(repository)
    repository.update_point_given_index(1,2,3,"blue")
    print("Updated list after updating point at index 1: ")
    print(repository)

    repository.delete_point_by_index(1)
    print(repository)
    repository.delete_points_inside_square(MyPoint(4,5,None),3)
    print(repository)
    repository.extra_delete_points_within_distance_from_point(MyPoint(6,8,None),8)
    print(repository)

    # print(repository.extra_maximum_distance_2_points())
    repository.extra_shift_on_x(100)
    print(repository)


if __name__ == "__main__":
    main()
