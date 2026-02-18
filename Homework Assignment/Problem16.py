def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

test_intervals = [[1, 10], [2, 5], [6, 12], [14, 20]]
result = merge_intervals(test_intervals)

print(f"Original: {test_intervals}")
print(f"Merged: {result}")
