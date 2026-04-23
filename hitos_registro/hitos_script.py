#!/usr/bin/env python3
import datetime, time
import os, re

"""Entrada de datos y envio a registro con fecha en un .txt"""

comentario_int = input("Hito importante: ")
def registro_de_hitos(coment):
	fecha_conf = input("¿Agregar una fecha (Y) o dejar fecha de hoy (N)? (Y/N) ")
	fecha = fecha_conf.lower()
	if fecha == "n":
		fecha_hoy = time.localtime()
		fh = fecha_hoy
		fecha_out = datetime.datetime(year=fh[0],month=fh[1],day=fh[2])
	elif fecha == "y":
		dia = int(input("Ingresa el dia: "))
		mes = int(input("Ingresa el mes: "))
		año = int(input("Ingresa el año: "))
		fecha_out = datetime.datetime(year=año,month=mes,day=dia)
	else:
		registro_de_hitos(coment)
	fecha_regex = re.search(r"^\d*[-]\d*", str(fecha_out))
	name_report = "hitos-" + fecha_regex[0].rstrip() + ".txt"
	if os.path.isdir(name_report) == True:
		with open(name_report, "a") as file:
			file.write(fecha_out + "\n {}".format(coment))
	else:
		with open(name_report, "x") as file:
			file.write("Inicio de reporte con fecha de: {} \n\n".format(fecha_out) + coment)
	return "archivo {} creado".format(name_report)
print(registro_de_hitos(comentario_int))
