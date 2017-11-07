
# coding: utf-8

# In[3]:

from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mission_to_mars


# In[ ]:

app = Flask(__name__)
mongo = PyMongo(app)
@app.route('/')
def index():
    mars_facts = mission_to_mars.read_from_mongodb("mars_facts")
    return render_template('index.html', mars_facts=mars_facts)


@app.route('/scrape')
def scrape():
    mission_to_mars.all_about_mars()
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

