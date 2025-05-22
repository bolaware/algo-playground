from contains_duplicate import contains_duplicate, contains_duplicate2

def test_no_duplicates():
    nums = [1, 2, 3, 4, 5]
    assert not contains_duplicate(nums)
    assert not contains_duplicate2(nums) # Test both versions

def test_with_duplicates():
    nums = [1, 2, 3, 4, 1]
    assert contains_duplicate(nums)
    assert contains_duplicate2(nums)

def test_all_duplicates():
    nums = [7, 7, 7, 7]
    assert contains_duplicate(nums)
    assert contains_duplicate2(nums)

def test_empty_list():
    nums = []
    assert not contains_duplicate(nums)
    assert not contains_duplicate2(nums)

def test_single_element_list():
    nums = [42]
    assert not contains_duplicate(nums)
    assert not contains_duplicate2(nums)

def test_multiple_duplicates():
    nums = [1, 2, 1, 3, 4, 2]
    assert contains_duplicate(nums)
    assert contains_duplicate2(nums)

def test_negative_numbers():
    nums = [-1, -2, -1, 0]
    assert contains_duplicate(nums)
    assert contains_duplicate2(nums)

def test_large_numbers():
    nums = [1000000000, 2000000000, 1000000000]
    assert contains_duplicate(nums)
    assert contains_duplicate2(nums)