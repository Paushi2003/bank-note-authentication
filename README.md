# bank-note-authentication
This bank note authentication system runs on top of an ML model that is trained to perform prediction. The model predicts whether the characteristics provided by the user belong to the original or fake currency note. 
Branch details:
The branch 'main' contains the code for API along with the notebook that was used to train the model. 
The branch 'frontend' contains the full implementation of the frontend developed with HTML and CSS.
Clone the repository and run 
```
uvicorn app.main:app --reload
```
