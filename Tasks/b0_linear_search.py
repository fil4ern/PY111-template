"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min_index = 0
	for i in range(len(arr)):
		if arr[i] < arr[min_index]:
			min_index = i
	return min_index

if __name__ == '__main__':
	print(min_search([1,2,4,6,7]))