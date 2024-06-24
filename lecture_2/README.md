# Uncertainty

**Unconditional Probability**
degree of belief in a proposition in absence of any other evidence

**Conditional Probability**
degree of belief in a proposition given some evidence that has already been revealed
    P(a|b)

    P(a|b) = P(a ∧ b)/P(b)

    P(a ∧ b) = P(b)P(a|b)
    P(a ∧ b) = P(a)P(b|a)

**random variable**
 a variable in probability theory with a domain of possible values it can take on

**Probability distribution**
 a mathematical function that describes the likelihood of possible outcomes of a random variable

 a probability distribution takes a random variable and gives the probability for each of the possible values in its domain

            P(Flight = on time) = 0.6
            P(Flight = delayed) = 0.3
            P(Flight = cancelled) = 0.1
                                  ==> 1

            P(Flight) = <0.6, 0.3, 0.1>

**independence**
 the knowledge that one event occurs does not affect the probability of other event
    P(a)P(b|a) = P(b)P(a|b)

**Bayes's Rule**
    P(b|a) = P(a|b)P(b)/P(a)

**Negation**
    P(¬a) = 1 - P(a)
    
**Inclusion-Exclusion**

    P(a ∨ b) = P(a) + P(b) - P(a ∧ b)

**Marginalization**
    P(a) = P(a,b) + P(a,¬b)

P(X=x) = ∑<sub>j</sub>P(X=x, Y=y)


**Conditioning**
    P(a) = P(a|b)P(b) + P(a|¬b)P(¬b)

**Bayesian Networks**
data structure that represents the dependencies among random variables

  - directed graphs
  - each node represents a random variable
  - arrow from X to Y means X is a parent of Y
  - each node X has a probability distribution P(X | Parents(X))

**Inference**
  - Query X: variable for which to compute distribution
  - Evidence variables E: observed variables for event e
  - Hidden variables Y: non-evidence, non-query variable.
  - Goal: Calculate P(X|e)

**Inference by Enumeration**
    P(X|e) = αP(X, e) = α∑<sub>y</sub>P(X,e,y)

  - X is the query variable.
  - e is the evidence
  - y ranges over values of hidden variables.
  - α normalizes the result

**Markov assumption**
the assumption  that current state depends on only a finite fixed number of previous states

**Markov chain**
a sequence of random variables where the distribution of each variable follows the Markov assumption

**Hidden Markov Model**
a Markov model for a system with hidden states that generate some observed event

**sensor Markov assumption**
the assumption that the evidence variable depends only the corresponding state