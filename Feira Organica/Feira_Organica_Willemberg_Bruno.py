folha_hortalica = {'Alface americano': 2.50, 'Alface crespa': 2.50, 'Alho poró': 2.00, 'Capim santo': 4.50,
                     'Cebola': 3.00, 'Cebolinha': 1.50, 'Coentro': 2.50, 'Couve folha': 2.50, 'Chinguezay (acelga chinesa)': 3.00, 'Espinafre': 3.00, 'Hortelã': 2.50, 'Salsinha': 2.50, 'Rúcula': 2.50}
frutas = {'Banana pacovan (unidade)': 0.25, 'Cana(saquinho)': 2.00,
          'Laranja comum (4 Unidades)': 2.00, 'Laranja mimo (4 Unidades)': 2.00, 'Maracujá (1kg)': 7.00}
Raizes_afins = {'Batata doce (kg)': 4.00, 'Cará (kg)': 5.00, 'Cenoura(molho)': 3.00,
                     'Jerimum (kg)': 5.00, 'Macaxeira (kg)': 4.00, 'Rabanete(molho)': 2.50, 'Quiabo (15 Un)': 2.00}
Outros = {'Fava seca (Kg)': 12.00, 'Mel italiana (250 g)': 20.00, 'Mel italiana (500 g)': 35.00, 'Mel no favo (450 g)': 25.00, 'Ovos de capoeira (un)': 1.00, 'Polpa de cajá (400g)': 6.00,
 'Própolis (20 ml)': 16.00, 'Pão sem trigo (grande)': 13.00, 'Pão com trigo (grande)': 13.00, 'Pão com trigo (pequeno)': 7.00, 'Bolo(sem trigo)': 10.00, 'Bolinho de bacia(c/trigo)': 2.00, 'Mini pizza (un)': 3.00, 
 'Pizza brotinho': 5.00, 'Bolacha com trigo (saquinho)': 5.00, 'Sucos sem açucar (200 ml)': 3.00, 'Sucos com açucar (200 ml)': 3.00,
          'Sucos com ou sem açucar (1 l)': 10.00, 'Refeições congeladas (500 g)': 12.00, 'Refeições congeladas (750 g)': 15.00, 'Hambúrguer de ora-pro-nóbis: (6 Un)': 12.00, 'Molhos prontos': 10.00, 'Massa artesanal (lasanha ou taglatelle)': 12.00}
Past_antepast_geleias = {'Pepita de girassol': 5.00, 'Homus de grão de bico com paprika': 5.00,
                         'Bisnaga Maionese de pepita de girassol (250 ml)': 10.00, 'Pimentas ao mel de engenho': 15.00, 'Confit de tomatinho, pimenta, pimentão ou berinjela': 15.00, 'Geleia de tomate com pimenta/abacaxi/manga': 13.00, 'Capotana Siciliana': 13.00}
Lanches_strigo = {'Quiche de macaxeira c/ alho poró': 5.00, 'Quiche de macaxeira c/ tomate seco': 5.00,
                    'Sanduíche sem glúten de ricota': 6.00, 'Sanduíche sem glúten de caponata Siciliana': 6.00, 'Sanduíche sem glúten de ragu': 6.00}
Lanches_ctrigo = {'Empada de falso camarão': 5.00, 'Empada de antepasto de berinjela': 5.00,
                    'Empada de tofu com cebola caramelizada': 5.00, 'Pãozinhos de inhames recheados': 5.00}

carrinho = 0
notafiscal = {}
qntpro = []
nome = []
end = []
pagar = []

print("-="*25)
print("         Folhas e Hortaliças         ")
print("Nº  Produtos              &              Preços")
print("-="*25)
i = 0
for a, b in folha_hortalica.items():
        print(i,f'{a:-<40}{b} R$')
        i+=1
print("-="*25)

while True:
    op = (str(input("Deseja alguma Folha ou Hortaliças? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))

            cont = 0 
            for chave in folha_hortalica.keys():
                if resposta == cont:
                    print(chave)
                    break
                    
                cont+=1
            
            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, folha_hortalica[chave]*qnt]
            carrinho = carrinho + folha_hortalica[chave]*qnt
            print("Valor da conta no momento:", carrinho)      

            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break     
    break

print("-="*25)
print("               Frutas             ")
print("Nº Produtos              &              Preços")
print("-="*25)
i = 0
for a, b in frutas.items():
        print(i,f'{a:-<40}{b} R$')
        i+=1
print("-="*25)

while True:
    op = (str(input("Deseja alguma Fruta? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in frutas.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, frutas[chave]*qnt]
            carrinho = carrinho + frutas[chave]*qnt
            print("Valor da conta no momento:", carrinho)

            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break     
    break

print("-="*25)
print("       Raízes, Tubérculos, Legumos e Afins            ")
print("Nº Produtos              &              Preços")
print("-="*25)
i = 0
for a, b in Raizes_afins.items():
        print(i,f'{a:-<40}{b} R$')
        i+=1
print("-="*25)

while True:
    op = (str(input("Deseja alguma Raízes, Tubérculos, Legumos e Afins? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in Raizes_afins.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, Raizes_afins[chave]*qnt]
            carrinho = carrinho + Raizes_afins[chave]*qnt
            print("Valor da conta no momento:", carrinho)
                
            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break     
    break

print("-="*25)
print("              Outros            ")
print("Nº Produtos              &              Preços")
print("-="*25)
i = 0
for a, b in Outros.items():
        print(i,f'{a:-<40}{b} R$')
        i+=1
print("-="*25)

while True:
    op = (str(input("Deseja alguma Produto dessa lista Outros? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in Outros.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, Outros[chave]*qnt]
            carrinho = carrinho + Outros[chave]*qnt
            print("Valor da conta no momento:", carrinho)
                
            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break       
    break

print("-="*35)
print("     Pastinhas, Antepasto e Geleias     ")
print("Nº Produtos                        &                        Preços")
print("-="*35)
i = 0
for a, b in Past_antepast_geleias.items():
        print(i,f'{a:-<60}{b} R$')
        i+=1
print("-="*35)

while True:
    op = (str(input("Deseja alguma Pastinhas, Antepasto ou Geleias? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in Past_antepast_geleias.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, Past_antepast_geleias[chave]*qnt]
            carrinho = carrinho + Past_antepast_geleias[chave]*qnt
            print("Valor da conta no momento:", carrinho)
                
            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break
    break

print("-="*35)
print("        Lanches (Sem Trigo)        ")
print("Nº Produtos                    &                   Preços")
print("-="*35)
i = 0
for a, b in Lanches_strigo.items():
        print(i,f'{a:-<50}{b} R$')
        i+=1
print("-="*35)

while True:
    op = (str(input("Deseja algum Lanche (Sem Trigo)? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in Lanches_strigo.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, Lanches_strigo[chave]*qnt]
            carrinho = carrinho + Lanches_strigo[chave]*qnt
            print("Valor da conta no momento:", carrinho)
                
            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break  
    break

print("-="*35)
print("        Lanches (Com Trigo)        ")
print("Nº Produtos                    &                    Preços")
print("-="*35)
i = 0
for a, b in Lanches_ctrigo.items():
        print(i,f'{a:-<50}{b} R$')
        i+=1
print("-="*35)

while True:
    op = (str(input("Deseja algum Lanche (Com Trigo)? S/N ")))
    if op in 'Nn':
        break
    else:
        while True: 

            resposta = int(input("Digite o numero do produto:"))
            
            cont = 0 
            for chave in Lanches_ctrigo.keys():
                if resposta == cont:
                    break
                cont+=1

            qnt = int(input("Digite quantidade do produto:"))
            notafiscal[chave] = qntpro = [qnt, Lanches_ctrigo[chave]*qnt]
            carrinho = carrinho + Lanches_ctrigo[chave]*qnt
            print("Valor da conta no momento:", carrinho)
                
            op = (str(input("Deseja comprar outro produto desta lista? S/N ")))
            if op in 'Nn':
                break
    break

print("Produto                                         Quantidade                   Preço")
for chave, valor in notafiscal.items():
    print(f'{chave:<55} {valor[0]:<20} {valor[1]} R$')

print(f'                                                Total a Pagar:{carrinho:>20}')

print('Vamos fazer seu cadastro:')
listnome = input("Digite seu nome:")
nome.append('Nome:')
nome.append(listnome)

listend = input('Digite seu endereço:')
end.append('Endereço:')
end.append(listend)

print("0- Cartão de Crédito")
print("1- Cartão de Débito")
print("2- Dinheito")
listpag = int(input("Digite o número da opção que deseja pagar:"))
if listpag == 0:
    pagar.append("Cartão de Crédito")
if listpag == 1:
    pagar.append("Cartão de Débito")
if listpag == 2:
    pagar.append("Dinheito")

        

with open('dadospedido.txt', 'w',encoding='utf8') as arquivo:
    arquivo.write('Dados de entrega:\n')
    arquivo.writelines(nome)
    arquivo.write('\n')
    arquivo.writelines(end)
    arquivo.writelines('\n')
    arquivo.write('Dados do pedido:\n')
    arquivo.write("Produto                                         Quantidade                   Preço\n") 
    for chave, valor in notafiscal.items():
        arquivo.writelines(f'{chave:<55} {valor[0]:<20} {valor[1]} R$\n')  
    arquivo.writelines(f'                                                Total a Pagar:{carrinho:>20}\n')
    arquivo.writelines(f'Forma de pagamento:{pagar}')