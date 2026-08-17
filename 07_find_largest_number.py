def find_largest(nums): # for find the largest number
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
        
print(find_largest([3, 7, 2, 9, 4]))  # should print 9

def find_smallest(nums): # for find the smallest number
    smallest = nums[0]

    for s in nums:
        if s < smallest:
            smallest = s
    return smallest

print(find_smallest([3,7,2,9,4]))

def find_largest_index(nums):
    largest = nums[0]
    idx = 0
    for i, num in enumerate(nums):
        if num > largest:
            largest = num
            idx = i

    return idx

print(find_largest_index([3,7,2,9,4]))
