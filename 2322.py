npecas = int(input())
pecasTot = [i+1 for i in range(npecas)]
pecas = list(map(int, input().split()))
r = [i for i in pecasTot if i not in pecas]
print(r[0])

