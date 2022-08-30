import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Final(dictProc):
    dictProc_this = {
        "FINAL_0": procFinal_0,
        "FINAL_1": procFinal_1,
        "FINAL_2_WRONG": procFinal_2_wrong,
        "FINAL_2_CORRECT": procFinal_2_correct,
        "FINAL_3": procFinal_3,
        "FINAL_4": procFinal_4,
        "FINAL_5": procFinal_5,
    }
    return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Final(dictWindow):
    layout0 = make_fullimage_layout("png/final00.png", "FINAL_0")
    layout1 = make_fullimage_layout("png/final01.png", "FINAL_1")
    layout2wrong = make_fullimage_layout(
        "png/final02wrong.png", "FINAL_2_WRONG")
    layout2correct = make_fullimage_layout(
        "png/final02correct.png", "FINAL_2_CORRECT")
    layout3 = make_fullimage_layout("png/final03.png", "FINAL_3")
    layout4 = make_fullimage_layout("png/final04.png", "FINAL_4")
    layout5 = make_fullimage_layout("png/final05.png", "FINAL_5")

    dictLayout = {
        "FINAL_0": layout0,
        "FINAL_1": layout1,
        "FINAL_2_WRONG": layout2wrong,
        "FINAL_2_CORRECT": layout2correct,
        "FINAL_3": layout3,
        "FINAL_4": layout4,
        "FINAL_5": layout5,
    }
    dictWindow_this = setGUI(dictLayout)

    return dict(dictWindow, **dictWindow_this)


# 標準タップ座標設定 ================================================
def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


# 電話タップ座標設定 ================================================
def getCallAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    vArea1 = [0, 0, 0, 0]
    vArea2 = [0, 0, 0, 0]
    vArea3 = [0, 0, 0, 0]
    vArea4 = [0, 0, 0, 0]
    vArea5 = [0, 0, 0, 0]
    vArea6 = [0, 0, 0, 0]
    vArea7 = [0, 0, 0, 0]
    vArea8 = [0, 0, 0, 0]
    vArea9 = [0, 0, 0, 0]

    listArea = [vArea0, vArea1, vArea2, vArea3,
                vArea4, vArea5, vArea6, vArea7, vArea8, vArea9]

    return listArea


# 最終問題タイトル
def procFinal_0(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

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
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_1":
        # TODO: 繰り返し処理
        isCorrect = False
        phoneNumber = []

        for _ in range(3):
            vPosition = pyautogui.position()
            listArea = getCallAreaDefinition()
            sTappedArea = CheckTappedArea(vPosition, listArea)
            print(sTappedArea)

            if sTappedArea == 0:  # 電話をかけるをタップ
                if isCorrect:
                    sStartTime = cState.updateState("FINAL_2_CORRECT")
                    dictArgument["Start time"] = sStartTime
                elif len(phoneNumber) < 3:
                    pass
                else:
                    sStartTime = cState.updateState("FINAL_2_WRONG")
                    dictArgument["Start time"] = sStartTime
            elif sTappedArea != -1:
                phoneNumber.append(sTappedArea)
            else:
                continue


# 電話番号不正解
def procFinal_2_wrong(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_2_WRONG":
        PlaySound("sound/wrong.wav")

        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("FINAL_0")
            dictArgument["Start time"] = sStartTime


# 電話番号正解
def procFinal_2_correct(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_2_CORRECT":
        PlaySound("sound/call.wav")
        PlaySound("sound/final1.wav")

        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("FINAL_3")
            dictArgument["Start time"] = sStartTime


# 合言葉話す
def procFinal_3(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_3":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("FINAL_4")
            dictArgument["Start time"] = sStartTime


def procFinal_4(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_4":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:
            sStartTime = cState.updateState("FINAL_5")
            dictArgument["Start time"] = sStartTime


def procFinal_5(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "FINAL_5":
        pass
