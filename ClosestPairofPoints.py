from math import pow
#Closest pair of points using divide and conquer algorithm
class ClosestPair:
    coordinates = []
    xCoordinates = []
    yCoordinates = []

    def distance(self, point1, point2): #distance between points
        return pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)

    def sortByX(self):  #using bubble sort, sorting points based on x coordinate
        p = self.coordinates.copy()
        l = []
        n = len(p)
        for i in range(len(self.coordinates)):
            l.append(i)
        for i in range(n):
            for j in range(0, n - i - 1):
                if p[j][0] > p[j + 1][0]:
                    p[j], p[j + 1] = p[j + 1], p[j]
        return l

    def sortByY(self):  #sorting points based on y coordinate
        p = self.coordinates.copy()
        l = []
        n = len(p)
        for i in range(len(self.coordinates)):
            l.append(i)
        for i in range(n):
            for j in range(0, n - i - 1):
                if p[j][1] > p[j + 1][1]:
                    p[j], p[j + 1] = p[j + 1], p[j]
        return l

    def divideAndConquer(self, l_index, r_index):   #recursive divide and conquer
        if l_index >= r_index:
            return None
        elif l_index + 1 == r_index:
            return (self.xCoordinates[l_index], self.xCoordinates[r_index])
        else:
            mid = (l_index + r_index) // 2
            part = self.divideAndConquer(l_index, mid)
            nextPart = self.divideAndConquer(mid + 1, r_index)

            if part is None:
                min = nextPart
                max = nextPart
            elif nextPart is None:
                (min, max) = part
            else:
                (left1, left2) = part
                (right1, right2) = nextPart
                nearest1 = self.distance(self.coordinates[left1], self.coordinates[left2])
                nearest2 = self.distance(self.coordinates[right1], self.coordinates[right2])
                if nearest1 < nearest2:
                    (min, max) = (left1, left2)
                else:
                    (min, max) = (right1, right2)

            d = self.distance(self.coordinates[min], self.coordinates[max])
            dx = self.coordinates[self.xCoordinates[mid]][0] + self.coordinates[self.xCoordinates[mid + 1]][0]
            xMargin = dx / 2

            space = [j for j in self.yCoordinates if abs(self.coordinates[j][0] - xMargin) <= d]

            for p in range(len(space)):
                r = p + 1
                while r < len(space) and (self.coordinates[self.yCoordinates[r]][1] - self.coordinates[self.yCoordinates[p]][1]) < d and r - p <= 6:
                    yMargin = self.distance(self.coordinates[self.yCoordinates[p]], self.coordinates[self.yCoordinates[r]])
                    if yMargin < d:
                        d = yMargin
                        min = p
                        max = r
                    r = r + 1
            return (min, max)

    def pair(self,t):
       self.coordinates = t
       self.xCoordinates = self.sortByX()
       self.yCoordinates = self.sortByY()
       return self.divideAndConquer(0, len(self.coordinates) - 1)


closestPair = ClosestPair()

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
cp = closestPair.pair(points)
print("Given points are = = => ",points)
print("Closest Pair of points are ---> ",points[cp[0]]," and ",points[cp[1]])
print()
print()
points = [(0,0), (-2,0), (4,0), (1,1), (3,3), (-2,2), (5,2)]
cp = closestPair.pair(points)
print("Given points are = = => ",points)
print("Closest Pair of points are ---> ",points[cp[0]]," and ",points[cp[1]])
