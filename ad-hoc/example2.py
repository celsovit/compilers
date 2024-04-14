"""
Implementação manual de um analisador léxico, ou seja, sem o uso de geradores de analisadores léxicos como o Lex ou o Flex

Exemplo ad-hoc de implementação de um analisador léxico para uma linguagem de expressões aritméticas simples.

Example2.py
"""

import re

# Definir os padrões para os tokens
patterns = [
    (r'[0-9]+', 'INT'),         # Números inteiros
    (r'\+', 'PLUS'),             # Operador de adição
    (r'-', 'MINUS'),             # Operador de subtração
    (r'\*', 'TIMES'),            # Operador de multiplicação
    (r'/', 'DIVIDE'),            # Operador de divisão
    (r'\s+', 'SPACE'),           # Espaços em branco
]

# Função para tokenizar o código-fonte
def tokenize(code):
    tokens = []
    while code:
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                code = code[len(value):].lstrip()
                break
        if not match:
            raise ValueError('Token inválido: ' + code)
    return tokens

# Exemplo de código-fonte
source_code = "3 + 4 * 2 - 8 / 4"

# Tokenizar o código-fonte
tokens = tokenize(source_code)
print(tokens)
