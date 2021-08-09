#22.07.2021
#ShchusS

#Зведення всіх таблиць з каталогу в одну. Таблиці повинні мати однакову структуру



#import modules
import pandas as pd
import glob
  
# path of the folder
path = input("Потрібен шлях до каталогу з таблицями: ")
table_out = input("Потрібен шлях збереження таблиці: ")
  
# reading all the excel files
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames)
  
# initializing empty data frame
finalexcelsheet = pd.DataFrame()
  
# to iterate excel file one by one 
# inside the folder
for file in filenames:
  
    # combining multiple excel worksheets
    # into single data frames
    df = pd.concat(pd.read_excel(
      file, sheet_name=None), ignore_index=True, sort=False)
  
    # appending excel files one by one
    finalexcelsheet = finalexcelsheet.append(
      df, ignore_index=True)
  
# to print the combined data
print('Final Sheet:')
display(finalexcelsheet)
  
finalexcelsheet.to_excel(table_out, index=False)