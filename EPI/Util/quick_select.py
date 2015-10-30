import random
 
def partition(vector, left, right, pivotIndex, key=None):
    pivotValue = vector[pivotIndex] if not key else key(vector[pivotIndex])
    vector[pivotIndex], vector[right] = vector[right], vector[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        val = vector[i] if not key else key(vector[i])
        if val < pivotValue:
            vector[storeIndex], vector[i] = vector[i], vector[storeIndex]
            storeIndex += 1
    vector[right], vector[storeIndex] = vector[storeIndex], vector[right] 
    return storeIndex
 
def _select(vector, left, right, k, key=None):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive."
    while True:
        pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
        pivotNewIndex = partition(vector, left, right, pivotIndex, key)
        pivotDist = pivotNewIndex - left
        if pivotDist == k:
            return vector[pivotNewIndex]
        elif k < pivotDist:
            right = pivotNewIndex - 1
        else:
            k -= pivotDist + 1
            left = pivotNewIndex + 1
 
def select(vector, k, key=None):
    """\
    Returns the k-th smallest, (k >= 0), element of vector within vector
    """
    return _select(vector, 0, len(vector) - 1, k, key)
 
if __name__ == '__main__':
    v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print([select(v, i) for i in range(10)])
