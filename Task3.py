class Worker:

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):

        self.name = name
        self.surname = surname
        self.position = position

        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):

        return ' '.join(sorted([self.name, self.surname]))

    def get_total_income(self):

        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Василий',
            'surname': 'Пупкин',
            'position': 'Баянист',
            'wage':  40000,
            'bonus': 20000
        },
        {
            'name': 'Инокентий',
            'surname': 'Смоктуновский',
            'position': 'Разработчик',
            'wage':  90000,
            'bonus': 60000
        },
        {
            'name': 'Иван',
            'surname': 'Царевич',
            'position': 'Сказочный персонаж',
            'wage':  60000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('Полное имя: ', position.get_full_name())
        print('Должность: ', position.position)
        print('Итоговый доход: ', position.get_total_income())
        print('\n')
