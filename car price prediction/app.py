from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')

def home():
    selling_price = ' '
    return render_template('home.html', **locals())

@app.route('/predict', methods=[ 'POST', 'GET'])
def predict():
    Car_Name = 	float(request.form['Car_Name'])
    Year = float(request.form['Year'])		
    Present_Price = float(request.form['Present_Price'])	
    Kms_Driven = float(request.form['Kms_Driven'])	
    Fuel_Type = float(request.form['Fuel_Type'])	
    Seller_Type = float(request.form['Seller_Type'])
    Transmission = float(request.form['Transmission'])	
    Owner = float(request.form['Owner'])
    selling_price = model.predict([[Car_Name,Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    return render_template('home.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
    