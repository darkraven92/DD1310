def br_search(v, target):
    """Returns True if the sorted list v contains target and False otherwise. 
    Undefined behaviour if v is not sorted"""
    def helper(v, target, left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        print(v[mid]) # print for testing purposes only
        if v[mid] == target:
            return True
        elif v[mid] > target:
            return helper(v, target, left, mid-1)
        else:
            return helper(v, target, mid+1, right)
    
    return helper(v, target, 0, len(v)-1)

v = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(br_search(v, 5)) # should print True
