from flask import Flask, request, render_template
import joblib
file_path = r"C:\Users\minyi.LAPTOP-TSJ2HKRC\OneDrive - T-RECs.ai Pte. Ltd\ntu mod2"

app = Flask(__name__) #__xx__

#which directory is file in
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST": #when user press 'Enter' in front end
        num = request.form.get("rates")
        #print(num)
        model = joblib.load('{0}\DBS_regression'.format(file_path))
        pred = model.predict([[float(num)]])
        #print(pred)
        s = "Predicted DBS Share Price : " + str(pred)
        #print(s)
        return(render_template("index.html", results=s))

    else: #before user press 'Enter' in front end
        return(render_template("index.html", results="DBS Share Price Prediction"))


if __name__ == "__main__": #need this to run in cloud environment, to verify that code is mine
    app.run()
    

