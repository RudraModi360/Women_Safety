import json
import pickle
import numpy as np

__Area_Names = None
__data_columns = None
__model = None


def get_Area_names():
    return __Area_Names


def get_data_columns():
    return __data_columns


def load_data():
    print("data is started to load..")
    global __data_columns
    global __Area_Names

    with open("Area_name.json") as f:
        __data_columns = json.load(f)["columns"]
        __Area_Names = __data_columns[3:]

    global __model
    if __model is None:
        with open("model.pkl", "rb") as f:
            __model = pickle.load(f)
        print("model is loaded sucessfully...")


def predict_safety(Area_name):
    try:
        loc_idx = __data_columns.index(Area_name.lower())
    except:
        loc_idx = -1
    with open("df.json",'r') as f:
        data=json.load(f)
        x = np.zeros(102)
        x[0] = data[loc_idx]["Type_Area"]
        x[1] = data[loc_idx]["Women_safety_ratio"]
        x[101] = data[loc_idx]["crowdness_factor"]
        if loc_idx >= 0:
            x[loc_idx] = 1
        x = np.expand_dims(x, axis=0)
    return round(__model.predict([x])[0][0])



if __name__ == "__main__":
    load_data()
    print(predict_safety("Waghodiya_Road"))
