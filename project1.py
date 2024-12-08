import random

class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = []

    def input_matrix(self):
        print("Введите элементы матрицы (через пробел):")
        for i in range(self.size):
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
            self.matrix.append(row)

    def generate_random_matrix(self):
        self.matrix = [[random.randint(1, 100) for _ in range(self.size)] for _ in range(self.size)]

    def swap_rows_and_columns(self):
        min_row_index = None
        max_col_index = None
        min_value = float('inf')
        max_value = float('-inf')

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] < min_value:
                    min_value = self.matrix[i][j]
                    min_row_index = i
                if self.matrix[i][j] > max_value:
                    max_value = self.matrix[i][j]
                    max_col_index = j
                    
        if min_row_index is not None and max_col_index is not None:
            for i in range(len(self.matrix)):
                self.matrix[min_row_index][i], self.matrix[i][max_col_index] = self.matrix[i][max_col_index], self.matrix[min_row_index][i]

    def display_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

class Menu:
    def print_menu(self):
        print("\nМеню:")
        print("1. Ввод исходных данных вручную")
        print("2. Генерация случайной матрицы")
        print("3. Выполнение алгоритма")
        print("4. Вывод результата")
        print("5. Завершение работы программы")

def main():
    matrix = None
    menu = Menu()
    
    while True:
        menu.print_menu()
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            n = int(input("Введите размер матрицы (n x n): "))
            matrix = Matrix(n)
            matrix.input_matrix()
        elif choice == '2':
            n = int(input("Введите размер матрицы (n x n): "))
            matrix = Matrix(n)
            matrix.generate_random_matrix()
            print("Сгенерированная матрица:")
            matrix.display_matrix()
        elif choice == '3':
            if matrix is not None:
                matrix.swap_rows_and_columns()
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите данные.")
        elif choice == '4':
            if matrix is not None:
                matrix.display_matrix()
            else:
                print("Сначала введите данные.")
        elif choice == '5':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
