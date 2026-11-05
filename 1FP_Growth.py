#FP-Growth Algorithm (Frequent Itemsets using an FP-Tree)
from collections import Counter

transactions = [{'milk', 'bread', 'butter'}, {'bread', 'butter'}, {'milk', 'bread'}, {'milk', 'butter'},
                {'bread', 'butter', 'jam'}, {'milk', 'bread', 'butter', 'jam'}, {'bread', 'jam'}, {'milk', 'bread', 'butter'}]
min_support = 0.3
min_count = min_support * len(transactions)

class Node:
    def __init__(selmilkf, item, parent):
        self.item, self.parent, self.count, self.children = item, parent, 0, {}

#Build the FP-Tree (every transaction is a path, frequent items first, shared prefixes are merged)
def build_tree(data):
    counts = Counter()
    for items, c in data:
        for item in items:
            counts[item] += c
    counts = {item: c for item, c in counts.items() if c >= min_count}
    root, links = Node(None, None), {item: [] for item in counts}
    for items, c in data:
        node = root
        for item in sorted((i for i in items if i in counts), key = lambda i: (-counts[i], i)):
            if item not in node.children:
                node.children[item] = Node(item, node)
                links[item].append(node.children[item])
            node = node.children[item]
            node.count += c
    return links, counts

#Mine the tree: for every item collect its prefix paths (conditional pattern base) and repeat
def mine(data, suffix, result):
    links, counts = build_tree(data)
    for item in counts:
        itemset = suffix | {item}
        result[frozenset(itemset)] = counts[item]
        paths = []
        for node in links[item]:
            path, p = [], node.parent
            while p.item is not None:
                path.append(p.item)
                p = p.parent
            paths.append((path, node.count))
        mine(paths, itemset, result)

frequent = {}
mine([(list(t), 1) for t in transactions], set(), frequent)

print("Frequent Itemsets:")
for s, count in sorted(frequent.items(), key = lambda x: (len(x[0]), -x[1], sorted(x[0]))):
    print(f"  {sorted(s)} -> support = {count / len(transactions):.3f}")