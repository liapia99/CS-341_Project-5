# CS-341_Project-5: Algorithm Analysis

## Question 1: Sorting and Searching Algorithms Comparison

This program demonstrates and compares the performance of different sorting and searching algorithms. It implements QuickSort for sorting and both Binary Search and Sequential Search for searching elements in an array.

### Features

- **QuickSort Implementation**: Efficient sorting algorithm with O(n log n) average time complexity
- **Binary Search**: Fast search algorithm with O(log n) time complexity
- **Sequential Search**: Linear search algorithm with O(n) time complexity
- **Performance Comparison**: Compares the number of comparisons made by both search algorithms
- **Random Data Generation**: Creates test data with 200 random numbers between 0 and 500

#### Main Functions

1. `quicksort(arr)`: Implements the QuickSort algorithm
   - Takes an array as input
   - Returns a sorted array
   - Uses middle element as pivot

2. `binary_search(arr, target)`: Implements Binary Search
   - Takes sorted array and target value as input
   - Returns tuple of (position, number of comparisons)
   - Returns -1 if element not found

3. `sequential_search(arr, target)`: Implements Sequential Search
   - Takes array and target value as input
   - Returns tuple of (position, number of comparisons)
   - Returns -1 if element not found

### Tests

The program tests the search algorithms with various scenarios:
- First element in array
- Last element in array
- Middle element
- Random values
- Values not present in array
- Specific positions in array

### Usage

```bash
python question1.py
```

### Output

The program provides:
1. First 20 numbers of the sorted array
2. Last 20 numbers of the sorted array
3. Comparison table showing:
   - Search value
   - Binary search results (position and comparisons)
   - Sequential search results (position and comparisons)

### Time Complexity

- QuickSort: O(n log n) average case
- Binary Search: O(log n)
- Sequential Search: O(n)

### Space Complexity

- QuickSort: O(n)
- Binary Search: O(1)
- Sequential Search: O(1)

## Question 2: Hash Table Implementation with Quadratic Probing

This program demonstrates the implementation of a hash table using quadratic probing for collision resolution. It compares the performance of hashing with different record space sizes.

### Features

- **Hash Function**: Simple modulo-based hash function
- **Quadratic Probing**: Collision resolution using quadratic probing
- **Performance Analysis**: Compares collision rates with different table sizes
- **Random Data Generation**: Creates test data with 30 random numbers between 0 and 1000

#### Main Functions

1. `hash_function(key, record_space)`: Implements the hash function
   - Takes key and record space size as input
   - Returns hash value (1-based indexing)

2. `quadratic_probing(hash_table, key, record_space)`: Implements quadratic probing
   - Takes hash table, key, and record space size as input
   - Returns number of collisions
   - Handles table full condition

### Tests

The program tests hashing with:
- Record space of 59
- Record space of 48
- 30 random values between 0 and 1000

### Usage

```bash
python question2.py
```

### Output

For each record space size, the program provides:
1. Table showing:
   - Input value
   - Initial hash value
   - Final position
   - Number of collisions
2. Total collisions for each record space
3. Comparison of collision rates between different record space sizes

### Analysis

The program demonstrates how different table sizes affect collision rates in hash tables, showing the importance of choosing appropriate table sizes for hash table implementations.
