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
        inc = R*(0.8/1000)+0.5
        print('{}+/-{:.1f}\u03A9'.format(R,inc))
        print('resolução: 0.1\u03A9')
    elif 200<R<2e3:
        inc = R*(0.8/1000)+3
        print('{} +/-{:1.0f}\u03A9'.format(R,inc))
        print('resolução: 1\u03A9')
    elif 2e3<R<2e4:
        inc = (R*(0.8/1000)+3e1)/1e1
        print('{} +/-{:10.0f}\u03A9'.format(R/1e1,round(inc,0)*10))
        print('resolução: 10\u03A9')
    elif 2e4<R<2e5:
        inc = (R*(0.8/1000)+3e2)/1e2
        print('{} +/-{:100.0f}\u03A91'.format(R/1e2,round(inc,0)*1e2))
        print('resolução: 100\u03A9')
    elif 2e5<R<2e6:
        inc = (R*(0.8/1000)+3e3)/1e3
        print('{} +/-{:10.0f}k\u03A9'.format(R/1e3,round(inc,0)*1e3))
        print('resolução: 1k\u03A9')
    elif 2e5<R<2e7:
        inc = (R*(5/1000)+10e5)/1e5
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

def capacitancia():
    C = float(input('Insira o valor em Farad '))

    if C<=2e-9:
        inc = (C*(2.5/1000)+0.02)*1e9
        print('{}+/-{:.1f}nF'.format(C*1e9,inc))
        print('resolução: 0.01nF')
    elif 200<C<2e3:
        inc = C*(0.8/1000)+3
        print('{} +/-{:1.0f}F'.format(C,inc))
        print('resolução: 1F')
    elif 2e3<C<2e4:
        inc = (C*(0.8/1000)+3e1)/1e1
        print('{} +/-{:10.0f}F'.format(C/1e1,round(inc,0)*10))
        print('resolução: 10F')
    elif 2e4<C<2e5:
        inc = (C*(0.8/1000)+3e2)/1e2
        print('{} +/-{:100.0f}F'.format(C/1e2,round(inc,0)*1e2))
        print('resolução: 100F')
    elif 2e5<C<2e6:
        inc = (C*(0.8/1000)+3e3)/1e3
        print('{} +/-{:10.0f}kF'.format(C/1e3,round(inc,0)*1e3))
        print('resolução: 1kF')
    elif 2e5<C<2e7:
        inc = (C*(5/1000)+10e5)/1e5
        print('{} +/-{:10.0f}kF'.format(C/1e3,round(inc,0)*1e5))
        print('resolução: 100kF')
    else:
        print('Essa entrada é inválida, retorne ao início')
        multimetro()

multimetro()