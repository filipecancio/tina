# -*- coding: utf-8 -*-
import json

students_file = "/home/cancio/Área de Trabalho/projetos/github/tina/data/students.json"
monday_file = "/home/cancio/Área de Trabalho/projetos/github/tina/data/monday.json"

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

def getStack():
    monday = getFile(monday_file)
    return monday

def getStudents():
    students = getFile(students_file)
    return students

