#3.0 model pull pricing from publix and wallmart and calculate expected bill.
#system recommends stapple do you need x x and x while you are out. Yes adds them all to cart.
#take snapshot of webscrap so program always works.


#Version 1.0

import random
from PySide2 import QtCore, QtWidgets, QtGui

class StapleIngredients:
    def __init__ (self):
        self.salt_dict = salt_dict
        self.gar_pow_dict = gar_pow_dict
        self.pepper_dict = pepper_dict


salt_dict = {"salt1":("Generic", "10 oz", 1.99), "salt2": ("Salters", "10 oz", 3.75)}
gar_pow_dict = {"garlic1":("Generic", "5 oz", 2.99), "garlic2":("Mrs. Dash", "6 oz", 4.00)}
pepper_dict = {"pep1": ("Generic", "15 oz", 2.99), "pep2": ("Pepemenselly", "15 oz", 5.99)}


#place block inside a function
StapleI = StapleIngredients()
print (StapleI.salt_dict["salt1"])

salt1_price = (StapleI.salt_dict["salt1"])
salt1_price = salt1_price[2]

print (salt1_price)
#block end


class Meats:
    #without init
        beef_cheap = {"skirt steak": [ "Skirt Steak", "Per Pound", 2.33]} #per pound price
        beef_premium = {"Porter House": ["14 oz","Per Steak", 44.44]} #single steak

Proteins = Meats()
per_pound_calculator = 1 #dummy value until gui placed
print (Proteins.beef_cheap["skirt steak"])
low_beef = Proteins.beef_cheap["skirt steak"]
low_beef = low_beef[2] * per_pound_calculator #calculating price after pounds needed

print (Proteins.beef_premium["Porter House"])
high_beef = (Proteins.beef_premium["Porter House"])
high_beef = high_beef[2]

