'''
Binary Search key point:
1. mid is (low + high) / 2
2. The search will always end up with head and tail pointing at
   the same index, assume the number at that index is a
   if a is the target, we are good
   if target is smaller than a, we will move high to be mid - 1, therefore low is the right place to put in
   if target is larger than a, we will move low to be mid + 1, therefore low is still the right place to put in 
3. I feel more comfortable comparing the target to the mid value
'''

def get_insertion_position(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)
        mid_val = nums[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            low = mid + 1
        else:
            high = mid - 1
    return low


nums = [1, 3, 6, 8]
targets = [0, 2, 6, 9]
for target in targets:
    print(get_insertion_position(nums, target))
