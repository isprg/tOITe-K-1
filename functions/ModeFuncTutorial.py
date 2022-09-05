from logging import getLogger

import pyautogui

from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea
from functions.DesignLayout import make_fullimage_layout

logger = getLogger("tOITe-K-1").getChild("Tutorial")


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
    layout0 = make_fullimage_layout("png/tutorial00.png", "TUTORIAL_0")
    layout1 = make_fullimage_layout("png/tutorial01.png", "TUTORIAL_1")
    layout2 = make_fullimage_layout("png/tutorial02.png", "TUTORIAL_2")
    layout3 = make_fullimage_layout("png/tutorial03.png", "TUTORIAL_3")
    layout4 = make_fullimage_layout("png/tutorial04.png", "TUTORIAL_4")
    layout5 = make_fullimage_layout("png/tutorial05.png", "TUTORIAL_5")

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


def getFullAreaDefinition():
    vArea0 = [0, 0, 0, 0]
    listArea = [vArea0, ]

    return listArea


# 標準タップ座標設定 ================================================
def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


# タイトル画面
def procTutorial_0(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "TUTORIAL_0":
        vPosition = pyautogui.position()
        listArea = getFullAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == -1:  # 次へをタップ
            PlaySound("sound/call.wav")
            sStartTime = cState.updateState("TUTORIAL_2")
            dictArgument["Start time"] = sStartTime


# コール音用 (未使用)
def procTutorial_1(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "TUTORIAL_1":
        PlaySound("sound/call.wav")
        sStartTime = cState.updateState("TUTORIAL_2")
        dictArgument["Start time"] = sStartTime


# 電話に出る
def procTutorial_2(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "TUTORIAL_2":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 電話に出るをタップ
            PlaySound("sound/tutorial1.wav")
            sStartTime = cState.updateState("TUTORIAL_3")
            dictArgument["Start time"] = sStartTime


# チュートリアル1
def procTutorial_3(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "TUTORIAL_3":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 次へをタップ
            PlaySound("sound/tutorial2.wav")
            sStartTime = cState.updateState("TUTORIAL_4")
            dictArgument["Start time"] = sStartTime


# チュートリアル2
def procTutorial_4(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL_4":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 次へをタップ
            cCtrlCard.write_result("tutorial", "T")
            sStartTime = cState.updateState("TUTORIAL_5")
            dictArgument["Start time"] = sStartTime


# カード除去指示
def procTutorial_5(dictArgument):
    event = dictArgument["Event"]

    if event == "TUTORIAL_5":
        pass
