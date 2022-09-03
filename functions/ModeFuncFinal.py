from logging import getLogger

import pyautogui

from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout

logger = getLogger("tOITe-K-1").getChild("Final")


# 処理の辞書割り当て ======================================================
def updateDictProc_Final(dictProc):
    dictProc_this = {
        "FINAL_0": procFinal_0,
        "FINAL_1": procFinal_1,
        "FINAL_1_WRONG": procFinal_1_wrong,
        "FINAL_1_CORRECT": procFinal_1_correct,
        "FINAL_2": procFinal_2,
        "FINAL_3": procFinal_3,
        "FINAL_3_WRONG": procFinal_3_wrong,
    }
    return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Final(dictWindow):
    layout0 = make_fullimage_layout("png/final00.png", "FINAL_0")
    layout1 = make_fullimage_layout("png/final01.png", "FINAL_1")
    layout1wrong = make_fullimage_layout(
        "png/final01wrong.png", "FINAL_1_WRONG")
    layout1correct = make_fullimage_layout(
        "png/final01correct.png", "FINAL_1_CORRECT")
    layout2 = make_fullimage_layout("png/final02.png", "FINAL_2")
    layout3 = make_fullimage_layout(
        "png/final03.png", "FINAL_3")
    layout3wrong = make_fullimage_layout(
        "png/final03wrong.png", "FINAL_3_WRONG")

    dictLayout = {
        "FINAL_0": layout0,
        "FINAL_1": layout1,
        "FINAL_1_WRONG": layout1wrong,
        "FINAL_1_CORRECT": layout1correct,
        "FINAL_2": layout2,
        "FINAL_3": layout3,
        "FINAL_3_WRONG": layout3wrong,
    }
    dictWindow_this = setGUI(dictLayout)

    return dict(dictWindow, **dictWindow_this)


# 標準タップ座標設定 ================================================
def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


# 4択タップ座標設定
def get4ChoiceAreaDefinition():
    vArea0 = [40, 310, 400, 100]
    vArea1 = [500, 310, 400, 100]
    vArea2 = [40, 460, 400, 100]
    vArea3 = [500, 460, 400, 100]
    listArea = [vArea0, vArea1, vArea2, vArea3]

    return listArea


# 電話タップ座標設定 ================================================
def getCallAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    vArea1 = [260, 80, 170, 130]
    vArea2 = [430, 80, 170, 130]
    vArea3 = [600, 80, 170, 130]
    vArea4 = [260, 210, 170, 130]
    vArea5 = [430, 210, 170, 130]
    vArea6 = [600, 210, 170, 130]
    vArea7 = [260, 340, 170, 130]
    vArea8 = [430, 340, 170, 130]
    vArea9 = [600, 340, 170, 130]

    listArea = [vArea0, vArea1, vArea2, vArea3,
                vArea4, vArea5, vArea6, vArea7, vArea8, vArea9]

    return listArea


# 最終問題タイトル
def procFinal_0(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_0":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 答えるをタップ
            sStartTime = cState.updateState("FINAL_1")
            dictArgument["Start time"] = sStartTime


# 電話番号入力
def procFinal_1(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    listCorrectNumber = [1, 9, 2, 8]

    if dictArgument["Option"] == 0 or dictArgument["Option"][0] == 0:
        dictArgument["Option"] = [0, 0, 0, 0, 0]

    if event == "FINAL_1":
        vPosition = pyautogui.position()
        listArea = getCallAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea >= 1:
            PlaySound("sound/button1.wav")
            if dictArgument["Option"][0] < 4:
                dictArgument["Option"][dictArgument["Option"]
                                       [0] + 1] = sTappedArea
                dictArgument["Option"][0] += 1
            else:
                PlaySound("sound/wrong.wav")
                sStartTime = cState.updateState("FINAL_1_WRONG")
                dictArgument["Start time"] = sStartTime
            print(dictArgument["Option"])

        elif sTappedArea == 0:
            dictArgument["Option"][0] = 0
            if dictArgument["Option"][1:5] == listCorrectNumber:
                PlaySound("sound/call.wav")
                PlaySound("sound/final1.wav")
                sStartTime = cState.updateState("FINAL_1_CORRECT")
                dictArgument["Start time"] = sStartTime
            else:
                PlaySound("sound/wrong.wav")
                sStartTime = cState.updateState("FINAL_1_WRONG")
                dictArgument["Start time"] = sStartTime


# 電話番号正解
def procFinal_1_correct(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_1_CORRECT":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 答えるをタップ
            sStartTime = cState.updateState("SR_Q")  # 音声認識へ
            dictArgument["Start time"] = sStartTime


# 電話番号不正解
def procFinal_1_wrong(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_1_WRONG":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("FINAL_0")
            dictArgument["Start time"] = sStartTime


# Final 4,5
def procFinal_2(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_2":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 次へをタップ
            cCtrlCard.write_result("complete", "T")
            sStartTime = cState.updateState("CLEAR")
            dictArgument["Start time"] = sStartTime


# 不正解時の4択
def procFinal_3(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_3":
        vPosition = pyautogui.position()
        listArea = get4ChoiceAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 1:
            PlaySound("sound/correct.wav")
            PlaySound("sound/final23.wav")
            sStartTime = cState.updateState("SR_CORRECT")
            dictArgument["Start time"] = sStartTime
        elif sTappedArea == 0 or sTappedArea == 2 or sTappedArea == 3:
            PlaySound("sound/wrong.wav")
            sStartTime = cState.updateState("FINAL_3_WRONG")
            dictArgument["Start time"] = sStartTime


# 4択不正解
def procFinal_3_wrong(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_3_WRONG":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # もう一度答えるをタップ
            sStartTime = cState.updateState("FINAL_3")
            dictArgument["Start time"] = sStartTime
