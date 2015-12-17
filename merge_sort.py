# coding: utf-8
def merge_sort(seq):
	if len(seq) <= 1:
		return seq

	mid = len(seq) / 2
	left = seq[:mid]
	right = seq[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	sorted_list = []
	li = 0
	ri = 0

	while li < len(left) and ri < len(right):
		if left[li] <= right[ri]:
			sorted_list.append(left[li])
			li += 1
		else:
			sorted_list.append(right[ri])
			ri += 1

	if left:
		sorted_list.extend(left[li:])
	if right:
		sorted_list.extend(right[ri:])

	return sorted_list