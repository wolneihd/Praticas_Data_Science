def mmc(denominadores: list[int], mostrar_conta: bool = False) -> float: 
    """
    Método que retorna o MMC - Mínimo Múltiplo Comum para uma lista de números inteiros.
    <br>
    `denominadores`: lista de números (obrigatório)
    <br>
    `mostrar_conta`: mostra o cálculo passo-a-passo - tipo: bool - valor default: False.
    """
    copia = denominadores.copy()
    for denominador in denominadores:
        
        is_primo = True
        array_primos = []

        for index in range(2,11):
            if (denominador%index) == 0:
                is_primo = False
        if is_primo:
            array_primos.append(denominador)

    divisores = []
    for index in range(2,11):
        for i, denominador in enumerate(denominadores):
            if (denominador%index) == 0:       
                if mostrar_conta:
                    print(f'Divindo todos elementos por: {index} | {denominadores}')                           
                denominadores[i] = denominador/index
                divisores.append(index)       

    resultado = 1
    for numero in divisores:
        resultado = resultado * numero

    for numero in array_primos:
        resultado = resultado * numero
        if mostrar_conta:
            print(f'Divindo todos elementos por: {numero} | {denominadores}')          
            print('Resultado: ', resultado)
        else: 
            print(resultado)