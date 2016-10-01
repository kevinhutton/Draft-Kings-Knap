import sqlite3
items = []
conn = sqlite3.connect('players.db')
cursor = conn.execute("SELECT name,salary,value from players")
for row in cursor:
    id =row[0]
    salary = row[1]
    value = row[2]
    player = (id,salary,value)
    items.append(player)

print "Operation done successfully";
print items[4]
conn.close()



try:
    xrange
except:
    xrange = range

def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 50000 else (0, 0)

#(id,salary,value)
# select id,salary,value from players where id
#items = (
#    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
#    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
#    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
#    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
#    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
#    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
#    ("socks", 4, 50), ("book", 30, 10),
#    )

def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result


bagged = knapsack01_dp(items, 50000)
#print("Bagged the following items\n  " +
#      '\n  '.join(sorted(item for item,_,_ in bagged)))
print bagged
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))