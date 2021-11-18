"Programa como entrada o tipo do vôo (N-noturno/D-diurno)"
"D<=50 R$200 / D>50 R$120"
"N<=50 R$100 / N>50 R$80"
"total = passageiros x tarifa"
#input
print("Vamos descobrir a tarifa e o total a ser pago")
print("Digite 'D' para vôos diurnos e 'N' para noturnos")
tipo=input("Informe o tipo de vôo: ").upper()
pessoas=int(input("Agora, digite o número de passageiros: "))
total = 0
#processo
if (tipo=="D") and (pessoas <=50):
    total = pessoas * 200 
    print("A tarifa será de R$200")
elif (tipo=="D") and (pessoas >50):
    total = pessoas * 120
    print("A tarifa será de R$120")
elif (tipo=="N") and (pessoas <=50):
    total = pessoas * 100
    print("A tarifa será de R$100")
else:
    (tipo=="N") and (pessoas >50)
    total = pessoas * 80
    print("A tarifa será de R$80")

print("O total a ser pago é: R$",format(total,".2f"),"reais.")    
    
