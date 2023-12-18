import random



animal = ['Macaco', 'Elefante', 'Rato', 'Urso', 'Timbu',
          'Lagartixa', 'Girafa', 'T-Rex', 'Pássaro', 'Tartaruga']

tema = ['Praia', 'Mecânico', 'Skate', 'Paris', 'Trabalhador', 'Nordestino',
        'Astronauta', 'Depressiva', 'Nerd', 'Medroso']


def aperte_sim():
    return f'{random.choice(tema)} + {random.choice(animal)}'
