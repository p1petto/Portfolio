import re
import time

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def xy(self):
        return (self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __ne__(self, other):
        return self.__x != other.__x or self.__y != other.__y

    def __str__(self):
        return f"({self.__x}; {self.__y})"


class Figure:
    def __init__(self, pts):
        self.__product = None
        self.__l = None
        self.__v1 = None
        self.__v2 = None
        self._pts = pts
        self.__area = self._update_area()

    # def _update_area(self):
    #     print("Figure::update_area")
    #     pass

    @property
    def area(self):
        return self.__area

    def __lt__(self, other):
        return self.__area < other.area

    def __le__(self, other):
        return self.__area <= other.area

    def __eq__(self, other):
        return self.__area == other.area

    def __ne__(self, other):
        return self.__area != other.area

    def __ge__(self, other):
        return self.__area >= other.area

    def __gt__(self, other):
        return self.__area > other.area

    def is_convex(self):
        self.__l = []
        for i in range(len(points)):
            self.__v1 = Point(self._pts[0].x - self._pts[1].x, self._pts[0].y - self._pts[1].y)
            self.__v2 = Point(self._pts[2].x - self._pts[1].x, self._pts[2].y - self._pts[1].y)
            self.__product = self.__v1.x * self.__v2.y - self.__v1.y * self.__v2.x
            self.__l.append(self.__product)
        return all([x > 0 for x in self.__l]) or all([x < 0 for x in self.__l])


class Triangle(Figure):

    def _update_area(self):
        return 1 / 2 * abs(self._pts[0].x * self._pts[1].y
                           + self._pts[1].x * self._pts[2].y
                           + self._pts[2].x * self._pts[0].y
                           - self._pts[1].x * self._pts[0].y
                           - self._pts[2].x * self._pts[1].y
                           - self._pts[0].x * self._pts[2].y)

    def __str__(self):
        return f"[{self._pts[0]}; {self._pts[1]}; {self._pts[2]}]"


class Quadrilateral(Figure):

    def _update_area(self):
        # return 1 / 2 * abs(self._pts[0].x * self._pts[1].y
        #                    + self._pts[1].x * self._pts[2].y
        #                    + self._pts[2].x * self._pts[3].y
        #                    + self._pts[3].x * self._pts[0].y
        #                    - self._pts[1].x * self._pts[0].y
        #                    - self._pts[2].x * self._pts[1].y
        #                    - self._pts[3].x * self._pts[2].y
        #                    - self._pts[0].x * self._pts[3].y)
        self.__temp1 = Triangle([self._pts[0], self._pts[1], self._pts[2]])
        self.__temp2 = Triangle([self._pts[3], self._pts[1], self._pts[2]])
        return self.__temp1.area + self.__temp2.area

    def __str__(self):
        return f"[{self._pts[0]}; {self._pts[1]}; {self._pts[2]}; {self._pts[3]}]"


def split_pairs(line):
    n = 2
    new_list = []
    for i in range(0, len(line), n):
        element = line[i:i + n]
        new_list.append(element)

    return new_list


s = open('plist.txt', "r", encoding="utf-8").readline()
s = (re.sub('\W+', ' ', s)).split()

points = []
for i in range(0, len(s), 2):
    points.append(Point(int(s[i]), int(s[i + 1])))
triangles = []

for i in range(len(points) - 2):
    for j in range(i, len(points) - 1):
        for k in range(j, len(points)):
            t = Triangle((points[i], points[j], points[k]))
            if t.area != 0:
                triangles.append(t)

triangles = sorted(triangles)

print(f"triangle with largest area: {triangles[len(triangles) - 1]}, {triangles[len(triangles) - 1].area}")

time_start = time.time()
quadrilaterals = []

for i in range(len(points) - 3):
    for j in range(i, len(points) - 2):
        for k in range(j, len(points) - 1):
            for m in range(k, len(points)):
                temp1 = Triangle([points[i], points[j], points[k]])
                temp2 = Triangle([points[j], points[k], points[m]])
                if (points[i] != points[j] and points[i] != points[k] and points[i] != points[m]
                        and points[j] != points[k] and points[j] != points[m]
                        and points[k] != points[m]):
                    if temp1.area != 0 and temp2.area != 0:
                        f = Quadrilateral((points[i], points[j], points[k], points[m]))
                        quadrilaterals.append(f)

quadrilaterals = sorted(quadrilaterals)

print(f"quadrilateral with largest area: {quadrilaterals[len(quadrilaterals) - 1]} {quadrilaterals[len(quadrilaterals) - 1].area}")
time_elapsed = (time.time() - time_start)
print("Время на выполнение", time_elapsed)