from sorting import *
def contains(my_list,element):
    #insert code here
    for e in my_list:
        if e == element:
            return True
    return False

def main():
    my_list = [9,3,4,3,23,432,234,2,3]
    insertion_sort(my_list)
    print(my_list)
    print(contains(my_list,4))

if __name__ == "__main__":
    main()
