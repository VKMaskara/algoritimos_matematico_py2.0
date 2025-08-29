import datetime # para importar toda 
data = datetime.date(2024,8,28) # gardando a data na var
print(data) # imprimir var

print(30 * '-') # linha separadora 
dia = data.day # pegue a classe dia
mes = data.month # pegue a classe mês
ano = data.year # pegue a classe ano
print(dia, mes, ano, sep="/") # imprimir 

print(30 * '-') # linha separadora 


'''data_user = input("Digite uma data no formato AAAA/MM/DD: ")
# Dividir a string para obter ano, mês e dia
ano, mes, dia = map(int, data_user.split('/'))

# Criar a data a partir dos valores fornecidos
data = datetime.date(ano, mes, dia)

# Imprimir os valores
print(dia, mes, ano, sep="/")

print(30 * '-') # linha separadora '''

nova_data = data.replace(month=10)
print(nova_data)


dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))

nova_data = ( data.replace(day = dia, month = mes, year = ano))
print(nova_data)

print(30 * '-') # linha separadora 

data_atual = datetime.date.today()
print(data_atual)
