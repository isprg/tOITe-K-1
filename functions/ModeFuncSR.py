import pyautogui
import speech_recognition as sr
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea
from functions.DesignLayout import make_fullimage_layout


def updateDictProc_SR(dictProc):
    dictProc_this = {
        "SR_Q": procSR_Q,
        "SR_CORRECT": procSR_Correct,
        "SR_WRONG": procSR_Wrong,
    }
    return dict(dictProc, **dictProc_this)


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


def getAreaDefinition():
    vArea0 = [260, 520, 260, 60]
    vArea1 = [520, 520, 260, 60]
    listArea = [vArea0, vArea1, ]

    return listArea


def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


def judgeAudio(strKeyword, strAudioFileName):
    recog = sr.Recognizer()
    try:
        with sr.AudioFile(strAudioFileName) as inputAudio:
            audio = recog.record(inputAudio)
        inputText = recog.recognize_google(audio, language='ja-JP')
        print(inputText)
    except sr.UnknownValueError:
        return False
    except sr.RequestError:
        return False

    if strKeyword in inputText:
        return True
    else:
        return False


def procSR_Q(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cAudio = dictArgument["AudioSensor"]

    if event == "SR_Q":
        vPosition = pyautogui.position()
        listArea = getAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)

        if sTappedArea == 0 and cAudio.getRecording() == False:
            print("start recording")
            PlaySound("sound/button1.wav")
            cAudio.startRecordThread()
        elif sTappedArea == 1 and cAudio.getRecording() == True:
            print("stop recording")
            PlaySound("sound/button1.wav")
            cAudio.setRecording(False)
            cAudio.record("test.wav")

            if judgeAudio("くらわんか", "test.wav"):
                PlaySound(["sound/correct.wav", "sound/final234.wav"])
                sStartTime = cState.updateState("SR_CORRECT")
                dictArgument["Start time"] = sStartTime
            else:
                sStartTime = cState.updateState("SR_WRONG")
                dictArgument["Start time"] = sStartTime


def procSR_Correct(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "SR_CORRECT":
        vPosition = pyautogui.position()
        listArea = getDefaultAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)

        if sTappedArea == 0:
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

        if sTappedArea == 0:
            dictSaveData = cCtrlCard.read_result()["voice"]
            if int(dictSaveData) < 4:
                cCtrlCard.write_result("voice", str(int(dictSaveData) + 1))
                sStartTime = cState.updateState("SR_Q")
                dictArgument["Start time"] = sStartTime
            else:
                sStartTime = cState.updateState("FINAL_3")
                dictArgument["Start time"] = sStartTime
