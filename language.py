import re

EXPRESSION = r'([a-z]*)+([0-9]*)'
OPERATOR = r'[+-]'
LITERAL_VALUE = r"(\d)|(\"(\w*)+(\d*)\")"
KEYWORD = r'(\belse\b)|(\bif\b)'

language = []

language.append(("OPERATOR", re.compile(OPERATOR)))
language.append(("KEYWORD", re.compile(KEYWORD)))
language.append(("LITERAL_VALUE", re.compile(LITERAL_VALUE)))
language.append(("EXPRESSION", re.compile(EXPRESSION)))

