# 87680593

def broken_search(nums, target) -> int:
    left_side = 0
    right_side = len(nums) - 1
    while left_side <= right_side:
        mid = (left_side + right_side) // 2
        if nums[mid] == target:
            return mid
        if nums[left_side] <= nums[mid]:
            if nums[left_side] <= target < nums[mid]:
                right_side = mid - 1
            else:
                left_side = mid + 1
        else:
            if nums[mid] < target <= nums[right_side]:
                left_side = mid + 1
            else:
                right_side = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
