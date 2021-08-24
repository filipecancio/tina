# -*- coding: utf-8 -*-
from os import name
from students import getStudentStack, incrementStudentRound
from files import getStack, getStudents
from menu import getRandomMenu

if __name__ == "__main__":
    # Definir prato do dia e limite
    menu = getRandomMenu()

    # Coletar identificação do aluno via reconhecimento facial
    photo_stack = getStack()
    student_stack = getStudentStack(photo_stack)

    # Coletar lista de alunos
    students_data = getStudents()

    # Entregar comida
    for student in student_stack:
        incrementStudentRound(students_data,student["name"],menu)

    #realizar relatório diario
    print("cantina fechada")
    if(menu["quantity"]>0):
        print('Houve sobras de ',menu["quantity"],' ',menu["food"],'s')
    else:
        print('nao sobrou ',menu["food"])