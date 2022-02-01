import maya.cmds as cmds
import MRA_library_variableNames_v01 as VARS 
import MRA_namingPipeline_v01 as NP

reload(VARS)
reload(NP)
def undo_publish_groups():
    cmds.select(all=True)

    allObjs = cmds.ls(selection=True,dag=True, transforms=True)

    for o in allObjs:
        obj = NP.get_nice_name(o)
        if any(obj[2] in t for t in VARS.pipeline_groups) == True:
            cmds.setAttr( o + ".tx",k=True)
            cmds.setAttr( o + ".ty",k=True)
            cmds.setAttr( o + ".tz",k=True)
            cmds.setAttr( o + ".rx",k=True)
            cmds.setAttr( o + ".ry",k=True)
            cmds.setAttr( o + ".rz",k=True)
            cmds.setAttr( o + ".sx",k=True)
            cmds.setAttr( o + ".sy",k=True)
            cmds.setAttr( o + ".sz",k=True)
            cmds.setAttr( o + ".v",k=True)

            cmds.setAttr( o + ".tx",l=False)
            cmds.setAttr( o + ".ty",l=False)
            cmds.setAttr( o + ".tz",l=False)
            cmds.setAttr( o + ".rx",l=False)
            cmds.setAttr( o + ".ry",l=False)
            cmds.setAttr( o + ".rz",l=False)
            cmds.setAttr( o + ".sx",l=False)
            cmds.setAttr( o + ".sy",l=False)
            cmds.setAttr( o + ".sz",l=False)
            cmds.setAttr( o + ".v",l=False)

