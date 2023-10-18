Dictionaries and conting sort
=============================

Counting sort
-------------

- Sort N numbers, each from 0 to K
- Comparison sort takes O(NlogN)
- Let's count number of occurences of each number
and then print each number as many times as it occured.
This takes O(N + K) time and O(K) memory
- We can shift values interval so it's not from 0 to K but from
min to max in array.


```python
def countsort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval + 1)
    count = [0] * k
    for now in seq:
        count[now - minval] += 1
    nowppos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
```


Problem 1.
Given to numberx X, Y without leading zeroz check if one
can be transformed to another via digits transposition.

Solution
```python
def isdigitpermutation(x, y):
    def countdigits(num):
        digitcoount = [0] * 10
        while num > 0:
            lastdigit = num %  10
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True
```


Dictionaries
------------

- Complexity constant is much bigger than for arrays,
so it's better to use count sort where possible
- Count sort is bad when the data are sparce

Problem 2.
N x N chess board has M rooks. Determine how many rook pairs attack each other.
Rooks are given by a pair of numbers I, J, which determine the square coordinates.
1 <= N <= 10^9, 0 <= M <= 2 * 10^5

** Remark. **
In C++ typical number of operations\sec = 10^9. In python it's two orders of magnitude
smaller ~ tens of millions.

So this problem can't be solved in O(N). Nor it can't be solved
in O(M^2)

Solution.

- Store num of rooks on each row and column
- Number of pairs in a row (column) = # rooks - 1.
- Sum this # for each row and column


```python
def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)
```
Complexity: O(M)

Using counter (my implementation)

Requires >= 3.10
```python
from collections import Counter
from itertools import repeat

def countbeatingrooks(rookcoords):
    rooksinrow = Counter()
    rooksincol = Counter()
    for row, col in rookcoords:
        rooksinrow[row] += 1
        rooksincol[col] += 1
    rooksinrow.subtract(repeat(-1, len(rooksinrow)))
    rooksincol.subtract(repeat(-1, len(rooksincol)))
    # Careful! total() requires python >= 3.10
    return rooksinrow.total() + rooksincol.total()
```

Problem 3.
Given string S output histogram

```python
def printchart(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduinqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ' end='')
        print()
    print(''.join(sorteduinqsyms))
```

Complexity: O(N^2) due to output

Gap for optimization
--------------------

Is asymptotic solution always better?
- 2 * NlogN or 1000*N?
- logN or 500?
- For N > 2^500 O(N) is better. But 2^500 is bigger than the number of
atoms in the visible universe.

Some other algorithm quality criteria:
- Memory complexity
- Implementation time
- Maintainence cost
- Parallelizable?
- Required programmer's skill
- Hardware cost


Problem 4.
Group words by common letters:
Sample input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample output: [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

Solution

```python
def groupwords(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
        return ans
```

Healty suspicion:
What if the words are long? Maybe better to count sort?

Let's factor out sorting which might need optimization in the future.

```python
def groupwords(words):
    def keybyword(word):
        sortedword = ''.join(sorted(word))

    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
        return ans
```
