# Data Structures and Algorithms

This repository contains Python implementations of functions for various data structures and algorithms.

## Stacks

### Function: `is_balanced(expression)`

Determines whether the provided expression containing parentheses, curly braces, and square brackets is balanced.

Example:
```python
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
```
## Sequences (Lists/Tuples)
***Function:*** remove_duplicates(sequence)
Removes duplicates from a given sequence (list or tuple) while maintaining the original order of elements.

***Example:***

```
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
```
## Dictionaries
Function: word_frequency(sentence)
Returns a dictionary containing the frequency of each word in a sentence. Punctuation is ignored, and words are considered in a case-insensitive manner.

***Example:***

```
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
h