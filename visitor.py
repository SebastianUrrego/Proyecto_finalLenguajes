import numpy as np
import math
import random
import cmath
import matplotlib.pyplot as plt
from asuaParser import asuaParser
from asuaVisitor import asuaVisitor

class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Inicialización aleatoria de pesos
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.learning_rate = 0.1
        self.errors = []  # Lista para almacenar los errores por época

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, X, y, epochs):
        X = np.array(X)
        y = np.array(y)

        for epoch in range(epochs):
            # Forward propagation
            hidden_layer_input = np.dot(X, self.weights_input_hidden)
            hidden_layer_output = self.sigmoid(hidden_layer_input)

            final_layer_input = np.dot(hidden_layer_output, self.weights_hidden_output)
            predicted_output = self.sigmoid(final_layer_input)

            # Error
            error = y - predicted_output
            self.errors.append(np.mean(np.abs(error)))  # Almacenar el error promedio

            # Backpropagation
            d_predicted_output = error * self.sigmoid_derivative(predicted_output)
            error_hidden_layer = d_predicted_output.dot(self.weights_hidden_output.T)
            d_hidden_layer = error_hidden_layer * self.sigmoid_derivative(hidden_layer_output)

            # Update weights
            self.weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * self.learning_rate
            self.weights_input_hidden += X.T.dot(d_hidden_layer) * self.learning_rate

            if epoch % 1000 == 0:
                print(f"Epoch {epoch} error: {self.errors[-1]}")

    def plot_errors(self):
        # Graficar los errores por época
        plt.figure(figsize=(10, 6))
        plt.plot(self.errors, label="Error")
        plt.xlabel("Épocas")
        plt.ylabel("Error Promedio")
        plt.title("Convergencia del Error durante el Entrenamiento")
        plt.legend()
        plt.grid()
        plt.show()

    def predict(self, X):
        hidden_layer_input = np.dot(X, self.weights_input_hidden)
        hidden_layer_output = self.sigmoid(hidden_layer_input)
        final_layer_input = np.dot(hidden_layer_output, self.weights_hidden_output)
        return self.sigmoid(final_layer_input)

class ASUAVisitor(asuaVisitor):
    def __init__(self):
        self.variables = {}
        self.memory = {}
        self.functions = {}  # Almacena las definiciones de funciones
        self.call_stack = []  # Pila para soportar recursividad
        self.imported_libraries = set()

    def visitImportStatement(self, ctx):
        library_name = ctx.ID().getText()
        if library_name in ["math", "numpy"]:
            self.imported_libraries.add(library_name)
        else:
            raise Exception(f"Biblioteca no soportada: {library_name}")

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if ctx.expr():
            value = self.visit(ctx.expr())
        elif ctx.matrixOperation():
            value = self.visit(ctx.matrixOperation())
        else:
            raise Exception("Expresión o operación no válida")
        
        self.variables[var_name] = value
        return value

    def visitExpr(self, ctx):
        text = ctx.getText()

        # Manejo de valores booleanos
        if text == "True":
            return True
        elif text == "False":
            return False

        # Manejo de números
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())

        # Manejo de cadenas de texto
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')

        # Llamada a función
        elif ctx.ID() and ctx.getChildCount() == 3:  # ID '(' arguments? ')'
            return self.visitFunctionCall(ctx)

        # Manejo de identificadores (variables)
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            raise Exception(f"Variable no definida: {var_name}")

        # Manejo de matrices
        elif ctx.matrix():
            return self.visit(ctx.matrix())

        # Manejo de operadores unarios (e.g., -expr, +expr)
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText()  # '+' o '-'
            value = self.visit(ctx.expr(0))       # Evalúa la expresión siguiente
            if operator == '-':
                return -value
            elif operator == '+':
                return value
        
        # Operaciones binarias (e.g., suma, resta, multiplicación)
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            # Operaciones entre matrices
            if isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
                if op == '+':
                    return np.add(left, right)
                elif op == '-':
                    return np.subtract(left, right)
                elif op == '*':
                    return np.dot(left, right)
                else:
                    raise Exception(f"Operación no válida entre matrices: {op}")

            if isinstance(left, str) or isinstance(right, str):
                if op == '+':  # Concatenar cadenas si uno de los operandos es str
                    return str(left) + str(right)
                else:
                    raise TypeError(f"Operación no compatible con cadenas: {op}")
            # Operaciones entre números
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise Exception("Error matemático: división entre cero")
                return left / right
            elif op == '%':
                return left % right
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right

        # Funciones matemáticas específicas
        elif text.startswith("sqrt("):
            value = self.visit(ctx.expr(0))
            if value < 0:
                # Usar cmath.sqrt para manejar números negativos
                return cmath.sqrt(value)
            return math.sqrt(value)
        elif text.startswith("pow("):
            base = self.visit(ctx.expr(0))
            exponent = self.visit(ctx.expr(1))
            return math.pow(base, exponent)
        elif text.startswith("abs("):
            value = self.visit(ctx.expr(0))
            return abs(value)
        elif text.startswith("sin("):
            value = self.visit(ctx.expr(0))
            return math.sin(value)
        elif text.startswith("cos("):
            value = self.visit(ctx.expr(0))
            return math.cos(value)
        elif text.startswith("tan("):
            value = self.visit(ctx.expr(0))
            return math.tan(value)

        # Constantes matemáticas
        elif text == "pi":
            return math.pi
        elif text == "e":
            return math.e

        # Manejo de paréntesis (e.g., (expr))
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))

        elif ctx.ID() and ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '(':
            return self.visitFunctionCall(ctx)

        # Manejo de identificadores (variables)
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            raise Exception(f"Variable no definida: {var_name}")

        # Error si la expresión no es válida
        raise Exception(f"Expresión no válida: {text}")


    def visitMatrix(self, ctx):
        rows = [self.visit(row) for row in ctx.row()]
        return np.array(rows)

    def visitRow(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]
        
    def visitMatrixOperation(self, ctx):
        operation = ctx.getChild(0).getText()  # 'transpose' o 'inverse'
        matrix_name = ctx.ID().getText()       # Nombre de la matriz

        # Verifica si la matriz existe
        if matrix_name not in self.variables:
            raise Exception(f"Matriz no definida: {matrix_name}")
        
        matrix = self.variables[matrix_name]
        
        # Verifica que sea una matriz válida (de tipo numpy.ndarray)
        if not isinstance(matrix, np.ndarray):
            raise Exception(f"El valor de {matrix_name} no es una matriz válida")
        
        # Transposición
        if operation == 'transpose':
            result = np.transpose(matrix)
            return result

        # Inversa
        elif operation == 'inverse':
            if np.linalg.det(matrix) == 0:
                raise Exception(f"La matriz {matrix_name} no es invertible")
            result = np.linalg.inv(matrix)
            return result
        
        # Operación no reconocida
        raise Exception(f"Operación desconocida para matrices: {operation}")

    def visitLogStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(f">>> {value}")
        return value 
        
    def visitList(self, ctx):
        # Crear una lista a partir de las expresiones dentro de los corchetes
        return [self.visit(child) for child in ctx.expr()]

    def visitArray(self, ctx):
        # Obtener el nombre del array y el tamaño
        array_name = ctx.ID().getText()
        size = int(ctx.NUMBER().getText())

        # Obtener los valores de la lista
        values = [self.visit(expr) for expr in ctx.expr()]

        # Validar que no se exceda el tamaño máximo
        if len(values) > size:
            raise Exception(f"El array '{array_name}' tiene más valores que el tamaño definido ({size})")

        # Rellenar con ceros si faltan valores
        while len(values) < size:
            values.append(0)

        # Guardar el array en memoria
        self.variables[array_name] = values
        print(f"Array '{array_name}' definido con valores: {values}")
        return values
   
    def visitAccessArray(self, ctx):
        array_name = ctx.ID().getText()
        index = int(self.visit(ctx.expr()))

        # Validar si el array existe
        if array_name not in self.variables:
            raise Exception(f"Array '{array_name}' no está definido")

        array = self.variables[array_name]

        # Validar el índice
        if index < 0 or index >= len(array):
            raise Exception(f"Índice fuera de rango para el array '{array_name}'")

        return array[index]

    def visitFunctionDef(self, ctx):
        func_name = ctx.ID().getText()
        parameters = [param.getText() for param in ctx.parameters().ID()] if ctx.parameters() else []
        body = ctx.statement()
        return_stmt = ctx.returnStatement()  # Puede ser None si no hay un return explícito

        self.functions[func_name] = {
            "parameters": parameters,
            "body": body,
            "return": return_stmt,
        }

        print(f"Función registrada: {func_name} con parámetros {parameters}")
        return None

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        if func_name not in self.functions:
            raise Exception(f"Función no definida: {func_name}")

        # Obtener definición de la función
        func_def = self.functions[func_name]
        parameters = func_def["parameters"]
        body = func_def["body"]
        return_stmt = func_def["return"]

        # Evaluar argumentos
        arguments = [self.visit(arg) for arg in ctx.arguments().expr()] if ctx.arguments() else []
        if len(arguments) != len(parameters):
            raise Exception(f"Se esperaban {len(parameters)} argumentos, pero se recibieron {len(arguments)}.")

        # Crear un contexto local
        local_context = dict(zip(parameters, arguments))
        self.call_stack.append(self.variables)  # Guardar el contexto actual
        self.variables = local_context  # Cambiar al contexto local

        # Ejecutar el cuerpo de la función
        result = None
        for stmt in body:
            result = self.visit(stmt)
            if result is not None:  # Salir si se encuentra un return
                break

        # Evaluar return si existe
        if return_stmt:
            result = self.visit(return_stmt.expr())

        # Restaurar el contexto anterior
        self.variables = self.call_stack.pop()

        return result

    def visitReturnStatement(self, ctx):
        return self.visit(ctx.expr())

    def visitGraph(self, ctx):
        # Obtener las expresiones para x y y
        x_expr = ctx.expr(0)
        y_expr = ctx.expr(1)

        # Obtener rango y paso
        range_start = self.visit(ctx.rangeStart())
        range_end = self.visit(ctx.rangeEnd())
        step = self.visit(ctx.step())

        # Generar rango de valores para x
        x_values = np.arange(range_start, range_end, step)
        y_values = []

        # Evaluar y para cada x
        for x in x_values:
            self.variables['x'] = x  # Asignar el valor de x en el contexto actual
            y_values.append(self.visit(y_expr))

        # Generar la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label="Gráfica de y en función de x")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfica personalizada")
        plt.grid(True)
        plt.legend()
        plt.show()

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def visitPrimeGraph(self, ctx):
        # Extraer el rango y paso desde los parámetros de la gramática
        range_start = int(self.visit(ctx.rangeStart()))
        range_end = int(self.visit(ctx.rangeEnd()))
        step = int(self.visit(ctx.step()))

        # Crear listas para almacenar índices y números primos
        x_indices = []
        prime_numbers = []

        # Determinar los números primos en el rango
        index = 0
        for x in range(range_start, range_end + 1, step):
            if self.is_prime(x):  # Usa la función de primos definida
                x_indices.append(index)
                prime_numbers.append(x)
                index += 1

        # Graficar los números primos
        plt.figure(figsize=(8, 6))
        plt.scatter(x_indices, prime_numbers, color='blue')
        plt.xlabel("Índice")
        plt.ylabel("Número primo")
        plt.title("Números Primos")
        plt.grid(True)
        plt.show()


    def visitConditional(self, ctx):
        condition = self.visit(ctx.expr())  # Evaluar la condición
        if condition:
            # Visitar las declaraciones dentro del bloque `if`
            for statement in ctx.statement()[:len(ctx.statement())//2]:
                self.visit(statement)
        else:
            # Visitar las declaraciones dentro del bloque `else`, si existe
            if len(ctx.statement()) > len(ctx.statement())//2:
                for statement in ctx.statement()[len(ctx.statement())//2:]:
                    self.visit(statement)

    def visitLoop(self, ctx):
        if ctx.getText().startswith("for"):
            self.visit(ctx.assignment(0))  # Inicialización
            while self.visit(ctx.expr()):  # Condición
                for statement in ctx.statement():
                    self.visit(statement)
                self.visit(ctx.assignment(1))  # Incremento
        elif ctx.getText().startswith("while"):
            while self.visit(ctx.expr()):  # Condición
                for statement in ctx.statement():
                    self.visit(statement)


    def visitFileOperation(self, ctx):
        if ctx.getChild(0).getText() == 'readFile':
            # Obtener el nombre del archivo de la regla readFile
            filename = ctx.STRING().getText().strip('"')  # Obtener el nombre del archivo
            try:
                # Intentar leer el archivo
                with open(filename, 'r') as file:
                    content = file.read()
                    print(f"Leyendo archivo {filename}: {content}")
                    return content  # Devolver el contenido leído
            except Exception as e:
                print(f"Error leyendo archivo {filename}: {str(e)}")
                return None  # En caso de error, devolvemos None

        elif ctx.getChild(0).getText() == 'writeFile':
            # Obtener el nombre del archivo y el contenido de la expresión a escribir
            filename = ctx.STRING().getText().strip('"')  # Obtener el nombre del archivo
            content = str(self.visit(ctx.expr()))  # Evaluar la expresión (contenido) a escribir
            try:
                # Intentar escribir el contenido en el archivo
                with open(filename, 'w') as file:
                    file.write(content)
                print(f"Escribiendo en archivo {filename}: {content}")
                return True  # Devolver True si la escritura fue exitosa
            except Exception as e:
                print(f"Error escribiendo en archivo {filename}: {str(e)}")
                return None  # En caso de error, devolvemos None
                
    # Función para manejar la operación kMeansOperation
    def visitKMeansOperation(self, ctx):
        k = int(ctx.NUMBER().getText())  # Número de clusters
        matrix_ctx = ctx.matrix()  # Obtenemos la matriz de puntos
        points = self.visit(matrix_ctx)  # Obtenemos los puntos de la matriz
        points = np.array(points)  # Convertimos los puntos en un array de numpy

        # Inicializamos aleatoriamente los centroides de los clusters
        centroids = points[np.random.choice(points.shape[0], k, replace=False)]
        
        # Algoritmo K-Means
        max_iters = 100
        for _ in range(max_iters):
            # Calcular distancias de cada punto a los centroides
            distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
            # Asignar puntos a los clusters más cercanos
            labels = np.argmin(distances, axis=1)
            
            # Recalcular los centroides
            new_centroids = np.array([points[labels == i].mean(axis=0) for i in range(k)])
            
            # Verificar si los centroides han cambiado
            if np.all(centroids == new_centroids):
                break
            
            centroids = new_centroids
        
        # Mostrar los resultados
        print("Centroides finales:", centroids)
        print("Etiquetas de los puntos:", labels)
        
        # Graficar los puntos y los centroides
        plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
        plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='X', s=200)
        plt.title("K-Means Clustering")
        plt.show()
        
    def visitRegressionOperation(self, ctx):
        # Obtener los nombres de las variables
        model_name = ctx.ID(0).getText()  # Nombre del modelo
        X_name = ctx.ID(1).getText()      # Características (X)
        y_name = ctx.ID(2).getText()      # Etiquetas (y)
        
        # Verificar que las variables X e y estén definidas
        if X_name not in self.variables or y_name not in self.variables:
            raise Exception(f"Variables '{X_name}' o '{y_name}' no definidas.")
        
        # Obtener los datos de las variables
        X = np.array(self.variables[X_name])  # Características (X)
        y = np.array(self.variables[y_name])  # Etiquetas (y)

        # Convertir y a un vector columna si es necesario
        if len(y.shape) == 1:
            y = y.reshape(-1, 1)  # Convertir de (n,) a (n,1)
        elif y.shape[0] == 1:
            y = y.T  # Transponer si es (1, n)

        # Verificar que las dimensiones de X y y coincidan
        if X.shape[0] != y.shape[0]:
            raise Exception(f"Las dimensiones de X ({X.shape}) y y ({y.shape}) no coinciden.")

        # Agregar columna de 1s a X para el término independiente
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # X con columna de 1s (intercepto)

        # Cálculo de los coeficientes w usando la fórmula de mínimos cuadrados
        w = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

        # Guardar los coeficientes en la variable model_name
        self.variables[model_name] = w

        # Imprimir los coeficientes
        print(f"Modelo '{model_name}' definido con coeficientes: {w.flatten()}")

        # Graficar los datos y la línea de regresión
        y_pred = X_b.dot(w)  # Predicción de y usando el modelo
        plt.scatter(X, y, color='blue', label='Datos Reales')  # Puntos originales
        plt.plot(X, y_pred, color='red', label='Línea de Regresión')  # Línea de regresión
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.title(f"Regresión Lineal: {model_name}")
        plt.show()

        return w

    def visitMlpOperation(self, ctx):
        input_size = int(ctx.NUMBER(0).getText())
        hidden_size = int(ctx.NUMBER(1).getText())
        output_size = int(ctx.NUMBER(2).getText())
        epochs = int(ctx.NUMBER(3).getText())
        X = self.visit(ctx.matrix(0))  # Primera matriz
        y = self.visit(ctx.matrix(1))  # Segunda matriz

        if len(X) != len(y):
            raise Exception("El número de muestras en X e y no coincide.")

        # Crear y entrenar el modelo
        model = MLP(input_size, hidden_size, output_size)
        model.train(X, y, epochs)

        # Guardar el modelo en las variables para uso futuro
        self.variables['mlp_model'] = model
        print("Modelo MLP entrenado y almacenado en 'mlp_model'.")

        # Mostrar la gráfica de errores
        model.plot_errors()



