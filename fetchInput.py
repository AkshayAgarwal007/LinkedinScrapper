import xlrd


def fetch(fileName):
    searchList= []
    names= []
    sh = xlrd.open_workbook(fileName).sheet_by_index(0)
    for rownum in range(1,sh.nrows):
        tmp = u' '.join((sh.cell(rownum, 2).value,sh.cell(rownum, 1).value)).encode('utf-8').strip()
        name = u' '.join((sh.cell(rownum, 3).value,sh.cell(rownum, 5).value)).encode('utf-8').strip()
        searchList.append(tmp)
        names.append(name)
    return searchList, names

### return [u' '.join((sh.cell(rownum, 2).value,sh.cell(rownum, 1).value)).encode('utf-8').strip() +'linkedin' for rownum in range(1,sh.nrows)]