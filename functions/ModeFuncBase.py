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
        "TUTORIAL1": tutorial1Proc,
        "ENDING1": ending1Proc,
        "Clear": clearProc,
        "CARD_ERROR": card_error_ModeProc,
    }
    return dictProc


# レイアウト設定・辞書割り当て =============================================
def createDictWindow():
    layoutStandby = make_fullimage_layout("png/standby01.png", "STANDBY")
    layoutGoOtherGame = make_fullimage_layout(
        "png/go_other_game.png", "GO_OTHER_GAME")
    layoutTutorial1 = make_4choice_layout(
        "png/tutorial1.png", "TUTORIAL1")
    layoutEnding1 = make_fullimage_layout("png/ending1.png", "ENDING1")
    layoutClear = make_fullimage_layout("png/clear.png", "CLEAR")
    layoutCard_Error = make_fullimage_layout(
        "png/card_alert.png", "CARD_ERROR")

    dictLayout = {
        "STANDBY": layoutStandby,
        "GO_OTHER_GAME": layoutGoOtherGame,
        "TUTORIAL1": layoutTutorial1,
        "ENDING1": layoutEnding1,
        "Clear": layoutClear,
        "CARD_ERROR": layoutCard_Error,
    }
    dictWindow = setGUI(dictLayout)

    return dictWindow


# standbyModeProc======================================================
def standbyModeProc(dictArgument):
    cCtrlCard = dictArgument["CtrlCard"]
    cState = dictArgument["State"]

    setFlag = cCtrlCard.setCard()

    if setFlag:
        PlaySound("sound/card_set.wav")
        sStartTime = cState.updateState("TITLE")
        dictArgument["Start time"] = sStartTime


# goOtherGameProc ======================================================
def goOtherGameProc(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "GO_OTHER_GAME":
        pass


# tutorial1Proc=================================================
def tutorial1Proc(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "TUTORIAL1":
        pass


# ending1Proc =========================================================
def ending1Proc(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

    if event == "ENDING1":
        sStartTime = cState.updateState("CLEAR")
        dictArgument["Start time"] = sStartTime


# clearProc=========================================================
def clearProc(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]

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
