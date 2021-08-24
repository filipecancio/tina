# -*- coding: utf-8 -*-
import random
from typing import Match
from recognition import comparePhotos
from files import getDirectory, getPhotos, getStudents

def getStudentInstances():
    global photo_stack
    global student_stack
    global verified_student_stack
    global student_list

    photo_stack = []
    student_stack = []
    verified_student_stack = []
    student_list = getStudents()

def getStudent(photo_unknown):
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
            photo = getDirectory(photo)
            match = comparePhotos(photo_unknown,photo)
            
            if match:
                total_match += 1

        if(total_match > 2):
            found = True
            response = student
            break
    
    return response

def getPhoto(env):
    global photo_stack
    
    while True:
        print("Aluno, Por favor posicione o seu rosto corretamente na camera.")
        photos = getPhotos()
        photo = random.choice(photos)
        print('Foto: ',photo, 'colocada para processamento.')
        photo_stack.append(photo)
        yield env.timeout(0.5)

def getStudentStack(env):
    global student_stack
    global photo_stack
    photos = getPhotos()

    while True:
        if(len(photo_stack)):
            for photo in photo_stack[:]:
                print("Processando foto ",env.now)
                student = getStudent(photo)
                student_stack.append(student)
                photo_stack.remove(photo)
                yield env.timeout(1)
            print("Foto Processada.")

def verifyStudent(env):
    global student_stack
    global verified_student_stack

    while True:
        #verificar se o aluno está dentro do limite de repetição
        if(len(student_stack)):
            print("Identificando pessoa ",env.now)
            for student in student_stack[:]:
                # Verificar se o aluno foi reconhecido
                if(student["grade"] == 0):
                    print("Pessoa nao identificada, chamar segurança")

                # Verifica se o aluno esta matriculado
                elif(student["student"] == False):
                    print("Aluno não matriculado, não poderá comer na cantina ate fazer matricula. Favor comparecer à secretaria.")

                # Caso o aluno esteja matriculado, manter na fila
                else:
                    print("Aluno identificado, pode entrar na fila.")
                    verified_student_stack.append(student)
                student_stack.remove(student)
                yield env.timeout(5)

def incrementStudentRound(student_name,menu):
    global student_list

    #verificar se o aluno está dentro do limite de repetição
    for student in student_list:
        #verificar se ainda ha lanche
        if(menu["quantity"]<=0):
            print('Acabou o ',menu["food"],'.')
            break

        if(student["name"] == student_name):
            if(student["round"] < menu["limit"]):
                #caso esteja, entregar comida
                student["round"] += 1
                menu["quantity"] -=1
                print(student["name"],' pegou ',menu["food"],' pela ',student["round"],'a vez.')
            else:
                #caso não esteja  informar que o aluno atingiu o limite
                print(student["name"],' atingiu o limite de ',menu["food"],'. Nao pode pedir mais')

def serveFood(env,menu):
    global verified_student_stack
    global student_list

    while True:
        #verificar se o aluno está dentro do limite de repetição
        if(len(verified_student_stack)):
            for student in verified_student_stack[:]:
                incrementStudentRound(student["name"],menu)
                verified_student_stack.remove(student)
                yield env.timeout(5)
