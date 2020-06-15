class Point():
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    def createVecteur(self, Point2):
        x = Point2.__x - self.__x
        y = Point2.__y - self.__y
        z = Point2.__z - self.__z
        return Vecteur(x,y,z)

    def __str__(self):
        return ("["+str(self.__x)+","+str(self.__y)+","+str(self.__z)+"]")

class Vecteur():
    def __init__(self,x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        z = self.__z + other.__z
        return Vecteur(x,y,z)

    def prodVectoriel(self, other):
        x = self.__y*other.__z-self.__z*other.__y
        y = self.__z*other.__x-self.__x*other.__z
        z = self.__x*other.__y-self.__y*other.__x
        return Vecteur(x,y,z)


    def __str__(self):
        return ("["+str(self.__x)+","+str(self.__y)+","+str(self.__z)+"]")




