import reader


def read_portfolio(filename):
    types = [str, str, int, float]
    return reader.read_csv(filename, types)