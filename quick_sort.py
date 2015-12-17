# coding: utf-8
def quick_sort(buff, low, high):
	pivot = buff[(low + high)/2]
	i = low
	j = high
	while True:
		while pivot > buff[i]:
			i += 1
		while pivot < buff[j]:
			j -= 1
		if i >= j:
			break
		tmp = buff[i]
		buff[i] = buff[j]
		buff[j] = tmp
		i += 1
		j -= 1
	if low < i - 1:
		quick_sort(buff, low, i - 1)
	if high > j + 1:
		quick_sort(buff, j + 1, high)

	return buff