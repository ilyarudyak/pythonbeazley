import sys


class TableFormatter:

    def __init__(self, outfile=sys.stdout):
        self.outfile = outfile

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):

    def __init__(self, outfile=sys.stdout, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


def print_table(objects, colnames, formatter):
    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj,colname)) for colname in colnames]
        formatter.row(rowdata)

class QuotedTextTableFormatter(TextTableFormatter):
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class QuotedMixin(object):
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class QuotedTextFormatter(QuotedMixin, TextTableFormatter):
    pass


class QuotedCSVFormatter(QuotedMixin, CSVTableFormatter):
    pass    
















