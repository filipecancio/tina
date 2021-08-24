# -*- coding: utf-8 -*-
import json
import os
import random

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir

data_dir = getDirectory("/data")
photos_dir = getDirectory("/photos/")

students_file = getDirectory("/data/students.json")
monday_file = getDirectory("/data/monday.json")

def getFile(file_name):
    with open(file_name,"r") as file_temp:
        return json.load(file_temp)

def loadGlobalFiles():
    global students
    global monday

    students = None
    monday = None

    students = getFile(students_file)
    monday = getFile(monday_file)

def getStudents():
    students = getFile(students_file)
    return students

def getPhotos():
    stack = []

    for image_path in os.listdir(photos_dir):
        stack.append(photos_dir+image_path)
    return stack

def getStack():
    photos = getPhotos()
    range = random.randint(3,6)
    stack = random.choices(photos, k = range)
    print(stack)
    return stack