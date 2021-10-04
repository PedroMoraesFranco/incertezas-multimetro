def multimetro():
    tipo = input('''
    Selecione o que você está medindo:
    1.Resistencia 
    2.Tensão
    3.Corrente 
    4.Capacitância

    Obs: Antes de anotar a resposta olhe a resolução

    ''') 
    if tipo == '1':
        ohmimetro()
    elif tipo == '2':
        voltimetro_select()
    elif tipo == '3':
        amperimetro_select()
    elif tipo == '4':
        capacitancia()
    else:
        print("Você digitou uma opção inválida")
        retornar()

def retornar():
    retorno=input('''
    Você deseja retornar?
    Digite Y caso queira ou digite N caso não queira

    ''')
    if retorno.upper() == 'Y':
        multimetro()
    elif retorno.upper() == 'N':
        print('Obrigado, até a próxima.')
    else:
        retornar()

def ohmimetro():
    R = float(input('Insira o valor em Ohms '))

    if R<=200:
        inc = R*(0.8/100)+0.5
        print('{}+/-{:.1f}\u03A9'.format(R,inc))
        print('resolução: 0.1\u03A9')
    elif 200<R<2e3:
        inc = R*(0.8/100)+3
        print('{} +/-{:1.0f}\u03A9'.format(R,inc))
        print('resolução: 1\u03A9')
    elif 2e3<R<2e4:
        inc = (R*(0.8/100)+3e1)/1e1
        print('{} +/-{:10.0f}\u03A9'.format(R/1e1,round(inc,0)*10))
        print('resolução: 10\u03A9')
    elif 2e4<R<2e5:
        inc = (R*(0.8/100)+3e2)/1e2
        print('{} +/-{:100.0f}\u03A91'.format(R/1e2,round(inc,0)*1e2))
        print('resolução: 100\u03A9')
    elif 2e5<R<2e6:
        inc = (R*(0.8/100)+3e3)/1e3
        print('{} +/-{:10.0f}k\u03A9'.format(R/1e3,round(inc,0)*1e3))
        print('resolução: 1k\u03A9')
    elif 2e5<R<2e7:
        inc = (R*(5/100)+10e5)/1e5
        print('{} +/-{:10.0f}k\u03A9'.format(R/1e3,round(inc,0)*1e5))
        print('resolução: 100k\u03A9')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

def voltimetro_select():
    select = input('''
    Qual tipo de voltimetro você quer?
    1.DC
    2.AC
    ''')
    if select == '1':
        DC_voltimetro()
    elif select == '2':
        AC_voltimetro()
    else:
        print('Opção inválida')
        multimetro()

def DC_voltimetro():
    V = float(input('Insira o valor em Volts '))

    if V<=2e-3:
        inc = V*(0.5/100)+0.3
        print('{}+/-{:1.1f}mV'.format(V,inc))
        print('resolução: 0.1mV')
    elif 2e-3<V<2:
        inc = V*(0.5/100)+3e-3
        print('{} +/-{:1.3f}V'.format(V,inc))
        print('resolução: 1mV')
    elif 2<V<2e1:
        inc = (V*(0.5/100)+3e-2)
        print('{} +/-{:10.2f}V'.format(V,inc))
        print('resolução: 10mV')
    elif 2e1<V<2e2:
        inc = (V*(0.5/100)+3e-1)
        print('{} +/-{:100.1f}V'.format(V,inc))
        print('resolução: 100mV')
    elif 2e2<V<1e3:
        inc = (V*(1/100)+5)
        print('{} +/-{:10.0f}V'.format(V,round(inc,0)))
        print('resolução: 1V')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

def AC_voltimetro():
    V = float(input('Insira o valor em Volts '))

    if V<=2:
        inc = V*(0.8/100)+5e-3
        print('{}+/-{:1.3f}V'.format(V,inc))
        print('resolução: 1mV')
    elif 2<V<2e1:
        inc = V*(0.8/100)+5e-2
        print('{} +/-{:1.2f}V'.format(V,inc))
        print('resolução: 10mV')
    elif 2e1<V<2e2:
        inc = V*(0.8/100)+3e-1
        print('{} +/-{:10.1f}V'.format(V,inc))
        print('resolução: 100mV')
    elif 2e2<V<750:
        inc = (V*(1.2/100)+5)
        print('{} +/-{:100.0f}V'.format(V,round(inc,0)))
        print('resolução: 1V')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

def amperimetro_select():
    select = input('''
    Qual tipo de amperimetro você quer?
    1.DC
    2.AC
    ''')
    if select == '1':
        DC_amperimetro()
    elif select == '2':
        AC_amperimetro()
    else:
        print('Opção inválida')
        multimetro()

def DC_amperimetro():
    A = float(input('Insira o valor em Ampère '))

    if A<=2e-2:
        inc = A*(0.8/100)+4e-5
        print('{}+/-{:.5f}mA'.format(A,inc))
        print('resolução: 10\u03BCA')
    elif 2e-2<A<2e-1:
        inc = A*(1.2/100)+4e-4
        print('{} +/-{:1.4f}mA'.format(A,inc))
        print('resolução: 100\u03BCA')
    elif 2e-1<A<2e1:
        inc = (A*(2/100)+5e-2)
        print('{} +/-{:10.2f}A'.format(A,inc))
        print('resolução: 10mA')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

def AC_amperimetro():
    A = float(input('Insira o valor em Ampère '))

    if A<=2e-2:
        inc = A*(1/100)+5e-5
        print('{}+/-{:.5f}mA'.format(A,inc))
        print('resolução: 10\u03BCA')
    elif 2e-2<A<2e-1:
        inc = A*(2/100)+5e-4
        print('{} +/-{:1.4f}mA'.format(A,inc))
        print('resolução: 100\u03BCA')
    elif 2e-1<A<2e1:
        inc = (A*(3/100)+10e-2)
        print('{} +/-{:10.2f}A'.format(A,inc))
        print('resolução: 10mA')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

def capacitancia():
    C = float(input('Insira o valor em Farad '))

    if C<=2e-9:
        inc = (C*(2.5/100)+0.02)*1e9
        print('{}+/-{:.2f}nF'.format(C*1e9,inc))
        print('resolução: 0.01nF')
    elif 2e-9<C<2e-7:
        inc = (C*(2.5/100)+0.2)*1e7
        print('{} +/-{:1.1f}nF'.format(C*1e7,inc))
        print('resolução: 0.1nF')
    elif 2e-7<C<2e-6:
        inc = (C*(2.5/100)+0.2)*1e6
        print('{} +/-{:1.3f}\u03BCF'.format(C*1e6,inc))
        print('resolução: 1nF')
    elif 2e-6<C<2e-4:
        inc = (C*(2.5/100)+0.2)*1e4
        print('{} +/-{:100.3f}\u03BCF'.format(C*1e4,inc))
        print('resolução: 100nF')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

multimetro()