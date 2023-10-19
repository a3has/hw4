def merge_list(list1, list2):

    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists.")

    for element in list1 + list2:
        if not isinstance(element, int):
            raise TypeError("Both lists must contain integers only.")

    mergeList = list1 + list2

    swapped = False
    for i in range(len(mergeList) - 1, 0, -1):

        for j in range(i):

            if mergeList[j] > mergeList[j+1]:

                mergeList[j], mergeList[j+1] = mergeList[j+1], mergeList[j]
                swapped = True

        if swapped:
            swapped = False

        else:
            break

    return mergeList

# print(merge_list([1, 5, 3, 7], [6, 2, 4]))
