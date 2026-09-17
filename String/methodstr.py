s = "  Hello, World  "

s.strip()            # "Hello, World"  — trim whitespace (also lstrip/rstrip)
s.lower()            # lowercase — for case-insensitive comparisons
s.upper()            # uppercase
"a b c".split()      # ['a', 'b', 'c'] — no arg splits on any whitespace
"a,b,c".split(",")   # ['a', 'b', 'c']
" ".join(["a","b"])  # "a b" — the opposite of split
s.replace("l", "L")  # replace all occurrences
s.find("World")      # index of first match, or -1 if not found
s.index("World")     # same, but raises ValueError if not found
s.count("l")         # number of occurrences
s.startswith("He")   # True/False (also endswith)