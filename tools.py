from dataclasses import replace
import threading, types, atexit
#import multiprocessing

def create_thread_method(target_cyclic_callback : types.FunctionType):
    def target(kwargs):
        while kwargs.get("do", False):
            target_cyclic_callback(**kwargs)
    data = {'do' : True}
    thread = threading.Thread(target=target, args=[data])
    thread.data = data
    thread.start()

    return thread


def eng_to_rus_diale(input_text : str) -> str:

    transp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    transa = 'авсиероьипкгмиоррвстугмхуеАВСИЕРОНИПКГМИОРОВСТУЬМХУЕ'

    result = str()
    for c in input_text:
        try:
            result += transa[transp.index(c)]
        except:
            result += c

    return result


def fitta_every_o(input_text : str) -> str:
    words = input_text.split(' ')

    result = str()
    for word in words:
        result += word + " " 
        for char in "oOоО":
            if word.find(char) != -1:
                result += "(" + word.replace(char, "ф") + ") "

    return result

def reflect_T_vertically_Rus(input_text : str) -> str:

    return input_text.replace('т', "⊥").replace("с", "ͼ")


def mutate_pp_rus(input_text: str) -> str:
    result, flag = "", False
    for c in input_text:
        if flag is False:
            if c.lower() == "п": c = "р"
            flag = not flag
        else:
            if c.lower() == "р": c = "п"
            flag = not flag
        result += c
    return result


def replace_transcr_rus_to_eng(input: str) -> str:

    dict = {
        "й" : "i`", "ц" : "c", "у" : "u",
        "к" : "k", "е" : "e", "н" : "n",
        "г" : "g", "ш" : "sh",
        "щ" : "sch", #sch?
        "з" : "z", "х" : "h", "ъ" : "`",
        "ф" : "f", "ы" : "i", # Бездынные - bezdinnyie    # ды - di, ны - ny
        "в" : "v", "а" : "a", "п" : "p",
        "р" : "r", "о" : "o", "л" : "l", "д" : "d",
        "ж" : "j", #jivaya - живая
        "э" : "e", "я" : "ya", "ч" : "ch",
        "с" : "s", "м" : "m", "и" : "i",
        "т" : "t", #Тьмо - t`mo
        "ь" : "`", "б" : "b",
        "ю" : "u" #Тью Ми -- t`u Mi
    }

    result = str()
    for ch in input:
        result += dict.get(ch.lower(), ch.lower())

    return result


if __name__ == "__main__":
    res = eng_to_rus_diale("Dog, cup, Do you think you're living an ordinary life? You are so mistaken it's difficult to even explain. The mere fact that you exist makes you extraordinary. The odds of you existing are less than winning the lottery, but here you are. Are you going to let this extraordinary opportunity pass?")
    print(fitta_every_o(res))
    print(reflect_T_vertically_Rus(res))
    res = eng_to_rus_diale(" Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing. ")
    print(fitta_every_o(res))

    print(reflect_T_vertically_Rus(fitta_every_o(mutate_pp_rus("""
    С учётом сложившейся международной обстановки, реализация намеченных плановых заданий не оставляет шанса для укрепления моральных ценностей. Сложно сказать, почему действия представителей оппозиции будут призваны к ответу. В частности, разбавленное изрядной долей эмпатии, рациональное мышление представляет собой интересный эксперимент проверки системы обучения кадров, соответствующей насущным потребностям. Также как начало повседневной работы по формированию позиции требует определения и уточнения прогресса профессионального сообщества. Независимые государства набирают популярность среди определенных слоев населения, а значит, должны быть в равной степени предоставлены сами себе. В своём стремлении улучшить пользовательский опыт мы упускаем, что некоторые особенности внутренней политики описаны максимально подробно.
    """))))

    print(eng_to_rus_diale("Explode Redzed, ELIOZIE"))

    print(eng_to_rus_diale("RasenGun! [Naruto]"))

    #ɸΨ

    print(eng_to_rus_diale("""Telling Layla's story spoken
'Bout how all her bones are broken
Hammers fall on all the pieces
Two months in the cover creases
Here she stands today
In her brilliant shining way
Fully alive
More than most, ready to smile, and love life
Fully alive and she knows
How to believe in futures
All my complaints shrink to nothing
I'm ashamed of all my somethings
She's glad for one day of comfort
Only because she has suffered
Here she stands today
In her brilliant shining way
Fully alive
More than most, ready to smile, and love life
Fully alive and she knows
How to believe in futures
Fully alive
More than most, ready to smile, and love life
Fully alive and she knows
How to believe in futures
Fully alive
More than most, ready to smile, and love life
Fully alive and she knows
How to believe in futures"""))


    print(replace_transcr_rus_to_eng("""Товарищь, тебе хана!
    
    Зачем мне считаться шпаной и бандитом -
Не лучше ль податься мне в антисемиты:
На их стороне хоть и нету законов,-
Поддержка и энтузиазм миллионов.

Решил я - и, значит, кому-то быть битым,
Но надо ж узнать, кто такие семиты,-
А вдруг это очень приличные люди,
А вдруг из-за них мне чего-нибудь будет!

Но друг и учитель - алкаш в бакалее -
Сказал, что семиты - простые евреи.
Да это ж такое везение, братцы,-
Теперь я спокоен - чего мне бояться!

Я долго крепился, ведь благоговейно
Всегда относился к Альберту Эйнштейну.
Народ мне простит, но спрошу я невольно:
Куда отнести мне Абрама Линкольна?

Средь них - пострадавший от Сталина Каплер,
Средь них - уважаемый мной Чарли Чаплин,
Мой друг Рабинович и жертвы фашизма,
И даже основоположник марксизма.

Но тот же алкаш мне сказал после дельца,
Что пьют они кровь христианских младенцев;
И как-то в пивной мне ребята сказали,
Что очень давно они бога распяли!

Им кровушки надо - они по запарке
Замучили, гады, слона в зоопарке!
Украли, я знаю, они у народа
Весь хлеб урожая минувшего года!

По Курской, Казанской железной дороге
Построили дачи - живут там как боги...
На все я готов - на разбой и насилье,-
И бью я жидов - и спасаю Россию!
    
    
"""))


    print(replace_transcr_rus_to_eng("""
    
    Л.В. Лифшицу

Я всегда твердил, что судьба — игра.
Что зачем нам рыба, раз есть икра.
Что готический стиль победит, как школа,
как способность торчать, избежав укола.
Я сижу у окна. За окном осина.
Я любил немногих. Однако — сильно.

Я считал, что лес — только часть полена.
Что зачем вся дева, раз есть колено.
Что, устав от поднятой веком пыли,
русский глаз отдохнет на эстонском шпиле.
Я сижу у окна. Я помыл посуду.
Я был счастлив здесь, и уже не буду.

Я писал, что в лампочке — ужас пола.
Что любовь, как акт, лишена глагола.
Что не знал Эвклид, что, сходя на конус,
вещь обретает не ноль, но Хронос.
Я сижу у окна. Вспоминаю юность.
Улыбнусь порою, порой отплюнусь.

Я сказал, что лист разрушает почку.
И что семя, упавши в дурную почву,
не дает побега; что луг с поляной
есть пример рукоблудья, в Природе данный.
Я сижу у окна, обхватив колени,
в обществе собственной грузной тени.

Моя песня была лишена мотива,
но зато ее хором не спеть. Не диво,
что в награду мне за такие речи
своих ног никто не кладет на плечи.
Я сижу у окна в темноте; как скорый,
море гремит за волнистой шторой.

Гражданин второсортной эпохи, гордо
признаю я товаром второго сорта
свои лучшие мысли и дням грядущим
я дарю их как опыт борьбы с удушьем.
Я сижу в темноте. И она не хуже
в комнате, чем темнота снаружи.
1971 г.
    """))


    print(replace_transcr_rus_to_eng("""
    Итак
Шаурма по-домашнему
Продукты (на 2 порции)
Лаваш тонкий - 2 листа
Куриное филе (крупное) - 1 шт.
Сыр твердый - 200-250 г
Капуста белокочанная - 150 г
Морковь по-корейски - 150 г
Огурцы маринованные - 2 небольших
Помидор свежий - 1 шт.
Майонез - 5-6 ст. ложек
Сметана - 2 ст. ложки
Зелень свежая (петрушка, укроп) - 0,5 небольшого пучка
Чеснок - 2-4 зубчика (по вкусу)
Масло растительное для жарки - 2 ст. ложки
Паприка молотая - 2 ч. л.
Перец кайенский - 1 щепотка (по вкусу)
Чеснок сушеный гранулированный - 1 ч. л.
Приправа для курицы - 2 ч. л.
Перец чёрный молотый - по вкусу
Соль - по вкусу
    """))