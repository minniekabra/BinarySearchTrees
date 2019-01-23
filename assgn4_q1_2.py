#python2
from __future__ import  print_function

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node():
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def construct_tree(R, l, r):
    if l >= 0:
        R.left = Node(A[l][0])
        construct_tree(R.left, A[l][1], A[l][2])
    else:
        pass

    if r >= 0:
        R.right = Node(A[r][0])
        construct_tree(R.right, A[r][1], A[r][2])
    else:
        pass


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end = ' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end= ' ')

def in_data():
    global A
    n = input()
    A = [[] for _ in range(n)]
    for i in range(0, n):
        S = list(map(int, raw_input().split()))
        A[i] = S

def main():
    global A
    in_data()
    root = Node(A[0][0])
    l = A[0][1]
    r = A[0][2]
    construct_tree(root, l, r)

    inorder(root)
    print()
    preorder(root)
    print()
    postorder(root)

threading.Thread(target=main).start()

