import sklearn.externals
import joblib

model = joblib.load('trained_weight_classifier_model.pkl')

#Get inputs from user

age = 0
height = 0
hair_black = hair_white = hair_others = 0
gender_female = gender_male = 0

age = int(input("Enter age: "))
height = int(input("Enter height: "))

hair_color = int(input("Enter hair color (1=Black, 2=white, 3=others): "))
if hair_color == 1:
    hair_black = 1
if hair_color == 2:
    hair_white = 1
if hair_color == 3:
    hair_others = 1

gender = int(input("Enter gender (1=male, 2=female)"))
if gender == 2:
    gender_female = 1
if gender == 1:
    gender_male = 1

weight_to_predict = [ 
    age,    
    height,  
    hair_black,     
    hair_white,    
    hair_others,     
    gender_female,   
    gender_male,     
]

weight_to_predict = [
    weight_to_predict
]

# Run the model and make a prediction the weight
predicted_weight_values = model.predict(weight_to_predict)

# Since we are only predicting the price of one house, just look at the first prediction returned
#predicted_value = predicted_weight_values[0]

for i in range(len(weight_to_predict)):
    predicted_value = predicted_weight_values[i]
    print("The weight is estimated to be {:,.2f}".format(predicted_value), "kg")
