"""
AI Assisted Programming - Algorithms Lab
This file contains functions, classes, and algorithms for the lab.
"""

import statistics
import time
from typing import Any, List, Optional


def greet_user(name: str) -> str:
    """
    Greets a user by name.
    Args:
        name (str): The name of the user.
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def calculate_statistics(numbers: List[int]) -> dict:
    """
    Calculate mean, median, and mode of a list of numbers.
    Args:
        numbers (List[int]): List of numbers.
    Returns:
        dict: Dictionary with mean, median, and mode.
    """
    if not numbers:
        return {"mean": None, "median": None, "mode": None}
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No unique mode"
    return {"mean": mean, "median": median, "mode": mode}


class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


class SortingAlgorithms:
    """A collection of sorting algorithms."""

    def bubble_sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = arr.copy()
        for i in range(n):
            for j in range(0, n-i-1):
                if result[j] > result[j+1]:
                    result[j], result[j+1] = result[j+1], result[j]
        return result

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


class SearchAlgorithms:
    """Search algorithms."""

    def linear_search(self, arr: List[int], target: int) -> Optional[int]:
        for i, value in enumerate(arr):
            if value == target:
                return i
        return None

    def binary_search(self, arr: List[int], target: int) -> Optional[int]:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None


class AIDataStructure:
    """Custom data structure (simple set-based example)."""

    def __init__(self):
        self.data = set()

    def insert(self, value: Any) -> None:
        self.data.add(value)

    def search(self, value: Any) -> bool:
        return value in self.data

    def delete(self, value: Any) -> bool:
        if value in self.data:
            self.data.remove(value)
            return True
        return False


def benchmark_algorithm(func, *args, **kwargs):
    """
    Benchmark an algorithm's performance.
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Execution time for {func.__name__}: {end - start:.6f} seconds")
    return result


if __name__ == "__main__":
    # Test greet_user
    print(greet_user("Alice"))

    # Test calculate_statistics
    stats = calculate_statistics([1, 2, 2, 3, 4])
    print("Statistics:", stats)

    # Test Calculator
    calc = Calculator()
    print("Add:", calc.add(2, 3))
    print("Subtract:", calc.subtract(5, 2))
    print("Multiply:", calc.multiply(3, 4))
    try:
        print("Divide:", calc.divide(10, 0))
    except ValueError as e:
        print("Error:", e)

    # Test SortingAlgorithms
    sorter = SortingAlgorithms()
    arr = [5, 2, 9, 1, 5, 6]
    print("Bubble Sort:", sorter.bubble_sort(arr))
    print("Quick Sort:", sorter.quick_sort(arr))
    print("Merge Sort:", sorter.merge_sort(arr))

    # Test SearchAlgorithms
    searcher = SearchAlgorithms()
    print("Linear Search (find 9):", searcher.linear_search(arr, 9))
    print("Binary Search (find 9):", searcher.binary_search(sorted(arr), 9))

    # Test AIDataStructure
    ds = AIDataStructure()
    ds.insert(10)
    ds.insert(20)
    print("Search 10:", ds.search(10))
    print("Delete 10:", ds.delete(10))
    print("Search 10 after delete:", ds.search(10))

    # Benchmark example
    benchmark_algorithm(sorter.bubble_sort, arr)
