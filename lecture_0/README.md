# Search

**Agent:**
entity that perceives its environment and acts upon that environment

**State:**
a configuration of the agent and its environment

**actions:**
choice that can be made in a state
ACTIONS(s) returns the set of actions that can be executed in state *s*.

**transition model:**
a description of what state returns from performing any applicable action in any state.
RESULT(*s*,*a*) returns the state resulting from performing  action *a* in state *s*. 

**state space:**
the set of all states reachable from the initial state by any sequence of actions

**goal test:**
way to determine whether a given state is a goal state.

**path cost:**
numerical cost  associated with a given path 

**search problem:**

+ initial state
+ actions
+ test
+ goal test
+ path cost function

**solution:**
a sequence of actions that leads from the initial state to a goal state.

**optimal solution:**
a solution that has the lowest path cost among all solutions.

**node:**
a data structure that keeps track of
- a state
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

**approach:**
+ Start with a frontier that contains the initial state.
+ Repeat:
  - If the frontier is empty, then no solution.
  - Remove a node from the frontier.
  - If node contains goal state, return the solution.
  - Expand node, add resulting nodes to the frontier. 

**revised approach:**
+ Start with a frontier that contains the initial state.
+ Start with an empty explored set.
+ Repeat:
  - If the frontier is empty, then no solution.
  - Remove a node from the frontier.
  - If node contains goal state, return the solution.
  - Add the node to the explored set.
  - Expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set. 

**stack:**
last-in first-out data type `(LIFO)`

**depth-first search:**
search algorithm that always expands the deepest node in the frontier.

**breadth-first search:**
search algorithm that always expands the shallowest node in the frontier.

**queue:**
first-in first-out data type `(FIFO)`.

**uniformed search:**
search strategy that uses no problem-specific knowledge

**informed search:**
search strategy that uses problem-specific knowledge to find solutions more efficiently

**greedy best-first search:**
search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)

**A* search:**
search algorithm that expands node with lowest value of g(n) + h(n)


g(n): cost from start to n
h(n): estimate of cost from n

optimal if
- h(n) is admissible (never overestimates the true cost), and
- h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)

**minmax:**
* MAX(X) aims to maximize score.
* MIN(O) aims to minimize score.
 
* Given a state s:
  - MAX picks action *a* in ACTIONS(*s*) that produces highest value of MIN-VALUE(RESULT(*s*, *a*))