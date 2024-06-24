from logic import *

rain = Symbol("rain") # It is raining.
hagrid = Symbol("hagrid") # Harry visited Hagrid.
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore.

knowledge = Not(rain)
print(knowledge.formula())