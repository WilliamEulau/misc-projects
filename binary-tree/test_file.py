from main import BST
from main import Node
import random

# This is a test file for the binary search tree file main.py

n = int(input("Enter the amount of nodes to be added: "))
tree = BST()
for i in range(0, n):
    tree.insert(random.randint(1, 500))


print(f"Tree Height: {tree.TreeHeight()}")
print(f"Min Value: {tree.MinVal()}")
print(f"Max Value: {tree.MaxVal()}")
print(f"Sum of all values in the tree is: {tree.TreeSum()}")
print(f"Tree (array): {tree.PrintTreeArray()}")
