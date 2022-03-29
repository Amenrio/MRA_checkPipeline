import CheckPipeline.MRA_library_variableNames_v01 as VARS

LOC_DICT = {}
ID_DICT = {}

nodeID_position = 0
locFlag_position = 0

LE_WARNINGS = []

def pipelineANIM(isTrue):

    global nodeID_position
    global locFlag_position
    global ID_DICT
    global LOC_DICT

    if isTrue:
        nodeID_position = 0
        ID_DICT = {k:v for k, v in VARS.naming_maya.items()}
        locFlag_position = 1
        LOC_DICT = {k:v for k, v in VARS.location_flags.items()}
        print(LOC_DICT)
        print(nodeID_position)
        print(locFlag_position)
    else:
        
        nodeID_position = 2
        locFlag_position = 0
        ID_DICT = {k:v.upper() for k, v in VARS.naming_maya.items()}
        LOC_DICT = {k:v.upper() for k, v in VARS.location_flags.items()}
        print(ID_DICT)
        print(LOC_DICT)
        print(nodeID_position)
        print(locFlag_position)


def check_syntax(name_obj):
    obj = VARS.get_nice_name(name_obj)
    if len(obj) > 3:
        LE_WARNINGS.append(name_obj)
    else:
        # si obj[0] existe dentro de los valores del diccionario namingMaya
        if obj[nodeID_position] not in ID_DICT.values():
            LE_WARNINGS.append(name_obj)
            print("Else NODE ID position")
            print(LOC_DICT)
            print(nodeID_position)
            print(locFlag_position)

        # si obj[1] existe dentro de los valores del diccionario LOC_FLAG_POSITIONs
        elif obj[locFlag_position] not in LOC_DICT.values():

            LE_WARNINGS.append(name_obj)
            print("Else LOC_FLAG position")
            print(LOC_DICT)
            print(nodeID_position)
            print(locFlag_position)


if __name__=="__main__":
    ID_DICT.clear()
    LOC_DICT.clear()


    nodo = "R_jointArm_GRP"

    pipelineANIM(False)

    check_syntax(nodo)

    print(LE_WARNINGS)
    
    