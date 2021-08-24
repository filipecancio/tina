# -*- coding: utf-8 -*-
from os import name
from students import validateStudent
from files import getStack
from menu import getRandomMenu
import random



if __name__ == "__main__":
    stack = getStack()

    # Definir prato do dia e limite
    # menu = getRandomMenu()

    # Coletar Informação do aluno
    stack_photo = random.choice(stack)

    stack_student = validateStudent(stack_photo)

    # Verificar se o aluno está matriculado
    print("O aluno e:", stack_student)

    #verificar se o aluno está dentro do limite de repetição

    #caso esteja, entregar comida

    #caso não esteja  informar que o aluno atingiu o limite
