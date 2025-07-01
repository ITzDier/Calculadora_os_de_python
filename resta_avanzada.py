def resta_n_numeros(*numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return resultado