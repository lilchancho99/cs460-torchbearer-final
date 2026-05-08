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


_So if the distances are wrong and it picks a route that costs less than it actually does, then the route planner will make more incorrect decisions based on the cost it had picked making it never picking the optimal path._

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



| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location |current_loc |node (string) | where the torchbearer is at |
| Relics already collected |relics_visited_order |list |relics collected in order visited |
| Fuel cost so far |cost_so_far |float |total fuel spent |

### Part 5b: Data Structure for Visited Relics



| Property | Your answer |
|---|---|
| Data structure chosen |set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | because we can use hashing to figure out where they are using the memory address they were assign to.|

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** _k!._
- **Why:** _there are k relics and each can be visited in any order which gives us k * (k-1) * (k-2) * ... * 1 = k!_

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** _the minimum cost is what is being tracked and same with the order of relics._
- **When it is used:** _It is checked at each recursive call right before checking a new branch._
- **What it allows the algorithm to skip:** _it skips any branch that cost more or equal to the known cost._

### Part 6b: Lower Bound Estimation



- **What information is available at the current state:** _we know the current location, cost so far, relics left, and the cost between all locations._
- **What the lower bound accounts for:** _the cheapest possible cost to reach exit T._
- **Why it never overestimates:** _it doesn't over estimate because we precomputed the shortest path distances so the actual travel cost can only be equal to or greater than the minimums._

### Part 6c: Pruning Correctness



- _The reason why we prune is because when a branch is the same or cost more than the best so far branch is so that we can keep the least cost branch.._

---

## References



lectures
geeks for geeks
