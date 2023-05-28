import ktrain
from ktrain import text

predictor2 = ktrain.load_predictor('C:/Users/97252/Desktop/pytorch-project/bert_model')

import pandas as pd
df = pd.read_csv('C:/Users/97252/Desktop/תואר שני/nlp/final_project/test.csv')
df.head()

qqq = (df['text'][:3]).to_numpy()
print('Some samples from test.csv')
for i in qqq:
  print(i , '\n')
  prediction = predictor2.predict(i)
  print(prediction , '\n')

print('Enter q to stop')
while(True):
  user_input = input("Enter sentance to be eveluated:")
  if user_input == 'q':
    break
  else:
    prediction = predictor2.predict(user_input)
    print(prediction)


