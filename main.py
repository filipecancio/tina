# -*- coding: utf-8 -*-
import json
import random

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


def getRandomStudent():
    return random.choice(students)

def getRandomMenu():
    food = ["banana","bolacha","achocolatado","pipoca","hotdog","pera"]

    menu = {
        "food": random.choice(food),
        "grade": random.randint(1,3),
        "limit": random.randint(1,3),
        "quantity": random.randint(6,15)
    }

    print('Bom dia, aqui e a Tina!')
    print('Hoje o prato e', menu["food"])
    print('apenas alunos do grau', menu["grade"], 'podem comer')
    print('Temos', menu["quantity"], menu["food"], 'e cada aluno podera comer ate', menu["limit"], menu["food"],'s. Bon Appetit!')

    return menu



if __name__ == "__main__":
    loadGlobalFiles()

    student = getRandomStudent()
    menu = getRandomMenu()

