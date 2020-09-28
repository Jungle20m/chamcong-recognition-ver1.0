import os
import numpy as np



def feature_to_string(feature):
    result = ""
    for element in feature:
        result += f" {num}"
    return result

def string_to_feature(feature_string):
    feature = feature_string.split(" ")
    print(feature)
    print(len(feature))
    feature = np.array(feature)
    feature = feature.astype(np.float32)
    return feature