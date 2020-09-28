'''
Some of below services are referring:
http://face-recognition.readthedocs.io/en/latest/_modules/face_recognition/api.html

'''

import numpy as np
import cupy as cp
# from configs import configs


def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return cp.empty((0))
    if len(face_to_compare) == 0:
        return cp.empty((0))

    face_encodings = cp.asarray(face_encodings)
    face_to_compare = cp.asarray(face_to_compare)

    face_dist_value = cp.sum(cp.square(face_encodings - face_to_compare))
    face_dist_value = cp.dot(face_encodings, face_to_compare.T)

    cp.cuda.Stream.null.synchronize()
    #print('[Face Services | face_distance] Distance between two faces is {}'.format(face_dist_value))
    return face_dist_value
    #return dist

#def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=configs.face_similarity_threshold):
def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.51):
    true_list = list(face_distance(known_face_encodings, face_encoding_to_check) >= tolerance)
    #similar_indx = list(np.where(true_list)[0])
    #return similar_indx
    return true_list
