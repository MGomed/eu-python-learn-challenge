class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list) == 0:
            return input_list

        max = input_list[0]
        for element in input_list:
            if max < element:
                max = element

        for index, element in enumerate(input_list):
            if element > 0:
                input_list[index] = max

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def binary_search(input_list: list[int], left, right, query: int) -> int:
            if len(input_list) == 0:
                return -1

            if left == right and input_list[left] != query:
                return -1

            median_ind = (left + right) // 2
            if input_list[median_ind] == query:
                return median_ind
            elif input_list[median_ind] > query:
                return binary_search(input_list, left, median_ind, query)
            else:
                return binary_search(input_list, median_ind + 1, right, query)

        return binary_search(input_list, 0, len(input_list) - 1, query)
