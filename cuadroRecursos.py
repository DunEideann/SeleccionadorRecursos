from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('problemaRecursos', __name__)

estado = None
contador = 0
personaActual = None
maxMotos = 2
actualMotos = maxMotos

informacion = {
    0: ["8:00-8:30", "Free", contador],
    1: ["8:30-9:00", "Free", contador],
    2: ["9:00-9:30", "Free", contador],
    3: ["9:00-10:00", "Free", contador],
    4: ["10:00-10:30", "Free", contador],
    5: ["10:30-11:00", "Free", contador],
    6: ["11:30-11:30", "Free", contador],
    7: ["11:30-12:00", "Free", contador],
    8: ["12:00-12:30", "Free", contador],
    9: ["12:30-13:00", "Free", contador],
    10: ["13:00-13:30", "Free", contador],
    11: ["13:30-14:00", "Free", contador],
    12: ["14:00-14:30", "Free", contador],
    13: ["14:30-15:00", "Free", contador],
    14: ["15:00-15:30", "Free", contador],
    15: ["15:30-16:00", "Free", contador],
    16: ["16:00-16:30", "Free", contador],
    17: ["16:30-17:00", "Free", contador],
    18: ["17:00-17:30", "Free", contador],
    19: ["17:30-18:00", "Free", contador],
    20: ["18:30-19:00", "Free", contador],
    21: ["19:00-19:30", "Free", contador],
    22: ["19:30-20:00", "Free", contador]
}


personas = {
    "persona1": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    },
    "persona2": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    },
    "persona3": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    }
}


def addMoto(key):
    if informacion[key][2]<maxMotos:
        contador =  informacion[key][2] + 1
        informacion[key][2] = contador

def delMoto(key):
    if informacion[key][2]>0:
        contador =  informacion[key][2] - 1
        informacion[key][2] = contador

@bp.route('/<string:nombre>/', methods=['POST'])
def selectPerson(nombre):
    personaActual = nombre
    print(f"La persona actual es {personaActual}")

    return render_template('index.html', informacion=informacion, personas=personas, personaActual=personaActual)


def assignSlot(estado):
    if estado == None:
        estado = "Free"
    ocupacion = estado
    print(ocupacion)
    return ocupacion


@bp.route('/<string:personaActual>/take/<int:hora>/', methods=['POST'])
def take(personaActual, hora):
    print(f"Entre a take con hora {hora}")
    estado = "Selected"
    personas[personaActual][hora][0] = assignSlot(estado)
    addMoto(hora)

    return redirect(url_for('problemaRecursos.index'))


@bp.route('/<string:personaActual>/drop/<int:hora>/', methods=['POST'])
def drop(personaActual, hora):
    estado = "Free"
    personas[personaActual][hora][0] = assignSlot(estado)
    print("Entre a drop")
    print(f"Drop: {personas[personaActual][hora]}")
    delMoto(hora)
    
    return redirect(url_for('problemaRecursos.index'))


@bp.route('/')
def index():
    return render_template('index.html', informacion=informacion, personas=personas, personaActual=personaActual)