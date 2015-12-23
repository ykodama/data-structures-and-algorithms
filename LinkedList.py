# coding: utf-8
class Node(object):
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class LinkList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def addNode(self, value):
		node = Node(value)
		if not self.head:
			self.head = node
		if self.tail:
			self.tail.next = node
		self.tail = node
		self.length += 1

	def printList(self):
		node = self.head
		while node:
			print(node.value)
			node = node.next

	def deleteNode(self, index):
		prev = None
		node = self.head
		i = 0
		while node and i < index:
			prev = node
			node = node.next
			i += 1
		if i == index:
			if not prev:
				self.head = node.next
			else:
				prev.next = node.next
			self.length -= 1
		else:
			print('Index not found')
