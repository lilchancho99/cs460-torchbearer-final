"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    
    return  """
    1. So we need the shortest path distances from S to each relic and not just S alone.
    2. to decide which route to pick since the algorthm doesn't tell you which is the cheapest
    3. There are k! possible orderings of relics so no single computation will be able to determine which ordering is cheapest
    """
   


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    
    """
    nodes = {spawn}
    nodes.update(relics)
    return list(nodes) 
    


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    
    """
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    heap = [(0, source)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return distance
    


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    
    """
    distance_table = {}
    start_nodes = select_sources(spawn, relics, exit_node)
    for node in start_nodes:
        distance_table[node] = run_dijkstra(graph, node)
    return distance_table
    
    


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    
    """
    return """
    3a. The distanced that was found is stored as the shortest path possible.
        the distance found so far can still be improved
    3b. Because the algorithm hasn't looked at any nodes so it cant say it made a mistake.
        because if we keep adding more nodes to the path, then it will cost more unless the new path adds 0.
        so once the algorithm ends, all distances will be as small as they can be since there is no possible way to improve it.
    3c. So if the distances are wrong and it picks a route that costs less than it actually does, then the route planner will make more incorrect decisions based on the cost it had picked making it never picking the optimal path.
    
    """


    


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

  
    """
    return """

    1. failure mode: Greedy will only look at the next cheapest relic without considering how the other choices will affect the remaining cost.
    2. Counter-example setup: an example would be s to A cost 10 and A to B is 100 and A to T is 2 and B to A cost 1 and B to T costs 1 since A and B are relics.
    3. What greedy picks: Greedy will pick A since it cost the cheapest in the example.
    4. What optimal picks: The optimal would pick B first then A then T since it is the shortest path.
    5. Why greedy loses: Greedy's route would pick the cheapest path and not consider any other options.
    
    What the Algorithm Must Explore:
    1. The algorithm must visit every possible order when visiting relics to guarantee finding the minimum cost route.
"""


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    best = [float('inf'), []]
    relics_remaining = set(relics)
    _explore(dist_table, spawn, relics_remaining, [], 0, exit_node, best)
    return best[0], best[1]
    


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if not relics_remaining:
        cost_to_exit = dist_table[current_loc][exit_node]
        total_cost = cost_so_far + cost_to_exit
        
        # pruning condition: 
        # we only prune when the cost is equal or cost more than the best cost the algorithm found so far.
        if total_cost < best[0]:
            best[0] = total_cost
        
            best[1] = relics_visited_order.copy()
        return
    
    if cost_so_far >= best[0]:
        return
    for relic in relics_remaining:
        travel_cost = dist_table[current_loc][relic]
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)
        
        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + travel_cost, exit_node, best)
        
        relics_remaining.add(relic)
        relics_visited_order.pop()
    
    


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)
    


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
