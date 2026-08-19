def two_pointers(nums, target):
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    all_pairs = []
    while left < right:
        store = nums[left] + nums[right]
        if store < target:
            left += 1
        elif store > target:
            right -= 1
        else:
            all_pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
    return all_pairs
        
print(two_pointers(nums=[1, 3, 2, 4, 9, 6, 8], target=10))