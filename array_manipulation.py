
def sortFunction(mylist):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i] < mylist[j]:
                mylist[i],mylist[j] =  mylist[j],mylist[i]
    return mylist


def inversePairs(mylist):
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
                if mylist[i] > mylist[j]:
                    print("(",mylist[i], mylist[j], ")")

def subArray(mylist):
    newlist = list()
    largestidx = [0,0]
    largestSum = 0
    for i in range(len(mylist)+1):
        for j in range(i + 1, len(mylist)+1):
           newlist.append((mylist[i:j]))
           if (sumSubArray(mylist[i:j]) > largestSum):
               largestSum = sumSubArray(mylist[i:j])
               largestidx= [i,j]
    print('largest sub array is: ', mylist[largestidx[0]:largestidx[1]],' and sum is ',largestSum )

    #return sortFunction(newlist)[0]



def subArray_old(mylist,startIndex):
    newlist = list()
    total = len(mylist) - 1
    if startIndex > 0:
        total = len(mylist) - 1
        while startIndex < total:
            print(mylist[startIndex:total])
            print(sumSubArray(mylist[startIndex:total]))
            newlist.append(sumSubArray(mylist[startIndex:total]))
            startIndex += 1
    else:
        i = 0
        while i < total:
            print(mylist[i:total])
            print(sumSubArray(mylist[i:total]))
            newlist.append(sumSubArray(mylist[i:total]))
            total-=1
    print (sortFunction(newlist)[0])


def sumSubArray(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum+=arr[i]
    return sum


if __name__ == "__main__":

    mylist = [-10,13,99,-7,9,21]
    #inversePairs(mylist)
    #print(mylist[1:4])
    subArray(mylist)
    #print(sortFunction(mylist))

