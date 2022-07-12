
import numpy as np
from flask import Flask, request, render_template
import json
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)

    if output == 0:
        return render_template('index.html', prediction_text='Kondisi Sungai Citarum Aman')
    elif output == 1:
        return render_template('index.html', prediction_text='Kondisi Sungai Citarum Siaga 1')
    elif output == 2:
        return render_template('index.html', prediction_text='Kondisi Sungai Citarum Siaga 2')

if __name__ == '__main__':
    app.run(debug=True)