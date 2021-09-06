from sorting import myBinarySearch
def count_down(n):
    while n > 0:
        print(n)
        n-=1
count_down(89)

def recursive_countdown(n):
    if n <= 0:
        return
    else:
        print(n)
        recursive_countdown(n-1)
def recursive_binary_search(mylist,element,low, mid,high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if mylist[mid] == element:
            return True
        else:
            if mylist[mid] > element:
                return recursive_binary_search(mylist,element,low,mid - 1)
            else:
                return recursive_binary_search(mylist,element,mid+1,high)
def main():
    my_list = [-343,33,-98,99,3,-55,2,34,3,3,8]
    print(my_list)

if __name__ == "__main__":
    main()
