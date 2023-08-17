#!/usr/bin/env python
# coding: utf-8

# In[488]:


from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np


# In[547]:


app = Flask(__name__)

# Load the model from file
#with open('code_model.pkl', 'rb') as f:
    #model = pickle.load(f)


# In[ ]:


@app.route('/predict', methods=['POST'])
def predict():
    print("Hello World")
    #data = request.json
    #milage = data['mileage']
    #model = data['model']
    #make = data['make']
    #fuel = data['fuel']
    #engine = data['engine']
    #age = data['age']
    #data = [[milage,make,model,fuel,engine,age]]
    #df = pd.DataFrame(data, columns=['odometerValue', 'make', 'model', 'fuelType', 'engineSize', 'vehicle_age'])
    
    #probabilities = model.predict_proba(df)
    #sorted_indices = np.argsort(probabilities, axis=1)
    #highest_prob_index = sorted_indices[:, -1]
    #second_highest_prob_index = sorted_indices[:, -2]
    #third_highest_prob_index = sorted_indices[:, -3]
    #fourth_highest_prob_index = sorted_indices[:, -4]
    #fifth_highest_prob_index = sorted_indices[:, -5]
    
    # Get the actual probabilities
    #highest_prob = probabilities[np.arange(len(probabilities)), highest_prob_index]
    #second_highest_prob = probabilities[np.arange(len(probabilities)), second_highest_prob_index]
    #third_highest_prob = probabilities[np.arange(len(probabilities)), third_highest_prob_index]
    #fourth_highest_prob = probabilities[np.arange(len(probabilities)), fourth_highest_prob_index]
    #fifth_highest_prob = probabilities[np.arange(len(probabilities)), fifth_highest_prob_index]

    # Get the class labels
    #most_probable_class = model.classes_[highest_prob_index]
    #second_most_probable_class = model.classes_[second_highest_prob_index]
    #third_most_probable_class = model.classes_[third_highest_prob_index]
    #fourth_most_probable_class = model.classes_[fourth_highest_prob_index]
    #fifth_most_probable_class = model.classes_[fifth_highest_prob_index]
    
    #return jsonify({
        #'first': most_probable_class,
        #'second': second_most_probable_class,
        #'third': third_most_probable_class,
        #'fourth': fourth_most_probable_class,
        #'fifth': fifth_most_probable_class,
        #'firstprob': highest_prob,
        #'secondprob': second_highest_prob,
        #'thirdprob': third_highest_prob,
        #'fourthprob': fourth_highest_prob,
        #'fifthprob': fifth_highest_prob
        #})

if __name__ == '__main__':
    app.run(debug=True)

