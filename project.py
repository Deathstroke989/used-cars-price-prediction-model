from wsgiref.handlers import BaseCGIHandler

import pandas as pd
from sqlalchemy.dialects.mssql.information_schema import columns

a=pd.read_csv("d:/car2.csv")
print(a.head)
print(a.isnull().sum())
a.dropna(axis=0,inplace=True)
print(a.isnull().sum())
print(a.shape)
print(a.columns)
a['AskPrice']=a['AskPrice'].apply(lambda x: x.split(' ')[-1].replace(",",'')).astype(int)


a["kmDriven"]=a["kmDriven"].apply(lambda x:x.split(" ")[0])
a["kmDriven"]=a["kmDriven"].apply(lambda  x:x.replace(",",'')).astype(float)
a["kmDriven"]=a["kmDriven"].astype(int)
# print(a.info())
a.drop(columns=['PostedDate', 'AdditionInfo'],inplace=True)
print(a.head())
from sklearn.preprocessing._label import LabelEncoder
b=LabelEncoder()
label_mapping=[]
c=['Brand', 'model','Transmission', 'Owner','FuelType']
for i in c:
    a[i]=b.fit_transform(a[i])
    label_mapping.append(dict(zip(b.classes_, range(len(b.classes_)))))
print("Label mapping:", len(label_mapping))
print(label_mapping[0])

print(a.head())


from sklearn.ensemble import RandomForestRegressor
B=RandomForestRegressor()

from sklearn.model_selection import train_test_split
x=a[['Brand','model','Year','Age','kmDriven','Transmission','Owner','FuelType']]
y=a['AskPrice']
xtn,xtst,ytrn,ytst=train_test_split(x,y,train_size=0.8,random_state=123)

B.fit(xtn,ytrn)




print(f"random {B.score(xtst,ytst)}")



import streamlit as st
import streamlit as st
st.set_page_config(layout="wide")
# Set the URL of your background image
image_url = "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"  # Replace with your image URL

# Inject CSS to set the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.header("Car Price Prediction")
st.subheader("Enter the data:")
st.markdown("Provide numerical inputs based on the label mappings below:")



# st.text_input("enter thse age of vehicle")
# st.text_input("kmdriven")
col1, col2, col3,col4,col5 = st.columns(5)

# Display DataFrames in each column
with col1:
    st.header("brand")
    st.dataframe(label_mapping[0])

with col2:
    st.header("model")
    st.dataframe(label_mapping[1],width=200,height=200)

with col3:
    st.header("transmission")
    st.dataframe(label_mapping[2],width=200,height=200)

with col4:
    st.header("owner")
    st.dataframe(label_mapping[3],width=200,height=200)
with col5:
    st.header("fuel type")
    st.dataframe(label_mapping[4],width=200,height=200)



j = []
j.append(int(st.number_input("Brand Value")))
j.append(int(st.number_input("Model Value")))
j.append(int(st.number_input("year Value")))
j.append(int(st.number_input("age Value")))
j.append(int(st.number_input("kmDriven")))
j.append(int(st.number_input("transmission")))
j.append(int(st.number_input("Owner Value")))
j.append(int(st.number_input("fuel type")))

if st.button("Predict Price"):
    d = B.predict([j])
    st.write(d) # Check before printing
    st.text(f"Predicted Price: {d[0]}")

