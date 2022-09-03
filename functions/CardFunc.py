from logging import getLogger

from functions.common import CheckEnding, isBlank

logger = getLogger("tOITe-K-1").getChild("CardFunc")


# ゲームの状態をカードに保存されているデータから設定
def SetGame_FromCard(dictArgument):
    cCtrlCard = dictArgument["CtrlCard"]
    cState = dictArgument["State"]

    dictSaveData = cCtrlCard.read_result()
    print("Save Data:", dictSaveData)

    if dictSaveData is not None and dictSaveData["complete"] == "T":
        sStartTime = cState.updateState("CLEAR")
        dictArgument["Start time"] = sStartTime

    elif dictSaveData["tutorial"] != "T":
        sStartTime = cState.updateState("FINAL_0")
        dictArgument["Start time"] = sStartTime

    elif CheckEnding(cCtrlCard):
        sStartTime = cState.updateState("FINAL_0")
        dictArgument["Start time"] = sStartTime

    elif isBlank(cCtrlCard):
        print("InitCard")
        cCtrlCard.initCard()

    else:
        sStartTime = cState.updateState("GO_OTHER_GAME")
        dictArgument["Start time"] = sStartTime


# カードの状態をチェック
def CheckCard(dictArgument):
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    # カードが存在するかをチェック
    result = cCtrlCard.check_exist()
    if result is False:
        print("Card Error")
        if cState.dictWindow[cState.strState] == "None":
            dictArgument["Return state"] = (cState.strState, True)
            # proc.closeWindows()
        else:
            dictArgument["Return state"] = (cState.strState, False)

        sStartTime = cState.updateState("CARD_ERROR")
        dictArgument["Start time"] = sStartTime

        return "CARD_ERROR"

    return cState.strState


# ゲーム終了用のカードかどうかを判定
def AdminFlag_fromCard(cCtrlCard, card_ID_list):
    ID = cCtrlCard.getID()
    if ID in card_ID_list:
        return True, ID

    return False, None
