import time
from dataclasses import dataclass
from typing import Callable


@dataclass
class SearchTest:
    name: str
    arr: list[int]
    elem: int


def search_perf_metrics(t_cases: list[SearchTest], func_call: Callable[[int, list[int]], int]):
    """
    Measures the execution time of a search algorithm

    Args:
        t_cases: List of search test case inputs
        func_call: Searching algorithm being tested

    Returns: void

    """
    for t_case in t_cases:
        start_time = time.perf_counter(), time.process_time()
        _ = func_call(t_case.elem, t_case.arr)
        end_time = time.perf_counter(), time.process_time()

        elapsed_real_time = end_time[0] - start_time[0]
        elapsed_cpu_time = end_time[1] - start_time[1]

        print(f"[{t_case.name}] {func_call.__name__}(arr_length: {len(t_case.arr):_})")
        print(f" Real time: {elapsed_real_time:.10f} seconds")
        print(f" CPU time: {elapsed_cpu_time:.10f} seconds")
        print()

def linear_search(elem: int, arr: list[int]) -> int:
    for i in range(0, len(arr)):
        if arr[i] == elem:
            return i

    return -1


def binary_search(elem: int, arr: list[int]) -> int:
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if arr[midpoint] == elem:
            return midpoint
        elif arr[midpoint] < elem:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return -1


def recursive_binary_search(elem: int, arr: list[int]) -> int:
    if len(arr) == 0:
        return -1

    midpoint = len(arr) // 2

    if arr[midpoint] == elem:
        return midpoint
    else:
        if arr[midpoint] < elem:
            return recursive_binary_search(elem, arr[midpoint+1:])
        else:
            return recursive_binary_search(elem, arr[:midpoint])
