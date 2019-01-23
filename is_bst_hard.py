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


def in_data():
    global A
    global n
    n = input()
    A = [[] for _ in range(n)]
    for i in range(0, n):
        S = list(map(int, raw_input().split()))
        A[i] = S

def inorder(root):
    global T
    if root:
        inorder(root.left)
        T.append(root.key)
        #print(root.key, end = ' ')
        inorder(root.right)

def check_bst(T):
    n = len(T)
    k = 1
    for i in range(1,n,2):
        if i < n-1:
            if T[i-1] < T[i]:
                pass
            else:
                k = 0
                break
            if T[i+1] > T[i]:
                pass
            else:
                k = 0
                break

        else:
            if T[i]>=T[i-1]:
                pass
            else:
                k = 0
                break

    return k

def main():
    global A
    global n
    in_data()
    if n == 0:
        print('CORRECT')
    else:

        root = Node(A[0][0])
        l = A[0][1]
        r = A[0][2]
        construct_tree(root, l, r)
        global T
        T = []
        inorder(root)
        k = check_bst(T)
        if k == 0:
            print('INCORRECT')
        else:
            print('CORRECT')


threading.Thread(target=main).start()

