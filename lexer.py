from language import language


class Lexer:

    def tokenize(self, string):
        for e in language:
            r = e[1].match(string)
            if r:
                return e[0], string.strip('\"')

    def word(self, string):
        for x in string.split():
            yield x

    def lex(self, string):
        return map(self.tokenize, self.word(string))
