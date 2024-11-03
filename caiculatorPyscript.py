import pickle
from sklearn.neural_network import MLPRegressor
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def calculate(value):
    with open('./model.pkl', 'rb') as f:
        model = pickle.load(f)

    num1, num2, sub, mult, div = evalu(value)
    
    exp = pd.DataFrame({"Num1": [num1], "Num2": [num2], "sub": [sub], "mult": [mult], "div": [div]})

    result = model.predict(exp)
    return result[0]

def evalu(value):
    op = ""
    sub = 0
    mult = 0
    div = 0
    if "+" in value:
        op = "+"
    elif "-" in value:
        op = "-"
        sub = 1
    elif "*" in value:
        op = "*"
        mult = 1
    elif "/" in value:
        op = "/"
        div = 1
    num1 = value[:value.index(op)]
    num2 = value[value.index(op) + 1:]
    return num1, num2, sub, mult, div
