# -*- coding: utf-8 -*-
import random

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
    print('Temos', menu["quantity"], menu["food"],'s e cada aluno podera comer ate', menu["limit"], menu["food"],'s. Bon Appetit!')

    return menu