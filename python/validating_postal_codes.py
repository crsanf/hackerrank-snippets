# must be a number in the range from  to  inclusive.
# must not contain more than one alternating repetitive digit pair.

import re

regex_integer_in_range = r"[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d{1})(?=\d{1}\1)"

P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
