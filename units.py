""" 
UNIT TRANSFORMATIONS
Just a bunch of functions for quick unit transformations.
2019
"""
def cctk2cgs(cctk, unit, M=1):
	"""Converts cctk quantity to cgs, for a given mass scale M
	cctk units assume c = G = M_sun = 1

	Arguments:
	cctk (float) : cctk quantity to transform
	unit (string) : nature of the unit to transform
	M (float) : optional, in solar masses, scales the conversion by the mass of the system

    	Returns:
    	cgs (float) : cgs quantity transformed

   	"""
	cactusM = 5.028916268544129e-34 / M
	cactusL = 6.772400341316594e-6 / M
	cactusT = 2.0303145448833407e5 / M
	if(unit == 'length' or unit == 'distance'):
		cgs = cctk / cactusL
	elif(unit == 'time'):
		cgs = cctk / cactusT
	elif(unit == 'mass'):
		cgs = cctk / cactusM
	elif(unit == 'density'):
		cgs = cctk * (cactusL * cactusL * cactusL) / cactusM
	elif(unit == 'energy density'):
		cgs = cctk * (cactusL * cactusT * cactusT) / cactusM
	else:
		print("ERROR: Unknown unit.")
		return
	return cgs

def cgs2cctk(cgs, unit, M=1):
	"""Converts cgs quantity to cctk, for a given mass scale M
	cctk units assume c = G = M_sun = 1

	Arguments:
    	cgs (float) : cgs quantity to transform
	unit (string) : nature of the unit to transform
	M (float) : optional, in solar masses, scales the conversion by the mass of the system

    	Returns:
    	cctk (float) : cctk quantity transformed

   	"""
	cactusM = 5.028916268544129e-34 / M
	cactusL = 6.772400341316594e-6 / M
	cactusT = 2.0303145448833407e5 / M
	if(unit == 'length' or unit == 'distance'):
		cctk = cgs * cactusL
	elif(unit == 'time'):
		cctk = cgs * cactusT
	elif(unit == 'mass'):
		cctk = cgs * cactusM
	elif(unit == 'density'):
		cctk = cgs * cactusM / (cactusL * cactusL * cactusL)
	elif(unit == 'energy density'):
		cctk = cgs * cactusM / (cactusL * cactusT * cactusT)
	else:
		print("ERROR: Unknown unit.")
		return
	return cctk

def cm2pc(cm):
	return cm / 3.08567758128e+18

def s2year(s):
	return s / 3.154e+7
