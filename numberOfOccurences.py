import sys


def count_occurrences():
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    sorted_sequence = list(map(int, data[1].split()))
    search_numbers = list(map(int, data[2].split()))
    
    def find_first_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                if mid == 0 or arr[mid - 1] != x:
                    return mid
                high = mid - 1
        return -1
    
    def find_last_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                if mid == len(arr) - 1 or arr[mid + 1] != x:
                    return mid
                low = mid + 1
        return -1
    
    results = []
    for number in search_numbers:
        first = find_first_occurrence(sorted_sequence, number)
        if first == -1:
            results.append(0)
        else:
            last = find_last_occurrence(sorted_sequence, number)
            results.append(last - first + 1)
    
    for result in results:
        print(result)

count_occurrences()