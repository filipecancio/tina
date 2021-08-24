# -*- coding: utf-8 -*-
from os import name
from students import getPhoto, getStudentInstances, getStudentStack, serveFood, verifyStudent
from files import getFileInstances
from menu import getRandomMenu
import simpy

if __name__ == "__main__":

    getStudentInstances()
    getFileInstances()

    env = simpy.Environment()

    # Definir prato do dia e limite
    menu = getRandomMenu()

    # Coletar identificação do aluno via reconhecimento facial
    env.process(getPhoto(env))
    env.process(getStudentStack(env))
    env.process(verifyStudent(env))

    # Coletar lista de alunos

    # Entregar comida
    env.process(serveFood(env,menu))
    env.run(until=20)

    #realizar relatório diario
    print("cantina fechada")
    if(menu["quantity"]>0):
        print('Houve sobras de ',menu["quantity"],' ',menu["food"],'s')
    else:
        print('nao sobrou ',menu["food"])