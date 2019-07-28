# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:12:54 2019

@author: NABAJYOTI
"""

#create a singly  linked list 
#add nodes
#traverse through them
class Node:
	def __init__(self,data):
		self.data=data;
		self.next= None;

class LinkedList:
	def __init__(self):
		self.head=None

	def insert(self,newNode):
		if self.head is None :
			self.head=newNode;


		else:
			lastNode=self.head;
			while True:
				if lastNode.next is None:
					break;
				lastNode=lastNode.next
			lastNode.next=newNode;
	def printList(self):
		currentNode=self.head
		while True:
			if currentNode is None:
				break;

		print(currentNode.data)
		currentNode=currentNode.next



#Node=> data,next;
firstNode=Node("John")
linkedlist=LinkedList()
linkedlist.insert(firstNode)
secondNode=Node("Ben");
linkedlist.insert(secondNode)
thirdNode=Node("Matthew")
linkedlist.insert(thirdNode)
linkedlist.printList();