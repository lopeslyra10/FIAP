faturamento = 1200
custo = 700 

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.10
lucro = faturamento - custo - imposto

margem_lucro = lucro / custo - imposto

print('o faturamento é de: ', faturamento)
print('o custo é de: ', custo)
print('O lucro foi de: ', lucro)
print('A margem de lucro foi de: ', margem_lucro)

tempo_contrato = 170
tempo_contrato_anos = 170 / 12
print('O tempo de contrato em anos foi de: ', int(tempo_contrato_anos))
tempo_contrato_meses = 170 % 12 
print('O tempo de contrato em meses foi de: ', tempo_contrato_meses)