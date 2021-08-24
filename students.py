# -*- coding: utf-8 -*-
from recognition import comparePhotos
from files import getDirectory, getStudents

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

def getStudentStack(photo_stack):
    stack = []
    print(" Abrindo a cantina: verificando se nossos alunos estão devidamente matriculados e podem entrar na fila")

    for photo in photo_stack:
        # Coletar Informação do aluno
        print("Verificando aluno ...")
        student = getStudent(photo)

        # Verificar se o aluno foi reconhecido
        if(student["grade"] == 0):
            print("Pessoa nao identificada, chamar segurança")

        # Verifica se o aluno esta matriculado
        elif(student["student"] == False):
            print("Aluno não matriculado, não poderá comer na cantina ate fazer matricula. Favor comparecer à secretaria.")
        
        # Caso o aluno esteja matriculado, manter na fila
        else:
            print("Aluno identificado, pode entrar na fila.")
            stack.append(student)

    print("Verificação concluída")
    return stack

def incrementStudentRound(students,student_name,menu):
    #verificar se o aluno está dentro do limite de repetição
    for student in students:
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