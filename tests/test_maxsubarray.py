from algo import max_subarray


def test_max_subarray_example():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(nums) == 6

def test_max_subarray_all_negative():
    nums = [-5, -2, -3]
    assert max_subarray(nums) == -2
