# Development Log – The Torchbearer

**Student Name:** Luis Alvarez
**Student ID:** 131702893

---

## Entry 1 – [May 5th, 2026]: Initial Plan

The first thing I want to implement is the cost to travel between the nodes.
After that I would want to implement backtracking in order to make sure each possible combination was used.
I think the hardest part would the backtracking with pruning because it will require us to track the state and undoing it's choices correctly
I plan to test it using the cases that are in torchbearer.py
---

## Entry 2 – [May 8th, 2026]: [type error]

I ran into a problem when i tried to run into a program.
I got a type error because I didnt finish the solve() function so it was returning nothing. 
In order to fix it, I need to call the right functions and return their results.

---

## Entry 3 – [May 7th, 2026]: [Backtracking]

I think backtracking was hard because just trying to think of how to get the algorthim to go backwards without having to draw it was hard.
I did learn that backtracking works by undoing your last choice after recursing.
So we remove the relic from visited and add it back to the remaining.
This allowed the algorithm to try every possible order without needing to copy the entire state each time.

---

## Entry 4 – [May 8th, 2026]: Post-Implementation Reflection

I think I would want to try adding more edge cases to test and learn more from it.
I would also want to improve the pruning to cut more brances to see if it makes the search faster for larger inputs.

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |.5hrs |
| Part 2: Precomputation Design | 1hrs|
| Part 3: Algorithm Correctness |1hrs |
| Part 4: Search Design |3hrs |
| Part 5: State and Search Space | 2hrs|
| Part 6: Pruning |3 hrs |
| Part 7: Implementation |2hrs |
| README and DEVLOG writing | 1hrs|
| **Total** | 13.5|
