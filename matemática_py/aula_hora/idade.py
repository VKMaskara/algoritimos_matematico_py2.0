import datetime
data_nasc = input("Digite uma data no formato AAAA/MM/DD: ")
# Dividir a string para obter ano, mês e dia
ano, mes, dia = map(int, data_nasc.split('/'))

# Criar a data a partir dos valores fornecidos
data_id = datetime.date(ano, mes, dia)

data_atual = datetime.date.today()

idade_dias = data_atual - data_id

idade_anos = idade_dias.days // 365  # Aproximação para idade em anos

# Imprimir os valores
print(idade_anos)

print(30 * '-') # linha separadora02