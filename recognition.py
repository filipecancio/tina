# -*- coding: utf-8 -*-
import face_recognition

def getEncondingPhoto(photo):
    load_photo = face_recognition.load_image_file(photo)
    encode_photo = face_recognition.face_encodings(load_photo)[0]
    return encode_photo

def comparePhotos(photo01,photo02):
    encode_photo01 = getEncondingPhoto(photo01)
    encode_photo02 = getEncondingPhoto(photo02)
    match = face_recognition.compare_faces([encode_photo01], encode_photo02)[0]
    return match