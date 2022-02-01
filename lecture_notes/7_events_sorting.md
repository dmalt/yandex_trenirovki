Events sorting
==============

 Problem 1.
 N people visited a website. For each person we know Ini and Outi:
 time of entrance and time of leaving. Assume the person was on site
 from Ini to Outi including ends.

 Determine how many people were on site simoultaneously at maximum.

 Solution.
 Create 2 events per person: entrance and exit.
 Each event is a pair (time, type).
 Entrance should occur before exit for parallel events.

`
      1
 -----|
      | ------------
      2
`


```python
def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((itn[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)
    return maxonline
```

Note.
Event types -1, 1 guarantee that in appears before out after sorting.


Problem 2.

Same setting as for problem 1. Determine how much time there's at
least one person on website.

Solution.
Keep track of the counter. If we get the new event with nonzero counter,
add difference between current and previous event times.

```python
def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((itn[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    notemptytime = 0
    for i in range(len(events)):
        if online > 0:
            notemptytime += events[i][0] - events[i - 1][0]
        if events[i][1] == 01:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)
    return notemptytime
```

Problem 3.
Same setting but also there's Boss who entered site M times and
observed how many people are online. Boss's visits are in increasing order by time.
Determine which online counter values did the Boss observe.

Solution.
Create 3-d event type: "boss entered" and when it occurs save
current counter value. Boss event will occur after entrance and before
exit.

```python
def bosscounter(n, tin, tout, m, tboss):
    events = []
    for in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    for i in range(m):
        events.append((tboss[i], 0))
    events.sort()
    online = 0
    bossans = []
    for i in range(len(events)):
        if events[i][1] == -1
            online += 1
        elif events[i][1] == 1
            online -= 1
        else:
            bossans.append(online)
    return bossans
```

Complexity: O((N + M)log(N + M)) (due to sort)


Events on a circle
------------------

Example:
- Events occuring daily
- Circle is a day
- Idea: cut intervals, intersecting midnight, in two
    Trick is to handle seam points at midnight
- Another idea: two passes
    Ignore unmatching closing events on the first pass; start the
    second pass with the state (unclosed events) from the first pass


Note.
N intervals on a circle may intersect N times


Problem 4.
There are N spots on a parking in a trading center (numbered from 1 to N).
On a single day M cars arrived, some of which were long and took
several adjacent spots. For each car arrival and departure time are known
together with two numbers: its starting and ending parking spots.
If at a certain point a car leaves a parking spot, the spot is considered
free and from that time on it can be occupied by another car.
Determine if there was a moment when all the parking spots were
occupied.


Solution.
Events: arrival and departure. Maintain a counter of occupied spots.
If at any time counter == N, all the spots were occupied.


```python
def is parkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True
    return False
```


Problem 5.
Same setting as for problem 4.
Determine if there was a moment when all the spots were occupied
and determine the minimal number of cars which took all the spots.
If there was no such moment, return M + 1.


Solution.
Add one more counter: number of cars.

```python
def is parkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    nowcars = 0                      # <--------- change
    mincars = len(cars) + 1          # <---------
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1             # <---------
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1             # <---------
        if occupied == n:
            mincars = min(mincars, nowcars)
    return mincars
```


Problem 6.
Same setting.
Determine moment, min number of cars and also
numbers of these cars (as they are mentioned in the list).
If the parking was never fully occupied, return empty list.


Solution.
Add car number to event. When updatng minimum, copy current
state to the answer

```python
def is parkingfull(cars, n):
    events = []
    for i in range(cars):  # <----
        timein, timeout, placefrom, placeto = cars[i]  # <---
        events.append((timein, 1, placeto - placefrom + 1, i))  # <---
        events.append((timeout, -1, placeto - placefrom + 1, i))  # <---
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    carnums = set()  # <-----
    bescarnums = set()  # <-------
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])  # <-----
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])  # <-----
        if occupied == n and nowcars < mincars:  # <----
            bestcarnums = carnums.copy()  # <----
            mincars = nowcars
    return bestcarnums  # <----
```

This solution can be broken (if bestcarnums updates too often).

Efficient solution.

- On the first pass count mincars
- On the second pass don't copy state; when all spots are occupied
and the number of cars == min, return current state.

```python
def is parkingfull(cars, n):
    events = []
    for i in range(cars):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom + 1, i))
        events.append((timeout, -1, placeto - placefrom + 1, i))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1

    # count mincars
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars

    carnums = set()
    nowcars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars == mincars:
            return carnums
    return set()
```



