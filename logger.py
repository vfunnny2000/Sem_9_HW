logfile = 'log.txt'
file = None

def fopen(mode):
    global file
    global logfile
    if(file == None):
        file = open(logfile,mode,encoding="UTF-8")
    else:
        file.close()
        file = open(logfile,mode,encoding='UTF-8')

def fclose():
    global file
    if(file != None):
        wlog("Exit")
        file.close()

def wlog(flag,line:str = None):
    global file
    if(file != None):
        match flag:
            case "Mode":
                file.write(f"Выбран режим: {line}\n")
            case "Variables":
                file.write(f"Операция для вычисления: {line}\n")
            case "Result":
                file.write(f"Результат вычислений: {line}\n")
            case "Exit":
                file.write(f"Инициирован выход из программы\n")