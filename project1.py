from random import randint
import numpy as np


class MatrixProcessor:
    def __init__(self):
        self.matrix = []
        print("Создание объекта MatrixProcessor...")  # Отладочное сообщение
        self.menu()  # Вызов метода menu при создании объекта

    def make_mat(self):
        firstLine = list(map(int, input("Введите 1-ю строку матрицы: ").split()))
        self.matrix = [firstLine]
        for i in range(1, len(firstLine)):
            nextLine = list(map(int, input(f"Введите {i + 1}-ю строку матрицы: ").split()))
            self.matrix.append(nextLine)
        print("Исходная матрица:")
        for row in self.matrix:
            print(row)

    def swap_row_col(self):
        # Преобразуем ввод в np.array
        arr = np.array(self.matrix)
        # Определяем размеры матрицы
        n = arr.shape[0]
        # Находим индекс строки с минимальным элементом
        min_value = np.min(arr)
        min_row_index = np.where(arr == min_value)[0][0]
        # Находим индекс столбца с максимальным элементом
        max_value = np.max(arr)
        max_col_index = np.where(arr == max_value)[1][0]
        # Создаем новую матрицу для результата
        result = arr.copy()
        # Меняем местами строку с минимальным элементом и столбец с максимальным
        result[min_row_index, :], result[:, max_col_index] = arr[:, max_col_index], arr[min_row_index, :]
        return result

    def vuvod(self):
        print("Результат работы алгоритма:")
        for row in self.matrix:
            print(row)

    def menu(self):
        """Основное меню приложения."""
        print("Запуск меню...")  # Отладочное сообщение
        while True:
            print("\nМеню:")
            print("1) Ввод матрицы вручную")
            print("2) Обработка матрицы")
            print("3) Вывод результата")
            print("0) Завершение работы")

            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.make_mat()
            elif choice == '2':
                res = self.swap_row_col()
                if res.all():
                    self.matrix = res
                    print("Матрица обработана.")
            elif choice == '3':
                self.vuvod()
            elif choice == '0':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    processor = MatrixProcessor()  # Создание объекта класса вызовет метод menu