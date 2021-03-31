import pickle
import streamlit as st

import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()
# loading the trained model
tfid= pickle.load(open('Tfidfmodels.pkl','rb'))
model=pickle.load(open('save.pkl','rb'))

data= pd.read_csv('https://raw.githubusercontent.com/makantr17/link_prediction/main/cleanDoc.csv')
@st.cache()

  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(pred): 
    if pred == 0:
        pred = 'Sport'
    elif prediction == 1:
        pred = 'Culture'
    elif prediction == 2:
        pred = 'Economy'
    else:
        pred = 'Politic'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:orange;padding:20px;font-weight:15px"> 
    <h1 style ="color:black;text-align:center;">Content Based Recommendation</h1> 
    </div> 
    """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    default_value_goes_here = ""
    Content = st.text_area("label goes here", default_value_goes_here)
    result =""
    
    
    # Display links
    data= pd.read_csv('https://raw.githubusercontent.com/makantr17/link_prediction/main/cleanDoc.csv')
    data["label"] = label_enc.fit_transform(data[["label"]])  
      # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
      pred = model.predict(tfid.transform([Content]))
      if pred==3:
        st.write('Culture')
        pred= int(pred)
        data_pred = data.loc[(data['label'] == pred)]
        data_pre = data_pred.loc[data_pred['site_url'].str.contains('culture', regex=True)]
        st.dataframe(data_pre['site_url'].unique())
      elif pred==2:
        st.write('business')
        pred= int(pred)
        data_pred = data.loc[(data['label'] == pred)]
        data_pre = data_pred.loc[data_pred['site_url'].str.contains('business', regex=True)]
        st.dataframe(data_pre['site_url'].unique())
      elif pred==0:
        st.write('politics') 
        pred= int(pred)
        data_pred = data.loc[(data['label'] == pred)]
        data_pre = data_pred.loc[data_pred['site_url'].str.contains('politic', regex=True)]
        st.dataframe(data_pre['site_url'].unique())
      elif pred==1:
        st.write('sport')
        pred= int(pred)
        data_pred = data.loc[(data['label'] == pred)]
        data_pre = data_pred.loc[data_pred['site_url'].str.contains('sport', regex=True)]
        st.dataframe(data_pre['site_url'].unique())
     
if __name__=='__main__': 
    main()
