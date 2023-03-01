import numpy as np
import matplotlib.tri as mtri
import matplotlib.pyplot as plt
from stl import mesh

def makestl(arr,filename="output.stl",basefrac=0.125,relheight=0.5):
    arr=arr+np.amin(arr)
    arr=arr/np.amax(arr)
    shape=np.shape(arr)
    arr=arr*shape[0]*relheight
    arr=arr+(shape[0]*basefrac)
    plt.imshow(arr)
    plt.show()
    if len(shape)!=2:
        print('wrong shape')
        exit()
    cubeNum=shape[0]*shape[1]
    print(f'Making {cubeNum} cubes...')
    cube = mesh.Mesh(np.zeros(12*cubeNum, dtype=mesh.Mesh.dtype))

    for i in range(shape[0]):
        for j in range(shape[1]):
            print(arr[i,j])
            height=arr[i,j]
            xpos=i
            ypos=j

            vertices = np.array([\
                [0+xpos, 0+ypos, 0],
                [+1+xpos, 0+ypos, 0],
                [+1+xpos, +1+ypos, 0],
                [0+xpos, +1+ypos, 0],
                [0+xpos, 0+ypos, height],
                [+1+xpos, 0+ypos, height],
                [+1+xpos, +1+ypos, height],
                [0+xpos, +1+ypos, height]])
            faces = np.array([\
                [0,3,1],
                [1,3,2],
                [0,4,7],
                [0,7,3],
                [4,5,6],
                [4,6,7],
                [5,1,2],
                [5,2,6],
                [2,3,6],
                [3,7,6],
                [0,1,5],
                [0,5,4]])
            val=(i*shape[1] +j)*12
            for h, f in enumerate(faces):
                for k in range(3):
                    cube.vectors[h+val][k] = vertices[f[k],:]

    cube.save(filename)
