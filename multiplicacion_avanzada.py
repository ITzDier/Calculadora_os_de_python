def multiplica_n_numeros(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado