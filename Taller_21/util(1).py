'''
	Useful functions for analysis

		- inspeccion
		- faltantes
'''
import numpy as np


def inspeccion(D):
	num, txt, unId = [], [], []
	for col in D.columns:
	    if (D[col].dtype == np.float64) or (D[col].dtype == np.int64):
	    	num.append(col)
	    elif (D[col].dtype == str) or (D[col].dtype == object):
	    	txt.append(col)
	    else:
	    	unId.append(col)
	print( "\nResumen Columnas" )
	print( "\tNumeric:\t" + str(len(num)) )
	print( "\tString: \t" + str(len(txt)) )
	print( "\tUniden.:\t" + str(len(unId)) )
	print("\n")

	return num, txt, unId


def faltantes(D, num, txt):
	nans = D.isnull().sum()
	for col in num:
		D[col].fillna( D[col].mean(skipna=True) )
	for col in txt:
		D[col].fillna( "" )
	return D

def obtener_mejor_R2( R ):
	primera_vez = True
	for r in R:
		if primera_vez:
			mejor = r
			valor = R[r]
			primera_vez = False

		if R[r] > valor:
			mejor = r
			valor = R[r]
	print("\t\tLas mejores variables fueron "+str(r)+" con un R2 de "+str(round(R[r],2)))
	print("\n")
	return r

