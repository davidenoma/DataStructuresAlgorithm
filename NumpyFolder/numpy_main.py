import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,3,4], np.int16)
y = np.ones(5)
z = np.array([[1,2,3,5],[7,2,24,2]])
z2 = np.array([[[1,2,3,4],[1,2,3,4]],[[-2,4,1,2],[5,6,3,1]]])
def main():
    #arrays()
    #()
   # matplotlib_run()
    #routines_for_random()
    #array_manipulation()
    #bitwise_operations()
    statistical_functions()

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

    plt.plot(x,y,'o--')
    plt.plot(x,y,'o-')
    plt.plot(x,-y,'o-')
   # plt.title('y and x from numpy')
    N = 11
    x = np.linspace(0,10,N)
    print(x)
    y = x
   # plt.plot(x,y,'o--')
    #plt.axis('off')
  #  plt.show()
  #  plt.plot(x,y,'o-')
    #plt.show()
   # y = np.logspace(0.1,1,N)
 #   y = np.logspace(0.1, 1000, N)
    y = np.geomspace(0.1,1000,N)
    plt.plot(x,y,'o--')
    plt.show()
def routines_for_random():
    x = np.random.randint(low=0,high=9,size=10)
    x=np.random.rand(3,3,3)
    print(x)
def array_manipulation():
    #Array Manipulation Routines
    x = np.arange(6)
    print(x)
    y=x.reshape((2,3))
   # print(y)
    x = np.array([[0,1,2],[3,4,5]],dtype=np.uint8)
   # print(x)
    z = np.stack((x,y), axis=-1)
    #z = np.vstack((x,y), axis = -1)

    x = np.arange(9)
    a,b,c = np.split(x,3)

    print(a,b,c )
    x = np.random.rand(4,4,4)
  #  print(x)
    y,z = np.split(x,2)
   # print('y',y,'z',z)
    print(y.shape,z.shape)
    x=np.arange(16).reshape(4,4)
   # print(x)
    #print(z)
    y = np.flip(x,axis=-1)
    y = np.flip(x,axis=1)
    y = np.roll(x,8)
    y = np.rot90(x)
    print(x)
    print(y)
def bitwise_operations():
    x = np.array([0,1,0,8],np.uint8)
    y = np.array([0,0,1,1],np.uint8)

    print(np.bitwise_and(x,y))
def statistical_functions():
    x = np.random.randint(0,10,15)
    print(np.average(x))
    print(np.std(x))
    print(np.var(x))
    print(np.histogram(x))

if __name__ == "__main__":
   main()
