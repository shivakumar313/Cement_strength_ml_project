from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from cementmlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 




@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            
            #  reading the inputs given by the user
            cement =float(request.form['cement'])
            blast_furnace_slag =float(request.form['blast_furnace_slag'])
            fly_ash =float(request.form['fly_ash'])
            water =float(request.form['water'])
            superplasticizer =float(request.form['superplasticizer'])
            coarse_aggregate =float(request.form['coarse_aggregate'])
            fine_aggregate =float(request.form['fine_aggregate'])
            age =float(request.form['age'])
            
    
         
            data = [cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]
            data = np.array(data).reshape(1, 8)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)