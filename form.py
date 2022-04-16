from email import header
import os
import csv
from prettytable import PrettyTable

# save datas to form from file
class Form:
    def __init__(self,file) -> None:
        self.columnsHeader=[]
        self.rowsHeader=[]
        self.datas=[]
        self.rowFile=file
        self.reserve="raw/column"

    def Check(self)->bool:
        if not os.path.exists(self.rowFile):
            print("%s is not exists"%(self.rowFile))

            return False
        
        return True

    def __getitem__(self,keys: list[str,str]):
        if len(keys)<2 or keys[0]=="" or keys[1]=="":
            return None
        
        try:
            return self.datas[self.rowsHeader.index(keys[0])][self.columnsHeader.index(keys[1])]
        except:
            return None

    # only change memory without write back to file
    def __setitem__(self, keys:list[str,str], value: float) -> bool:
        if len(keys)<2 or keys[0]=="" or keys[1]=="":
            return False
        
        try:
            self.datas[self.rowsHeader.index(keys[0])][self.columnsHeader.index(keys[1])]=value
        except:
            return False

    # get column headers list
    def Columns(self)->list:
        return self.columnsHeader
    
    # get row headers list
    def Rows(self)->list:
        return self.rowsHeader

    # get column count
    def ColumnCount(self)->int:
        return len(self.columnsHeader)

    # get row count
    def RowCount(self)->int:
        return len(self.rowsHeader)

    # print all data
    def Print(self):
        table=PrettyTable([self.reserve]+self.columnsHeader)
        for r in range(len(self.rowsHeader)):
            table.add_row([self.rowsHeader[r]]+self.datas[r])
        print(table)

    def LoadCSV(self):
        with open(self.rowFile, encoding='UTF-8') as f:
            data = csv.reader(f)

            header=next(data)
            if header==None or len(header)<1:
                return
            self.reserve=header[0]
            self.columnsHeader=[s.strip() for s in header[1:]]
            
            for raw in data:
                if raw==None or len(raw)<1:
                    continue

                if len(raw[0])>0:
                    self.rowsHeader.append(raw[0].strip())
                
                new_raw=[]
                for i in raw[1:]:
                    if len(i.strip())<1:
                        new_raw.append(-1)
                    else:
                        new_raw.append(float(i.strip()))
                self.datas.append(new_raw)

        # load data finished, ready to delete blank column

        # find column blank
        delete_column=[]
        for i in range(len(self.columnsHeader)):
            for j in range(len(self.rowsHeader)):
                if self.datas[j][i]<0:
                    # column with blank
                    delete_column.append(i)
                    break

        # delete column
        for i in delete_column[::-1]:
            # delete header
            del self.columnsHeader[i]
            # delete data
            for j in range(len(self.rowsHeader)):   
                del self.datas[j][i]

        # find row blank
        delete_row=[]
        for i in range(len(self.rowsHeader)):
            for j in range(len(self.columnsHeader)):
                if self.datas[i][j]<0:
                    # column with blank
                    delete_row.append(i)
                    break

        # delete column
        for i in delete_row[::-1]:
            # delete header
            del self.rowsHeader[i]
            # delete data 
            del self.datas[i]
        
