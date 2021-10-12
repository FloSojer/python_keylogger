filteredFile: str = "filtered.txt"
filename: str = "keylogs.txt"
shitList = []

def filterWords():
    f = open(filename, 'r')
    counter = 0
    for i in f.read():
        shitList.append(i)

    for c in shitList:
        counter = counter + 1
        if (c == "."):
            if (shitList[counter - 2] == "y" and shitList[counter - 3] == "e" and shitList[counter - 4] == "K"):
                # delete key.shift_r
                if (shitList[counter] == "s" and shitList[counter + 6] == "r"):
                    shitList[counter - 4:counter + 7] = " "
                # delete key.esc
                elif (shitList[counter] == "e" and shitList[counter + 1] == "s" and shitList[counter + 2] == "c"):
                    shitList[counter - 4:counter + 3] = " "
                # delete Key.space
                elif (shitList[counter] == "s" and shitList[counter + 1] == "p" and shitList[counter + 4] == "e"):
                    shitList[counter - 4:counter + 3] = " "
                # delete Key.backspace
                elif (shitList[counter] == "b" and shitList[counter + 1] == "a" and shitList[counter + 3] == "k" and shitList[counter + 6] == "a" and shitList[counter + 8] == "e"):
                    shitList[counter - 4:counter + 9] = " "
                # delete Key.enter
                elif (shitList[counter] == "e" and shitList[counter + 1] == "n" and shitList[counter + 4] == "r"):
                    shitList[counter - 4:counter + 5] = " "
                # delete Key.cmd_r
                elif (shitList[counter] == "c" and shitList[counter + 1] == "m" and shitList[counter + 2] == "d"):
                    shitList[counter - 4:counter + 5] = " "
                # delete Key.alt_r
                elif (shitList[counter] == "a" and shitList[counter + 1] =="l" and shitList[counter + 4] == "r"):
                    shitList[counter - 4:counter + 5] = " "
                # delete key.alt
                elif (shitList[counter] == "a" and shitList[counter + 1] =="l" and shitList[counter + 2] == "t"):
                    shitList[counter - 4:counter + 3] = " "
                # delete Key.ctrl
                elif (shitList[counter] == "c" and shitList[counter + 1] =="t" and shitList[counter + 2] == "r"):
                    shitList[counter - 4:counter + 4] = " "
                # delete Key.shift
                elif (shitList[counter] == "s" and shitList[counter + 1] =="h" and shitList[counter + 2] == "i" and shitList[counter + 4]):
                    shitList[counter - 4:counter + 5] = " "
                # delete Key.tab
                elif (shitList[counter] == "t" and shitList[counter + 1] =="a" and shitList[counter + 2] == "b"):
                    shitList[counter - 4:counter + 3] = " "
                #Key.caps_lock
                elif (shitList[counter] == "c" and shitList[counter + 1] =="a" and shitList[counter + 2] == "p" and shitList[counter+3] == "s" and shitList[counter+8] == "k"):
                    shitList[counter - 4:counter + 9] = " "

def writeFilteredFiles():
    f = open(filteredFile, 'a')
    for a in shitList:
        if(a != ' '):
            print(a)
            f.write(a)
    f.close()