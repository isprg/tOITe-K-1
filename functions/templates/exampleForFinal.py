def procFinal1(dictArgument):
    event = dictArgument["Event"]
    cState = dictArgument["State"]
    cCtrlCard = dictArgument["CtrlCard"]
    listCorrectNumber = [3, 4, 5, 6]

    if dictArgument["Option"][0] == 0:
        dictArgument["Option"] = [0, 0, 0, 0, 0]

    if event == "FINAL1":
        vPosition = pyautogui.position()
        listArea = getCallAreaDefinition()
        sTappedArea = CheckTappedArea(vPosition, listArea)
        print(sTappedArea)

        if sTappedArea >= 1:
            # PlaySound("sound/correct.wav")
            dictArgument["Option"][dictArgument["Option"][0] + 1] = sTappedArea
            print(dictArgument["Option"])
            dictArgument["Option"][0] += 1

        elif sTappedArea == 0:
            dictArgument["Option"][0] = 0
            print(dictArgument["Option"][1:5])
            if dictArgument["Option"][1:5] == listCorrectNumber:
                sStartTime = cState.updateState("FINAL_CORRECT")
                dictArgument["Start time"] = sStartTime
            else:
                sStartTime = cState.updateState("FINAL_WRONG")
                dictArgument["Start time"] = sStartTime
