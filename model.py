# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 02:25:53 2019

@author: Shiva
"""


from simpletransformers.classification import ClassificationModel


# Create a TransformerModel
model = ClassificationModel('roberta', 'roberta-base')


# Train the model
model.train_model(train_df)


import pickle
file='trick'
of=open(file,'wb')
pickle.dump(model,of)
of.close()


# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df)
print(result)
print(model_outputs)

predictions, raw_outputs = model.predict(['The ambience of hotel was worst'])
print(predictions)
print(raw_outputs)