guides = [ {
  "pk": 1,
  "fields": {
    "user": 2,
    "surname": "Васечкин",
    "full_name": "Андрей Васечкин",
    "tours_count": 5,
    "bio": "Я обожаю Москву, и изучаю город с необычных ракурсов. С радостью поделюсь с вами своими лучшими открытиями. Мы поднимемся на сталинские высотки и посмотрим на исторический центр сверху. Я покажу вам то, что скрыто от глаз большинства туристов и даже жителей города. Маршруты подобраны индивидуально под ваш запрос. Для влюбленных доступна услуга свидания на крыше.",
    "is_pro": True,
    "company": 1
  }
},
{
  "pk": 2,
  "fields": {
    "user": 1,
    "surname": "Новикова",
    "full_name": "Людмила Новикова",
    "tours_count": 2,
    "bio": "Я петербурженка в 7-м поколении. Люблю делиться историями и секретами дореволюционных петербургских зданий и особняков. Поделюсь историями моей бабушки. Вместе со мной работает небольшая дружная команда влюбленных в Петербург местных гидов. Мы раскроем вам секреты старинных домов и покажем то, что скрыто от глаз большинства туристов и жителей города.",
    "is_pro": True,
    "company": 2
  }
},
{
  "pk": 3,
  "fields": {
    "user": 3,
    "surname": "Беридзе",
    "full_name": "Георги Беридзе",
    "tours_count": 5,
    "bio": "Филолог-журналист по образованию. За плечами более 9 лет экскурсий по Грузии и барменский опыт. Писатель. Перфекционист. И просто увлеченный человек. Родился и вырос в Тбилиси. Более 10 поколений тут. Люблю этот райский уголок на планете и свою работу. Мама-кулинар привила любовь к вкусной еде.",
    "is_pro": True,
    "company": None
  }
},
{
  "pk": 4,
  "fields": {
    "user": 4,
    "surname": "Ласкина",
    "full_name": "Оксана Ласкина",
    "tours_count": 2,
    "bio": "Я всегда увлекалась историей и, как следствие, получила образование гида-экскурсовода. С удовольствием знакомлю гостей города с историей, татарской культурой и традициями. Вы влюбитесь в наш край.",
    "is_pro": True,
    "company": 5
  }
},
{
  "pk": 5,
  "fields": {
    "user": 5,
    "surname": "Горячий",
    "full_name": "Иван Горячий",
    "tours_count": 7,
    "bio": "Работал учителем истории более 10 лет, последние 5 лет живу в Сочи и уже третий год провожу экскурсии, организовываю туры. На моих прогулках и турах вы узнаете не только об экскурсионных объектах, но и о том, чем живет современный Сочи: о ценах, недвижимости, об интересных местах города и его необычных заведениях. Есть туры разного уровня сложности и комфорта, где можно с детьми и без. Бесплатным бонусом ко всем экскурсиям станет фотосессия на зеркальный фотоаппарат.",
    "is_pro": True,
    "company": 4
  }
},
{
  "pk": 6,
  "fields": {
    "user": 6,
    "surname": "Ивлева",
    "full_name": "Яна Ивлева",
    "tours_count": 5,
    "bio": "Я живу в Стамбуле много лет. По образованию филолог и историк. О Стамбуле читаю, пишу, живу этим городом и люблю его. Раскрою его вам таким, какой он есть: великолепный, приветливый, неизменно интересный и всегда загадочный. Ваше путешествие по этому сказочному городу навсегда останется в памяти и сердце. ",
    "is_pro": True,
    "company": 1
  }
},
]

number = int(input())
guides = [f'{i["fields"]["full_name"]}, туров: {i["fields"]["tours_count"]}\n{i["fields"]["bio"]}' for i in guides if i["pk"] == number]
print(*guides)