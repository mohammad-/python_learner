#!/usr/bin/python
#Learning things about dictionary.
address = {
            "Pincode":"272-0112",
            "Country":"Japan",
            "State":"Chiba",
            "City":"Ichikawa",
            "Street":"Shioyaki 2-1-35",
            "Other":"Copo-Sunrse 105"
            }

print address["Pincode"],
print address["Country"],
print address["State"],address["City"],address["Street"],address["Other"]

newAddress = {}
newAddress["Pincode"] = raw_input("Enter Pincode > ")
newAddress["Country"] = raw_input("Enter Country > ")
newAddress["State"] = raw_input("Enter State > ")
newAddress["City"] = raw_input("Enter City > ")
newAddress["Street"] = raw_input("Enter Street > ")
newAddress["Other"] = raw_input("Enter Other > ")

for key,val in newAddress.items():
    print "%s %s" %(key,val),

print ""

del newAddress["Pincode"]
for key,val in newAddress.items():
    print "%s %s" %(key,val),
