# Julia Piascik
# CS-341 Spring 2025
# Project 5 - Question 2
# create a program which uses a recordspace of size greater than 30. (it may help to use a prime of form 4n+3, such as 59 ) Hash 30 values in the program using quadratic collision processing. Indicate the number of collisions. Now do the same for a recordspace of size 48. (use the same values) Use hash(key)=(key mod recordspace) + 1

import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def main():
    # generate 200 random numbers between 0 and 500
    random_numbers = [random.randint(0, 500) for _ in range(200)]
    
    # sort the array using quicksort
    sorted_numbers = quicksort(random_numbers)
    
    # print first 20 and last 20 numbers
    print("First 20 numbers:")
    print(sorted_numbers[:20])
    print("\nLast 20 numbers:")
    print(sorted_numbers[-20:])
    
    # test values for searching 
    test_values = [
        sorted_numbers[0],  # first element
        sorted_numbers[-1],  # last element
        sorted_numbers[100],  # middle element
        random.randint(0, 500),  # random value 
        random.randint(0, 500),  # random value 
        -1,  # not present
        501,  # not present
        sorted_numbers[50],  # present value
        random.randint(0, 500),  # random value
        sorted_numbers[101]  # present value
    ]
    
    print("\nSearch Results:")
    print("Value\tBinary Search\t\t\tSequential Search")
    print("     \tPosition\tComparisons\tPosition\tComparisons")
    print("-" * 70)
    
    for value in test_values:
        bin_pos, bin_comps = binary_search(sorted_numbers, value)
        seq_pos, seq_comps = sequential_search(sorted_numbers, value)
        
        print(f"{value}\t{bin_pos}\t\t{bin_comps}\t\t{seq_pos}\t\t{seq_comps}")

if __name__ == "__main__":
    main()
