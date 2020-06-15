import numpy as np

class StlParser:
    def __init__(self, filepath):
        self.__file_content = open(filepath).read().split('\n')
        self.__vertex, self.__facet_normal = self.extract_facet_data()
        self.__facet_surfaces = self.calculSurface()
        self.__Zmoyen = self.calculZmoyen()
       # print (self.__Zmoyen)
       # print(self.__vertex)

    def extract_facet_data(self):
        data_types = ['facet normal', 'vertex']
        vertex = []
        facet_normal = []
        for line in self.__file_content:
            if data_types[0] in line:
                facet_normal.append([float(i) for i in line.split(' ')[-3:]])
                vertex.append([])
            elif data_types[1] in line:
                vertex[-1].append([float(i) for i in line.split(' ')[-3:]])

        return np.array(vertex),np.array(facet_normal)

    def calculSurface(self):
        facet_surface = []
        for vertex in self.__vertex:
            A, B, C = vertex
            facet_surface.append(np.cross(B-A,C-A)/2)
        return np.array(facet_surface)


    def calculZmoyen(self):
        z_moyen = []
        for vertex in self.__vertex:
            z_moyen.append(sum(vertex[:,2])/3)
        return np.array(z_moyen)


if __name__ == '__main__':
    stl_passer = StlParser('Rectangular_HULL.stl')








