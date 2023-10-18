Prefix sums and two pointers
============================


Prefix sums
-----------

- Suppose we have array nums (N numbers) and we want to
know "What's the sum of elements in half-interval [L,R)"
- Precompute array prefixsum (N + 1 numbers), where prefixsum[k]
stores sum of all numbers from nums indexed from 0 to k-1
- Can be computed in O(N): prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
- Don't forget the sizes are different
- Overflows!

- O(1) request answer: prefixsum[R] - prefixsum[L]
- Find sum(2, 5) = prefixsum[5] - prefixsum[2] = 21 - 8 = 13

RSQ implementation (prefix sums)
```python
def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum

def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]
```


Problem 1.
Given seq of len N and M requests implement queries:
"How many numbers on half-interval [L, R)"

Solution O(N + M)

For each prefix count num of zeros (prefixzeroes). Then the answer on
[L, R) = prefixzeroes[R] - prefixzeroes[L]


Problem 2.
Given seq of len N find number of intervals with zero-sum.

Solution.
Precompute prefix sums. Equal prefix sums mean that sum on
interval with start and end in position on which equal prefix sums
are achieved equals zero

```python
def contprefixsums(nums):
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def countzerosumranges(prefixsumbyvalue):
    cntranges = 0
    if nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges
```

Two pointers
------------

Problem 3.
Given sorted seq of numbers of len N and number K,
find number of pairs A, B s.t. B - A > K.


Solution.
Take smalles number and find first acceptable larger.
All bigger numbers are guaranteed to fit. Take next smaller,
pointer of the first fit larger we'll move starting from it's
current position

```python
def cntpairswithdiffgtk(sortednums, k):
    cntpairs = 0
    last = 0
    for first in range(len(sortednums)):
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1
        cntpairs += len(sortednums) - last
    return cntpairs
```

Problem 4.
Football player has one quantifier: professionalizm.
Team is called close-knit, if professionalizm of each player
is less or equal to the sum professionalizms of any two
other players. Team can have any number of players.
Given a sorted seq of nums of len N -- players' professionalizms,
find max aggregated professionalizm of a close-knit team.


Solution.

- Two pointers?
- Sort professionalizms


```python
def bestteamsum(players):
    bestsum = 0
    nowsum = 0
    last = 0
    for first in range(len(players)):
        while (last < len(players) and
        (last == first or players[first]
        + players[first + 1] >= players[last])):
            nowsum  += players[last]
            last += 1
        bestsum = max(bestsum, nowsum)
        nowsum -= players[first]
    return bestsum
```


Problem 5.
Implement merge.

Solution.
Place two pointers at the start of each seq.
Choose that which points to the smaller number, write this
number to the result and shift pointer.


```python
def merge(nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    inf = max(nums1[-1], nums2[-1]) + 1
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) - 2):
        if nums1[first1] <= nums2[first2]:
            merged[k] = nums[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    nums1.pop()  # remove inf
    nums2.pop()
    return merged
```

Problems with this solution:
- Poor readability (?)
- What if sequences are immutable
