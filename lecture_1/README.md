# Knowledge

**knowledge-based agents:**
agents that reason by operation on internal representations of knowledge

**Logical Connectives:**
not ->  ¬ (the tilde symbol or an overline)
and ->  ∧ (the caret symbol)
or  ->  ∨ (the wedge symbol)
implication  -> → (the right arrow symbol)
biconditional -> ↔ (the double arrow symbol)


**not (¬):**
 P       ¬P
false   true
true    false


**and (∧):**
 P           Q          P ∧ Q
false       false       false
false       true        false
true        false       false
true        true        true


**or (∨):**
 P           Q          P ∨ Q
false       false       false
false       true        true
true        false       true
true        true        true


**implication (→):**
 P           Q          P → Q
false       false       true
false       true        true
true        false       false
true        true        true

**biconditional (↔):**
 P           Q          P ↔ Q
false       false       true
false       true        false
true        false       false
true        true        true


**model:**
assignment of a truth value to every propositional symbol (a "possible world")

**knowledge base:**
a set of sentences known by a knowledge-based agent

**Entailment:**
α ⊨ β
we read it as, α entails β
in every model in which sentence α is true, sentence β is also true.

**inference:**
the process of deriving new sentences from old ones

**model checking:**
+ To determine if KB ⊨ α:
  - Enumerate all possible models.
  - If in every model where KB is true, α is true, then KB entails α.
  - Otherwise, KB does not entails α.

**De Morgan's Law:**
  - ¬(α ∧ β) ≡ ¬α ∨ ¬β
  - ¬(α ∨ β) ≡ ¬α ∧ ¬β

**Distributive Property:**
  - α ∧ (β ∨ γ) ≡ (α ∧ β) ∨ (α ∧ γ)
  - α ∨ (β ∧ γ) ≡ (α ∨ β) ∧ (α ∨ γ)

**Theorem Proving:**
  - initial state: starting knowledge base
  - actions: inference rule
  - transition model: new knowledge base after inference
  - goal test: check statement we're trying to prove
  - path cost function: number of steps in proof

**clause:**
a disjunction of literals
eg: P ∨ Q ∨ R

**conjunctive normal form:**
logical sentence that is conjunction of clauses
eg: (A ∨ B ∨ C) ∧ (D ∨ ¬E) ∧ (F ∨ G)

**Conversion to CNF:**
  - Eliminate bi conditionals
    - turn(α ↔️ β) into (α → β) ∧ (β → α)
  - Eliminate implications
    - turn(α → β) into ¬α ∨ β
  - Move ¬ inwards using De Morgan's Laws
    - eg: turn (¬α ∧ β) into ¬α ∨ ¬β

  - (P ∨ Q) → R
    - ¬(P ∨ Q) ∨ R     eliminate implication
    - (¬P ∧ ¬Q) ∨ R     De Morgan's Law
    - (¬P ∨ R) ∧ (¬Q ∨ R)     distributive law

**Inference by Resolution**
  -  P ∨ Q
    ¬P ∨ R
  ----------------
    (Q ∨ R)

  -  P ∨ Q ∨ S
    ¬P ∨ R ∨ S
  ----------------
    (Q ∨ R ∨ S) 

  - To determine if KB ⊨ α:
    - Check if (KB ∧ ¬α) is a contradiction? 
      - If so, then KB ⊨ α.
      - Otherwise, no entailment.
  
  - To determine if KB ⊨ α:
    - Convert (KB ∧ ¬α) to Conjunctive Normal Form.
    - Keep checking to see if we can use resolution to produce a new clause.
      - If ever we produce the empty clause (equivalent to False), we have a contradiction, and KB ⊨ α.
      - Otherwise, if we can't add new clauses, no entailment. 


**Existential Quantification**

- ∃x. House(x) ∧ BelongsTo(Minerva, x)
  
  There exists an object x such that x is a house and Minerva belongs to x.

- ∀x.Person(x) → (∃y.House(y) ∧ BelongsTo(x,y))
  
  For all objects x, if x is a person, then there exists an object y such that y is a house and x belongs to y.
  Every person belongs to a house.