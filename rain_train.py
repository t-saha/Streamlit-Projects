import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

train = pd.read_csv("/Users/titassaha/code/python/rainfall_kaggle/train.csv")
train.drop(columns = 'id', inplace=True)
train= train.rename(columns = {'temparature' : 'temperature'})

features = ['pressure','temperature','humidity','cloud','sunshine','winddirection','windspeed']
X = train[features]
y = train['rainfall']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'rain_model.pkl') 


      
        
         
          
         
           

  