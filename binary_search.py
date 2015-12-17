def binary_search(aList, val):
	left = 0
	right = len(aList) - 1
	while left <= right:
		mid = (left + right) // 2
		if aList[mid] == val:
			return True
		elif val > aList[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return False
