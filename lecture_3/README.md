# Optimization

**Optimization**
choosing the best option from the set of options

**local search**
search algorithms that maintain a single node and searches by moving to a neighboring node

**Hill climbing variants**
    - steepest-ascent   ->  choose the highest-valued neighbor
    - stochastic        ->  choose randomly from higher-valued neighbors
    - first-choice      ->  choose the first higher-valued neighbor
    - random-restart    ->  conduct hill climbing multiple times
    - local beam search ->  choose the k highest-valued neighbors

**Linear Programming**
    - Minimize a cost function c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + ... + c<sub>n</sub>x<sub>n</sub>
    - With constraints of form a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> <= b 
        or of form a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... a<sub>n</sub>x<sub>n</sub> = b
    - With bounds for each variable l<sub>i</sub> <= x<sub>i</sub> <= u<sub>i</sub>  

**node consistency**
when all the values in a variable's domain satisfy the variable's unary constraints

**arc consistency**
when all the values in a variable's domain satisfy the variable's binary constraints

to make X arc-consistent with respect to Y, remove elements from X's domain until every choice for X has a possible choice for Y

**CSPs are Search Problems**
  - initial state: empty assignment (no variables)
  - actions: add a {variable=value} to assignment
  - transition model: shows how adding an assignment changes the assignment
  - goal test: check if all variables assigned and constraints all satisfied
  - path cost function: all paths have same cost

**maintaining arc-consistency**
algorithm for enforcing aec-consistency every time we make a new assignment

**DOMAIN-VALUES**
 - least-constraining values heuristic: return variables in order by number of choices that are ruled out for neighboring variables
    - try least-constraining values first