# The Torchbearer

**Student Name:** Luis Alvarez
**Student ID:** 131702893
**Course:** CS 460 – Algorithms | Spring 2026



---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  So we need the shortest path distances from S to each relic and not just S alone.

- **What decision remains after all inter-location costs are known:**
  to decide which route to pick since the algorthm doesn't tell you which is the cheapest

- **Why this requires a search over orders (one sentence):**
 There are k! possible orderings of relics so no single computation will be able to determine which ordering is cheapest

---

## Part 2: Precomputation Design

### Part 2a: Source Selection



| Source Node Type | Why it is a source |
|---|---|
| _spawn S_ | _we need distances from S to find the cheapest path to the next relic we need to visit_ |
| _relic nodes_ | _we need distances from it to reach the next relic or exit_ |

### Part 2b: Distance Storage


| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | each node in the graph |
| What the values represent | minimum cost from source to that node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | it uses hashing to map keys to memory locations |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** _there is a relic + 1 spawn which in the total run it's k+1_
- **Cost per run:** _shortest path cost O(m log n)_
- **Total complexity:** _(k+1) x O(m log n) = O((k+1)m log n)_
- **Justification (one line):** _we need to run dijkstra once from spawn and once from each of the relics and then run costs O(m log n) which gives us a O(k m log n)_

---

## Part 3: Algorithm Correctness




### Part 3a: What the Invariant Means



- **For nodes already finalized (in S):**
  _The distanced that was found is stored as the shortest path possible._

- **For nodes not yet finalized (not in S):**
  _the distance found so far can still be improved._

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  _Because the algorithm hasn't looked at any nodes so it cant say it made a mistake._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _because if we keep adding more nodes to the path, then it will cost more unless the new path adds 0._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _so once the algorithm ends, all distances will be as small as they can be since there is no possible way to improve it._

### Part 3c: Why This Matters for the Route Planner


_So if the distances are wrong and it picks a route that costs less than it actually does, then the route planner will make more incorrect decisions based on the cost it haad picked making it never picking the optimal path._

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** _Greedy will only look at the next cheapest relic without considering how the other choices will affect the remaining cost._
- **Counter-example setup:** _an example would be s to A cost 10 and A to B is 100 and A to T is 2 and B to A cost 1 and B to T costs 1 since A and B are relics._
- **What greedy picks:** _Greedy will pick A since it cost the cheapest in the example_
- **What optimal picks:** _The optimal would pick B first then A then T since it is the shortest path_
- **Why greedy loses:** _Greedy's route would pick the cheapest path and not consider any other options_

### What the Algorithm Must Explore

- _The algorithm must visit every possible order when visiting relics to guarantee finding the minimum cost route._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
