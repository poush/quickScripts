### Running Scripts present here


1. SimplifyDept

Simply run it directly with the Python 3 interpreter or you can import the ```simplifyDebts``` function and provide it the transation in this format  

```
transactions = [
    {   'paidBy': 'A',  'paidFor': { 'B': 100, 'C': 50 } },
    {   'paidBy': 'A',  'paidFor': { 'C': 500 } },
    {   'paidBy': 'B',  'paidFor': { 'A': 150, 'C': 200 } },
    {   'paidBy': 'C',  'paidFor': { 'A': 250, 'B': 200 }   }
]
```
