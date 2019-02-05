class Contact:

    def __init__(self, name, surname, telephone, *args, favourite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.additional = args
        self.favourite = favourite
        self.more = kwargs
        if self.favourite is False:
            self.favourite_status = 'нет'
        else:
            self.favourite_status = 'да'

    def __str__(self):
        self.printable = str(
            'Имя: ' + self.name + '\n' +
            'Фамилия: ' + self.surname + '\n' +
            'Телефон: ' + self.telephone + '\n' +
            'В избранных: ' + self.favourite_status + '\n'
        )
        if self.additional:
            for additional_number in self.additional:
                self.printable += str('Дополнительный номер: ' + additional_number + '\n')
        if self.more:
            self.printable += str('Дополнительная информация: ' + '\n')
            for key in self.more.keys():
                self.printable += str('\t\t' + key + ': ' + self.more[key] + '\n')
        return self.printable
