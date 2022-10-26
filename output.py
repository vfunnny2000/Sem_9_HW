import logger

def plog(i,line:str = None):
    match i:
        case "Mode":
            print("Выбран режим: " + line)
            logger.wlog(i,line)
        case "Variables":
            print("Операция для вычисления: "+ line)
            logger.wlog(i,line)
        case "Result":
            print("Результат вычислений: " + line)
            logger.wlog(i,line)
        case "Exit":
            logger.wlog(i)

def viewlog():
    logger.fopen('r')
    for line in logger.file:
        print(line)
    logger.file.close()
    logger.fopen('a')