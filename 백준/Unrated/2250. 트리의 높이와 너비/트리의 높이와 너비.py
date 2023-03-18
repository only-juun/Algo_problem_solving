import sys
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())

def inorder(root, tree, lv):
    if root == -1:
        return
    inorder(tree[root][0], tree, lv + 1)
    arr.append(root)
    level[lv] = level.get(lv, []) + [root]
    inorder(tree[root][1], tree, lv + 1)

tree = {}
in_degree = [0 for _ in range(n + 1)]
for _ in range(n):
    root, left, right = list(map(int, input().split()))
    tree[root] = [left, right]

    if left != -1:
        in_degree[left] += 1
    if right != -1:
        in_degree[right] += 1

root = -1
for i in range(1, n + 1):
    if in_degree[i] == 0:
        root = i
        break

arr = []
level = {}
inorder(root, tree, 1)

ans = []
for lv, v in level.items():
    w = arr.index(v[-1]) - arr.index(v[0]) + 1
    ans.append((lv, w))

ans.sort(key = lambda x: (-x[1], x[0]))
print(ans[0][0], ans[0][1], sep='\n')