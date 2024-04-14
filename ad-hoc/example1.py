"""
Implementação manual de um analisador léxico, ou seja, sem o uso de geradores de analisadores léxicos como o Lex ou o Flex

Exemplo ad-hoc de implementação de um analisador léxico para uma linguagem de expressões aritméticas simples.

Example1.py
"""

import re

# Tokens
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
EOF = 'EOF'

# Expressão regular para números inteiros
INTEGER_REGEX = re.compile(r'\d+')

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception('Caractere inválido')

    def get_next_token(self):
        text = self.text

        # Checa se chegou ao final do texto
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # Pula espaços em branco
        while self.pos < len(text) and text[self.pos].isspace():
            self.pos += 1

        # Checa se o caractere atual é um número inteiro
        if INTEGER_REGEX.match(text[self.pos]):
            num_str = ''
            while self.pos < len(text) and INTEGER_REGEX.match(text[self.pos]):
                num_str += text[self.pos]
                self.pos += 1
            return Token(INTEGER, int(num_str))

        # Checa os operadores
        if text[self.pos] == '+':
            self.pos += 1
            return Token(PLUS, '+')
        elif text[self.pos] == '-':
            self.pos += 1
            return Token(MINUS, '-')
        elif text[self.pos] == '*':
            self.pos += 1
            return Token(MULTIPLY, '*')
        elif text[self.pos] == '/':
            self.pos += 1
            return Token(DIVIDE, '/')

        # Caractere inválido
        self.error()

# Exemplo de uso
text = '3 + 4 * 2 - 10 / 5'
lexer = Lexer(text)
token = lexer.get_next_token()
while token.type != EOF:
    print(token.type, token.value)
    token = lexer.get_next_token()
