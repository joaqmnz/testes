def selection_sort(array: list, reverse: bool = False) -> None:
    for i in range(len(array)):
        for j in range(len(array)):
            if reverse:
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
            else:
                if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
