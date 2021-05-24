import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..."))
Data_File = "../TestData/Repository.xlsx"
Exl = pd.ExcelFile(Data_File)

sheet_Names = []
sheet_Names = Exl.sheet_names
#print(sheet_Names)
getProperty = {}
columnNames = []
ExlKey = []
ExlValue = []

for sheet in sheet_Names:
    df = pd.read_excel(Data_File, sheet_name=sheet)
    columnNames = list(df.columns)
    #print(columnNames)
    length = len(df)
    for i in range(length):
        assert df[columnNames[0]].loc[i] not in ExlKey, "Key is duplicated,Please check the Excel sheet with this key :"+df[columnNames[0]].loc[i]
        ExlKey.append(df[columnNames[0]].loc[i])
        ExlValue.append(df[columnNames[1]].loc[i])

getProperty = dict(zip(ExlKey, ExlValue))












"""
#Read the entire Excel sheet 
SheetNames=[]
SheetNames=Exl.sheet_names                 #Reading all the sheets names adding it in the empty list
#print(SheetNames)
getcolValue=[]
AllData={}
for sheet in SheetNames:
    df=pd.read_excel(Data_File,sheet_name =sheet)       #Reading the excel file based on the sheet
    #print(df)
    colname=list(df.columns)
    #print(colname)
    for i in colname:
        getcolValue.append(df[i][0])                    #Here i'm read the value under the perticular column so 'm hardcoded the indexing value 
        Datafile=dict(zip(colname, getcolValue))        #Here zipping the two list and converting into dictionary so i can get any value refering the key 
        #print(Datafile)
    AllData.update(Datafile)                            # Here i'm extending the dictionary after completion of one loop (main)
    Datafile.clear()                                        
    colname.clear()
    getcolValue.clear()


#print(AllData)
























getcolValue=[]
def GetTheValueFromDataFile(Value):
    for sheet in SheetNames:
        df=pd.read_excel(Data_File,sheet_name =sheet)
        #print(df)
        colname=list(df.columns)
        print(colname)

        for i in colname:
            getcolValue.append(df[i][0])
        print(getcolValue)



        Datafile=dict(zip(colname, getcolValue))
        print(Datafile)
        DataValue=Datafile.get(Value)
        print(DataValue)
        return DataValue
GetTheValueFromDataFile('er')
#######
def get():
    print()
    print(GetTheValueFromDataFile("URL"))


get()
"""

"""
import pandas as pd
import getpass  # Get The User Name of the system
UserName = getpass.getuser()
Data_File = "C:\\Users\\"+UserName+"\\Desktop\\HTAA\\TestData\\Repository.xlsx"
Exl = pd.ExcelFile(Data_File)  # Read the entire Excel sheet
SheetNames = []
SheetNames = Exl.sheet_names  # Reading all the sheets names adding it in the empty list
# print(SheetNames)
getcolValue = []
AllTestData = {}
for sheet in SheetNames:
    df = pd.read_excel(Data_File, sheet_name=sheet)  # Reading the excel file based on the sheet
    # print(df)
    colname = list(df.columns)
    # print(colname)
    for i in colname:
        getcolValue.append(
            df[i][0])  # Here i'm read the value under the perticular column so 'm hardcoded the indexing value
        Datafile = dict(zip(colname,
                            getcolValue))  # Here zipping the two list and converting into dictionary so i can get any value refering the key
        # print(Datafile)
    AllTestData.update(Datafile)  # Here i'm extending the dictionary after completion of one loop (main)
    Datafile.clear()
    colname.clear()
    getcolValue.clear()

"""