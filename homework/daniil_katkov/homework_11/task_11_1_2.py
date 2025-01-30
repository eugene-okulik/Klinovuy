class Book:
    material_stranic = 'бумага'
    nalichie_teksta = 'Да'
    rezerv = False
    def __init__(self, nazvanie_knigi, avtor, kolichestvo_stranic, isbn):
        self.nazvanie_knigi = nazvanie_knigi
        self.avtor = avtor
        self.kolichestvo_stranic = kolichestvo_stranic
        self.isbn = isbn

book_1 = Book('Идиот', 'Достоевский',500, '978-5-17-118366-5')
book_2 = Book('Преступление и наказание', 'Достоевский',364, '978-5-17-118274-3')
book_3 = Book('Выбор', 'Эдит Ева Эгер',609, '978-5-17-118291-4')
book_3.rezerv = True
book_4 = Book('Мемуары', 'Карл Густав Маннергейм',1003, '978-5-17-118537-5')
book_5 = Book('Дети кукурузы', 'Стивен Кинг',154, '978-5-17-118476-2')


def print_book(number_book):
    if number_book.rezerv is True:
        print(f'Название: {number_book.nazvanie_knigi}, Автор: {number_book.avtor}, '
              f'страниц: {number_book.kolichestvo_stranic}, материал: {number_book.material_stranic}, зарезервирована')
    else:
        print(f'Название: {number_book.nazvanie_knigi}, Автор: {number_book.avtor}, '
              f'страниц: {number_book.kolichestvo_stranic}, материал: {number_book.material_stranic}')


print_book(book_3)

#######################################################################################################################


class SchoolBooks(Book):
    def __init__(self, nazvanie_knigi, avtor, kolichestvo_stranic, isbn, predmet, klass, tasks):
        super().__init__(nazvanie_knigi, avtor, kolichestvo_stranic, isbn)
        self.predmet = predmet
        self.klass = klass
        self.tasks = tasks


school_book_1 = SchoolBooks('Алгебра', 'Иванов', '200', '978-5-17-118876-2',
                            'Математика', 9, 'Да')
school_book_1.rezerv = True
school_book_2 = SchoolBooks('Геометрия', 'Сергеев', '180', '978-5-17-118647-3',
                            'Математика', 10, 'Да')
school_book_3 = SchoolBooks('Физика', 'Антонова', '195', '978-5-17-118654-4',
                            'Физика', 8, 'Нет')


def school_book(books):
    if books.rezerv is True:
        print(f'Название: {books.nazvanie_knigi}, Автор: {books.avtor}, '
              f'страниц: {books.kolichestvo_stranic}, предмет: {books.predmet}, класс: {books.klass}, зарезервирована')
    else:
        print(f'Название: {books.nazvanie_knigi}, Автор: {books.avtor}, '
              f'страниц: {books.kolichestvo_stranic}, предмет: {books.predmet}, класс: {books.klass}')


school_book(school_book_1)
