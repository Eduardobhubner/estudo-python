seg = float(input("Por favor, entre com o número de segundos que deseja converter:"))

dia = int(seg // 86400)
rest_h = seg % 86400
h = int(rest_h // 3600)
rest_m = rest_h % 3600
m = int(rest_m // 60)
rest_s = rest_m % 60
segFinal = int(rest_s)

print(dia,"dias,",h,"horas,",m,"minutos e",segFinal,"segundos.")
