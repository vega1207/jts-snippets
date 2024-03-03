import re,json

with open("jabiltest_chm.txt", "r", encoding='utf-8') as f:
    data = f.read()

# Find Usage: counts
pattern = r'Usage:([\s\S]*)Description:'# Find all matches
matches = re.findall(pattern, data)
# print("matches:",matches)

# Get the count
num_matches = len(matches)

for i in range(num_matches):
     
    w1  =  'Usage:'
    w2  =  'Description:'
    w3  =  'Example:'
    w4  =  '\* * *'

    #清除换行符,请取消下一行注释
    buff = data.replace('\n','')
    pat  =  re. compile (w1 + '(.*?)' + w2,re.S)
    Variable_Expression  =  pat.findall(buff)

    pat  =  re.compile (w2 + '(.*?)' + w4,re.S)
    Variable_Example_List  =  pat.findall(data)
    # print(Variable_Example_List)
    
    for variable_str,description_str in zip(Variable_Expression,Variable_Example_List):
        # print(variable_str)
        # print(description_str)
        
        # Get variable name
        if(";" not in variable_str):
            variable_str = variable_str + ";"
        variable_function_name = variable_str
        # print(variable_function_name)
        if("=" in variable_function_name):
            Variable_Function_Pattern = re.compile(r'\=(.*)(\()')
            # Variable_Function_Pattern = re.compile(r'[\= |\=| \= ](.*)(\()')
            variable_function_str = Variable_Function_Pattern.findall(variable_function_name)
        else:
            Variable_Function_Pattern = re.compile(r'(.*)(\()')
            variable_function_str = Variable_Function_Pattern.findall(variable_function_name)
        # print(variable_function_str)
        # print(variable_function_str[0][0])
        # print(variable_function_name)
        
        with open(r'snippets\variables.json', 'a') as f:
            d = {'JTS '+ variable_function_str[0][0].replace(' ',''): {'prefix':variable_function_str[0][0].replace(' ',''), 'body':[variable_str.replace(' ','').replace('$','$$')],'description': description_str}}
            json.dump(d, f, indent=num_matches)
        f.close

with open(r"snippets\variables.json", "r", encoding='utf-8') as f:
    data = f.read()
# print(data)

#read
with open(r"snippets\variables.json","r") as f:
    lines=f.readlines() 
    data=[]  
    for i in lines:
    #根据条件修改
        if('}{' in i):
            i=i.replace('}{',',')   
        data.append(i)    
#write
with open(r"snippets\variables.json","w") as f:
    for i in data:
        f.writelines(i)
f.close()

    









