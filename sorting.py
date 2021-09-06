pyList = [4,12,2,34,17]
pyList.append(18)
pyList.append(64)
pyList.append(6)
pyList.append(99)

pyListA = [34,12]
pyListB = [4,6,31,9]
c = pyListA.extend(pyListB)
print(pyListA)

#Sets
smith = set()
smith.add("CSCI-112")
smith.add("MATH-121")
smith.add("HIST-340")
smith.add("ECON-101")

roberts = set()
roberts.add("POL-101")
roberts.add("ANTH-230")
roberts.add("CSCI-112")
roberts.add("ECON-101")
def testingSet():

    if smith == roberts:
        print('Smith and roberts are taking same course')
    else:
        sameCourses = smith.intersection(roberts)
    if len(sameCourses) == 0:
        print("Smith and Roberts are not taking same courses")
    else:
        print("Smith and roberts are taking some of the same courses:")
        for course in sameCourses:
            print(course)

    uniqueCourses = smith.difference(roberts)
    for course in uniqueCourses:
        print(course)

    smith.add("CSCI-112")
    print(smith)
    smith.add("MATH-121")
    print(smith)

def myBinarySearch(xlist,y):
    high = len(xlist) - 1
    low = 0
    while low <= high:
        mid = (low + high)//2
        if xlist[mid] == y:
            return True
        elif xlist[mid] > y:
            high = mid - 1
        else:
            low = mid + 1
    return False
#print(toSort)


def myBubbleSort(xlist):
    num = len(xlist) - 1
    for i in range(num):
        for j in range(num):
                if xlist[j] < xlist[j+1]:
                    xlist[j],xlist[j+1] = xlist[j+1],xlist[j]

    return xlist
#print(myBubbleSort([21,33,4,12,33,17]))

def insertion_sort(mylist):
    num = len(mylist)
    for i in range(1,num):
        value = mylist[i]
        pos = i
        while pos > 0 and value < mylist[pos-1]:
            mylist[pos] = mylist[pos - 1]
            pos -= 1
        mylist[pos] = value

    return mylist


def selection_sort(mylist):
    length = len(mylist)
    for i in range(length):
        for j in range(i+1,length):
            if mylist[i] > mylist[j]:
                mylist[i],mylist[j]=mylist[j],mylist[i]
    return mylist

def selection_sort2(seq):
    n = len(seq)
    for i in range(n-1):
        smIdx = i
        for j in range(i+1,n):
            if seq[j] > seq[smIdx]:
                smIdx = j
        if smIdx != i:
            seq[i],seq[smIdx] = seq[smIdx],seq[i]

    return seq
#print(selection_sort2([21,33,4,12,33,17]))

def mergeSortedList(listA,listB):
    newList = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a+=1
        else:
            newList.append(listB[b])
            b+=1

    while a < len(listA):
        newList.append(listA[a])
        a +=1
    while a < len(listB):
        newList.append(listB[b])
        b+=1

    return newList

def main():
    print(mergeSortedList([21,33,4,12,33,17],[10,22,33]))

if __name__ == "__main__":
    main()




