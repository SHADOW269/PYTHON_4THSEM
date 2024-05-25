import pandas as pd
data1 = {'rollno':[101,102,103],
        'name':['Eshaan','Dhanush','Deekshith'],
        'Total Marks':[85,90,88]}
data2 = {'rollno':[104,105,106],
         'name':['Vamshith','Naresh','Bhoomika'],
         'Total Marks': [91,87,89]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

result = pd.concat([df1,df2], ignore_index=True)

print("Joined DataFrame:") 
print(result) 