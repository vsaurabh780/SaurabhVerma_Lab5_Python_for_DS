import numpy as np
import sklearn
from flask import Flask, request, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@app.route('/',methods=['GET']) # Homepage
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
      Present_Price  = float(request.form['Present_Price'])
      Kms_Driven  = int(request.form['Kms_Driven'])
      Owner = int(request.form['Owner'])
      Age_of_the_car = int(request.form['Age_of_the_car'])
      Fuel_Type = request.form['Fuel_Type']
      Seller_Type = request.form['Seller_Type']
      Transmission = request.form['Transmission']

      prediction = model.predict([[Present_Price, Kms_Driven, Owner, Age_of_the_car, Fuel_Type, Seller_Type, Transmission]])
      output = round(prediction[0], 2)
      return render_template('index.html', prediction_text='You can sell your car for {} lakhs'.format(output))

if __name__ == "__main__":
    app.run(debug=True)