import pandas as pd
import os
from openpyxl import load_workbook
import os

def create_excelsheet_orread(file_name,sheet_name):
    if os.path.exists(file_name):
        #print("create_excelsheet_orread")
        sheet_names_list = pd.ExcelFile(file_name).sheet_names
        #print(sheet_names_list)
        if sheet_name not in sheet_names_list:
            #print("No sheet name")
            data_head = [{'nick_name':'','emp_code':'','dept_origin':'','deptL_class':'','semL':'','L_code':'',"L_hr":'',
                'deptT_class':'','semT':'','T_code':'',"T_hr":'','deptP_class':'','semP':'','P_code':'',"P_hr":'',
                'deptR_class':'','semR':'','R_code':'',"R_hr":''}]
            df_init = pd.DataFrame(data_head)
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
                df_init.to_excel(writer,sheet_name=sheet_name,index=False,engine = "openpyxl")
            df = pd.read_excel(file_name,sheet_name=sheet_name,engine="openpyxl")
            return(df)
        else:
            #print("Sheet name in list")  
            df = pd.read_excel(file_name,sheet_name=sheet_name,engine="openpyxl")
            return(df)
    else:
        #print("Created new file with Sheet name")
        data_head = [{'nick_name':'','emp_code':'','dept_origin':'','deptL_class':'','semL':'','L_code':'',"L_hr":'',
            'deptT_class':'','semT':'','T_code':'',"T_hr":'','deptP_class':'','semP':'','P_code':'',"P_hr":'',
            'deptR_class':'','semR':'','R_code':'',"R_hr":''}]
        df_init = pd.DataFrame(data_head)
        df_init.to_excel(file_name,sheet_name,index=False,engine = "openpyxl")
        df = pd.read_excel(file_name,sheet_name=sheet_name,engine="openpyxl")
        return(df)
def update_excel():
    pass
sheet_name = "CE"
df_sel = create_excelsheet_orread('output_data.xlsx',sheet_name)
print(df_sel)
faculty_name ="ELI"
code_val = "C102"
if faculty_name in list(df_sel.nick_name):
    index_new = list(df_sel.nick_name).index(faculty_name)
    new_val = 'C101'
    my_val = f"{df_sel.at[index_new,"L_code"]},{new_val}"
    df_sel.loc[index_new,"L_code"] = my_val
    #df_sel.to_excel('output_data.xlsx',sheet_name,index=False,engine="openpyxl")
    print(my_val)
else:
    new_record = pd.DataFrame([{'nick_name':faculty_name,'L_code':code_val,"L_hr":1,}])
    df_sel = pd.concat([df_sel,new_record],ignore_index=True)    
    df_sel.to_excel('output_data.xlsx',sheet_name,index=False,engine="openpyxl")
    print(df_sel)
read_val = df_sel.at[index_new,"L_code"]
read_val_lst = read_val.split(",")
print(read_val_lst[0])
