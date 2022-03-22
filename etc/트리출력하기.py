# CT실습 - 트리출력하기
# 0322
def print_tree(nodes, depth):
    node = nodes[0]
    if depth == 0:
        print('[{}]--'.format(node), end='')
    childs = []
    for child in nodes:
        if child == node:
            continue
        childs.append(child)

    if childs:
        print('+--[{}]'.format(node), end='')
        print_tree(child, depth+1)

    else:
        print('----[{}]'.format(child))
        for _ in range(depth):
            print('       ', end='')



tree = [['030', '054', '002', '045'],['054', '001', '005'],['002'],['045', '123']]

N= len(tree)
root = tree[0][0]
nodes=[]

for n in tree[0]:
    if n == root:
        continue
    nodes.append(n)

depth = 0
print_tree(tree[1], 0)
# print('[{}]--' .format(root), end='')
# for node in nodes:
#     print('+--[{}]' .format(node), end='')
#     for i in range(N):
#         if tree[i][0] == node:
#             for child in tree[i]:
#                 if child == node:
#                     continue
#                 print('----[{}]' .format(child), end='')
#             print('')
#             print('       ', end='')


