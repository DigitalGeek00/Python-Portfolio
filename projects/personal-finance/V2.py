# =========================
# 1. DATOS BASE:
# =========================

def datos_financieros():

    capital = float(input('Indique el capital inicial, sin puntos (P.ej. 10000, 20000, etc): '))
    while capital < 0:
        print('Por favor, introduzca un valor igual o superior a 0.')
        capital = float(input('Nuevo valor: '))
    print('Perfecto, continuemos.')
    input('Pulse ENTER para continuar')

    tiempo = float(input('Indique los años invertido, en número entero o decimal (P.ej. 2, 4, 5.6, etc): '))
    while tiempo < 1:
        print('Por favor, introduzca un valor igual o superior a 1.')
        tiempo = float(input('Nuevo valor: '))
    print('Perfecto, continuemos.')
    input('Pulse ENTER para continuar')

    tasa_anual = float(input('Indique la tasa de interés anual, con número entero o decimal (P. ej. 2, 4, 2.3, etc): ')) / 100
    while tasa_anual <= 0:
        print('Por favor, introduzca un valor superior a 0.')
        tasa_anual = float(input('Nuevo valor: '))
    print('Perfecto, continuemos.')
    input('Pulse ENTER para finalizar el cálculo.')

    return capital, tiempo, tasa_anual

# =========================
# 2. INTERÉS SIMPLE Y COMPUESTO:
# ¿CUÁNTO TENDRÉ EN X AÑOS, CON X APORTACIÓN, Y X TIPO DE INTERÉS? 
# =========================

def interes_simple(capital, tiempo, tasa_anual):

    intereses_s = capital * tiempo * tasa_anual

    capital_final_s = capital + intereses_s

    return intereses_s, capital_final_s

def interes_compuesto(capital, tiempo, tasa_anual):
   
    capital_final_c = capital * (1 + tasa_anual) ** tiempo
   
    intereses_c = capital_final_c - capital

    return intereses_c, capital_final_c

# =========================
# 3. APORTACIONES PERIODICAS:
# ¿CUÁNTO TENDRÉ EN X AÑOS, CON X APORTACIÓN, Y X TIPO DE INTERÉS, SI ADEMÁS VOY APORTANDO MENSUALMENTE?
# =========================

def calculo_aportaciones(capital, aportacion, tiempo, tasa_anual):

    tiempo_meses = tiempo * 12

    tasa_mensual = tasa_anual / 12

    capital_aportaciones = aportacion * (
        ((1 + tasa_mensual) ** tiempo_meses - 1)
        / tasa_mensual
    )

    capital_total_aportado = capital + (aportacion * tiempo_meses)

    capital_inicial_final = capital * (1 + tasa_mensual) ** tiempo_meses

    capital_final = capital_aportaciones + capital_inicial_final

    diferencia_rendimiento = capital_final - capital_total_aportado

    return capital_total_aportado, capital_final, diferencia_rendimiento

while True:
    print('==============================')
    print('     CALCULADORA FINANCIERA')
    print('==============================')
    print('1. Interés simple')
    print('2. Interés compuesto')
    print('3. Aportaciones periódicas')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        print('Has elegido interés simple')
        capital, tiempo, tasa_anual = datos_financieros()

        intereses_s, capital_final_s = interes_simple(capital, tiempo, tasa_anual)

        print(f'Estos son los intereses de la inversión a {tiempo} años: {intereses_s:.2f} €')
        input('Pulse ENTER para ver el capital final:')
        print(f'Este es el capital final resultante: {capital_final_s:.2f} €')
        input('Pulse ENTER para volver al menú.')

    elif opcion == '2':
        print('Has elegido interés compuesto')
        capital, tiempo, tasa_anual = datos_financieros()
        intereses_c, capital_final_c = interes_compuesto(capital, tiempo, tasa_anual)
        print(f'Estos son los intereses de la inversión a {tiempo} años: {intereses_c:.2f} €')
        input('Pulse ENTER para ver el capital final:')
        print(f'Este es el capital final: {capital_final_c:.2f} €')
        input('Pulse ENTER para volver al menú.')

    elif opcion == '3':
        print('Has elegido aportaciones periódicas')
        capital, tiempo, tasa_anual = datos_financieros()
        aportacion = float(input('Indique su aportación mensual, sin puntos (P.ej. 100, 200, etc): '))
        while aportacion <= 0:
            print('Por favor, introduzca un valor superior a 0.')
            aportacion = float(input('Nuevo valor: '))
        capital_total_aportado, capital_final, diferencia_rendimiento = calculo_aportaciones(capital, aportacion, tiempo, tasa_anual)
        print(f'Este es el capital total aportado: {capital_total_aportado:.1f} €')
        input('Pulse ENTER para continuar.')
        print(f'Este es el capital final de la inversión: {capital_final:.1f} €')
        input('Pulse ENTER para continuar.')
        print(f'Esta es el rendimiento bruto sobre el dinero invertido: {diferencia_rendimiento:.1f} €')
        input('Pulse ENTER para continuar.')

    elif opcion == '4':
        print('Hasta pronto')
        break

    else:
        print('Opción no válida')