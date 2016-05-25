from lexer import Lexer
string = 'if bob then 0  else "bob1" '

l = Lexer()
result = l.lex(string)
for x in result:
    print(x)
