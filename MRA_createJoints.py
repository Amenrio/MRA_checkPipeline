import maya.cmds as cmds

lct_arms = ["clavicle","upperArm", "lowerArm", "hand"]
lct_spine = ["pelvis","spine00", "spine01", "spine02", "spine03", "spine04","chest","chestExtra"]
lct_legs = ["upperLeg","lowerLeg","foot","toe","toeEnd"]
pelvis = "lct_c_pelvis"
chestExtra = "lct_c_chestExtra"
limb = ["Arm", "Leg"]
grps = ["grp_x_skin","grp_x_ctl","grp_x_toolkit"]
lct_armPosition = []
lct_legsPosition = []
jointList = []

side = [ "l", "r"]
groups = ["rig","skin","ctl","toolkit"]
def create_chain(chain_list,position_list,chain_name,side):
    idx=0
    jointList = []
    for pos in position_list:
        newPosition = pos    
        jointList.append(cmds.joint(name = "skin_{}_{}".format(side,chain_list[idx]), position = newPosition))
        idx += 1
        for j in jointList:
            cmds.joint(j, e=True,oj="xzy",sao="zup", ch=True, zso=True)
            cmds.joint(jointList[-1],e=True,oj="none",zso=True)
    cmds.select(clear=True)


def createSymmetryGrp(chain_list,location,symmetry,scaleOffset,chain_name):
    symmetry_name = "grp_{}_skinSymmetry{}".format(location,chain_name)
    cmds.group(empty=True ,a=True, name=symmetry_name)
    sym_position = cmds.xform(symmetry, q = True , ws = True , m=True)
    cmds.xform(symmetry_name,ws = True , m = sym_position)
    cmds.parent("skin_{}_{}".format(location,chain_list[0]),symmetry_name)
    if location is "r":
        cmds.setAttr("{}.scale{}".format(symmetry_name,scaleOffset),-1)
        if chain_name== limb[0]:
            cmds.rename("{}".format(symmetry_name),"grp_r_skinSymmetryArm")
        elif chain_name== limb[1]:
            cmds.rename("{}".format(symmetry_name),"grp_r_skinSymmetryLeg")
    cmds.select(clear=True)
    

def getLctPositions(s,listNames):
    list_positions = []
    for l in listNames:
        pos = cmds.xform("lct_{}_{}".format(s,l), q=True, translation=True)
        list_positions.append(pos)
    return list_positions

def parent_everything():
    jnts = ["pelvis"]
    for g in grps:
        cmds.parent(g, "grp_x_rig")
    cmds.select(clear=True)
    cmds.parent("skin_c_root","grp_x_skin")
    cmds.parent("skin_c_pelvis","skin_c_root")
    for s in side:
        cmds.parent("grp_{}_skinSymmetryArm".format(s),"skin_c_chestExtra")
        cmds.parent("grp_{}_skinSymmetryLeg".format(s),"skin_c_pelvis")

#Cacho de codigo reutilizado gracias Angel o/
def zeroOrient(o):
    if cmds.nodeType(o) == 'joint':

        valueX = cmds.getAttr(o + '.jointOrientX')
        valueY = cmds.getAttr(o + '.jointOrientY')
        valueZ = cmds.getAttr(o + '.jointOrientZ')		
        
        cmds.setAttr(o + '.rotateX' , valueX)	
        cmds.setAttr(o + '.rotateY' , valueY)
        cmds.setAttr(o + '.rotateZ' , valueZ)
            
        cmds.setAttr(o + '.jointOrientX' , 0)
        cmds.setAttr(o + '.jointOrientY' , 0)
        cmds.setAttr(o + '.jointOrientZ' ,0)


def create_bending_joints(joint1, joint2):
    pos1 = cmds.xform(joint1, q = True, t = True)
    pos2 = cmds.xform(joint2, q = True, t = True)
    jointList = []
    posBend01 = (pos1 + pos2) /2
    posBend00 = (pos1 + posBend01) / 2
    posBend02 = (pos2 + posBend01) / 2
    bendPosition = [posBend00,posBend01,posBend02]
    for b in bendPosition:

        jointList.append(cmds.joint(name="skin_l_{}Bend",position = b))
    for j in jointList:
        cmds.joint(j, e=True,oj="xzy",sao="zup", ch=True, zso=True)
        cmds.joint(jointList[-1],e=True,oj="none",zso=True)
    cmds.select(clear=True)

def run():

    for g in groups:
        cmds.group(empty=True ,a=True, name="grp_x_{}".format(g))
    
    cmds.joint(name="skin_c_root")
    zeroOrient("skin_c_root")
    cmds.select(clear=True)
    
    lct_armPosition = getLctPositions("l",lct_arms)
    lct_legsPosition = getLctPositions("l",lct_legs)
    lct_spinePosition = getLctPositions("c",lct_spine)
    create_chain(lct_spine, lct_spinePosition, "Spine","c")
    for s in side:
        create_chain(lct_arms,lct_armPosition, limb[0],s)
        create_chain(lct_legs, lct_legsPosition, limb[1],s)
   
    for s in side:
        createSymmetryGrp(lct_arms,s,chestExtra,"X",limb[0])
        createSymmetryGrp(lct_legs,s,pelvis,"X",limb[1])
    create_bending_joints("skin_l_upperArm","skin_l_LowerArm")
    parent_everything()
    cmds.select(all=True,hi=True)
    joints = cmds.ls(selection=True)
    for o in joints:
        zeroOrient(o)