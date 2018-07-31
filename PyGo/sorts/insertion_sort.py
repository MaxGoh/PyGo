from typing import Sequence

def insertion_sort(list: Sequence[float]) -> Sequence[float]:
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while (i > 0 and list[i] > key):
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = key

    return list

if __name__ == '__main__':
    print(insertion_sort([1, 3, 2, 10, 5]))
    print(insertion_sort([1, 8, 1, 20, 7]))
    print(insertion_sort([1, 7, 3, 11, 8]))
