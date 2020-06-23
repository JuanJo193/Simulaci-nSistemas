import simpy
'''
Sympi

Semi cuarentena CodVid19

'''
wo= "mujeres"; m ="hombres"; b="ambos"; l="lunes"; m="martes"; w="miercoles"; j="jueves"; f="viernes";s="sabado";d="domingo"


def cuarentena(env):

    print("Qué día es hoy?")
    day=input()
    if day == (l or w or f) :
        print("Salen Mujeres")
    elif day == (m or j or s) :
        print("Salen hombres")
    else:
        print("Salen ambos")

env = simpy.Environment()
env.process(cuarentena(env))
