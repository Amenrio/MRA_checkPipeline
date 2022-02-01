'''A simple example of a custom marking menu in Maya. The benefits of doing it this way with Python are that 
it is very flexible and easily maintainable. Additionally, you can keep it in a version control system.
This file is used for demonstration purposes, to be followed along with in this blog post
http://bindpose.com/custom-marking-menu-maya-python/
'''
import maya.cmds as cmds
import MRA_scr_rig_addConstraints_v01
MENU_NAME = "markingMenu"


class markingMenu():
    '''The main class, which encapsulates everything we need to build and rebuild our marking menu. All
    that is done in the constructor, so all we need to do in order to build/update our marking menu is
    to initialize this class.'''

    def __init__(self):

        self._removeOld()
        self._build()

    def _build(self):
        '''Creates the marking menu context and calls the _buildMarkingMenu() method to populate it with all items.'''
        menu = cmds.popupMenu(MENU_NAME, mm=1, b=3, aob=1, ctl=1, alt=1,
                              sh=0, p="viewPanes", pmo=1, pmc=self._buildMarkingMenu)

    def _removeOld(self):
        '''Checks if there is a marking menu with the given name and if so deletes it to prepare for creating a new one.
        We do this in order to be able to easily update our marking menus.'''
        if cmds.popupMenu(MENU_NAME, ex=1):
            cmds.deleteUI(MENU_NAME)

    def _buildMarkingMenu(self, menu, parent):
        '''This is where all the elements of the marking menu our built.'''

        # Radial positioned
        cmds.menuItem(p=menu, l="South West Button",
                      rp="SW", c="print 'SouthWest'")
        cmds.menuItem(p=menu, l="AJX Add Constraints",
                      i="menuIconAdd.png", rp="SE", c=importAJX_Constraints)
        cmds.menuItem(p=menu, l="MRA Add Constraints", rp="NE",
                      i="C:/Users/Amenrio/Documents/maya/2022/prefs/icons/MRA.png", c=importMRA_Constraints)

        subMenu = cmds.menuItem(p=menu, l="North Sub Menu", rp="N", subMenu=1)
        cmds.menuItem(p=subMenu, l="North Sub Menu Item 1")
        cmds.menuItem(p=subMenu, l="North Sub Menu Item 2")

        cmds.menuItem(p=menu, l="South", rp="S", c="print 'South'")
        cmds.menuItem(p=menu, ob=1, c="print 'South with Options'")

        # List

        cmds.menuItem(p=menu, l="Bind Skin",
                      i="smoothSkin.png", c="cmds.bindSkin()")
        cmds.menuItem(p=menu, ob=1, c="cmds.SmoothBindSkinOptions()")
        cmds.menuItem(p=menu, l="Paint Skin Weights",
                      c="cmds.ArtPaintSkinWeightsToolOptions()", i="paintSkinWeights.png")
        cmds.menuItem(p=menu, l="Add Influence",
                      c="cmds.AddInfluence()", i="addWrapInfluence.png")
        cmds.menuItem(p=menu, ob=1, c="cmds.AddInfluenceOptions()")
        cmds.menuItem(p=menu, l="Remove Influence",
                      c="cmds.RemoveInfluence()", i="removeWrapInfluence.png")
        cmds.menuItem(p=menu, l="Unbind Skin",
                      c="cmds.DetachSkin()", i="detachSkin.png")
        cmds.menuItem(p=menu, d=True, dl="BindSkin Options")

        # Rebuild
        cmds.menuItem(p=menu, l="Rebuild Marking Menu", c=rebuildMarkingMenu)


def run():
    markingMenu()


def importAJX_Constraints(*args):
    import AJX_scr_rig_addConstraints_v02
    reload(AJX_scr_rig_addConstraints_v02)
    AJX_scr_rig_addConstraints_v02.run()


def importMRA_Constraints(*args):

    reload(MRA_scr_rig_addConstraints_v01)
    MRA_scr_rig_addConstraints_v01.run()


def exampleFunction(*args):
    '''Example function to demonstrate how to pass functions to menuItems'''
    print("example function")


def rebuildMarkingMenu(*args):
    '''This function assumes that this file has been imported in the userSetup.py
    and all it does is reload the module and initialize the markingMenu class which
    rebuilds our marking menu'''
    cmds.evalDeferred("""
reload(MRA_markingMenu)
MRA_markingMenu.run()
""")
