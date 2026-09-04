# =========================
# 1. CAPACIDAD DE AHORRO
# =========================
def capacidad_ahorro():

    input('Bienvenid@, pulse ENTER para comenzar...')

    ingresos = float(input('Introduzca sus ingresos netos: '))

    while ingresos <= 0:
        print('Por favor, introduzca un valor superior a 0')
        ingresos = float(input('Nuevo valor: '))
    
    print('Perfecto, continuemos...')
    input('Pulse ENTER para continuar...')

    gastos = float(input('Introduzca sus gastos mensuales: '))

    while ingresos <= gastos or gastos <= 0:
        print('Los ingresos deben ser superiores a los gastos')
        gastos = float(input('Nuevo valor: '))
    
    print('Perfecto')

    cap_ahorro = ingresos - gastos

    return ingresos, cap_ahorro

ingresos, cap_ahorro = capacidad_ahorro()

print(f'Su capacidad de ahorro es {cap_ahorro}')

# =========================
# 2. TASA DE AHORRO
# =========================

def tasa_ahorro(cap_ahorro, ingresos):

    print('A continuación, calcularemos su tasa de ahorro en base a los datos ofrecidos:')
    input('Pulse ENTER para continuar...')

    tasa_ahorro = (cap_ahorro/ingresos)*100

    return tasa_ahorro

result_tasa = tasa_ahorro(cap_ahorro, ingresos)
print(f'Su tasa de ahorro mensual es {result_tasa}')

# =========================
# 3. AHORRO NO INVERTIDO
# =========================

def ahorro_no_invertido(cap_ahorro):

    print('Ahora calculemos su ahorro no invertido, para ello primero necesitamos definir sus aportaciones mensuales a inversión:')
    input('Pulse ENTER para continuar...')

    aportacion = float(input('Introduzca su aportación mensual: '))

    while aportacion <= 0 or aportacion > cap_ahorro:
        print('Por favor, introduzca un valor superior a 0')
        aportacion = float(input('Nuevo valor: '))
    
    print('Perfecto, vamos a calcular su ahorro no invertido...')
    input('Pulse ENTER para continuar...')

    ahorro_no_invertido = cap_ahorro - aportacion

    return ahorro_no_invertido

result_ahorro_no = ahorro_no_invertido(cap_ahorro)

print(f'Su ahorro no invertido es {result_ahorro_no}')
