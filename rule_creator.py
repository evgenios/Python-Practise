import re

def build_match_and_apply_function(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, pattern, word)

    return (matches_rule, apply_rule)

# patterns = \
#     (
#         ('[sxz]$', '$', 'es'),
#         ('[^aeioudgkprt]h$', '$', 'es'),
#         ('(qu|[^aeiou])y$', '$', 'ies'),
#         ('$', '$', 's')
#     )

rules = []
with open('rules.txt', encoding='utf-8') as rules_file:
    for line in rules_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_function(pattern, search, replace))

# rules = [build_match_and_apply_function(search, pattern, replace)
#             for (pattern, search, replace) in patterns]

# if __name__ == "__main__":
#     print(addNums(1,2))
#     print(subtractNums(1,2))
#     print(subtractNums(6))
 