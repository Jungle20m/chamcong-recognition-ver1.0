import os
import pickle

import cv2

# from face_recognition import face_model

DATA_PATH = "mface_recognition/features.pickle"

def load_data():
	data = pickle.loads(open(DATA_PATH, "rb").read())
	return data


if __name__ == '__main__':
	data = load_data()
	print(type(data['encodings'][0][0]))