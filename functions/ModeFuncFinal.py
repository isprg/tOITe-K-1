import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout, make_4choice_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Final(dictProc):
    dictProc_this = {
        "FINAL_0": procFinal_0,
        "FINAL_1": procFinal_1,
        "FINAL_1_WRONG": procFinal_1_wrong,
        "FINAL_1_CORRECT": procFinal_1_correct,
        "FINAL_2": procFinal_2,
        "FINAL_3": procFinal_3,
        "FINAL_4": procFinal_4,
        "FINAL_5": procFinal_5,
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

    dictLayout = {
        "FINAL_0": layout0,
        "FINAL_1": layout1,
        "FINAL_1_WRONG": layout1wrong,
        "FINAL_1_CORRECT": layout1correct,
        "FINAL_2": layout2,
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
                    PlaySound("sound/call.wav")
                    sStartTime = cState.updateState("FINAL_1_CORRECT")
                    dictArgument["Start time"] = sStartTime
                elif len(phoneNumber) < 3:
                    pass
                else:
                    PlaySound("sound/wrong.wav")
                    sStartTime = cState.updateState("FINAL_1_WRONG")
                    dictArgument["Start time"] = sStartTime
            elif sTappedArea != -1:
                phoneNumber.append(sTappedArea)
            else:
                continue

        # Test
        # vPosition = pyautogui.position()
        # listArea = getDefaultAreaDefinition()
        # sTappedArea = CheckTappedArea(vPosition, listArea)
        # print(sTappedArea)

        # if sTappedArea == 0:
        #     PlaySound("sound/call.wav")
        #     sStartTime = cState.updateState("FINAL_1_CORRECT")
        #     dictArgument["Start time"] = sStartTime


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


# 電話番号正解
def procFinal_1_correct(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]

    if event == "FINAL_1_CORRECT":
        PlaySound("sound/final1.wav")

        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 答えるをタップ
            sStartTime = cState.updateState("SR_Q")  # 音声認識へ
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


# Final クリア
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
            pass


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
