from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')

def home():
    result = ' '
    return render_template('home.html', **locals())




@app.route('/predict', methods=[ 'POST', 'GET'])
def predict():
    PassengerId	= float(request.form['PassengerId'])
    Survived = float(request.form['Survived'])
    Pclass = float(request.form['Pclass'])
    Name = 	float(request.form['Name'])
    Sex	= float(request.form['Sex'])
    Age	= float(request.form['Age'])
    SibSp =	float(request.form['SibSp'])
    Parch = float(request.form['Parch'])
    Ticket = float(request.form['Ticket'])
    Fare =	float(request.form['Fare'])
    Embarked = float(request.form['Embarked'])
    result = model.predict([[PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Embarked]])
    return render_template('home.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)