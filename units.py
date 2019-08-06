""" 
UNIT TRANSFORMATIONS
Just a bunch of functions for quick unit transformations.
"""
def cctk2cgs(cctk, unit, M=1):
	"""Converts cctk quantity to cgs, for a given mass scale M
	CCTK UNITS
	Are geometrical units, ie c = G = 1, but the unit of length has been set to gravitational radius M
	Furthermore, the unit of M is the mass of the Sun (or a multiple M)

	Arguments:
	cctk (float) : cctk quantity to transform
	unit (string) : nature of the unit to transform
	M (float) : optional, in solar masses, scales the conversion by the mass of the system

    	Returns:
    	cgs (float) : cgs quantity transformed

   	"""
	g = 5.028916268544129e-34 / M
	cm = 6.772400341316594e-6 / M
	s = 2.0303145448833407e5 / M
	if(unit == 'length' or unit == 'distance'):
		cgs = cctk / cm
	elif(unit == 'time'):
		cgs = cctk / s
		print(cgs)
	elif(unit == 'mass'):
		cgs = cctk / g
	elif(unit == 'density'):
		cgs = cctk * (cm * cm * cm) / g
	elif(unit == 'energy density'):
		cgs = cctk * (cm * s * s) / g
	else:
		print("ERROR: Unknown unit.")
		return
	return cgs

def cgs2cctk(cgs, unit, M=1):
	"""Converts cgs quantity to cctk, for a given mass scale M
	CCTK UNITS
	Are geometrical units, ie c = G = 1, but the unit of length has been set to gravitational radius M
	Furthermore, the unit of M is the mass of the Sun (or a multiple M)

	Arguments:
    	cgs (float) : cgs quantity to transform
	unit (string) : nature of the unit to transform
	M (float) : optional, in solar masses, scales the conversion by the mass of the system

    	Returns:
    	cctk (float) : cctk quantity transformed

   	"""
	g = 5.028916268544129e-34 / M
	cm = 6.772400341316594e-6 / M
	s = 2.0303145448833407e5 / M
	if(unit == 'length' or unit == 'distance'):
		cctk = cgs * cm
	elif(unit == 'time'):
		cctk = cgs * s
	elif(unit == 'mass'):
		cctk = cgs * g
	elif(unit == 'density'):
		cctk = cgs * g / (cm * cm * cm)
	elif(unit == 'energy density'):
		cctk = cgs * g / (cm * cm * cm)
	else:
		print("ERROR: Unknown unit.")
		return
	return cctk

def cm2pc(cm):
	return cm / 3.08567758128e+18

def s2year(s):
	return s / 3.154e+7

def natural2cgs(natural,unit):
	"""Converts natural units quantity to cgs
	NATURAL UNITS FOR ASTROPHYSICIST: 
	Most measured in energy since: c = h_bar = k_B = 1, and the unit of E is 1eV
	The unit of charge is fixed by eps0 = 1/4pi, and given by q = sqrt(alpha)
	
	Arguments:
    	natural (float) : natural quantity to transform
	unit (string) : nature of the unit to transform

    	Returns:
    	cgs (float) : cgs quantity transformed

   	"""
	g = 1 / 1.78E-33
	cm = 1 / 1.97E-5
	s = 1 / 6.58E-16
	K = 1 / 1.16E4
	C = 1 / 1.88E-18

	if(unit == 'length' or unit == 'distance'):
		cgs = natural / cm
	elif(unit == 'time'):
		cgs = natural / s
	elif(unit == 'mass'):
		cgs = natural / g
	elif(unit == 'temperature'):
		cgs = natural / K
	elif(unit == 'electric charge'):
		cgs = natural / C # Actually we are returning Coulombs
	elif(unit == 'density'):
		cgs = natural * (cm * cm * cm) / g
	elif(unit == 'energy density'):
		cgs = cctk * (cm * s * s) / g
	else:
		print("ERROR: Unknown unit.")
		return
	return cgs

	
def cgs2natural(cgs,unit):
	"""Converts natural units quantity to cgs
	NATURAL UNITS FOR ASTROPHYSICIST: 
	Most measured in energy since: c = h_bar = k_B = 1, and the unit of E is 1eV
	The unit of charge is fixed by eps0 = 1/4pi, and given by q = sqrt(alpha)
	
	Arguments:
    	cgs (float) : cgs quantity to transform
	unit (string) : nature of the unit to transform

    	Returns:
    	natural (float) : natural quantity transformed

   	"""
	g = 1 / 1.78E-33
	cm = 1 / 1.97E-5
	s = 1 / 6.58E-16
	K = 1 / 1.16E4
	C = 1 / 1.88E-18

	if(unit == 'length' or unit == 'distance'):
		natural = cgs * cm
	elif(unit == 'time'):
		natural = cgs * s
	elif(unit == 'mass'):
		natural = cgs * g
	elif(unit == 'temperature'):
		natural = cgs * K
	elif(unit == 'electric charge'):
		natural = cgs * C # Actually we are returning Coulombs
	elif(unit == 'density'):
		natural = cgs * g / (cm * cm * cm)
	elif(unit == 'energy'):
		natural = cgs * g * cm * cm / (s * s) 
	elif(unit == 'energy density'):
		natural = cgs * g / (cm * s * s)
	else:
		print("ERROR: Unknown unit.")
		return
	return natural
	
