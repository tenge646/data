import string

def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return not stack

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

def word_frequency(sentence):
    word_count = {}
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# test
if __name__ == "__main__":
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  # Output: True
    print(is_balanced(expression2))  # Output: False

    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    print(result)  # Output: [2, 3, 4, 5, 6, 7]

    sentence = "testing to see the out put. This is my test."
    result = word_frequency(sentence)
    print(result)
