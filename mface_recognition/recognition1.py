import os

import cv2

from mface_recognition import face_services


def recognition(image, model, data):
	crop_img = model.get_input(image)
	if crop_img is None:
		name = "-1"
		return name
	encoding = model.get_feature(crop_img)
	name = "-1"
	if encoding is None:
		name = "-1"
		return name
	if encoding is not None:
		names = []
		matches = face_services.compare_faces(data["features"], encoding)
		name = "-1"
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["user_ids"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)
		names.append(name)
	return name
