# Language

**n-gram**
a contiguous sequence of n items from a sample of text

**bag-of-words model**
model that represents text as an unordered collection of words

**Naive Bayes**
the probability of an event, based on prior knowledge of conditions that might be related to the event
    - P(A∣B)= P(B∣A)⋅P(A)/P(B)
    - P(B∣A)= P(A∣B)⋅P(B)/P(A)

**additive smoothing**
adding a value α to each value in our distribution to smooth the data

**Laplace smoothing**
adding 1 to each value in our distribution:
 pretending we've seen each value one more time than we actually have

**one-hot representation**
representation of meaning as a vector with a single 1, and with other values as 0

**distributed representation**
representation of meaning distributed across multiple values

**word2vec**
model for generating word vectors