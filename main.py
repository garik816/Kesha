import os, shutil, random, psutil, ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Кеша, для чистки кэша")

userDir = os.path.expanduser('~')
path = f'{userDir}\\AppData\\Local\\Plagiatus\\'

choice = random.randint(0, 12)

hiPhrase1 = "Вжух — и Адвегин кэш почищен!"
hiPhrase2 = "У Вас тут завелась сущность в виде гномика.\nСейчас я её почистию и можно будет продолжать работу…"
hiPhrase3 = "Мирыкыл! Кэш Вашей Адвеги почищен!"
hiPhrase4 = "Мыли-мыли трубочиста: чисто-чисто, конкретно-конкретно…\nА тем временем и кэш Вашей Адвеги выдраили."
hiPhrase5 = "Пссс, чел, хочешь немного очистительной магии?\nОп — и кэш твоей Адвеги почищен!"
hiPhrase6 = "Между прочим, пока я Вам тут кэш чищу, Вы могли бы зарядку для глаз сделать."
hiPhrase7 = "Вуаля! Стоило только запустить этот скрипт — и вот уже кэш Вашей Адвеги почищен!"
hiPhrase8 = "Раз, два, три, четыре, пять —\nКэш почищу я опять!"
hiPhrase9 = "ШОК!!! Один маленький скрипт только что почистил кэш всей Вашей Адвеги!\nВся Москва ахнула!!!\nДа что Москва! Даже врачи перестали скрывать то, что…"
hiPhrase10 = "Съешь ещё этих мягких французских булок, да выпей же чаю — а я пока почищу кэш…"
hiPhrase11 = "Привет! Как дела? А я тут это… кэш Вам чищу. Вот.\nМог бы и в квартире поубирать, но я всего лишь скрипт…"
hiPhrase12 = "ЗНАЕТЕ ЛИ ВЫ, ЧТО\nна чистку кэша Вашей Адвеги уходит в среднем 0,12 секунды — ровно столько времени достаточно одному человеку для того, чтобы влюбиться в другого человека?"
hiPhrase13 = "Нельзя так просто взять и почистить кэш.\nСперва нужно прочитать это сообщение."

donePhrase1 = "Для продолжения работы нажмите любую клавишу."
donePhrase2 = "Всё, почистиил, можете закрывать скрипт и продолжать работать."
donePhrase3 = "Для продолжения работы нажмите эникей."
donePhrase4 = "Так что можете нажимать любую клавишу и продолжать работать."
donePhrase5 = "Всё, закрывай этот скриптик и работай дальше."
donePhrase6 = "Не хотите — как хотите. Тогда нажимайте любую клавишу и продолжайте работать. Кэш почищен."
donePhrase7 = "Можете не благодарить. Просто нажмите любую кнопку и продолжайте работать."
donePhrase8 = "Чтобы дальше продолжать,\nНа «Закрыть» спеши нажать!"
donePhrase9 = "Короче, жмите любую клавишу, продолжайте работать и никогда не читайте тизеры."
donePhrase10 = "Впрочем, я уже всё.\nМожешь жать любую клавишу."
donePhrase11 = "К тому же я уже закончил с кэшем и меня можно смело закрывать.\nНо я буду скучать. Так что нажимайте на меня чаще.\nВот."
donePhrase12 = "А теперь можете спокойно нажимать любую клавишу и продолжать работать как работали.\nВаш скрипт"
donePhrase13 = "Потом нажать любую клавишу.\nА затем продолжать работать.\nУдачи!"

nonePhrase1 = "Чтобы что-нибудь продать, нужно что-нибудь купить, а чтобы почистить кэш, его сперва нужно засорить!\nТак что закрывайте этот скрипт и приступайте к работе — ибо кэш Вашей Адвеги пока ещё чист!"
nonePhrase2 = "Опять прокрастинируете? Нашли чем заняться!\nСперва проверьте тексты в Адвеге, а затем уж начинайте её кэш чистить!\nВ общем, закрывайте этот скрипт и работайте!"
nonePhrase3 = "Чисто не там, где убирают, а там, где не сорят!\nНапример, в кэше Вашей Адвеги — в нём пока что идеальная чистота.\nТак что можете закрывать этот скрипт и приступать к проверке текстов."
nonePhrase4 = "В салоне тихо, чисто и пусто. Только в одном из углов вышивает гладью пожилая княжна.\nНо её чистить не надобно. Посему соблаговолите закрыть скрипт и приступить к работе."
nonePhrase5 = "ЗНАЕТЕ ЛИ ВЫ, ЧТО\nбоязнь грязи называется рипофобия и относится к психическим расстройствам?\nТак что, дабы не прослыть психом, закрывайте скорее скрипт и приступайте к работе, ибо кэш Вашей Адвеги ещё безупречно чист."
nonePhrase6 = "Вы ещё даже не поработали в Адвеге, а уже кэш её чистить собрались!\nИ не стыдно Вам?\nА ну-ка быстро закрывайте этот скрипт и приступайте к работе!"
nonePhrase7 = "Ну и зачем Вы открыли этот скрипт? Кэш Вашей Адвеги ещё девственно чист.\nЗакрывайте этот скрипт и беритесь за дело, наконец."
nonePhrase8 = "Если ты ждёшь, когда Вселенная пошлёт тебе тот самый знак, то вот он!\nСкорее закрывай этот скрипт и принимайся за то дело, до которого всё никак не доходили руки!\nP.S. А кэш твоей Адвеги ещё чист."
nonePhrase9 = "Этот скрипт — ясновидящий. И сейчас он видит то, что кэш твоей Адвеги идеально чист, будто программу и не запускали ещё.\nСкорее пользуйся этой чистотой и проверяй тексты!"
nonePhrase10 = "Олег, проект пока не готов, потому что кэш Вашей Адвеги чист.\nДавайте сперва прогоним тексты на Плагиатусе, а затем уж будем что-то думать.\nДля начала закройте этот скрипт."
nonePhrase11 = "Хочешь заработать один миллион долларов?\nТогда жми «Закрыть» на этом скрипте, пиши тексты, проверяй их по Адвеге, отправляй заказчику и зарабатывай свой чёртов миллион!"
nonePhrase12 = "Засяльника, зачем скрипт запускаиш мана? Тут и так чиста мана. Спирва текст напиши да, патом по Адвеге прагани да, а патом скрипт запускай да. Сийчас скрипт закрывай да."
nonePhrase13 = "Здравствуйте!\nЕсли Вы видите данное сообщение, значит Ваш скрипт запущен при чистом кэше Адвеги.\nПожалуйста, засорите кэш Вашего Плагиатуса, а затем попробуйте вновь запустить данный скрипт.\nВсего Вам доброго! До свидания!"

hiPhraseList = [hiPhrase1,hiPhrase2,hiPhrase3,hiPhrase4,hiPhrase5,hiPhrase6,hiPhrase7,hiPhrase8,hiPhrase9,hiPhrase10,hiPhrase11,hiPhrase12,hiPhrase13]
donePhraseList = [donePhrase1,donePhrase2,donePhrase3,donePhrase4,donePhrase5,donePhrase6,donePhrase7,donePhrase8,donePhrase9,donePhrase10,donePhrase11,donePhrase12,donePhrase13]
nonePhraseList = [nonePhrase1,nonePhrase2,nonePhrase3,nonePhrase4,nonePhrase5,nonePhrase6,nonePhrase7,nonePhrase8,nonePhrase9,nonePhrase10,nonePhrase11,nonePhrase12,nonePhrase13]

# проверка, пусты ли папкы
# for dirpath, dirnames, files in os.walk(path):
#     if files:
#         print(dirpath, 'not empty')
#     if not files:
#         print(dirpath, 'is empty')

# проверка, запущщени ли процесс
def processCheck():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "Plagiatus.exe":
            return 1
    return 0

# проверка, пуста ли папка
def emptyCheck():
    dir_contents = [x for x in os.listdir(path) if not x.startswith('.')]
    if len(dir_contents) > 0:
        return 1
    return 0

# удаление содержи
def cleanFolder():
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Не могу удалить %s. Причина: %s' % (file_path, e))
    pass

def main():
    if processCheck():
        print("Проблемка нарисовалась. Адвега то открыта. Закрой!")
    else:
        if emptyCheck():
            print(hiPhraseList[choice])
            cleanFolder()
            print(donePhraseList[choice])
        else:
            print(nonePhraseList[choice])
    # input()
    os.system('pause >nul')

main()
