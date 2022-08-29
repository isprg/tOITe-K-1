import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Pizza(dictProc):
	dictProc_this = {
		"PIZZA_Q"		: procPizza_Q,
		"PIZZA_CORRECT"	: procPizza_Correct,
		"PIZZA_WRONG"	: procPizza_Wrong,
	}
	return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Pizza(dictWindow):
	layoutPizza_Q = make_fullimage_layout("png/question02.png", "PIZZA_Q")
	layoutPizza_Correct = make_fullimage_layout("png/correct.png", "PIZZA_CORRECT")
	layoutPizza_Wrong = make_fullimage_layout("png/wrong.png", "PIZZA_WRONG")

	dictLayout = {
		"PIZZA_Q"		: layoutPizza_Q,
		"PIZZA_CORRECT"	: layoutPizza_Correct,
		"PIZZA_WRONG"	: layoutPizza_Wrong,
	}
	dictWindow_this = setGUI(dictLayout)

	return dict(dictWindow, **dictWindow_this)


# PIZZA_Qモードタッチ座標設定 ================================================
def getAreaDefinition():
	vArea0 = [40, 280, 400, 100]
	vArea1 = [500, 280, 400, 100]
	vArea2 = [40, 420, 400, 100]
	vArea3 = [500, 420, 400, 100]
	listArea = [vArea0, vArea1, vArea2, vArea3]

	return listArea


# Ice_Qモード処理 ======================================================
def procPizza_Q(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]

	if event == "PIZZA_Q":
		vPosition = pyautogui.position()
		listArea = getAreaDefinition()
		sTappedArea = CheckTappedArea(vPosition, listArea)
		print(sTappedArea)

		if sTappedArea == 2:
			PlaySound("sound/correct.wav")
			cCtrlCard.write_result("pizza", "T")
			sStartTime = cState.updateState("PIZZA_CORRECT")
			dictArgument["Start time"] = sStartTime
		elif sTappedArea == 0 or sTappedArea == 1 or sTappedArea == 3:
			PlaySound("sound/wrong.wav")
			sStartTime = cState.updateState("PIZZA_WRONG")
			dictArgument["Start time"] = sStartTime


# Ice_correctモード処理 ======================================================
def procPizza_Correct(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]

	if event == "PIZZA_CORRECT":
		cState.dictWindow["SELECT_GAME"]["ピザ"].update(disabled=True)

		if CheckComplete(cCtrlCard):
			cCtrlCard.write_result("complete", "T")
			sStartTime = cState.updateState("ENDING")
			dictArgument["Start time"] = sStartTime
		else:
			sStartTime = cState.updateState("SELECT_GAME")
			dictArgument["Start time"] = sStartTime


# Ice_wrongモード処理 ======================================================
def procPizza_Wrong(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]

	if event == "PIZZA_WRONG":
		sStartTime = cState.updateState("PIZZA_Q")
		dictArgument["Start time"] = sStartTime