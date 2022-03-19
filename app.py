#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS_regression")
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "The predicted DBS share price is " + str(pred[0][0])
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="No Input"))


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:





# In[ ]:
