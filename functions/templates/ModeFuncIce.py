import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Ice(dictProc):
	dictProc_this = {
		"ICE_Q"			: procIce_Q,
		"ICE_CORRECT"	: procIce_Correct,
		"ICE_WRONG"		: procIce_Wrong,
	}
	return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Ice(dictWindow):
	layoutIce_Q = make_fullimage_layout("png/question01.png", "ICE_Q")
	layoutIce_Correct = make_fullimage_layout("png/correct.png", "ICE_CORRECT")
	layoutIce_Wrong = make_fullimage_layout("png/wrong.png", "ICE_WRONG")

	dictLayout = {
		"ICE_Q"			: layoutIce_Q,
		"ICE_CORRECT"	: layoutIce_Correct,
		"ICE_WRONG"		: layoutIce_Wrong,
	}
	dictWindow_this = setGUI(dictLayout)

	return dict(dictWindow, **dictWindow_this)


# ICE_Qモードタッチ座標設定 ================================================
def getAreaDefinition():
	vArea0 = [40, 310, 400, 100]
	vArea1 = [500, 310, 400, 100]
	vArea2 = [40, 460, 400, 100]
	vArea3 = [500, 460, 400, 100]
	listArea = [vArea0, vArea1, vArea2, vArea3]

	return listArea


# Ice_Qモード処理 ======================================================
def procIce_Q(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]

	if event == "ICE_Q":
		vPosition = pyautogui.position()
		listArea = getAreaDefinition()
		sTappedArea = CheckTappedArea(vPosition, listArea)
		print(sTappedArea)

		if sTappedArea == 1:
			PlaySound("sound/correct.wav")
			cCtrlCard.write_result("ice", "T")
			sStartTime = cState.updateState("ICE_CORRECT")
			dictArgument["Start time"] = sStartTime
		elif sTappedArea == 0 or sTappedArea == 2 or sTappedArea == 3:
			PlaySound("sound/wrong.wav")
			sStartTime = cState.updateState("ICE_WRONG")
			dictArgument["Start time"] = sStartTime


# Ice_correctモード処理 ======================================================
def procIce_Correct(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]

	if event == "ICE_CORRECT":
		cState.dictWindow["SELECT_GAME"]["アイス"].update(disabled=True)

		if CheckComplete(cCtrlCard):
			cCtrlCard.write_result("complete", "T")
			sStartTime = cState.updateState("ENDING")
			dictArgument["Start time"] = sStartTime
		else:
			sStartTime = cState.updateState("SELECT_GAME")
			dictArgument["Start time"] = sStartTime


# Ice_wrongモード処理 ======================================================
def procIce_Wrong(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]

	if event == "ICE_WRONG":
		sStartTime = cState.updateState("ICE_Q")
		dictArgument["Start time"] = sStartTime