class TableFormatter:

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()


class TablePrinter(object):
    def __init__(self, formatter):
        self.formatter = formatter

    def print_table(self, objects, colnames):
        self.formatter.headings(colnames)
        for obj in objects:
            rowdata = [str(getattr(obj,colname)) for colname in colnames]
            self.formatter.row(rowdata)

