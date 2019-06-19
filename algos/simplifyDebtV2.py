# Set of transactions
# i,j, A
# i has to pay j the A amount
transactions = [
    [0,1 ,150],
    [0,2 ,250],
    [1,0 ,100],
    [1,2 ,200],
    [2,0 ,550],
    [2,1 ,200]
]

transactions = [
    [4,2 ,40],
    [3,2 ,30],
    [2,2 ,20],
    [6,7 ,320],
    [4,7 ,40],
    [2,7 ,40],
    [8,1 ,100],
    [7,1 ,100],
    [4,1 ,100],
    [1, 4, 200]
]
ts = transactions


# This Algorithm is based on the concept of simplifying
# transitive relations iteratively
# In each iteration it looks for A->B->C relation and simplfies as:
# 1. Is it completely transitive? then make it A->C
# 2. If not, can chain be simplified by reducing the amount of cash flow?
# 3. Cycles are also reduced through the same way for eg: A->B->A is resolved using the same
#    transitive concept, making it A->A and then reducing the edges that starts and
#    end with same node.
# The step 2 breaks the chain as much as possible so that smallest cycle can be found
# and reduced to zero
def simplifyDebt(ts):
    cut = True
    reattempt = 0

    while True:
        cut = False
        # ts = ts2
        for i in range(0, len(ts)):
            if ts[i][0] == ts[i][1]:
                ts = ts[:i] + ts[i+1:]
                # print("eehhaa", ts)
                cut = True
                break


            if i>0:
                if ts[0][0] == ts[i][0] and ts[0][1] == ts[i][1]:
                    ts[0][2] = ts[0][2] + ts[i][2]
                    ts = ts[:i] + ts[i+1:]
                    # print("meow", ts)
                    cut = True
                    break

                if ts[i-1][1] == ts[i][0]:
                    # print(ts, 'sm', i)
                    if ts[i-1][2] >= ts[i][2]:
                        if ts[i-1][2] == ts[i][2]:
                            ts[i-1][1] = ts[i][1]
                            ts = ts[:i] + ts[i+1:]
                        else:
                            ts[i-1][2] = ts[i-1][2] - ts[i][2];
                            ts[i][0] = ts[i-1][0]
                    else:
                        ts[i][2] = ts[i][2] - ts[i-1][2];
                        ts[i-1][1] = ts[i][1]
                    cut = True
                    # print('ms', ts, i)
                    reattempt = 0
                    break

                if ts[0][1] == ts[i][0]:
                    if ts[0][2] >= ts[i][2]:
                        if ts[0][2] == ts[i][2]:
                            # print('yes', i)
                            ts[0][1] = ts[i][1]
                            ts = ts[:i] + ts[i+1:]
                        else:
                            ts[0][2] = ts[0][2] - ts[i][2]
                            ts[i][0] = ts[0][0]
                    else:
                        ts[i][2] = ts[i][2] - ts[0][2]
                        ts[0][1] = ts[i][1]

                    cut = True
                    reattempt = 0
                    # print('sd', ts)
                    break

        
            # print("==>", i, ts)

        if not cut:
            # print("rre", ts)
            ts = [ts[-1]] + ts[0:-1]
            # print("re", ts)
            reattempt += 1

        if len(ts) is 1:
            break

        if cut is True or reattempt <= len(ts) + 1:
            continue
        else:
            # print('called')
            break

    return ts

print(simplifyDebt(ts))
