#!/usr/bin/python3
import random

from algorithms.searching import *


def random_array(arr_len: int, min_value: int = 0, max_value: int = 10) -> list[int]:
    rand_arr = []

    if arr_len < 0 or min_value > max_value:
        return rand_arr

    random.seed()
    for _ in range(0, arr_len):
        random_number = random.randint(min_value, max_value)
        rand_arr.append(random_number)

    return rand_arr


if __name__ == "__main__":
    for arr_size in [1000000]:
        arr = random_array(arr_size, 0, arr_size)
        sorted_arr = sorted(arr)
        reversed_arr = sorted(arr, reverse=True)

        random.seed()

        test_cases = [
            SearchTest("Best Case", sorted_arr, sorted_arr[0]),
            SearchTest("Average Case", arr, random.choice(arr)),
            SearchTest("Worst Case", reversed_arr, reversed_arr[len(reversed_arr) - 1]),
        ]

        search_perf_metrics(test_cases, binary_search)
        print("=" * 32)

        search_perf_metrics(test_cases, recursive_binary_search)
        print("=" * 32)
