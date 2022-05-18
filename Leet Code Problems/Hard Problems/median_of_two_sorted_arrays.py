def find_median_sorted_array(nums1, nums2):
    """
    >>> find_median_sorted_array([1, 3], [2])
    2.0
    >>> find_median_sorted_array([1, 2], [3, 4])
    2.5
    >>> find_median_sorted_array([1, 3], [2, 7])
    2.5
    """
    nums = nums1+nums2
    nums.sort()
    if len(nums) % 2 == 0:
        return ((nums[int(len(nums)/2)]) + (nums[int(len(nums)/2-1)])) / 2
    return float(nums[len(nums)//2])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
