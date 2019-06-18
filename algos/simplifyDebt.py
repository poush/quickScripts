transactions = [
    {   'paidBy': 'A',  'paidFor': { 'B': 100, 'C': 50 } },
    {   'paidBy': 'A',  'paidFor': { 'C': 500 } },
    {   'paidBy': 'B',  'paidFor': { 'A': 150, 'C': 200 } },
    {   'paidBy': 'C',  'paidFor': { 'A': 250, 'B': 200 }   }
]

transactions1 = [
    {   'paidBy': 'A',  'paidFor': { 'C': 300, 'E': 35, 'F': 35 } },
    {   'paidBy': 'B',  'paidFor': { 'D': 40, 'G': 10 } }
]

transactions2 = [
    {   'paidBy': 'A',  'paidFor': { 'C': 300, 'E': 40, 'F': 30 } },
    {   'paidBy': 'B',  'paidFor': { 'D': 50 } }
]


def simplifyDept(transactions):
    subgraphs = []
    curr = -1
    transactions = sorted(transactions, key=lambda k: k['paidBy'])
    for transaction in transactions:
        if len(subgraphs) < 1 or transaction.get('paidBy') not in subgraphs[curr]:
            curr+=1
            subgraphs.append({})
        
        paidBy = transaction.get('paidBy')

        if paidBy not in subgraphs[curr]:
            subgraphs[curr][paidBy] = 0

        transfers = transaction.get('paidFor')
        for person in transfers:
            if person not in subgraphs[curr]:
                subgraphs[curr][person] = transfers[person]
            else:
                subgraphs[curr][person] += transfers[person]

            # removing from the debt of person who paid
            subgraphs[curr][paidBy] -= transfers[person]


    for people_dept in subgraphs:
        people_dept = sorted(people_dept.items(), key=lambda k: k[1])

        while True:
            # print(people_dept)
            # Now calculating who will pay to whom
            total = len(people_dept)
            debit = people_dept[total-1]
            credit = people_dept[0]
            # ccheck = findSame(people_dept, debit[1])
            # credit = people_dept[ccheck] if ccheck is not -1 else credit
            # c = ccheck if ccheck is not -1 else 0


            if credit[1] == 0 and debit[1]  == 0:
                # sorted, there is nothing to do now
                # Rupya Pohonch gaya
                break

            m = min([-credit[1], debit[1]])
            # settling the transaction
            people_dept[0] = (credit[0], credit[1] + m)
            people_dept[total-1] = (debit[0], debit[1] - m)
            # break
            
            print("Person " + debit[0] + " will pay " + str(m) + " to "+ credit[0])
            people_dept = sorted(people_dept, key=lambda k: k[1])


simplifyDept(transactions2)
