# Random Numbers and Choices

The `random` library in Python is a built-in module that provides functions for generating random numbers and making random choices. It's a versatile library with a range of functions for various randomization tasks. Here are some of the key functions and their capabilities:

0. **Importing the Library**:

    - `import random`: Imports the random library.
    - `from random import *`: Imports all the functions in the random library.
    - `from random import randrange, randint`: Imports specific functions from the random library.

1. **Generating Random Numbers**:

    - `random.random()`: Returns a random floating-point number between 0 and 1.
    - `random.randint(a, b)`: Returns a random integer between `a` and `b`, inclusive.
    - `random.uniform(a, b)`: Returns a random floating-point number between `a` and `b`.
    - `random.randrange(start, stop, step)`: Returns a random element from the range `start` (inclusive) to `stop` (exclusive) with the specified step.

2. **Random Choices**:

    - `random.choice(seq)`: Returns a random element from the given sequence (`seq`), which can be a list, tuple, or string.
    - `random.choices(population, weights=None, k=1)`: Returns a list of `k` random elements from the population. You can specify the probability weights for each element using the `weights` parameter.

3. **Random Sequences**:

    - `random.shuffle(seq)`: Shuffles the elements of a sequence in place.
    - `random.sample(population, k)`: Returns a new list containing `k` unique elements randomly chosen from the population without replacement.
    - Differences between sample and choices:
        - `sample` returns unique elements, while `choices` may return duplicates.
        - `sample` requires the `k` parameter, while `choices` returns a single element by default.
        - `choices` can take a `weights` parameter, while `sample` cannot.

4. **Randomizing with Seeds**:

    - `random.seed(a=None)`: Initializes the random number generator with the given seed (an integer or string). Using the same seed will produce the same random sequence, allowing for reproducibility.

# Examples

Let's try out some examples to understand how these functions work.

**Exercise 1: Random Number Generator**

Write a Python program to generate and print a random integer between 1 and 10. You can use the `random.randint(a, b)` function.

```python
import random

random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)
# Random number between 1 and 10: 7
```

This exercise demonstrates how to use `random.randint()` to generate random integers within a specified range.

**Exercise 2: Coin Flip Simulator**

Create a simple coin flip simulator in Python. The program should randomly simulate the outcome of a coin flip (heads or tails).

```python
import random

coin = random.choice(["Heads", "Tails"])
print("Coin landed on:", coin)
```

Here, we use `random.choice()` to randomly select an item from a list, simulating a coin flip.

**Exercise 3: Random Choice from a List**

Write a program that randomly selects and prints a day of the week from a list of days.

```python
import random

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
random_day = random.choice(days_of_week)
print("Random day of the week:", random_day)
```

This exercise demonstrates how to use `random.choice()` to make a random selection from a list.

**Exercise 4: Dice Roll Simulator (2 Dice)**

Simulate the roll of two six-sided dice and print the results. Calculate and display the sum of the two dice. You can use `random.randint(a, b)` for each die.

```python
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print("Die 1:", die1)
print("Die 2:", die2)
print("Total:", total)
```

This exercise combines the use of `random.randint()` to simulate the roll of two dice and calculate their sum.

**Exercise 5: Random Choices from a List**

Write a program that randomly selects and prints three names from a list of names. You can use `random.choices()`.

```python
import random

names = ["John", "Bob", "Alice", "Mary", "Jane", "Jack"]
random_names = random.choices(names, k=3)
# Random names: ['Jack', 'Jane', 'Bob']
print("Random names:", random_names)
```

**Exercise 6: Random Choices from a List with weight**

Write a program that randomly selects and prints three names from a list of names. You can use `random.choices()` with the `weights` parameter.

```python
import random

names = ["John", "Bob", "Alice", "Mary", "Jane", "Jack"]
weights = [0.1, 0.1, 0.3, 0.3, 0.1, 0.1]
random_names = random.choices(names, weights=weights, k=3)
# Random names: ['Bob', 'Mary', 'Jane']
print("Random names:", random_names)
```

**Exercise 7: Random Shuffling**

Write a program that shuffles a list of names in place. You can use `random.shuffle()`.

```python
import random

names = ["John", "Bob", "Alice", "Mary", "Jane", "Jack"]
random.shuffle(names)
print("Shuffled names:", names)
# Shuffled names: ['Bob', 'John', 'Jack', 'Jane', 'Mary', 'Alice']
```

**Exercise 8: Random Sampling**

Write a program that randomly selects and prints three names from a list of names without replacement. You can use `random.sample()`.

```python
import random

names = ["John", "Bob", "Alice", "Mary", "Jane", "Jack"]
random_names = random.sample(names, k=3)
# Random names: ['Bob', 'Mary', 'Jane']
print("Random names:", random_names)
```
