import re

#TODO: Make work for stuff like below
# new = []
# for i in loop_list:
#     i = i.replace(':', '')
#     new += [i]
# loop_list = new
#TODO: actually use Lexical analysis

def loop_to_list_comp(loop_string: str) -> str:
    """
    Convert a very simple for loop to a list comprehension.

    EXAMPLE METHOD INPUT REFERENCED IN BELOW COMMENTS:

    METHOD INPUT
    example_result = []
    for val in example_list:
        example_result.append(val + 2)

    METHOD OUTPUT
    example_result = [val + 2 for val in example_list]
    """

    # Each line of input expression stored in list ('example_result = []', 'for val in example_list'...).
    lines = loop_string.split('\n')
    for i, line in enumerate(lines):
        lines[i] = line.replace(':', '').strip()

    # Delete non-empty lists at top of expression.
    for i, s in enumerate(lines):
        if re.findall("\\[.+\\]", s):
            del lines[i]
        else:
            break

    # Store all empty list initialization(s) at top of input expression ([example_result = []]).
    empty_lists = []
    for i, line in enumerate(lines):
        if ('= []' or '=[]') in line:
            empty_lists.append(line)
        else:
            if not empty_lists:
                raise Exception("No empty list initialized in the provided expression")
            del lines[:i]
            break

    # Left side of equals sign of final list comp (example_result =).
    left_side = ', '.join([string.split(' =')[0] for string in empty_lists]) + ' = '

    # Value inside the original append statement(s) ([val + 2]).
    append_values = [index[index.find("(") + 1:index.find(")")] for index in lines if 'append' in index]

    # Indexes of append lines ([2]).
    append_statement_indexs = [lines.index(string) for string in lines if 'append' in string]

    # Divide expressions related to each result_variable ([['for val in example_list']]).
    expression_lists = [lines[0:index] for index in append_statement_indexs]

    # Join related sub-expressions (['for val in example_list']).
    expressions = []
    for expression_list in expression_lists:
        new = ''
        for s in expression_list:
            if not '.append' in s:
                new += (s + ' ')
        expressions += [new.strip()]

    # Right side of final expression ('[val + 2 for val in example_list]')
    result_expressons = [' '.join(z) for z in zip(append_values, expressions)]
    right_side = ", ".join(['[' + i + ']' for i in result_expressons])

    return left_side + right_side



