from typing import Any, List


def find_uniq(dataset: List[int]) -> int:
    while True:
        ret_element = dataset.pop()
        if ret_element in dataset:
            dataset.remove(ret_element)
        else:
            return ret_element


print(find_uniq([1, 2, 3, 2, 1]))

print(find_uniq([54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]))
