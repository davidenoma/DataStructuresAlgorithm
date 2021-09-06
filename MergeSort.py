def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list)//2
    left_list = my_list[:mid]
    right_list = my_list[mid:]
    print(left_list,right_list)

    merge_sort(left_list)
    merge_sort(right_list)


    return left_list,right_list
def main():
    my_list = [-343,33,-98,99,3,-55,2,34,3,3,8]
    print(merge_sort(my_list))

if __name__ == "__main__":
    main()


