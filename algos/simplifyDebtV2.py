transactions = [
    [0,1 ,150],
    [0,2 ,250],
    [1,0 ,100],
    [1,2 ,200],
    [2,0 ,550],
    [2,1 ,200],
]
ts = transactions



cut = True
reattempt = 0
while True:
    cut = False
    # ts = ts2
    for i in range(0, len(ts)):
        # print(i, ts[i])
        if ts[i][0] == ts[i][1]:
            ts = ts[:i] + ts[i+1:]
            cut = True
            break


        if i>0:
            if ts[0][0] == ts[i][0] and ts[0][1] == ts[i][1]:
                ts[0][2] = ts[0][2] + ts[i][2]
                ts = ts[:i] + ts[i+1:]
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


            ts = [ts[-1]] + ts[0:-1]
            # print("re", ts)
            reattempt += 1
    if len(ts) is 1:
        break

    if cut is True or reattempt <= len(ts) +1:
        continue
    else:
        # print('called')
        break

print(ts)
