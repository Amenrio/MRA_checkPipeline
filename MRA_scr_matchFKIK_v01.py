import maya.cmds as cmds

fkChain = ["ctl_c_spineFKDw","ctl_c_spineFKMd","ctl_c_spineFKUp"]
ikChain = ["ctl_c_spineDw","ctl_c_spineMd","ctl_c_spineUp"]
toolkitChain = ["lct_c_matchSpineDw","lct_c_matchSpineMd","lct_c_matchSpineUp"]
constraintChain = ["pans_c_grpCautoCtlCspineDwToctlCspineFKDw","pans_c_grpCautoAutoCtlCspineMdToctlCspineFKMd","pans_c_grpCautoCtlCspineUpToctlCspineFKUp"]

tempTranslate = [0.000,0.000,0.000]
tempRotate = [0.000,0.000,0.000]


def matchFKIK():
    i=0
    if cmds.getAttr("ctl_c_gravity.ChainControl") == 0:
        for o in ikChain:
            copyPosition(o, fkChain[i])
            
            i+=1
        weightConstraint(constraintChain,1)
        resetPosition(ikChain)
        
        
        

    i=0
    if cmds.getAttr("ctl_c_gravity.ChainControl") == 1:
        weightConstraint(constraintChain,0)
        for o in toolkitChain:
            copyPosition(o, ikChain[i])
            
            i+=1
        resetPosition(fkChain)
        
        
            


def copyPosition(targetChain, newChain):
    tempTranslate = cmds.xform (targetChain , q = True , ws = True , t = True )
    tempRotate = cmds.xform (targetChain , q = True , ws = True , ro = True )
    cmds.xform (newChain , ws = True , t = tempTranslate )
    cmds.xform (newChain , ws = True , ro = tempRotate )
          
    

def resetPosition(chain):
    for o in chain:
        cmds.setAttr(o + ".translateX",0)
        cmds.setAttr(o + ".translateY",0)
        cmds.setAttr(o + ".translateZ",0)

        cmds.setAttr(o + ".rotateX", 0)
        cmds.setAttr(o + ".rotateY", 0)
        cmds.setAttr(o + ".rotateZ", 0)

def weightConstraint(chain, value):
    for c in constraintChain:
        cmds.setAttr(c + ".Weight0",value)

cmds.scriptJob(attributeChange = ["ctl_c_gravity.ChainControl",matchFKIK])