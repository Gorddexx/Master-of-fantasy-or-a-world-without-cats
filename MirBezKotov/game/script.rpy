﻿# Вы можете расположить сценарий своей игры в этом файле.




# Определение персонажей игры.
define matwei = Character('Матвей', color="#ac1ba3")
define andrei = Character('Андрей', color="#44ece2")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    image logos = "images/logo.png"

# Игра начинается здесь:


label start:
    jump splashscreen
    stop music
# Что-то в тему к ниже тексту сцена
    "Говорят, что любовь самое лучшее чувство на земле."
    "Что ничего прекраснее не существует."
    "Но это блядское чувство не даёт жить Матвею."
    "Его любовь - это просто кровоточащая рана, которая не может зажить уже несколько месяцев."
    "И его последнее, предсмертное желание это хоть на один день забыть про него."
    scene razdevalka
    play sound vecherinka
    matwei "Новогодняя школьная дискотека."
    matwei "Тут все на веселе."
    matwei "Я тоже."
    matwei "По крайней мере должен быть."
    matwei "Но не могу."
    matwei "Просто блять не могу."
    matwei "Поэтому сижу с бутылкой водки в туалете мужской раздевалки."
    matwei "Мне бы напиться до смерти."
    matwei "И забыть про эту жизнь."
    matwei "Про это поглощающее чувство к этому придурку."
    play sound dvernaya_ruchka
    "Ручку двери кто-то дергает."
# Анимация дергания ручки двери
    "После громкие стуки, которые бьют по барабанным перепонкам."
# Звуки громных стуков по двери
    matwei "Занято!"
    "Гордо и громко крикнул Матвей."
    matwei "А то блять много непонятливых завелось. Я хочу побыть один. Только я, мое ебучее чувство любви и водка."
    andrei "Сорян"
    play sound cerdze volume 1.0
    matwei "Блять... Это же он... Сука..."
    "Алкоголь ударяет в голову. Туда же приходит ахуенная мысль. Сейчас сбудется то, о чем Матвей мечтал каждую ночь."
    matwei "Стой!"
    stop sound
    scene dveri
    menu:
        "Открыть дверь?"

        "Да":
            jump da

        "Нет":
            jump no

label no:
    "Андрей берет монтировку и начинает ломать дверь"
    "..."
    andrei "А вот и я!"
    matwei "Нет, что ты сделал? Дебил блять!"
    andrei "Ты не открывал дверь, вот я и выломал."
    window hide
    with fade
    window show
    andrei "Кстати ты ничего не хочешь рассказать?"
    matwei "Например?"
    andrei "Мне сказали что ты натурал.... Это правда?"
    matwei "Да.."
    "..."
    andrei "Ах ты"
    andrei "Ах ты сукин сын!"
    andrei "Как ты мог променять меня на каких то шмар с пиздой!!"
    andrei "Мы ведь... тогда ... с тобой.."
    andrei "эх.."
    "..."
    andrei "Ведь не даром говорят 'Нет лучше влагалища чем очко товарища!'"
    matwei "Это так... Но меня начали привлекать мохнатые писечки"
    andrei "Ах ты сука!"
    andrei "Так умри же ты, пиздатой сука, смертью!"
    matwei "НЕЕЕЕЕЕЕТ!"
    scene montirovka
    "Андрей берет монтировку и разбивает голову Матвея"
return

label da:
    scene koridor
    show andrei lol
    "Матвей открывает дверь и видит его. В серой водолазке. Такой весь из себя ахуенный. Такой блять красивый. Такой настоящий."
    matwei "Вперед."
    "И Андрей улыбается. Видимо он действительно хочет в туалет. А Матвей реально хочет его. Хочет его всего."
    scene tualet
    "Андрей заходит в кабинку туалета. А за ним заходит Матвей."
    matwei "Встань на колени."
    "Любовь Матвея явно не ожидала такого. В его взгляде было видно недоумение и страх."
    andrei "Матвей, чо за хуйню ты несешь? Выйди."
    matwei "Нет. Выйду я только после того, как получу желаемое. Я столько месяцев страдаю. И хочу утешительный приз."
    matwei "Вставай на колени, Андрей. Я не хочу применять к тебе силу."
    "И он не слушается."
    andrei "Матвей, хватит нести..."
    "Поэтому Матвей нажимает ему на плечи. Прерывает на половине предложения. Он не ожидает. И падает перед Матвеем на колени. Андрей пытается встать, но Матвей не даёт ему это сделать."
    matwei "За эти месяцы я слишком много страдал. Слишком."
    matwei "А теперь растегивай ширинку."
    "Андрей отнекивается. До сих пор в попытках встать на ноги."
    matwei "Ну же, любовь моя."
    "Матвей гладит его по щеке и поднимает ему голову так, что бы их взгляды встретились."
    matwei "Ты же хороший мальчик?"
    matwei "Такие, как ты, должны слушаться."
    "И он подчиняется. Слушается. Растегивает ширинку и смотрит на Матвея снизу так невинно. Как брошенный котенок. Матвей бы забрал его к себе домой. Тогда бы он стал его."
    matwei "Спусти штаны вместе с трусами."
    andrei "Что за хуйня происходит? Нахуй тебе это надо от меня?"
    matwei "Глупенький..."
    "Пытается показаться злым. Но выглядит беззащитно. Особенно с ракурса Матвея."
    matwei "Твой рот сейчас будет занят делом. Не надо его перенапрягать. Помолчи и делай, что говорю."
    "Но он не хочет. И тогда Матвей хватает его за волосы. Тянет его за голову и чуть наклоняется."
    matwei "Это любовь. Ты разве не понимаешь?"
    "Матвей начинает злиться. А у Андрея в глазах опять страх. Более жуткий. И тогда Матвею становится его жаль."
    matwei "Ну не надо меня боятся."
    matwei "Я люблю тебя. И поэтому хочу этого."
    matwei "Сделай, что я прошу..."
    "Рука давно уже ослабила хватку. И теперь она просто плавно гладит его волосы. Немного жестковатые. Но Матвею нравится."
    "Из глаз Андрея текут слезы. Матвей их замечает не сразу. Только после того, как джинсы и трусы Андрея оказались возле обуви."
    matwei "Слёзы не помогут."
    matwei "Я тоже так думал. Поэтому плакал первый месяц. Но без толку.."
    matwei "Легче не становилось..."
    matwei "Помни - я люблю тебя."
    "Если бы существовал Дед Мороз и новогоднее волшебство, то Матвей бы загадал Андрея. Можно даже без обертки. Главное - настоящего и любящего."
    matwei "Я думаю, ты понимаешь, что дальше делать."
    "Андрей кивает. Конечно он понимает. Перед его лицом уже стоящий член Матвея."
    matwei "Давай. Начинай."
    "И он начинает. Так неумело, но так ахуенно. Иногда задевает зубами. Даже это от него приносит Матвею удовольствие."
    matwei "Лишь бы не кончить слишком быстро. Я хочу немного продлить это..."
    "Андрей положил руки Матвею на бедра. Матвей начал двигать тазом ему в такт. И смотреть на него."
    "Время начало лететь как пуля..."
    #звуки отсоса
    "Интенсивность работы языка Андрея начала переходить все человеческие возможности..."
    "У Матвея начала кружиться голова..."
    matwei "Андрей, мне плохо"
    "Андрей пытается разговаривать с хуем во рту"
    andrei "Ммхмхмх"
    andrei "*Чмок*"
    andrei "*Чмок*"
    andrei "Что с тобой?"
    matwei "Андрей..."
    matwei "Я..Я больше.."
    matwei "Я больше так не могу..."
    matwei "Ой ой ой..."
    matwei "Это так, так сладко"
    "Ярко, словно летнее солнце, всё тело Матвея почувствовало невозможный кайф."
    "Однако это было всего лишь чудесное мгновенье...."
    "Через секунду Матвей почувствовал стремительное приближение неизбежного."
    matwei "Андрюша, ой андрончик"
    andrei "Чего, чего такое дорогой?"
    matwei "Готовься."
    matwei "Раскрой свой рот, пошире пидармот!"
    "Андрейка раскрыл свою голубую пасть похлеще любого динозавра."
    "Матвей в свою очередь, начал неистово тарабанить свою 'седьмую струну'."
    matwei "Раз."
    matwei "Два."
    matwei "Пидорас, на!."
    #звуки жёстких оргазмов













    return
