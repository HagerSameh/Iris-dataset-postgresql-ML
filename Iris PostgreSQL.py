import pandas as pd
import pickle
import numpy as np
import sqlalchemy as db

 
con = db.create_engine('postgresql://iti:iti@localhost/DM')
con.table_names() 

model = pickle.load(open('/home/hager/Desktop/Python_Round2/model.pkl', 'rb'))

sepal_length = input("Please Enter sepal_length: ")
sepal_width = input("Please Enter sepal_width: ")
petal_length = input("Please Enter petal_length: ")
petal_width = input("Please Enter petal_width: ") 

data=[[sepal_length,sepal_width,petal_length,petal_width]]
df = pd.DataFrame(data, columns = ['sepal_length','sepal_width','petal_length','petal_width']) 

df['Predicted_Species'] = model.predict(df) 

df.to_sql(name ='iris',con=con,schema = 'public',if_exists='append',index=False)    

