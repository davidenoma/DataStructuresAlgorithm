import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,4], np.int16)
y = np.ones(5)
z = np.array([[1,2,3,5],[7,2,24,2]])
z2 = np.array([[[1,2,3,4],[1,2,3,4]],[[-2,4,1,2],[5,6,3,1]]])
def main():
    #arrays()
    #()
    matplotlib_run()

def arrays():
    print(y)
    print(y[-1])
    print(z[1:,])
    print(z2[0,1,3])
    print(z.shape,y.shape,z2.shape)
    print(z2.ndim,y.ndim)
    print(z2.dtype,z2.size)
def matrices():

    x = np.tri(5,3,k=-1,dtype=np.uint16)
    x=np.ones((5,5),dtype=np.uint8)
    y = np.tril(x,k=-1)
    print(y)
    print(x )
    print(x*y)

def matplotlib_run():
    x = np.arange(5)
    y = x

    plt.plot(x,y,'o')
    plt.show()
if __name__ == "__main__":
  main()
