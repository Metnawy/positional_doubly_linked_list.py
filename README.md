

```markdown
# Positional Doubly Linked List

This Python script implements a **Positional Doubly Linked List**, a data structure that allows for efficient insertion, deletion, and traversal of elements in both forward and backward directions. The list is designed to provide positional access to nodes, enabling operations like adding, deleting, and swapping elements at specific positions.

## Features

- **Doubly Linked List**: Each node contains references to both the next and previous nodes, allowing for bidirectional traversal.
- **Positional Access**: Nodes are accessed via `_position` objects, which act as handles to specific nodes in the list.
- **Basic Operations**:
  - **Add/Remove Elements**: Add or remove elements at the beginning, end, or any specific position in the list.
  - **Swap Nodes**: Swap the values or positions of two nodes in the list.
  - **Sorting**: Sort the list based on node values or access counts.
  - **Iteration**: Iterate through the list using Python's `__iter__` method.
  - **Reversing**: Reverse the order of elements in the list.
- **Advanced Operations**:
  - **Merge Sort**: Sort the list using a merge sort algorithm.
  - **Access Count Sorting**: Sort the list based on the number of times nodes have been accessed.
  - **Positional Manipulation**: Add, delete, or swap nodes based on their positions.

## Usage

### Initialization

To create a new positional doubly linked list:

```python
f = positional_doubly_linked_list()
```

### Adding Elements

- **Add to the beginning**:
  ```python
  f.add_first(10)
  ```
- **Add to the end**:
  ```python
  f.add_last(20)
  ```
- **Add before/after a specific position**:
  ```python
  pos = f.first()  # Get the first position
  f.add_before_position(15, pos)  # Add 15 before the first element
  f.add_after_position(25, pos)   # Add 25 after the first element
  ```

### Removing Elements

- **Remove the first element**:
  ```python
  f.delete_first()
  ```
- **Remove the last element**:
  ```python
  f.delete_last()
  ```
- **Remove a specific element**:
  ```python
  pos = f.first()  # Get the first position
  f.delete_position(pos)  # Delete the first element
  ```

### Swapping Nodes

- **Swap values of two nodes**:
  ```python
  pos1 = f.first()
  pos2 = f.last()
  f.swap(pos1, pos2)
  ```
- **Swap nodes themselves**:
  ```python
  f.swap_nodes(pos1, pos2)
  ```

### Sorting

- **Sort by value**:
  ```python
  sorted_list = f.sort_value(f.first().node, f.last().node, f.size)
  ```
- **Sort by access count**:
  ```python
  sorted_list = f.access_count_sort(f.first().node, f.last().node, f.size)
  ```

### Iteration

- **Iterate through the list**:
  ```python
  for value in f:
      print(value)
  ```

### Reversing the List

- **Reverse the list**:
  ```python
  reversed_list = reversed(f)
  ```

### Finding Elements

- **Find the first occurrence of a value**:
  ```python
  pos = f.find(10)
  ```
- **Find all occurrences of a value**:
  ```python
  positions = f.findall(10)
  ```

## Example

```python
f = positional_doubly_linked_list()
f.add_first(6)
f.add_first(4)
f.add_first(2)
f.add_last(555)

print(f)  # Output: head-->2-->4-->6-->555-->tail

# Reverse the list
reversed_list = reversed(f)
print(reversed_list)  # Output: head-->555-->6-->4-->2-->tail

# Sort the list by value
sorted_list = f.sort_value(f.first().node, f.last().node, f.size)
for value in sorted_list:
    print(value)  # Output: 2, 4, 6, 555
```

## Notes

- The list uses **sentinel nodes** (`head` and `tail`) to simplify boundary conditions.
- The `_position` class acts as a handle to nodes, allowing for safe and efficient manipulation of the list.
- The list supports **1-based indexing** for positional operations.

