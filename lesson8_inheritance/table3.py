class TableFormatter:

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


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