import MRA_library_variableNames_v01 as VARS

skinChain = "pene"

if skinChain not in VARS.naming_maya.values() :
    print("Encontrado")
else:
    print("No encontrado")
