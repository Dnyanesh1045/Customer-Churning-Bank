from flask import Flask,render_template,request
import pickle
import numpy as np
#from flask_cors import cross_origin
import sklearn

model = pickle.load(open('best_RF_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
#@cross_origin()
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
#@cross_origin()
def predict():
    if request.method == "POST":

        CreditScore = eval(request.form.get('CreditScore'))

        Age = eval(request.form.get('Age'))

        Balance = eval(request.form.get('Balance'))

        NumOfProducts = eval(request.form.get('NumOfProducts'))

        HasCrCard = eval(request.form.get('HasCrCard'))

        Tenure = eval(request.form.get('Tenure'))

        IsActiveMember = eval(request.form.get('IsActiveMember'))

        EstimatedSalary = eval(request.form.get('EstimatedSalary'))

        # Geography
        Geography = request.form["Geography"]
        # if (Geography == 'Geography_France'):
        #     France = 1
        #     Spain = 0
        #     Germany = 0

        # elif (Geography == 'Geography_Spain'):
        #     France = 0
        #     Spain = 1
        #     Germany = 0

        # elif (Geography == 'Geography_Germany'):
        #     France = 0
        #     Spain = 0
        #     Germany = 1

        if (Geography == 'France'):
            Geography_France = 1
            Geography_Spain = 0
            Geography_Germany = 0

        elif (Geography == 'Spain'):
            Geography_France = 0
            Geography_Spain = 1
            Geography_Germany = 0

        elif (Geography == 'Germany'):
            Geography_France = 0
            Geography_Spain = 0
            Geography_Germany = 1


        # Gender
        Gender = request.form["Gender"]
        if (Gender == 'Male'):
            Gender = 1

        else:
            Gender=1
    
        

    # prediction
    result = model.predict([[CreditScore,Geography_France,Geography_Spain,Geography_Germany,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    if result == 1:
        result = 'Exited'
    else:
        result = 'Not Exited'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

print(__name__)
