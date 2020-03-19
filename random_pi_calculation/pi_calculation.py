import random
from math import *

def points_generator(nb_points):
    nb_pt_in_circle = 0
    nb_pt_in_square = 0
    for i in range (nb_points):
        X = random.uniform(0, 1)
        Y = random.uniform(0, 1)
        #Si le point est dans le carré on incremente  le nb  de carré
        #Si le point est dans le cercle on incremente le nb de cercle et le nb de carré
        if sqrt( (X**2) + (Y**2) ) <= 1:
            nb_pt_in_circle += 1
            nb_pt_in_square += 1
        else:
            nb_pt_in_square += 1
    print(4*nb_pt_in_circle/nb_pt_in_square)

points_generator(100000)