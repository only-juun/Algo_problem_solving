# boj 1991. 트리순회

import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    tree = {}
    for _ in range(n):
        root, left, right = sys.stdin.readline().strip().split()
        tree[root] = [left, right]
    return tree

def preorder(root, tree):
    if root == '.':
        return
    print(root, end='')
    preorder(tree[root][0], tree)
    preorder(tree[root][1], tree)

def inorder(root, tree):
    if root == '.':
        return
    inorder(tree[root][0], tree)
    print(root, end='')
    inorder(tree[root][1], tree)

def postorder(root, tree):
    if root == '.':
        return
    postorder(tree[root][0], tree)
    postorder(tree[root][1], tree)
    print(root, end='')

def main():
    tree = read_input()
    root = 'A'
    preorder(root, tree)
    print()
    inorder(root, tree)
    print()
    postorder(root, tree)

if __name__ == '__main__':
    main()
