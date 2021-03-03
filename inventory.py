## TODO: Need to implement unmarshalling json to variables
import json as j
import os

## baby steps! Using realpython to relearn a ton of this stuff ;P
with open("itemList.json","r") as read_file:

## Class Inventory will initialize with basic user gear - weapon fist, gear tattered clothing
class Inventory:
    def __init__(self, inv):
        inv = [100,2]

## TODO: METHODS FOR INVENTORY CLASS - GET INVENTORY, ADD TO INVENTORY, REMOVE FROM INVENTORY 

    # Getter for retrieving inventory data 
    def getInv(self, inv):
        return self.inv
