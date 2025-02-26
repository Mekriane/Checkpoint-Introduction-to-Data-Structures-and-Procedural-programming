def sum_of_distinct_elements(arr1, arr2):
    sum_distinct = 0  
    for num in arr1:
        if num not in arr2:
            sum_distinct += num
    for num in arr2:
        if num not in arr1:
            sum_distinct += num

    return sum_distinct

# TEST
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
result = sum_of_distinct_elements(set1, set2)
print("Output:", result)  
