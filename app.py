# # Dependencies
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)

from sklearn.externals import joblib

#################################################
# Flask Setup
#################################################
app = Flask(
    __name__, 
    template_folder='templates',
    static_url_path='/static',
)
model = None 

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/BC_diagnosis.db"
# Create DB object to pass Flask app to it - SQLAlchemy object that can be used in Flask
#db = SQLAlchemy(app)
#Create route that renders index.html template
@app.route("/", methods = ['GET'])
def index():
    active_tab = "index"
    return render_template("index.html", active = active_tab)

# Query the database and send the jsonified results
@app.route('/start-over')
def startover():
	return redirect("/", code=302)


@app.route('/get-patient-data', methods=['POST'])
def make_predict():
    global model
    global radius_mean, perimeter_mean, area_mean, concavity_mean
    global concave_points_mean, radius_worst, perimeter_worst 
    global area_worst, concavity_worst, concave_points_worst

    if request.method == 'POST':
        model = joblib.load('predict_cancer_type.pkl')

        print('-----line 27--------')
        print(request.form.get('radius_mean'))
        #if radius_mean is not None:
        radius_mean = float(request.form.get('radius_mean'))
        #print(radius_mean)

        #if perimeter_mean is not None:
        perimeter_mean = float(request.form.get('perimeter_mean'))
        #if area_mean is not None:
        area_mean  = float(request.form.get('area_mean'))
        #if concavity_mean is not None:
        concavity_mean  = float(request.form.get('concavity_mean'))
        #if concave_points_mean is not None:
        concave_points_mean = float(request.form.get('concave_points_mean'))
        #if radius_worst is not None:
        radius_worst  = float(request.form.get('radius_worst'))
        #if perimeter_worst is not None:
        perimeter_worst  = float(request.form.get('perimeter_worst'))
        #if area_worst is not None:
        area_worst  = float(request.form.get('area_worst'))
        #if concavity_worst is not None:
        concavity_worst  = float(request.form.get('concavity_worst'))
        #if concave_points_worst is not None:
        concave_points_worst  = float(request.form.get('concave_points_worst'))
        
        diagnosis_features= [
        radius_mean, #radius_mean                                 
		perimeter_mean, #perimeter_mean                                      
		area_mean, #area_mean 
		concavity_mean, #concavity_mean 
        concave_points_mean, #concave points_mean 
        radius_worst, #radius_worst 
        perimeter_worst , #perimeter_worst
        area_worst , #area_worst 
        concavity_worst, #concavity_worst 
        concave_points_worst, #concave points_worst                                   
        ]
        #diagnosis_features= [diagnosis_features]
        diagnosis = model.predict([diagnosis_features])
            
        print(diagnosis)
    
        if diagnosis==0:
            cancer = 'Benign'

        elif diagnosis==1:
            cancer = 'Malignant'
        print("The breast cancer of this patient should be: %s" % (cancer,) )

        return render_template('model.html', diagnosis = cancer )


if __name__ == '__main__':
	app.run(debug=True)