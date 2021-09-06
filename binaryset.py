class Set:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self,element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx] == element

    def remove(self, element):
        assert element in self, "the element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def __iter__(self):
        return _SetIterator(self._theElements)

    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while low <= high:
            mid = (high + low) /2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid -1
            else:
                low = mid + 1
