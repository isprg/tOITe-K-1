import time
import PySimpleGUI as sg
import pyautogui

from functions.setGUI import setGUI
from functions.common import Reset_Game, PlaySound, CheckTappedArea
from functions.CardFunc import SetGame_FromCard
from functions.DesignLayout import *


# 処理の辞書割り当て ======================================================
def createDictProc():
    dictProc = {
        "STANDBY": standbyModeProc,
        "GO_OTHER_GAME": goOtherGameProc,
        "CLEAR": clearProc,
        "CARD_ERROR": card_error_ModeProc,
    }
    return dictProc


# レイアウト設定・辞書割り当て =============================================
def createDictWindow():
    layoutBackGround = [[sg.Text()]]
    layoutStandby = make_fullimage_layout("png/standby.png", "STANDBY")
    layoutGoOtherGame = make_fullimage_layout(
        "png/go_other_game.png", "GO_OTHER_GAME")
    layoutClear = make_fullimage_layout("png/clear.png", "CLEAR")
    layoutCard_Error = make_fullimage_layout(
        "png/card_alert.png", "CARD_ERROR")

    dictLayout = {
        "BACKGROUND": layoutBackGround,
        "STANDBY": layoutStandby,
        "GO_OTHER_GAME": layoutGoOtherGame,
        "CLEAR": layoutClear,
        "CARD_ERROR": layoutCard_Error,
    }
    dictWindow = setGUI(dictLayout)

    return dictWindow


# 標準タップ座標設定 ================================================
def getDefaultAreaDefinition():
    vArea0 = [260, 520, 520, 60]
    listArea = [vArea0, ]

    return listArea


# standbyModeProc======================================================
def standbyModeProc(dictArgument):
    cCtrlCard = dictArgument["CtrlCard"]

    setFlag = cCtrlCard.setCard()

    if setFlag:
        PlaySound("sound/card_set.wav")
        SetGame_FromCard(dictArgument)


# goOtherGameProc ======================================================
def goOtherGameProc(dictArgument):
    event = dictArgument["Event"]

    if event == "GO_OTHER_GAME":
        pass


# clearProc=========================================================
def clearProc(dictArgument):
    event = dictArgument["Event"]

    if event == "CLEAR":
        pass


# card_error_ModeProc ======================================================
def card_error_ModeProc(dictArgument):
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]
    proc = dictArgument["ImageProc"]

    exist = cCtrlCard.check_exist()  # カードが存在するかをチェック
    identical = cCtrlCard.check_identity()  # カードが同一かをチェック
    if exist is True and identical is True:
        ReturnState, ImageProc_Flag = dictArgument["Return state"]

        if ImageProc_Flag:
            proc.createWindows()

        sStartTime = cState.updateState(ReturnState)
        dictArgument["Return state"] = None
        dictArgument["Start time"] = sStartTime

    elif identical is False or time.time() - dictArgument["Start time"] > 20:
        Reset_Game(dictArgument)
