import datetime


def logging(func):
    def write_logs(phone_book_instance):
        date = datetime.datetime.today()
        log_string = f'{date} // {phone_book_instance.name} // {func.__name__}\n'
        with open('log.txt', 'a') as log_file:
            log_file.write(log_string)
        return func(phone_book_instance)
    return write_logs
