"""
 Analisador léxico que reflete diretamente um AF para reconhecer números inteiros

AF é a abreviação de "Autômato Finito", que é uma representação matemática de
um modelo computacional que opera em uma quantidade limitada de memória. No 
contexto da análise léxica, um autômato finito pode ser usado para reconhecer
padrões em cadeias de caracteres, como tokens em um código-fonte.

"""

def tokenize(code):
    tokens = []
    current_token = ''
    state = 'START'
    for char in code:
        if state == 'START':
            if char.isdigit():
                state = 'INT'
                current_token += char
            elif char in ['+', '-', '*', '/']:
                tokens.append(('OPERATOR', char))
        elif state == 'INT':
            if char.isdigit():
                current_token += char
            else:
                tokens.append(('INT', current_token))
                current_token = ''
                state = 'START'
                if char in ['+', '-', '*', '/']:
                    tokens.append(('OPERATOR', char))
    if current_token:
        tokens.append(('INT', current_token))
    return tokens

# Exemplo de uso
source_code = "3 + 4 * 2 - 8 / 4"
tokens = tokenize(source_code)
print(tokens)
