import sys
from antlr4 import *
from asuaLexer import asuaLexer
from asuaParser import asuaParser
from visitor import ASUAVisitor

def main():
    # Verificar que se haya proporcionado un archivo como argumento
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <archivo.txt>")
        sys.exit(1)

    input_file = sys.argv[1]  # Obtener el archivo desde los argumentos
    if not input_file.endswith(".txt"):
        print("Error: Solo se permiten archivos .txt")
        sys.exit(1)

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")
        sys.exit(1)

    lexer = asuaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = asuaParser(stream)
    tree = parser.program()

    interpreter = ASUAVisitor()
    interpreter.visit(tree)

if __name__ == "__main__":
    main()


