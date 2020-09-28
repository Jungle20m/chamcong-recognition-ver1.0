import os

import cv2

from mface_recognition import face_services


def recognition(image, model, data):
	crop_img = model.get_input(image)
	if crop_img is None:
		name = "Detecting"
		return name
	encoding = model.get_feature(crop_img)
	name = "Unknown"
	if encoding is None:
		name = "Detecting"
		return name
	if encoding is not None:
		names = []
		matches = face_services.compare_faces(data["encodings"], encoding)
		name = "Unknown"
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)
		names.append(name)
	return name
