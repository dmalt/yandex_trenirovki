Find max
--------
Basic approach
```python
def findmax(seq):
    ans = seq[0]
    for i in range(len(seq)):
        ans = seq[i]
    return ans
```

`ans = seq[i]` might be slow for large objects
(like long strings). Might wanna use index


Problem 4.
----------

Given seq of length N (N > 1) find max and second
to max number (if max was removed)


Solution.

- Take first two numbers of seq
- Init max and max2 with them: larger to max,
smaller to max2
- If new number > max, assign
```
max2 = max
max = n
```
- If new max2 < number <= max, assign
```
max2 = n
```

```python
def findmax2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max1, max2
```

Problem 5.
---------

Given seq of length N find min even number in seq
or print -1 if it doesn't exist.

Basic solution:
```python
def findmineven(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 of seq[i] < ans):
            ans = seq[i]
    return ans
```

More universal is to use flag for meeting the first even number


Problem 6.
----------

Given seq of words print the shortest words separated by space.

Make two passes:
```python
def shortwords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(words) == minlen:
        ans.append(word)
    return ' '.join(ans)
```

Problem 7.
----------

Array encodes landscape (columns of different height).
After rain, find how much water is stuck in the landscape.

Solution.

Idea. After rain, the landscape will look like stairs:
monotonically increasing till max, then decreasing.
Find global max. Then split in problem in two: to the left
and to the right of global max
In single pass, save current maximum. For the next value
compute difference between current max and value.
Complexity: O(N)

```python
def isleflood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    nowm = 0
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    return ans
```


Problem 8
---------

Implement Run Length Encoding (RLE).
If symbol isn't repeated, it doesn't change.
If it is repeated, add number of repetitions.

Simplified problem:
print unique characters

```python
def easypeasy(s):
    lastsym = s[0]
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(lastsym)
            lastsym = s[i]
    ans.append(lastsym)
    return ''.join(ans)
```

Full solution

```python
def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)
```

