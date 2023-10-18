Sets
====

Operations on sets:
- add
- contains
- delete

Easy implementation:

- initialize array
- invent function from elements to natural numbers
f: e -> N
- index array with f(e)

f -- hash function

Example:
last digit of numer (f(x) = x % 10)
137 -> 7, 17 -> 7 -- collision

To store values with equal hashes, use list for each element
of the original array.

Iteration: O(N + K), where N = len(array), K = # of elements
Contains: K / N on average.
Delete:
- find element
- in corresponding list swap found elem. and the last one
- delete last

Implementation of (multi)set

```python
setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    myset[x % setsize].append(x)

def find(x):
    for now in muset[x % setsize]:
        if now == x:
            return True
    return False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
```

Multi because we don't check if element is already there in add

Amortized complexity
--------------------
Nothing new

Problem 1.
----------
Given seq of positive numbers of len N and number X
find 2 different numbers A and B from seq: A + B = X or
return (0, 0) if no such pair exists

```python
def twotermswithsumx(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x = nownum
        prevnums.add(nownum)
    return 0, 0
```

Problem 2.
----------

Given dict of N words with len of each word <= K:

In spelling of each of M words one letter can be missing.
For each word check if it contains in dict, possibly with one missing letter.

Solution in O(NK^2 + M):
For each word in dict remove every possible letter and add back to dict.
Then just check if word in dict.

```python
def wordsindict(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        for delpops in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos + 1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans
```
