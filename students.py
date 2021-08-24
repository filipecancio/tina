# -*- coding: utf-8 -*-
from recognition import comparePhotos
from files import getStudents

def validateStudent(photo_unknown):
    found = False
    response = {
        "name":"unknown",
        "age":"none",
        "grade":0,
        "photos":[
            photo_unknown
        ],
        "student":False
    }

    students = getStudents()

    for student in students:
        photos = student["photos"]
        total_match = 0

        for photo in photos:
            match = comparePhotos(photo_unknown,photo)
            
            if match:
                total_match += 1

        if(total_match > 2):
            found = True
            response = student
            break
    
    return response