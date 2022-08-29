import pyautogui
from functions.setGUI import setGUI
from functions.common import PlaySound, CheckTappedArea, CheckComplete
from functions.DesignLayout import make_fullimage_layout


# 処理の辞書割り当て ======================================================
def updateDictProc_Sea(dictProc):
	dictProc_this = {
		"SEA_Q"			: procSea_Q,
		"SEA_CORRECT"	: procSea_Correct,
		"SEA_WRONG"		: procSea_Wrong,
	}
	return dict(dictProc, **dictProc_this)


# レイアウト設定・辞書割り当て =============================================
def updateDictWindow_Sea(dictWindow):
	layoutSea_Q = make_fullimage_layout("png/question03.png", "SEA_Q")
	layoutSea_Correct = make_fullimage_layout("png/correct.png", "SEA_CORRECT")
	layoutSea_Wrong = make_fullimage_layout("png/wrong.png", "SEA_WRONG")

	dictLayout = {
		"SEA_Q"			: layoutSea_Q,
		"SEA_CORRECT"	: layoutSea_Correct,
		"SEA_WRONG"		: layoutSea_Wrong,
	}
	dictWindow_this = setGUI(dictLayout)

	return dict(dictWindow, **dictWindow_this)


# SEA_Qモードタッチ座標設定 ================================================
def getAreaDefinition():
	vArea0 = [110, 290, 300, 100]
	vArea1 = [600, 290, 300, 100]
	vArea2 = [110, 430, 300, 100]
	vArea3 = [600, 430, 300, 100]
	listArea = [vArea0, vArea1, vArea2, vArea3]

	return listArea


# Ice_Qモード処理 ======================================================
def procSea_Q(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]

	if event == "SEA_Q":
		vPosition = pyautogui.position()
		listArea = getAreaDefinition()
		sTappedArea = CheckTappedArea(vPosition, listArea)
		print(sTappedArea)

		if sTappedArea == 3:
			PlaySound("sound/correct.wav")
			cCtrlCard.write_result("sea", "T")
			sStartTime = cState.updateState("SEA_CORRECT")
			dictArgument["Start time"] = sStartTime
		elif sTappedArea == 0 or sTappedArea == 1 or sTappedArea == 2:
			PlaySound("sound/wrong.wav")
			sStartTime = cState.updateState("SEA_WRONG")
			dictArgument["Start time"] = sStartTime


# Ice_correctモード処理 ======================================================
def procSea_Correct(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]
	cCtrlCard = dictArgument["CtrlCard"]
	
	if event == "SEA_CORRECT":
		cState.dictWindow["SELECT_GAME"]["海"].update(disabled=True)

		if CheckComplete(cCtrlCard):
			cCtrlCard.write_result("complete", "T")
			sStartTime = cState.updateState("ENDING")
			dictArgument["Start time"] = sStartTime
		else:
			sStartTime = cState.updateState("SELECT_GAME")
			dictArgument["Start time"] = sStartTime


# Ice_wrongモード処理 ======================================================
def procSea_Wrong(dictArgument):
	event = dictArgument["Event"]
	cState = dictArgument["State"]

	if event == "SEA_WRONG":
		sStartTime = cState.updateState("SEA_Q")
		dictArgument["Start time"] = sStartTime