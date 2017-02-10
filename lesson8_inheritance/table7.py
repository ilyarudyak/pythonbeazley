from abc import ABC, abstractmethod

class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod    
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()


class CSVTableFormatter(object):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

def print_table(objects, colnames, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('wrong formatter')

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj,colname)) for colname in colnames]
        formatter.row(rowdata)