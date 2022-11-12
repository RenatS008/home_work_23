import functions

CMD_TO_FUNCTION = {
    'filter': functions.filter_query,
    'map': functions.filter_query,
    'unique': functions.filter_query,
    'sort': functions.filter_query,
    'limit': functions.filter_query,
}
FILE_NAME = 'data/apache_logs.txt'


def search_query(cmd, param, data):
    if data is None:
        with open(FILE_NAME) as f:
            prepared_data = list(map(lambda x: x.split(), f))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
