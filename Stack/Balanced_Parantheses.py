class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



#WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
def is_balanced_parentheses(expr):
    if len(expr)==0:
        return True
    test_stack = Stack()
    for c in expr:
        if c =='(':
            test_stack.push(c)  
        elif c == ')':
            #on closing braket, pop an opening bracket
            # if there was none left, there is more closing brackets than opening
            # also it helps to verify expr doesnt start with a closing bracket
            ## then nothing to append, so stack will be empty
            if test_stack.is_empty() or test_stack.pop() != '(':
                return False
    if test_stack.is_empty():
        return True
    else:
        return False            

###############################################




def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()
