from logging import getLogger

import pyautogui
import speech_recognition as sr

from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea
from functions.DesignLayout import make_fullimage_layout

logger = getLogger("tOITe-K-1").getChild("SR")


# 処理の辞書割り当て ======================================================
def updateDictProc_SR(dictProc):
    dictProc_this = {
        "SR_Q": procSR_Q,
        "SR_CORRECT": procSR_Correct,
        "SR_WRONG": procSR_Wrong,
    }
    return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_SR(dictWindow):
    layoutSR_Q = make_fullimage_layout("png/sr01.png", "SR_Q")
    layoutSR_Correct = make_fullimage_layout(
        "png/sr01correct.png", "SR_CORRECT")
    layoutSR_Wrong = make_fullimage_layout("png/sr01wrong.png", "SR_WRONG")

    dictLayout = {
        "SR_Q": layoutSR_Q,
        "SR_CORRECT": layoutSR_Correct,
        "SR_WRONG": layoutSR_Wrong,
    }
    dictWindow_this = setGUI(dictLayout)

    return dict(dictWindow, **dictWindow_this)


def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


def procSR_Q(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    r = sr.Recognizer()
    keyword = "くらわんか"

    if event == "SR_Q":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)

        if sTappedArea == 0:  # 音声認識開始ボタン
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='ja-JP')
                if query == keyword:
                    PlaySound("sound/correct.wav")
                    PlaySound("sound/final23.wav")

                    sStartTime = cState.updateState("SR_CORRECT")
                    dictArgument["Start time"] = sStartTime
                else:
                    PlaySound("sound/wrong.wav")
                    sStartTime = cState.updateState("SR_WRONG")
                    dictArgument["Start time"] = sStartTime
            except sr.UnknownValueError:
                PlaySound("sound/wrong.wav")
                sStartTime = cState.updateState("SR_WRONG")
                dictArgument["Start time"] = sStartTime
                logger.warning("Could not understand audio")
            except sr.RequestError as e:
                logger.error(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))


def procSR_Correct(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "SR_CORRECT":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 次へをタップ
            PlaySound("sound/final45.wav")
            cCtrlCard.write_result("voice", "T")
            sStartTime = cState.updateState("FINAL_2")
            dictArgument["Start time"] = sStartTime


def procSR_Wrong(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "SR_WRONG":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea == 0:  # 答えるをタップ
            dictSaveData = cCtrlCard.read_result()["voice"]
            if int(dictSaveData) < 4:
                cCtrlCard.write_result("voice", str(int(dictSaveData) + 1))
                sStartTime = cState.updateState("SR_Q")
                dictArgument["Start time"] = sStartTime
            else:
                sStartTime = cState.updateState("FINAL_3")
                dictArgument["Start time"] = sStartTime
