# coding: utf-8
class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		return self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)
