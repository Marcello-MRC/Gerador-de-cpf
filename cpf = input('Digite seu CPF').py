#função para verificar CPF 's
def validar_cpf(cpf): 

    #tirando pontos, espaços, itens indesejados
    cpf = cpf.replace(".","").replace("-","").replace(" ","")
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF são um conjunto de nmeros de 11 digitos!!")
        return False
    #Conferindo o primeiro digito verificador
    soma = 0 
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    if int(cpf[9]) != digito1:
        return False 
        
    #Conferindo o segundo digito verificador
    soma = 0 
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    if int(cpf[10]) != digito2:
        return False
    return True

#Conferindo uma condição que roda enquanto o usuario nao colocar um cpf valido
controle = True
while controle:
    cpf = input("Digite um CPF: \n")
    if validar_cpf(cpf):
        print(f"O CPF digitado: {cpf} é valido!")
        controle = False
    else:
        print("Cpf invalido! Tente Novamente")
