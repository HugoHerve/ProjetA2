from vecteur import *
file = open('Rectangular_HULL.stl')


stl = file.read().split('\n')
print(stl)

#types = ['facet normal','vertex']
#
#facets = []
#for line in stl:
#    if types[0] in line:
#        facets.append({})
#        facets[-1]['facet_normal'] = tuple([float(i) for i in line.split(' ')[-3:]])
#        facets[-1]['vertex'] = []
#    elif types[1] in line:
#        facets[-1]['vertex'].append(tuple([float(i) for i in line.split(' ')[-3:]]))


#xAB = facets[0]['vertex'][1][0]-facets[0]['vertex'][0][0]
#yAB = facets[0]['vertex'][1][1]-facets[0]['vertex'][0][1]
#zAB = facets[0]['vertex'][1][2]-facets[0]['vertex'][0][2]
#xAC = facets[0]['vertex'][2][0]-facets[0]['vertex'][0][0]
#yAC = facets[0]['vertex'][2][1]-facets[0]['vertex'][0][1]
#zAC = facets[0]['vertex'][2][2]-facets[0]['vertex'][0][2]
#zmoy = (facets[0]['vertex'][0][2]+facets[0]['vertex'][0][1]+facets[0]['vertex'][0][0])/3
#xdSk = 1/2*(yAB*zAC-zAB*yAC)
#ydSk = 1/2*(zAB*xAC-xAB*zAC)
#zdSk = 1/2*(xAB*yAC-yAB*xAC)
#dsK = [xdSk,ydSk,zdSk]
#print(dsK)
#print(zmoy)

#for e in facets:
#    for i in e['vertex']:
#        point = Point(i[0],i[1],i[2])
#        print(point)

e = 0
while e != len(facets):
    #print(facets[e]['vertex'])
    for i in facets[e]['vertex']:
        print (i)

    e+=1


