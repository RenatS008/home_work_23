def filter_query(param, data):
    """
    Для фильтровации строки входных данных.
    """
    return list(filter(lambda x: param in x, data))


def map_query(param, data):
    """
    Изменяем формат исходных данных (проекция).
    В качестве аргумента <col> команда map принимает номер колонки.
    """
    transform_colum = int(param)
    return list(map(lambda x: x.split(' ')[transform_colum], data))


def unique_query(data, *args, **kwargs):
    """
    Оставляет только уникальные значения
    """
    return list(set(data))


def sort_query(param, data):
    """
    Сортирует данные в алфавитном порядке или в обратном алфавитном порядке,
    в зависимости от переданного аргумента.

    """
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    """
    Выводим только указанный лимит
    """
    limit = int(param)
    return list(data)[:limit]
