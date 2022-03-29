import maya.cmds as cmds
import MRA_library_variableNames_v01 as VARS 
import MRA_namingPipeline_v01 as NP

reload(VARS)
reload(NP)
def publishGroups():
    

    allObjs = cmds.ls(selection=True,dag=True, transforms=True)

    if not allObjs:
        cmds.select(all=True)
        allObjs = cmds.ls(selection=True,dag=True, transforms=True)

    for o in allObjs:
        obj = NP.get_nice_name(o)
        if any(obj[2] in t for t in VARS.pipeline_groups) == True:
            cmds.setAttr( o + ".tx",k=False,cb=False)
            cmds.setAttr( o + ".ty",k=False,cb=False)
            cmds.setAttr( o + ".tz",k=False,cb=False)
            cmds.setAttr( o + ".rx",k=False,cb=False)
            cmds.setAttr( o + ".ry",k=False,cb=False)
            cmds.setAttr( o + ".rz",k=False,cb=False)
            cmds.setAttr( o + ".sx",k=False,cb=False)
            cmds.setAttr( o + ".sy",k=False,cb=False)
            cmds.setAttr( o + ".sz",k=False,cb=False)
            cmds.setAttr( o + ".v",k=False,cb=False)

            cmds.setAttr( o + ".tx",l=True,cb=False)
            cmds.setAttr( o + ".ty",l=True,cb=False)
            cmds.setAttr( o + ".tz",l=True,cb=False)
            cmds.setAttr( o + ".rx",l=True,cb=False)
            cmds.setAttr( o + ".ry",l=True,cb=False)
            cmds.setAttr( o + ".rz",l=True,cb=False)
            cmds.setAttr( o + ".sx",l=True,cb=False)
            cmds.setAttr( o + ".sy",l=True,cb=False)
            cmds.setAttr( o + ".sz",l=True,cb=False)
            cmds.setAttr( o + ".v",l=True,cb=False)

