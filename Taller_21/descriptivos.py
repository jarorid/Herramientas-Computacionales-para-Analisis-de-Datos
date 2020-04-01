import pandas as pd
import util
import CoreModels as cm

DF = pd.read_csv("ProyeccionesPension.csv")

numeric, text_ob, unident = util.inspeccion(DF)

DF = util.faltantes(DF, numeric, text_ob)

print("Indices columnas numericas:\n")
for i in range(len(DF.columns)):
	if DF.columns[i] in numeric:
		print( (i, DF.columns[i]) )
print("\n")

indep_candid = [2, 5, 6]
dep = [4, 3]

mod = cm.seleccion_vars(DF, dep, indep_candid)

