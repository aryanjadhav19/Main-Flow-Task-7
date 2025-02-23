# 47. Count Inversions using a modified Merge Sort
def merge_count_split_inv(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_count_split_inv(arr, temp_arr, left, mid)
        inv_count += merge_count_split_inv(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index to be sorted
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count
def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_count_split_inv(arr, temp_arr, 0, n - 1)

# 48. Find the Longest Palindromic Substring
def longest_palindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd = expand_around_center(s, i, i)
        if len(odd) > len(longest):
            longest = odd
        # Even length palindromes
        even = expand_around_center(s, i, i + 1)
        if len(even) > len(longest):
            longest = even
    return longest

# 49. Traveling Salesman Problem (TSP) using Dynamic Programming (Approximate Solution)
import itertools
def tsp_bruteforce(dist_matrix):
    cities = list(range(len(dist_matrix)))
    min_path = None
    min_distance = float('inf')
    for path in itertools.permutations(cities):
        current_distance = 0
        for i in range(len(path) - 1):
            current_distance += dist_matrix[path[i]][path[i + 1]]
        current_distance += dist_matrix[path[-1]][path[0]]  # Return to the origin city
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = path
    return min_path, min_distance

# 50. Graph Cycle Detection
def dfs_cycle(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor] and dfs_cycle(graph, neighbor, visited, rec_stack):
            return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[node] = False
    return False
def has_cycle(graph):
    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            if dfs_cycle(graph, node, visited, rec_stack):
                return True
    return False

# 51. Longest Substring Without Repeating Characters
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# 52. Find All Valid Parentheses Combinations
def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    result = []
    backtrack('', 0, 0)
    return result

# 53. Zigzag Level Order Traversal of Binary Tree
from collections import deque
def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result

# 54. Palindrome Partitioning
def palindrome_partitioning(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    result = []
    backtrack(0, [])
    return result

# Menu-driven Program
def menu():
    while True:
        print("\n1. Count Inversions")
        print("2. Longest Palindromic Substring")
        print("3. Traveling Salesman Problem (TSP)")
        print("4. Graph Cycle Detection")
        print("5. Longest Substring Without Repeating Characters")
        print("6. Find All Valid Parentheses Combinations")
        print("7. Zigzag Level Order Traversal of Binary Tree")
        print("8. Palindrome Partitioning")
        print("9. Exit")
        choice = int(input("\nEnter your choice (1-9): "))
        if choice == 1:
            arr = list(map(int, input("Enter array elements: ").split()))
            print(f"Number of inversions: {count_inversions(arr)}")
        elif choice == 2:
            s = input("Enter a string: ")
            print(f"Longest palindromic substring: {longest_palindrome(s)}")
        elif choice == 3:
            dist_matrix = [
                list(map(int, input(f"Enter distances for city {i}: ").split()))
                for i in range(int(input("Enter the number of cities: ")))
            ]
            path, distance = tsp_bruteforce(dist_matrix)
            print(f"Shortest path: {path}, Total distance: {distance}")
        elif choice == 4:
            graph = {}
            n = int(input("Enter number of nodes: "))
            for i in range(n):
                graph[i] = list(map(int, input(f"Enter neighbors of node {i}: ").split()))
            print(f"Cycle detected: {has_cycle(graph)}")
        elif choice == 5:
            s = input("Enter a string: ")
            print(f"Length of the longest substring without repeating characters: {longest_substring(s)}")
        elif choice == 6:
            n = int(input("Enter the number of pairs of parentheses: "))
            print(f"All valid combinations: {generate_parentheses(n)}")
        elif choice == 7:
            # Assume TreeNode is defined with val, left, right
            root = TreeNode(1)
            print(f"Zigzag level order: {zigzag_level_order(root)}")
        elif choice == 8:
            s = input("Enter a string: ")
            print(f"Palindrome partitions: {palindrome_partitioning(s)}")
        elif choice == 9:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()