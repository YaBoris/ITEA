class Dot3D:

    def __init__(self, dot_x, dot_y, dot_z):
        self._dot_x = dot_x
        self._dot_y = dot_y
        self._dot_z = dot_z

    def __add__(self, other):
        new_dot_x = self._dot_x + other.get_dot_x()
        new_dot_y = self._dot_y + other.get_dot_y()
        new_dot_z = self._dot_z + other.get_dot_z()
        return Dot3D(new_dot_x, new_dot_y, new_dot_z)

    def __sub__(self, other):
        new_dot_x = self._dot_x - other.get_dot_x()
        new_dot_y = self._dot_y - other.get_dot_y()
        new_dot_z = self._dot_z - other.get_dot_z()
        return Dot3D(new_dot_x, new_dot_y, new_dot_z)

    def __mul__(self, other):
        new_dot_x = self._dot_x * other.get_dot_x()
        new_dot_y = self._dot_y * other.get_dot_y()
        new_dot_z = self._dot_z * other.get_dot_z()
        return Dot3D(new_dot_x, new_dot_y, new_dot_z)

    def __truediv__(self, other):
        new_dot_x = self._dot_x / other.get_dot_x()
        new_dot_y = self._dot_y / other.get_dot_y()
        new_dot_z = self._dot_z / other.get_dot_z()
        return Dot3D(new_dot_x, new_dot_y, new_dot_z)

    def __neg__(self):
        new_dot_x = self._dot_x * -1
        new_dot_y = self._dot_y * -1
        new_dot_z = self._dot_z * -1
        return Dot3D(new_dot_x, new_dot_y, new_dot_z)

    def get_dot_x(self):
        return self._dot_x

    def get_dot_y(self):
        return self._dot_y

    def get_dot_z(self):
        return self._dot_z

    def set_dot_x(self, new_dot_x):
        self._dot_x = new_dot_x

    def set_dot_y(self, new_dot_y):
        self._dot_y = new_dot_y

    def set_dot_z(self, new_dot_z):
        self._dot_z = new_dot_z


dot1 = Dot3D(1, 2, 3)
dot2 = Dot3D(1, 2, 3)

dots = [dot1, dot2]

for dot in range(len(dots)):
    while True:
        try:
            print("Enter coordinate X (it must be integer): ")
            x_coordinate = int(input())
            break
        except ValueError:
            print("Enter correct value for coordinate: integer")
    while True:
        try:
            print("Enter coordinate Y (it must be integer): ")
            y_coordinate = int(input())
            break
        except ValueError:
            print("Enter correct value for coordinate: integer")

    while True:
        try:
            print("Enter coordinate Z (it must be integer): ")
            z_coordinate = int(input())
            break
        except ValueError:
            print("Enter correct value for coordinate: integer")

    dots[dot].set_dot_x(x_coordinate)
    dots[dot].set_dot_y(y_coordinate)
    dots[dot].set_dot_z(z_coordinate)


print(f"Coordinates of dot1 = {dots[0].get_dot_x()}, {dots[0].get_dot_y()}, {dots[0].get_dot_z()}")
print(f"Coordinates of dot2 = {dots[1].get_dot_x()}, {dots[1].get_dot_y()}, {dots[1].get_dot_z()}")

extra_dot = dots[0] + dots[1]
print(f"Summ dot1 and dot2 = {extra_dot.get_dot_x()}, {extra_dot.get_dot_y()}, {extra_dot.get_dot_z()}")

extra_dot = dots[0] * dots[1]
print(f"Plural dot1 and dot2 = {extra_dot.get_dot_x()}, {extra_dot.get_dot_y()}, {extra_dot.get_dot_z()}")

extra_dot = dots[0] / (-dots[1])
print(f"Division dot1 and negative dot2 = {extra_dot.get_dot_x()}, {extra_dot.get_dot_y()}, {extra_dot.get_dot_z()}")

