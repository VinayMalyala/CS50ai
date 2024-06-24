# Learning

**Supervised learning**
given a dataset of input-output pairs, learn a function to map inputs  to outputs

**classification**
supervised learning task of learning a function mapping an input point to a discrete category

**nearest-neighbor classification**
algorithm that, given an input, chooses the class of the nearest data point to that input

**k-nearest-neighbor classification**
algorithm that, given an input, chooses the most common class out of the k nearest data points to that input.

**Weight Vector w: (w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>)**

h(x<sub>1</sub>, x<sub>2</sub>) = 1 if w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> >= 0
                                  0 otherwise

Weight Vector w: (w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>)
Input Vector x: (1, x<sub>1</sub>, x<sub>2</sub>)
   w . x: w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>

h<sub>w</sub>(x) = 1 if w . x >= 0
                   0 otherwise

**perceptron learning rule**
Given data point (x, y), update each weight according to:
    w<sub>i</sub> = w<sub>i</sub> + α(y-h<sub>w</sub>(x)) × x<sub>i</sub>
    w<sub>i</sub> = w<sub>i</sub> + α(actual value - estimate) × x<sub>i</sub>

**maximum margin separator**
boundary that maximizes the distance between any of the data points

**regression**
supervised learning task of learning a function mapping an input point to a continuous value

**loss function**
function that expresses how poorly our hypothesis performs

**0-1 loss function**
L(actual, predicted) = 0 if actual = predicted,
                       1 otherwise

**L1 loss function**                       
L(actual, predicted) = |actual - predicted|

**L2 loss function**
L(actual, predicted) = (actual - predicted)<sup>2</sup>

**over fitting**
a model that fits too closely to a particular data set and therefore may fail to generalize to further data

**regularization**
penalizing hypothesis that are more complex to favor simpler, more general hypothesis
     
     cost(h) = loss(h) +  λcomplexity(h)

**holdout cross-validation**     
splitting data into a training set and a test set, such that learning happens on the training set and is evaluated on the test set

**k-fold cross-validation**
splitting data into k sets, and experimenting k times, using each set as a test set once, and using remaining data as training set

**Markov Decision Process**
model for decision-making, representing states, actions, and their rewards
    - Set of states S
    - Set of actions ACTIONS(s)
    - Transition model P(s'|s, a)

**Q-learning**    
method for learning a function Q(s, a), estimate of the value of performing action a in state s
    - Start with Q(s, a) = 0 for all s, a
    - When we taken an action and receive a reward:
        - Estimate the value of Q(s, a) based on current reward an expected future rewards
        - Update Q(s, a) to take into account old estimate as well as our new estimate

    - Every time we take an action a in state s and observe a reward r, we update:
        - Q(s, a) ← Q(s, a) + α(new value estimate - old value estimate)

**Greedy Decision-Making**
- When in state s, choose action a with highest Q(s, a)

**ε-greedy**
- Set ε equal to how often we want to move randomly.
- With probability 1-ε, choose estimated best move.
- With probability ε, choose a random move.

**function approximation**
approximating Q(s, a), often by a function combining various features, rather than storing one value for state-action pair

**unsupervised learning**
given input data without any additional feedback, learn patterns

**clustering**
organizing a set of objects into groups in such a way that similar objects tend to be in the same group

**k-means clustering**
algorithm for clustering data based on repeatedly assigning points to clusters and updating those cluster' centers