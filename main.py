import sqlite3
import time
items = []


def grabPlayers():
    conn = sqlite3.connect('players.db')
    cursor = conn.execute(
    "SELECT name,salary,value from players ORDER BY RANDOM() limit 20 ")
    for row in cursor:
        id = row[0]
        salary = row[1]
        value = row[2]
        player = [id, salary, value]
        items.append(player)
    #print "Operation done successfully";
    conn.close()


def getPosition(player):
    conn = sqlite3.connect('players.db')
    cursor = conn.execute(
    "SELECT position from players where name=? " , [player])
    position = cursor.fetchone()[0]
    conn.close()
    return position



def validateLineup(lineup):

    slots = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'Def': 1, 'FLEX'   : 1}

    if len(lineup) != 9:
        return False
    for player in lineup:
        position = getPosition(player[0])
        if slots[position] > 0:
            slots[position] -= 1
        elif slots[position] <= 0 and slots['FLEX'] > 0 and position != 'Def' and position != 'QB' :
            slots['FLEX'] -= 1
        else:
            return False
    return True
    print  slots


try:
    xrange
except:
    xrange = range


def totalvalue(comb, maxweight):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= maxweight else (0, 0)


def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j - 1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result

counter = 50000
print "Max salary is %i" % counter
while counter > 0:
    items = []
    grabPlayers()
    bagged = knapsack01_dp(items, counter)
    val, wt = totalvalue(bagged,counter)

    if validateLineup(bagged):
        print "Valid Lineup"
        print("for a total value of %i and a total weight of %i" % (val, -wt))
        print "Lineup:"
        for x in bagged:
            print x
    else:
        pass


