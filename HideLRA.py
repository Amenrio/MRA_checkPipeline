import maya.cmds as cmds

selection = cmds.select(all=True)

obj = cmds.ls(selection=True, dag=True, transforms=True)

for o in obj:
    if cmds.getAttr(o + ".displayLocalAxis") › 0:
        cmds.setAttr(o + ".displayLocalAxis", 0)
