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

    # AI Assisted Programming - Algorithms Lab Template
    # This file is a template for students. Complete the tasks as instructed in the lab README.

    # Task 1: Basic Function
    # TODO: Write a function that greets a user by name

    # def greet_user(name):
    pass

# Task 2: Statistics Function
# TODO: Write a function that calculates mean, median, and mode of a list of numbers

# def calculate_statistics(numbers):
    pass

# Task 3: Calculator Class
# TODO: Create a Calculator class with add, subtract, multiply, and divide methods

# class Calculator:
    pass

# Task 4: Sorting Algorithms
# TODO: Implement bubble sort, quick sort, and merge sort algorithms in a class

# class SortingAlgorithms:
    pass

# Task 5: Search Algorithms
# TODO: Implement linear search and binary search algorithms in a class

# class SearchAlgorithms:
    pass

# Task 6: Data Structure
# TODO: Create a custom data structure class with insert, search, and delete methods

# class AIDataStructure:
    pass

# Task 7: Benchmarking
# TODO: Write a function to benchmark the performance of an algorithm

# def benchmark_algorithm(func, *args, **kwargs):
    pass


if __name__ == "__main__":
    # TODO: Add test code here to demonstrate your implementations
    pass
