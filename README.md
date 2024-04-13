# Compiladores, análise léxica, entre outros
_UNIVESP :: Compiladores_


### Ambiente para executar códigos Python

```bash
$ mkdir ~/compiler
$ cd ~/compiler
$ python -m venv venv
$ pip install ply
```

### Compilar, linkar e executar código Assembly (GNU)
```bash
# montagem
$ as hello.s -o hello.o

# linkagem
$ gcc hello.o -o hello -no-pie

# execução
$ ./hello

# saída: 
# Hello, World!
```

## Mais sobre compiladores

- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/ply.html#ply_nn4)
- [JavaCC (Java Compiler-Compiler)](http://www.inf.ufes.br/~tavares/labcomp2000/javacc.html)
- [Processamento de Linguagem](https://www.di.ubi.pt/~desousa/DLPC/dlpc.html)




## Lex & Yacc e Bibliotecas de Análise Léxica e Sintática em Python
### Lex & Yacc
Lex e Yacc são ferramentas populares para gerar analisadores léxicos e sintáticos para processamento de linguagens formais. Lex é usado para análise léxica, enquanto Yacc é usado para análise sintática. Juntos, eles permitem a construção de compiladores e interpretadores para linguagens de programação e outras linguagens formais.

### Lex
Lex (ou Flex) é uma ferramenta de geração de analisadores léxicos. Ele funciona definindo padrões de expressões regulares e associando ações a esses padrões. Quando uma entrada é fornecida, o analisador léxico gerado pelo Lex identifica os padrões na entrada e executa as ações associadas a esses padrões.

### Yacc
Yacc (ou Bison) é uma ferramenta de geração de analisadores sintáticos. Ele funciona usando gramáticas livres de contexto para descrever a estrutura sintática de uma linguagem. Com base nessa gramática, o Yacc gera um analisador sintático que pode ser usado para analisar entradas de acordo com as regras da gramática.

### Bibliotecas em Python
Além do Lex & Yacc tradicionais, existem várias bibliotecas disponíveis em Python para análise léxica e sintática. Algumas das principais são:

### PLY (Python Lex-Yacc)
PLY é uma implementação em Python das ferramentas Lex e Yacc. Ele permite definir analisadores léxicos e sintáticos diretamente em Python, usando classes e funções. PLY é amplamente utilizado devido à sua facilidade de uso e flexibilidade.

### ANTLR
ANTLR é uma ferramenta de geração de analisadores léxicos e sintáticos que suporta várias linguagens de programação, incluindo Python. Ele usa uma gramática baseada em EBNF (Extended Backus-Naur Form) para descrever a estrutura da linguagem e gera código Python para o analisador correspondente.

### PyParsing
PyParsing é uma biblioteca Python para análise de texto baseada em expressões gramaticais. Ele permite definir gramáticas diretamente em Python usando uma sintaxe de expressão, facilitando a criação de analisadores léxicos e sintáticos para formatos de texto complexos.

