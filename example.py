# -*- coding: utf-8 -*-
"""
    Created: 10/03/2020
    Last modification: 10/03/2020

    @creator: Corentin J

    Brief: Example file
"""

#-- Import --#
import EC
#- End Import -#

if __name__ == '__main__':
	# Instanciating M-511 curve object
	nM511=2**508 + 10724754759635747624044531514068121842070756627434833028965540808827675062043
	CM511 = EC.EllipticCurve("M-511", nM511, 2**511 - 187, [530438,1,0])

	# Instantiating generator for the group of points of M-511 curve
	GM511 = EC.Point(CM511, 0x5, 0x2fbdc0ad8530803d28fdbad354bb488d32399ac1cf8f6e01ee3f96389b90c809422b9429e8a43dbf49308ac4455940abe9f1dbca542093a895e30a64af056fa5)

	# Instanciating infinite point (zero element for +)
	Z = EC.Point(CM511)
	print(Z + GM511 == GM511)

	# Testing efficiency of multiplication by large integers
	n = 654656845357984954675767598651271325802657127103756757421371765121076751076571757257965331197796511321646517
	P = n * GM511
	Q = P - GM511
	print(Q == (n - 1) * GM511)

	# Multiplying by order results in the infinity point (zero element for +)
	print(nM511 * GM511 == Z)
	print(nM511 * P == Z)
	print(nM511 * Q == Z)
	print(265321 * Z == Z)

