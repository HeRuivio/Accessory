import codecs
import xlrd
import copy
import xlwt
from xlwt import Style
import xlutils.copy
import random
Address=r'C:\HeRui\MathModel\TaskOne\Modle.xls'
def excel_style(fileaddress,num):
    workbook=xlrd.open_workbook(Address,formatting_info=True)
    table=workbook.sheet_by_name('Sheet1')
    col=[1,3,5]
    F=[]
    for i in col:
        list=table.col_values(i)[1:]
        list=list[:-1]
        F=F+list
    Tem=copy.deepcopy(F)#��tem��������
    Ord=[] #���ݴӴ�С���򣬷������ݵ����� 
    Tem.sort(reverse=True)
    for i in range (0,num):
        for n in range(0,len(F)):
            if Tem[i]==F[n]:
                Ord.append(n)
                continue
    Resu=[x+1 for x in Ord]
    coordinate=[]
    tem=[]
    for i in Resu:
        col=i/17*2+1
        tem.append(col)
        row=i%17
        tem.append(row)
        coordinate.append(tem)
        tem=[]
    #  �õ����ݵ�����
    writebook=xlutils.copy.copy(workbook)
    writesheet=writebook.get_sheet(0)
    t=1
    for i in coordinate:
        writesheet.write(i[1],i[0]+1,t+3)
        t=t+1
    writebook.save(fileaddress)
excel_style(Address,17)