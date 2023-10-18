Binary search
=============

- Left binseach: first good value

```python
def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l
```


- Right binsearch: last good value

```python
def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l
```

Problem 1.
Governing school council includes parents, teachers and students.
Num of parents must be >= 1/3 num of all participants. Currently
there are N participants and K parents. Find out how many parents
must be added so their number is >= 1/3 num of participants.


Solution.
Add min num of parents with bin search. Don't forget that new parents add
to num of participants. Don't use division. L=0, R = N (we overshoot on purpose).

```python
def checkendownment(m, params):
    n, k = params
    return (k + m) * 3 >= n + m

ans = lbinsearch(0, N, checkendownment, N, K)
```

Problem 2.
Yura decided to prepare to interview. He chose N problems on leetcode.
On the first day he solved K problems and on each next day he solved
one problem more than on the previous. Find out how many days will it take
for Yura to prepare for interview.

```python
def checkproblemcount(days, params):
    n, k = params
    return (k + (k + days - 1)) * days

ans = lbinsearch(0, N, checkproblemcount, N, K)
```

Problem 3.
Misha reads lectures on algorithms. Behind the screen there's a W * H
centimeters board. Misha wants to place N square stickers with notes so
that side length of the note in cm is int.
Find minimal length of sticker's side so that all the stickers fit on the board.

```python
def checkstickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n

ans = rbinsearch(l, r, checkstickers, N, W, H)
```

Problem 4.
Given nondecreasing seq of len N and number x find index of the\
first occurence of the number in seq that is >= X.
If no such number exists, return N.


```python
def checkisge(index, params):
    seq, x = params
    return seeq[index] >= x

def findfirstge(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans
```

Problem 5.
Given nondecreasing seq of len N and num X, find number of occurence
of number X in seq.


Solution
- find first >= X with lbinsearch
- find first > X with lbinsearch
- Indices difference -> ans

```python
def checkisgt(index, params):
    seq, x = params
    return seeq[index] > x

def checkisge(index, params):
    seq, x = paramsreturn seq[index] >= x

def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    return indexgt - indexge
```


Problem 6.
Given interest rate on a credit (X% per year), credit period
(N months) and credit amount (M rubles) compute the amount of
annuity payment.

- Monthly percent doesn't equal X / 12. Find it with binsearch.


```python
def checkmonthlyperc(mperc, yperc):
    msum = 1 + mperc / 100
    ysym = 1 + yperc / 100
    return msum ** 12 >= ysym

# float bin search
def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

x = 12
eps = 0.0001
mperc = fbinsearch(0, x, eps, checkmonthlyperc, x)
```

Search payment amount with binsearch, as a check model process of monthly
payment, decreasing the body of credit by the difference between the amount
of payment and monthly percent.

```python
def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

eps = 0.01
m = 100000000
n = 300
monthlypay = fbinsearch(0, m, eps, checkcredit, (n, m, mperc))
```

Ternary search (which there's none)
-----------------------------------

Problem 7.
Bicyclists participating in a race at a certain point in time
which is called initial, appeared at x1, x2, ..., xn meters from the
start (n is the total number of bicyclists, < 100 000). Each
bicyclist moves with a constant speed v1, v2, ..., vn m / s.
All bicyclists move in the same direction. News reporter wants to
find a moment at which the distance between the leader and the last
bicyclist becomes minimal to make a picture with all the participants from
a helicopter. Find this moment.

Solution
- Define function dist(t), which in O(N) determines
distance between leader and the last bicyclist at instant t.
- If dist(t + eps) > dist(t), the funciton is increasing and
the left bound must be moved; otherwise -- the right


```python
def dist(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0] * t
    for i in range(1, len(x)):
        nowpos = x[i]+ v[i] * t
        minpos = min(minpos, nowpos)
        maxpos = max(maxpos, nowpos)
    val = maxpos - minpos
    return val

def checkasc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)

ans = fbinsearch(...)
```
