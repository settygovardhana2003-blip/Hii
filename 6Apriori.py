#Apriori Algorithm (Frequent Itemsets and Association Rules)
from itertools import combinations

transactions = [{'milk', 'bread', 'butter'}, {'bread', 'butter'}, {'milk', 'bread'}, {'milk', 'butter'},
                {'bread', 'butter', 'jam'}, {'milk', 'bread', 'butter', 'jam'}, {'bread', 'jam'}, {'milk', 'bread', 'butter'}]
min_support = 0.3
min_confidence = 0.7

#Support = fraction of transactions that contain the itemset
def support(itemset):
    return sum(itemset <= t for t in transactions) / len(transactions)

#Start with single items, keep only the frequent ones, then grow them one item at a time
frequent = {}
current = {frozenset([item]) for t in transactions for item in t}
while current:
    level = {s: support(s) for s in current if support(s) >= min_support}
    frequent.update(level)
    #Join frequent itemsets to make bigger ones (prune if any smaller subset is not frequent)
    joined = {a | b for a in level for b in level if len(a | b) == len(a) + 1}
    current = {c for c in joined if all(frozenset(s) in level for s in combinations(c, len(c) - 1))}

print("Frequent Itemsets:")
for s, sup in sorted(frequent.items(), key = lambda x: (len(x[0]), -x[1], sorted(x[0]))):
    print(f"  {sorted(s)} -> support = {sup:.3f}")

print("\nAssociation Rules:")
for s in frequent:
    for item in (s if len(s) > 1 else []):
        confidence = frequent[s] / frequent[s - {item}]
        if confidence >= min_confidence:
            print(f"  {sorted(s - {item})} -> {item}   (confidence = {confidence:.2f})")