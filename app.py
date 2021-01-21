
import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle
import logging

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))
logger = logging.getLogger("app")

FEATURES = ["experience", "test_score", "interview_score"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    extracting features from Web-form (request.form)
    For rendering results on HTML GUI
    '''
    
    X = [[int(x) for x in request.form.values()]]
    prediction = model.predict(X)    
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Employee Salary should be $ {output}')


@app.route('/api/v1/predict',methods=['GET'])
def api_predict():
    """
    extracting features from request.args

    OK:
        http://127.0.0.1:5000//api/v1/predict?experience=5&interview_score=8&test_score=6
    ERROR:        
        http://127.0.0.1:5000//api/v1/predict?experience=5&interviewscore=8&english_score=6
    """
    
    args = request.args
    
    missing_features = np.setdiff1d(FEATURES, list(args.keys()))
    if len(missing_features):
        msg  = f"{missing_features} feature is missing"
        logger.error(msg)
        return jsonify({"status": 409, "error": msg})
            
    X = [[int(args.get(key)) for key in FEATURES]]
    prediction = model.predict(X)    
    output = round(prediction[0], 2)

    return jsonify({"status": 200, "salary": output})


if __name__ == "__main__":
    app.run()
