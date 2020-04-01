from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import normalize
from itertools import combinations
import util


def reg_lin(X, y):	
	reg = LinearRegression().fit(X, y)
	return reg.score(X, y), reg


def seleccion_vars(D, dep, ind):	
	comb = []
	for i in range(len(ind)):
		comb += combinations( ind, i+1 )

	modelo = {}
	for i in range(len(dep)):
		print("Probando modelos para la variable "+str( dep[i] ))
		R2 = {}
		M = {}
		var_y = D.iloc[:, dep[i] ].values
		for j in comb:
			sel = list(j)			
			var_X = D.iloc[:, sel].values

			R2[j], M[j] = reg_lin(var_X, var_y)

		j_mejor = util.obtener_mejor_R2( R2 )

		modelo[i] = M[ j_mejor ]

	return modelo

