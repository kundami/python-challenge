
# coding: utf-8

# In[140]:

import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import matplotlib.pyplot as plt


# In[141]:

got_bb_biod_data = pd.read_csv("Resources/Belly_Button_Biodiversity_Metadata.csv")
got_bb_biod_data.head(5)
unique_sample_ids = got_bb_biod_data.SAMPLEID.unique()
unique_sample_ids
got_bb_biod_data.head(5)


#  BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940


# In[ ]:




# In[142]:

got_otu_data = pd.read_csv("Resources/belly_button_biodiversity_otu_id.csv")
got_otu_data.head(5)
unique_otu_desc = got_otu_data.lowest_taxonomic_unit_found.unique()
#unique_otu_desc


# In[143]:

got_bb_samples = pd.read_csv("Resources/belly_button_biodiversity_samples.csv")
got_bb_samples.head(5)


# In[144]:

sample="BB_940"
got_bb_samples.sort_values(by=sample,ascending=False, inplace=True)
sample_otus = got_bb_samples["otu_id"].values
sample_values = got_bb_samples[sample].values
sample_otus


# In[145]:

got_meta_data = pd.read_csv("Resources/metadata_columns.csv")
got_meta_data.head(5)


# In[146]:

app = Flask(__name__)

@app.route('/')
def index():
    #hard coding for noe..
    return render_template('index.html', belly_bacteria_names = json.dumps(unique_sample_ids.tolist()) )


# In[147]:

@app.route('/names')
def get_names():
    return json.dumps(unique_sample_ids.tolist())


# In[148]:

get_names()


# In[ ]:




# In[149]:

@app.route('/otu')
def get_otu():
    return json.dumps(unique_otu_desc.tolist())


# In[150]:

get_otu()


# #### Args: Sample in the format: `BB_940`
# ######    Returns a json dictionary of sample metadata in the format
#     {
#         AGE: 24,
#         BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940
#     }

# In[151]:

@app.route('/metadata/<sample>')
def get_sample(sample):
    sample_data = {}
    sample_data["SAMPLEID"] = got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['AGE'].values[0] 
    sample_data["BBTYPE"] = got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['BBTYPE'].values[0]
    sample_data["ETHNICITY"] = got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['ETHNICITY'].values[0]
    sample_data["GENDER"] = got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['GENDER'].values[0]
    sample_data["LOCATION"] = got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['LOCATION'].values[0]
    return  json.dumps(sample_data)


# In[152]:

get_sample(940)
#got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == 940 ]['AGE'].values[0]


# In[ ]:




# @app.route('/wfreq/<sample>')
#     """Weekly Washing Frequency as a number.
# 
#     Args: Sample in the format: `BB_940`
# 
#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """

# In[153]:

@app.route('/wfreq/<sample>')
def get_weekly_wash_freq(sample):
    return json.dumps(got_bb_biod_data.loc[got_bb_biod_data.SAMPLEID == int(sample) ]['WFREQ'].values[0] )


# In[154]:

get_weekly_wash_freq(940)


# @app.route('/samples/<sample>')
#     """OTU IDs and Sample Values for a given sample.
# 
#     Sort your Pandas DataFrame (OTU ID and Sample Value)
#     in Descending Order by Sample Value
# 
#     Return a list of dictionaries containing sorted lists  for `otu_ids`
#     and `sample_values`
# 
#     [
#         {
#             otu_ids: [
#                 1166,
#                 2858,
#                 481,
#                 ...
#             ],
#             sample_values: [
#                 163,
#                 126,
#                 113,
#                 ...
#             ]
#         }
#     ]

# In[155]:

@app.route('/samples/<sample>')
def get_sorted_samples(sample):
    result_set = {} 
    got_bb_samples.sort_values(by=sample,ascending=False, inplace=True)
    result_set["otu_ids"] = got_bb_samples["otu_id"].values.tolist()
    result_set["sample_value"] = got_bb_samples[sample].values.tolist()
    return json.dumps(result_set)


# In[157]:

get_sorted_samples("BB_940")


# In[158]:

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




# In[ ]:



