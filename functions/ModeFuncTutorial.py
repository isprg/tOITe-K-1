import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Tutorial(dictProc):
    dictProc_this = {
        "TUTORIAL_0": procTutorial_0,
        "TUTORIAL_1": procTutorial_1,
        "TUTORIAL_2": procTutorial_2,
        "TUTORIAL_3": procTutorial_3,
        "TUTORIAL_4": procTutorial_4,
        "TUTORIAL_5": procTutorial_5,
    }
    return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Tutorial(dictWindow):
    layout0 = make_fullimage_layout("png/tutorial00.png", "TUTORIAL0")
    layout1 = make_fullimage_layout("png/tutorial01.png", "TUTORIAL1")
    layout2 = make_fullimage_layout("png/tutorial02.png", "TUTORIAL2")
    layout3 = make_fullimage_layout("png/tutorial03.png", "TUTORIAL3")
    layout4 = make_fullimage_layout("png/tutorial04.png", "TUTORIAL4")
    layout5 = make_fullimage_layout("png/tutorial05.png", "TUTORIAL5")

    dictLayout = {
        "TUTORIAL_0": layout0,
        "TUTORIAL_1": layout1,
        "TUTORIAL_2": layout2,
        "TUTORIAL_3": layout3,
        "TUTORIAL_4": layout4,
        "TUTORIAL_5": layout5,
    }
    dictWindow_this = setGUI(dictLayout)

    return dict(dictWindow, **dictWindow_this)


# 標準タップ座標設定 ================================================
def getDefaultAreaDefinition():
    vArea0 = [0, 0, 0, 0]
    listArea = [vArea0]

    return listArea


def procTutorial_0(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_0":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("TUTORIAL_1")
            dictArgument["Start time"] = sStartTime


def procTutorial_1(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_1":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        PlaySound("sound/call.wav")

        if sTappedArea == 0:
            sStartTime = cState.updateState("TUTORIAL_2")
            dictArgument["Start time"] = sStartTime


def procTutorial_2(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_2":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("TUTORIAL_3")
            dictArgument["Start time"] = sStartTime


def procTutorial_3(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_3":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        PlaySound("sound/tutorial1.wav")

        if sTappedArea == 0:
            sStartTime = cState.updateState("TUTORIAL_4")
            dictArgument["Start time"] = sStartTime


def procTutorial_4(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_4":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        PlaySound("sound/tutorial2.wav")

        if sTappedArea == 0:
            sStartTime = cState.updateState("TUTORIAL_5")
            dictArgument["Start time"] = sStartTime


def procTutorial_5(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_5":
        pass
