import tkinter as tk
import matplotlib.pyplot as plt
import urllib3
import webbrowser
def Genre_Family():
    print("BEST TAMIL FAMILY MOVIES:")
    print(" 1.Aambala",'\n',"2.Papanasam",'\n',"3.Vanam Kottatum",'\n',"4.Namma Veetu Pillai",'\n',
          "5.Kadaikutti Singam",'\n',"6.Thambi",'\n',"7.Annathe",'\n',"8.Visvasam",'\n',
          "9.Kaatrin Mozhi",'\n',"10.Deiva Thirumagal",'\n',"11.Sundara Pandian",'\n',
          "12.Thozha",'\n',"13.Pichaikaran",'\n',"14.MGR Magan",'\n',"15.Kaala",'\n')
def Rating_Family():
     Movies=["Aambala","Papanasam","Vanam Kottatum","Namma Veetu Pillai","Kadaikutti Singam",
             "Thambi","Annathe","Visvasam","Kaatrin Mozhi",
             "Deiva Thirumagal","Sundara Pandian","Thozha","Pichaikaran",
             "MGR Magan","Kaala"]
     IMDb_Ratings=[4.6,8.4,6.3,6.1,7.0,6.8,4.4,6.6,6.2,8.2,6.9,8.0,7.6,7.7,6.7]
     plt.title("RATINGS OF TAMIL FAMILY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color='purple')
     plt.xlabel("IMDb RATING")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Thriller():
    print("BEST TAMIL THRILLER MOVIES:")
    print(" 1.Penguin",'\n',"2.Jai bhim",'\n',"3.Kaithi",'\n',"4.Immaika Nodigal",'\n',"5.24",'\n',
          "6.Papanasam",'\n',"7.Psycho",'\n',"8.Thuparivalan",'\n',"9.K.G.F(tamil)",'\n',
          "10.Irumbu thirai",'\n',"11.U-turn",'\n',"12.Aruvam",'\n',"13.Visaranai",'\n',
          "14.Kuttram 23",'\n',"15.Aarudhra",'\n')
def Rating_Thriller():
     Movies=["Penguin","Jai bhim","Kaithi","Immaika Nodigal","24","Papanasam","Psycho",
             "Thuparivalan","K.G.F(tamil)","Irumbu thirai","U-turn","Aruvam","Visaranai",
             "Kuttram 23","Aarudhra"]
     IMDb_Ratings=[4.6,9.3,8.5,7.4,7.9,8.4,6.3,7.6,8.3,7.7,7,4.7,8.5,7.4,5.8]
     plt.title("RATINGS OF TAMIL THRILLER MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="orange")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Horror():
    print("BEST TAMIL HORROR MOVIES:")
    print(" 1.Balloon",'\n',"2.Mohini",'\n',"3.Shivalinga",'\n',"4.Kanchana 1",'\n',
          "5.Kanchana 2",'\n',"6.Kanchana 3",'\n',"7.Aranmanai 1",'\n',"8.Aranmanai 2",'\n',
          "9.Aranmanai 3",'\n',"10.Aval",'\n',"11.Devi 1",'\n',"12.Devi 2",'\n',
          "13.Diya",'\n',"14.Airaa",'\n',"15.Cinderella",'\n')
def Rating_Horror():
     Movies=["Balloon","Mohini","Shivalinga","Kanchana 1","Kanchana 2","Kanchana 3",
             "Aranmanai 1","Aranmanai 2","Aranmanai 3","Aval","Devi 1","Devi 2","Diya","Airaa",
             "Cinderella"]
     IMDb_Ratings=[4.6,3.2,4.8,6.7,5.6,4.3,5.2,4.3,4.3,9.0,5.5,3.8,5.7,4.7,6.3]
     plt.title("RATINGS OF TAMIL HORROR MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="green")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Action():
    print("BEST TAMIL ACTION MOVIES:")
    print(" 1.Sultan",'\n',"2.Bahubali 1",'\n',"3.Bahubali 2",'\n',"4.Vivegam ",'\n',"5.Spyder",'\n',
          "6.Theeran adikaram ondru",'\n',"7.Petta",'\n',"8.Darbar",'\n',"9.Sarkar",'\n',
          "10.Mersal",'\n',"11.Action",'\n',"12.Kaala",'\n',"13.Theri",'\n',"14.2.0",'\n',
          "15.Singam 1",'\n',"16.Singam 2",'\n',"17.Singam 3",'\n',"18.Thupakki",'\n',
          "19.Maari",'\n',"20.Veeram",'\n')
def Rating_Action():
     Movies=["Sultan","Bahubali 1","Bahubali 2","Vivegam ","Spyder","Theeran adikaram ondru",
             "Petta","Darbar","Sarkar","Mersal","Action","Kaala","Theri","2.0",
             "Singam 1","Singam 2","Singam 3","Thupakki",
             "Maari","Veeram"]
     IMDb_Ratings=[6.3,8,8.2,5.5,6.6,8.3,7.3,6.1,7,7.8,4.6,6.7,7.4,6.2,6.9,6.4,6.3,8.1,6.4,6.5]
     plt.title("RATINGS OF TAMIL ACTION MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="deepskyblue")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()     
def Genre_Comedy():
    print("BEST TAMIL COMEDY MOVIES:")
    print(" 1.Doctor",'\n',"2.Anabelle Sethupathi",'\n',"3.Kalakalappu",'\n',"4.Kalakalappu 2",'\n',
          "5.Sangali Bungali Kadhava Thorae",'\n',"6.Varutha Padatha Valibar Sangam",'\n',
          "7.Tamil Padam 2.0",'\n',"8.Nanban",'\n',"9.Tenaliraman",'\n',"10.Kakki Sattai",'\n',
          "11.Oru kal Oru Kannadi",'\n',"12.Bangalore Naatkal",'\n',"13.Monster",'\n',
          "14.Naai Sekar",'\n',"15.Mandela",'\n')
def Rating_Comedy():
     Movies=["Doctor","Anabelle Sethupathi","Kalakalappu","Kalakalappu 2",
             "Sangali Bungali Kadhava Thorae","Varutha Padatha Valibar Sangam",
              "Tamil Padam 2.0","Nanban","Tenaliraman","Kakki Sattai",
              "Oru kal Oru Kannadi","Bangalore Naatkal","Monster","Naai Sekar","Mandela"]
     IMDb_Ratings=[7.6,3.7,6.9,5.1,5.4,6.9,7.8,7.7,5.4,5.7,6.4,5.7,6.8,5.3,8.5]
     plt.title("RATINGS OF TAMIL COMEDY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="Magenta")
     plt.xlabel("IMDb_RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Romance():
    print("BEST TAMIL ROMANTIC MOVIES:")
    print(" 1.96",'\n',"2.Pyaar prema kadhal",'\n',"3.Maara",'\n',"4.Dev",'\n',"5.Thalli Pogathey",'\n',
          "6.Kavan",'\n',"7.Velan",'\n',"8.Enna solla pogirai",'\n',"9.Adithya Varma",'\n',
          "10.Biskoth",'\n',"11.Enai Noki Paayum Thotta",'\n',"12.100% Kadhal",'\n',
          "13.Kalavani 2",'\n',"14.Ok Kanmani",'\n',"15.Raja Rani",'\n')
def Rating_Romance():
     Movies=["96","Pyaar prema kadhal","Maara","Dev","Thalli Pogathey","Kavan","Velan",
             "Enna solla pogirai","Adithya Varma","Biskoth","Enai Noki Paayum Thotta",
             "100% Kadhal","Kalavani 2","Ok Kanmani","Raja Rani"]
     IMDb_Ratings=[8.5,6.6,7.6,4.8,5.7,7.1,5.1,6.3,4.5,6.1,5.6,3.9,4.0,7.4,7.6]
     plt.title("RATINGS OF TAMIL ROMANCE MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="Red")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Family1():
     print("BEST TELUGU FAMILY MOVIES:")
     print(" 1.Kaadhali",'\n',"2.Super Machi",'\n',"3.Chalte Chalte",'\n',"4.Annapurnamma gari Manavadu",'\n',
          "5.Mahanadhi",'\n',"6.Shyam Singha Roy",'\n',"7.Alavaikuntha purramuloo",'\n',"8.Bharath ane nenu",'\n',
          "9.Nuuvu Naaku Nachchav",'\n',"10.Bommarillu",'\n',"11.Pelli Choopulu",'\n',
          "12.Okkadu",'\n',"13.Kshanam",'\n',"14.Malli malli idhi rani roju",'\n',"15.Middle class abbayi",'\n')
def Rating_Family1():
     Movies=["Kaadhali","Super Machi","Chalte Chalte","Annapurnamma gari Manavadu","Mahanadhi",
             "Shyam Singha Roy","Alavaikuntha purramuloo","Bharat ane nenu","Nuuvu Naaku Nachchav","Bommarillu",
             "Pelli Choopulu","Okkadu","Kshanam","Malli malli idhi rani roju",
             "Middle class abbayi"]
     IMDb_Ratings=[9.4,9.2,8.9,8.5,8.6,8.5,8.2,8.8,8.7,8.2,8.2,8,8.3,7.5,6]
     plt.title("RATINGS OF TELUGU FAMILY MOVIES")
     plt.barh(Movies,IMDb_Ratings)
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Thriller1():
    print("BEST TELUGU THRILLER MOVIES:")
    print(" 1.Evaru",'\n',"2.Hit",'\n',"3.Game over",'\n',"4.V",'\n',"5.Awe",'\n',"6.Seven",'\n',
          "7.Nishabdham",'\n',"8.U turn",'\n',"9.Spyder",'\n',"10.118",'\n',"11.Yevadu",'\n',
          "12.16 Extremes",'\n',"13.Abhimanyudu",'\n',"14.Anaamika",'\n',"15.Raahu",'\n')
def Rating_Thriller1():
     Movies=["Evaru","Hit","Game over","V","Awe","Seven","Nishabdham","U turn","Spyder","118",
              "Yevadu","16 Extremes","Abhimanyudu","Anaamika","Raahu"]
     IMDb_Ratings=[8.2,7.7,7.1,7,7.8,5.2,5.8,7,6.6,6.6,5.7,8.3,8.0,5.6,5.6]
     plt.title("RATINGS OF TELUGU THRILLER MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="lightcoral")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Horror1():
    print("BEST TELUGU HORROR MOVIES:")
    print(" 1.The house next door",'\n',"2.Ezra",'\n',"3.Deyyam",'\n',"4.Maya",'\n',
          "5.Prema katha chithram 2",'\n',"6.Avunu",'\n',"7.Pisaasu",'\n',"8.Bhaagamathie",'\n',
          "9.Tripura",'\n',"10.13B: FEAR HAS A NEW ADDRESS",'\n',"11.Bhoot",'\n',
          "12.Abinetri No 1",'\n',"13.Shaitan",'\n',"14.Jessie",'\n',"15.Arundati",'\n')
def Rating_Horror1():
     Movies=["The house next door","Ezra","Deyyam","Maya","Prema katha chithram 2","Avunu",
              "Pisaasu","Bhaagamathie","Tripura","13B: Fear has a new address","Bhoot",
             "Abinetri No 1","Shaitan","Jessie","Arundati"]
     IMDb_Ratings=[6.8,6.7,8.6,6.8,4.8,6.2,7.6,7.1,5.5,7.4,5.5,5.5,6.2,6.9,7.4]
     plt.title("RATINGS OF TELUGU HORROR MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="springgreen")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Action1():
    print("BEST TELUGU ACTION MOVIES:")
    print(" 1.Pushpa the rise",'\n',"2.Akhanda",'\n',"3.Narappa",'\n',"4.Rangasthalam",'\n',
          "5.Maha samudram",'\n',"6.Dhruva",'\n',"7.Race Gurram",'\n',"8.Red",'\n',
          "9.Naannaku prematho",'\n',"10.Sye Raa Narasimha reddy",'\n',"11.Seetimaar",'\n',
          "12.Makkhi",'\n',"13.Pokiri",'\n',"14.Sahoo",'\n',"15.Katamarayudu",'\n')
def Rating_Action1():
     Movies=["Pushpa the rise","Akhanda","Narappa","Rangasthalam","Maha samudram",
             "Dhruva","Race Gurram","Red","Naannaku prematho","Sye Raa Narasimha reddy",
              "Seetimaar","Makkhi","Pokiri","Sahoo","Katamarayudu"]
     IMDb_Ratings=[7.9,7.2,8.1,8.4,5.2,7.8,7.3,6.6,7.6,7.4,5.4,7.8,7.9,6.0,5.7]
     plt.title("RATINGS OF TELUGU ACTION MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="darkviolet")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Comedy1():
    print("BEST TELUGU COMEDY MOVIES:")
    print(" 1.Jathi ratnalu",'\n',"2.F2 Fun and Frustration",'\n',"3.Brochevarevura",'\n',
          "4.Nuvvu nakku nachav",'\n',"5.Agent sai srinivas athreya",'\n',"6.Raja the great",'\n',
          "7.Anukunnati okati ayyinadhi okkati",'\n',"8.Bhale bhale magadivoy",'\n',
          "9.Nenu local",'\n',"10.Radha",'\n',"11.Oh baby",'\n',"12.Bheesma",'\n',"13.DJ",'\n',
          "14.A Aa",'\n',"15.Deva dassu",'\n')
def Rating_Comedy1():
     Movies=["Jathi ratnalu","F2 Fun and Frustration","Brochevarevura","Nuvvu nakku nachav",
              "Agent sai srinivas athreya","Raja the great","Anukunnati okati ayyinadhi okkati",
              "Bhale bhale magadivoy","Nenu local","Radha","Oh baby","Bheesma","DJ","A Aa",
              "Deva dassu"]
     IMDb_Ratings=[7.6,6.2,8.1,8.7,8.4,6.5,3.9,7.8,6.5,5.5,7.4,6.7,5.9,6.9,6.7]
     plt.title("RATINGS OF TELUGU COMEDY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="deeppink")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Romance1():
    print("BEST TELUGU ROMANTIC MOVIES:")
    print(" 1.Most eligible bachelor",'\n',"2.Varadu kaavalenu",'\n',"3.Tholi prema",'\n',
          "4.Upenna",'\n',"5.Nenu sailaja",'\n',"6.Dear comrade",'\n',"7.Arjun reddy",'\n',
          "8.World famous lover",'\n',"9.Fidaa",'\n',"10.Nenu local",'\n',
          "11.Middle class abbayi",'\n',"12.Jaanu",'\n',"13.Majili",'\n',"14.Geetha govindam",'\n',
          "15.RX 100",'\n')
def Rating_Romance1():
     Movies=["Most eligible bachelor","Varadu kaavalenu","Tholi prema","Upenna","Nenu sailaja",
             "Dear comrade","Arjun reddy","World famous lover","Fidaa","Nenu local",
             "Middle class abbayi","Jaanu","Majili","Geetha govindam","RX 100"]
     IMDb_Ratings=[6.4,6.5,7.3,6.8,7,7.4,8.1,5.1,7.5,6.5,6,7,7.3,7.8,7]
     plt.title("RATINGS OF TELUGU ROMANTIC MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="lime")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Family2():
    print("BEST HINDI FAMILY MOVIES:")
    print(" 1.Taare zameen par",'\n',"2.3 idiots",'\n',"3.Zindagi na milegi dobara",'\n',
          "4.Queen",'\n',"5.Kapoor and sons",'\n',"6.Dil chahta hai",'\n',"7.Jab we met",'\n',
          "8.English vinglish",'\n',"9.Barfi",'\n',"10.Do dooni chaar",'\n',"11.Dil dhadakne do",'\n',
          "12.Wake up sid",'\n',"13.Kuch kuch hota hai",'\n',"14.Dear zindagi",'\n',
          "15.I am kalam",'\n')
def Rating_Family2():
     Movies=["Taare zameen par","3 idiots","Zindagi na milegi dobara","Queen",
              "Kapoor and sons","Dil chahta hai","Jab we met","English vinglish",
              "Barfi","Do dooni chaar","Dil dhadakne do","Wake up sid","Kuch kuch hota hai",
              "Dear zindagi","I am kalam",]
     IMDb_Ratings=[8.5,8.4,8.2,8.2,7.7,8,7.9,7.6,8,7.5,6.9,7.6,7.4,7.5,8.9]
     plt.title("RATINGS OF HINDI FAMILY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="indigo")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()              
def Genre_Thriller2():
    print("BEST HINDI THRILLER MOVIES:")
    print(" 1.Ittefaq",'\n',"2.Talvar",'\n',"3.Drishyam",'\n',"4.Badla",'\n',"5.Te3n",'\n',
          "6.A Wednesday",'\n',"7.Talaash: the answer lies within",'\n',"8.Kahaani",'\n',
          "9.Bell bottom",'\n',"10.Johnny gaddaar",'\n',"11.The body",'\n',"12.Wazar",'\n',
          "13.Batla house",'\n',"14.Bob biswas",'\n',"15.Satyameva jayate",'\n')
def Rating_Thriller2():
     Movies=["Ittefaq","Talvar","Drishyam","Badla","Te3n","A Wednesday","Talaash: the answer lies within",
              "Kahaani","Bell bottom","Johnny gaddaar","The body","Wazar","Batla house","Bob biswas",
              "Satyameva jayate"]
     IMDb_Ratings=[7.3,8.2,8.3,7.8,7.4,8.1,7.2,8,6.2,7.7,5.5,7.2,7.1,6.8,4.7]
     plt.title("RATINGS OF HINDI THRILLER MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="greenyellow")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Horror2():
    print("BEST HINDI HORROR MOVIES:")
    print(" 1.Roohi",'\n',"2.Bhoot part1",'\n',"3.Chhoorii",'\n',"4.Haunted 3D",'\n',"5.Stree",'\n',
          "6.Bulbul",'\n',"7.Machhil jai ki raani hai",'\n',"8.Lupt",'\n',"9.1920",'\n',
          "10.Dybbuk",'\n',"11.Ghost stories",'\n',"12.Raat",'\n',"13.Raaz",'\n',"14.Laxmi",'\n',
          "15.3 A.M",'\n')
def Rating_Horror2():
     Movies=["Roohi","Bhoot part1","Chhoorii","Haunted 3D","Stree","Bulbul",
              "Machhil jai ki raani hai","Lupt","1920","Dybbuk","Ghost stories",
              "Raat","Raaz","Laxmi","3 A.M"]
     IMDb_Ratings=[7.5,7.6,7.9,8.2,6.6,2.3,6.6,6.4,5.1,4.3,7.1,6.5,6.6,2.4,5]
     plt.title("RATINGS OF HINDI HORROR MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="aquamarine")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Action2():
    print("BEST HINDI ACTION MOVIES:")
    print(" 1.URI: The surgical strike",'\n',"2.Baaghi 3",'\n',"3.War",'\n',
          "4.Antim: the final truth",'\n',"5.Radhe",'\n',"6.Commando 3",'\n',
          "7.Khuda haafiz",'\n',"8.krrish",'\n',
          "9.Sooryavanshi",'\n',"10.The power",'\n',"11.Ek tha tiger",'\n',"12.Baaghi",'\n',
          "13.Malang",'\n',"14.Mumbai saga",'\n',"15.Chennai central",'\n')
def Rating_Action2():
     Movies=["URI: The surgical strike","Baaghi 3","War","Antim: the final truth","Radhe",
             "Commando 3","Khuda haafiz","krrish","Sooryavanshi",
              "The power","Ek tha tiger","Baaghi","Malang","Mumbai saga","Chennai central"]
     IMDb_Ratings=[8.3,5.3,7.8,7,1.8,6.3,7.4,6.2,6.3,5.7,5.5,6.5,6.6,6,8.5]
     plt.title("RATINGS OF HINDI ACTION MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="mediumpurple")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Comedy2():
    print(" BEST HINDI COMEDY MOVIES:")
    print(" 1.Hungama 2",'\n',"2.Minnal murali",'\n',"3.Indoo ki jawani",'\n',"4.Chhalang",'\n',
          "5.Ginny weds sunny",'\n',"6.pagal panti",'\n',"7.badhai ho",'\n',"8.Coolie No 1",'\n',
          "9.Made in china",'\n',"10.Luka chupi",'\n',"11.good newwz",'\n',"12.House full 4",'\n',
          "13.Andhadhun",'\n',"14.Total dhamaal",'\n',"15.Befikre",'\n')
def Rating_Comedy2():
     Movies=["Hungama 2","Minnal murali","Indoo ki jawani","Chhalang","Ginny weds sunny",
             "pagal panti","badhai ho","Coolie No 1","Made in china","Luka chupi","good newwz",
             "House full 4","Andhadhun","Total dhamaal","Befikre"]
     IMDb_Ratings=[3.1,8.1,3,6.8,5.7,3.2,8,4.2,6.6,6.3,6.9,3.5,8.2,4.2,4]
     plt.title("RATINGS OF HINDI COMEDY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="salmon")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Genre_Romance2():
    print("BEST HINDI ROMANTIC MOVIES:")
    print(" 1.Yeh jawaani hai deewani",'\n',"2.Geharaaiyan",'\n',"3.Love aaj kal",'\n',
          "4.Ae dil hai mushkil",'\n',"5.Dil se",'\n',"6.Rockstar",'\n',"7.Aashiqui 1",'\n',
          "8.Aaashiqui 2",'\n',"9.Jab tak hai jaan",'\n',"10.Raam leela",'\n',"11.Fanaa",'\n',
          "12.Student of the year",'\n',"13.Kabir singh",'\n',"14.Raabta",'\n',"15.Jodhaa akbar",'\n')
def Rating_Romance2():
     Movies=["Yeh jawaani hai deewani","Geharaaiyan","Love aaj kal","Ae dil hai mushkil",
              "Dil se","Rockstar","Aashiqui 1","Aaashiqui 2","Jab tak hai jaan","Raam leela",
              "Fanaa","Student of the year","Kabir singh","Raabta","Jodhaa akbar"]
     IMDb_Ratings=[7.2,6.4,4.7,5.8,7.7,6.3,6.3,7,6.7,6.4,7.2,5.3,7.1,5.2,7.6]
     plt.title("RATINGS OF HINDI ROMANCE MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="mediumvioletred")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()              
def Genre_Family3():
    print("BEST ENGLISH FAMILY MOVIES:")
    print(" 1.Harry potter",'\n',"2.Cindrella",'\n',"3.Spider man",'\n',
          "4.Charlie and the chocolate factory",'\n',"5.Enchanted",'\n',"6.The parent trap",'\n',
          "7.Inside out",'\n',"8.Jumanji",'\n',"9.Alice in wonderland",'\n',"10.Frozen",'\n',
          "11.Beauty and the beast",'\n',"12.Tangled",'\n',"13.Home alone",'\n',"14.Aladdin",'\n',
          "15.Mulan",'\n')
def Rating_Family3():
     Movies=["Harry potter","Cindrella","Spider man","Charlie and the chocolate factory",
              "Enchanted","The parent trap","Inside out","Jumanji","Alice in wonderland",
              "Frozen","Beauty and the beast","Tangled","Home alone","Aladdin","Mulan"]
     IMDb_Ratings=[7.6,4.2,7.3,6.6,7,6.6,8.1,7,6.4,7.4,7.1,7.7,7.6,6.9,5.7]
     plt.title("RATINGS OF ENGLISH FAMILY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="firebrick")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()             
def Genre_Thriller3():
    print("BEST ENGLISH THRILLER MOVIES:")
    print(" 1.Gone girl",'\n',"2.Shutter island",'\n',"3.Prisoners",'\n',"4.The invisible man",'\n',
          "5.Don't breathe",'\n',"6.Inception",'\n',"7.The woman in the window",'\n',
          "8.Tenet",'\n',"9.Wrath of man",'\n',"10.Parasite",'\n',"11.Nightcrawler",'\n',
          "12.No time to die",'\n',"13.The sixth sense",'\n',"14.Black swan",'\n',
          "15.A quiet place 2",'\n')
def Rating_Thriller3():
     Movies=["Gone girl","Shutter island","Prisoners","The invisible man","Saw",
             "Inception","The woman in the window","Tenet","Wrath of man","Parasite",
             "Nightcrawler","No time to die","The sixth sense","Black swan","A quiet place 2"]
     IMDb_Ratings=[8.1,8.2,8.1,7.1,7.6,8.8,5.7,7.4,7.1,8.6,7.8,7.3,8.1,8,7.3]
     plt.title("RATINGS OF ENGLISH THRILLER MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="darkturquoise")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()             
def Genre_Horror3():
    print("BEST ENGLISH HORROR MOVIES:")
    print(" 1.A quiet place",'\n',"2.The conjuring",'\n',"3.The nun",'\n',"4.Hereditary",'\n',
          "5.IT",'\n',"6.Insidious",'\n',"7.Possessions of Hannah grace",'\n',"8.The witch",'\n',
          "9.Blumhouse's fantasy island",'\n',"10.The curse of the weeping women",'\n',"11.Sinister",'\n',
          "12.Anabelle comes home",'\n',"13.The night house 2",'\n',"14.Malignant",'\n',
          "15.The cabin in the woods",'\n')
def Rating_Horror3():
     Movies=["A quiet place","The conjuring","The nun","Hereditary","IT","Insidious",
              "Possessions of Hannah grace","The witch","Blumhouse's fantasy island",
              "The curse of the weeping women","Sinister","Anabelle comes home","The night house 2",
              "Malignant","The cabin in the woods"]
     IMDb_Ratings=[7.5,7.5,5.3,7.3,7.3,6.8,5.2,6.9,4.9,7.1,6.8,5.9,6.5,6.3,6.8]
     plt.title("RATINGS OF ENGLISH HORROR MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="darkblue")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()       
def Genre_Comedy3():
    print(" BEST ENGLISH COMEDY MOVIES:")
    print(" 1.Free guy",'\n',"2.Ghostbustlers: afterlife",'\n',"3.The hangover",'\n',
          "4.Due date",'\n',"5.That's my boy",'\n',"6.Red notice",'\n',"7.21 jump street",'\n',
          "8.Jungle cruise",'\n',"9.Bad teacher",'\n',"10.Ted",'\n',"11.Central intelligence",'\n',
          "12.17 again",'\n',"13.Men in black",'\n',"14.Clueless",'\n',"15.Last christmas",'\n')
def Rating_Comedy3():
     Movies=["Free guy","Ghostbustlers: afterlife","The hangover","Due date","That's my boy",
             "Red notice","21 jump street","Jungle cruise","Bad teacher","Ted","Central intelligence",
             "17 again","Men in black","Clueless","Last christmas"]
     IMDb_Ratings=[7.2,7.2,7.7,6.5,5.5,6.3,7.2,6.6,5.6,6.9,6.3,6.4,7.3,6.9,6.5]
     plt.title("RATINGS OF ENGLISH COMEDY MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="yellowgreen")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()       
def Genre_Action3():
    print("BEST ENGLISH ACTION MOVIES:")
    print(" 1.Shang chi",'\n',"2.Venom",'\n',"3.Mission:impossible",'\n',"4.The dark knight",'\n',
          "5.Lucy",'\n',"6.The hunger games: catching fire",'\n',"7.Red notice",'\n',
          "8.Mad max:fury road",'\n',"9.Matrix",'\n',"10.The suicide squad",'\n',
          "11.Nobody",'\n',"12.Eternals",'\n',"13.Watchmen",'\n',"14.Black widow",'\n',
          "15.Jack reacher",'\n')
def Rating_Action3():
     Movies=["Shang chi","Venom","3.Mission:impossible","The dark knight","Lucy","The hunger games: catching fire",
             "Red notice","Mad max:fury road","The matrix","The suicide squad","Nobody","Eternals",
             "Watchmen","Black widow","Jack reacher"]
     IMDb_Ratings=[7.5,6.7,7.3,9,6.4,7.2,6.3,8.7,7.2,8.7,7.4,6.4,7.6,6.7,7]
     plt.title("RATINGS OF ENGLISH ACTION MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="chocolate")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()       
def Genre_Romance3():
    print("BEST ENGLISH ROMANTIC MOVIES:")
    print(" 1.The notebook",'\n',"2.The fault in our stars",'\n',"3.Me before you",'\n',
          "4.Call me by your name",'\n',"5.Twilight",'\n',"6.After",'\n',
          "7.The lucky one",'\n',"8.Titanic",'\n',"9.Pride and prejuidice",'\n',
          "10.The shape of water",'\n',"11.The curious case of benjamin button",'\n',
          "12.The great gatsby",'\n',"13.The proposal",'\n',"14.La La Land",'\n',
          "15.Gone with the wind",'\n')
def Rating_Romance3():
     Movies=["The notebook","The fault in our stars","Me before you","Call me by your name",
             "Twilight","After","The lucky one","Titanic","Pride and prejuidice",
             "The shape of water","The curious case of benjamin button","The great gatsby",
             "The proposal","La La Land","Gone with the wind"]
     IMDb_Ratings=[7.8,7.7,7.4,7.9,5.2,5.3,6.5,7.8,7.8,7.3,7.8,7.2,6.7,8,8.1]
     plt.title("RATINGS OF ENGLISH ROMANTIC MOVIES")
     plt.barh(Movies,IMDb_Ratings,color="darkgrey")
     plt.xlabel("IMDb RATINGS")
     plt.ylabel("MOVIES")
     plt.show()
def Tamil_1():
     window3=tk.Tk()
     label2=tk.Label(window3,text="TAMIL MOVIE RATINGS",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window3,text="FAMILY MOVIE RATINGS",fg="black",borderwidth=12,
                       font="timesnewroman 20 bold",bg="orangered",width=21,height=1,command=Rating_Family).pack()
     button2=tk.Button(window3,text="THRILLER MOVIE RATINGS",fg="black",bg="tomato",borderwidth=12,
                       font="timesnewroman 20 bold",width=21,height=1,command=Rating_Thriller).pack()
     button3=tk.Button(window3,text="HORROR MOVIE RATINGS",fg="black",borderwidth=12,
                       font="timesnewroman 20 bold",bg="coral",width=21,height=1,command=Rating_Horror).pack()
     button4=tk.Button(window3,text="ACTION MOVIE RATINGS",fg="black",borderwidth=12,
                       font="timesnewroman 20 bold",bg="lightsalmon",width=21,height=1,command=Rating_Action).pack()
     button5=tk.Button(window3,text="COMEDY MOVIE RATINGS",fg="black",borderwidth=12,
                       font="timesnewroman 20 bold",bg="lightcoral",width=21,height=1,command=Rating_Comedy).pack()
     button6=tk.Button(window3,text="ROMANCE MOVIE RATINGS",fg="black",borderwidth=12,
                       font="timesnewroman 20 bold",bg="salmon",width=21,height=1,command=Rating_Romance).pack()
     window3.mainloop()
def Tamil():
     window2=tk.Tk()
     label1=tk.Label(window2,text=" TAMIL MOVIE GENRES",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window2,text="FAMILY",fg="black",bg="orangered",borderwidth=12,                  
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Family).pack()
     button2=tk.Button(window2,text="THRILLER",fg="black",bg="tomato",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Thriller).pack()
     button3=tk.Button(window2,text="HORROR",fg="black",bg="coral",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Horror).pack()
     button4=tk.Button(window2,text="COMEDY",fg="black",bg="lightsalmon",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Comedy).pack()
     button5=tk.Button(window2,text="ACTION",fg="black",bg="lightcoral",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Action).pack()
     button6=tk.Button(window2,text="ROMANCE",fg="black",bg="salmon",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Romance).pack()
     button7=tk.Button(window2,text="RATING",fg="white",bg="dimgrey",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Tamil_1).pack()
     window2.mainloop()
def Telugu_1():
     window3=tk.Tk()
     label2=tk.Label(window3,text="TELUGU MOVIE RATINGS",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window3,text="FAMILY MOVIE RATINGS",fg="black",bg="limegreen",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Family1).pack()
     button2=tk.Button(window3,text="THRILLER MOVIE RATINGS",fg="black",bg="lime",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Thriller1).pack()
     button3=tk.Button(window3,text="HORROR MOVIE RATINGS",fg="black",bg="yellowgreen",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Horror1).pack()
     button4=tk.Button(window3,text="ACTION MOVIE RATINGS",fg="black",bg="greenyellow",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Action1).pack()
     button5=tk.Button(window3,text="COMEDY MOVIE RATINGS",fg="black",bg="lawngreen",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Comedy1).pack()
     button6=tk.Button(window3,text="ROMANCE MOVIE RATINGS",fg="black",bg="palegreen",borderwidth=12,
                font="timesnewroman 20 bold",width=21,height=1,command=Rating_Romance1).pack()
     
     window3.mainloop()
def Telugu():
     window2=tk.Tk()
     label1=tk.Label(window2,text=" TELUGU MOVIE GENRES",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window2,text="FAMILY",fg="black",bg="limegreen",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Family1).pack()
     button2=tk.Button(window2,text="THRILLER",fg="black",bg="lime",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Thriller1).pack()
     button3=tk.Button(window2,text="HORROR",fg="black",bg="yellowgreen",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Horror1).pack()
     button4=tk.Button(window2,text="COMEDY",fg="black",bg="greenyellow",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Comedy1).pack()
     button5=tk.Button(window2,text="ACTION",fg="black",bg="lawngreen",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Action1).pack()
     button6=tk.Button(window2,text="ROMANCE",fg="black",bg="palegreen",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Genre_Romance1).pack()
     button7=tk.Button(window2,text="RATING",fg="white",bg="dimgrey",borderwidth=12,
                       font="timesnewroman 20 bold",width=20,height=1,command=Telugu_1).pack()
     window2.mainloop()
def Hindi_1():
     window3=tk.Tk()
     label2=tk.Label(window3,text="HINDI MOVIE RATINGS",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window3,text="FAMILY MOVIE RATINGS",fg="black",bg="blueviolet",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Family2).pack()
     button2=tk.Button(window3,text="THRILLER MOVIE RATINGS",fg="black",bg="darkviolet",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Thriller2).pack()
     button3=tk.Button(window3,text="HORROR MOVIE RATINGS",fg="black",bg="darkorchid",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Horror2).pack()
     button4=tk.Button(window3,text="ACTION MOVIE RATINGS",fg="black",bg="mediumorchid",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Action2).pack()
     button5=tk.Button(window3,text="COMEDY MOVIE RATINGS",fg="black",bg="violet",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Comedy2).pack()
     button6=tk.Button(window3,text="ROMANCE MOVIE RATINGS",fg="black",bg="plum",borderwidth=12,
            font="timesnewroman 20 bold",width=21,height=1,command=Rating_Romance2).pack()
     window3.mainloop()
def Hindi():
     window2=tk.Tk()
     label1=tk.Label(window2,text="HINDI MOVIE GENRES",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window2,text="FAMILY",fg="black",bg="blueviolet",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Family2).pack()
     button2=tk.Button(window2,text="THRILLER",fg="black",bg="darkviolet",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Thriller2).pack()
     button3=tk.Button(window2,text="HORROR",fg="black",bg="darkorchid",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Horror2).pack()
     button4=tk.Button(window2,text="COMEDY",fg="black",bg="mediumorchid",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Comedy2).pack()
     button5=tk.Button(window2,text="ACTION",fg="black",bg="violet",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Action2).pack()
     button6=tk.Button(window2,text="ROMANCE",fg="black",bg="plum",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Genre_Romance2).pack()
     button7=tk.Button(window2,text="RATING",fg="white",bg="dimgrey",borderwidth=12,
              font="timesnewroman 20 bold",width=20,height=1,command=Hindi_1).pack()
     window2.mainloop()
def English_1():
     window3=tk.Tk()
     label2=tk.Label(window3,text="ENGLISH MOVIE RATINGS",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window3,text="FAMILY MOVIE RATINGS",fg="black",bg="mediumvioletred",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Family3).pack()
     button2=tk.Button(window3,text="THRILLER MOVIE RATINGS",fg="black",bg="deeppink",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Thriller3).pack()
     button3=tk.Button(window3,text="HORROR MOVIE RATINGS",fg="black",bg="hotpink",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Horror3).pack()
     button4=tk.Button(window3,text="ACTION MOVIE RATINGS",fg="black",bg="palevioletred",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Action3).pack()
     button5=tk.Button(window3,text="COMEDY MOVIE RATINGS",fg="black",bg="lightpink",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Comedy3).pack()
     button6=tk.Button(window3,text="ROMANCE MOVIE RATINGS",fg="black",bg="pink",borderwidth=12,
              font="timesnewroman 20 bold",width=21,height=1,command=Rating_Romance3).pack()
     window3.mainloop()
def English():
     window2=tk.Tk()
     label1=tk.Label(window2,text="ENGLISH MOVIE GENRES",font="timesnewroman 25 bold").pack()
     button1=tk.Button(window2,text="FAMILY",fg="black",bg="mediumvioletred",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Family3).pack()
     button2=tk.Button(window2,text="THRILLER",fg="black",bg="deeppink",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Thriller3).pack()
     button3=tk.Button(window2,text="HORROR",fg="black",bg="hotpink",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Horror3).pack()
     button4=tk.Button(window2,text="COMEDY",fg="black",bg="palevioletred",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Comedy3).pack()
     button5=tk.Button(window2,text="ACTION",fg="black",bg="lightpink",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Action3).pack()
     button6=tk.Button(window2,text="ROMANCE",fg="black",bg="pink",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=Genre_Romance3).pack()
     button7=tk.Button(window2,text="RATING",fg="white",bg="dimgrey",borderwidth=12,
                font="timesnewroman 20 bold",width=20,height=1,command=English_1).pack()
     window2.mainloop()
window=tk.Tk()
label=tk.Label(text="MOVIE LANGUAGES",font="timesnewroman 25 bold",fg="black")
label.pack()
button1=tk.Button(text="TAMIL",fg="black",width=20,height=2,borderwidth=12,command=Tamil,
                  font="timesnewroman 20 bold",bg="lightseagreen").pack()
button2=tk.Button(text="ENGLISH",fg="black",width=20,height=2,borderwidth=12,command=English,
                  font="timesnewroman 20 bold",bg="mediumturquoise").pack()
button3=tk.Button(text="TELUGU",fg="black",width=20,height=2,borderwidth=12,command=Telugu,
                  font="timesnewroman 20 bold",bg="turquoise").pack()
button4=tk.Button(text="HINDI",fg="black",width=20,height=2,borderwidth=12,command=Hindi,
                  font="timesnewroman 20 bold",bg="aquamarine").pack()
window.mainloop()
dict={"Aambala":"https://www.youtube.com/watch?v=NohOBlQDEr0",
     "Papanasam":"https://www.youtube.com/watch?v=qTnYaTYl9RQ", 
     "Vanam Kottatum":"https://www.youtube.com/watch?v=NA9gTne07OY", 
     "Namma Veetu Pillai":"https://www.youtube.com/watch?v=59_Fl_e46IU",
     "Kadaikutti Singam":"https://www.youtube.com/watch?v=v5YO-Zred7w",
     "Thambi":"https://www.youtube.com/watch?v=y2vwIiLyt1Y", 
     "Annathe":"https://www.youtube.com/watch?v=zyVX8g71TGo", 
     "Visvasam":"https://www.youtube.com/watch?v=TiDyv53adt0", 
     "Kaatrin Mozhi":"https://www.youtube.com/watch?v=gYlm_zgSxvk", 
     "Deiva Thirumagal":"https://www.youtube.com/watch?v=6-pxL99c3F4",
     "Sundara Pandian":"https://www.youtube.com/watch?v=m4JsZMBzBOw", 
     "Thozha":"https://www.youtube.com/watch?v=EaxHnDbsfws", 
     "Pichaikaran":"https://www.youtube.com/watch?v=m2gaBEJxoxY", 
     "MGR Magan":"https://www.youtube.com/watch?v=yG6Q36vpUzA",  
     "Kaala":"https://www.youtube.com/watch?v=mMCEvr3VWqQ",
     "Penguin":"https://www.youtube.com/watch?v=1Mwp1CfFV-k",
     "Jai bhim":"https://www.youtube.com/watch?v=Gc6dEDnL8JA",
     "Kaithi":"https://www.youtube.com/watch?v=g79CvhHaj5I",
     "Immaika Nodigal":"https://www.youtube.com/watch?v=Q0QoCgbwPjs",
     "24":"https://www.youtube.com/watch?v=wqXE_es_I3M",
     "Papanasam":"https://www.youtube.com/watch?v=qTnYaTYl9RQ",
     "Psycho":"https://www.youtube.com/watch?v=SDZCXPBYHY0",
     "Thuparivalan":"https://www.youtube.com/watch?v=FSDUhmOn6bY",
     "K.G.F(tamil)":"https://www.youtube.com/watch?v=-KfsY-qwBS0",
     "Irumbu thirai":"https://www.youtube.com/watch?v=3n3L428I8MQ",
     "U-turn":"https://www.youtube.com/watch?v=GVEJMhdK_d0",
     "Aruvam":"https://www.youtube.com/watch?v=t8av5RjuupM",
     "Visaranai":"https://www.youtube.com/watch?v=4mnzK2KIz9U",
     "Kuttram 23":"https://www.youtube.com/watch?v=XV4btHdEMxg",
     "Aarudhra":"https://www.youtube.com/watch?v=LoMHgklWZHs",
     "Balloon":"https://www.youtube.com/watch?v=9VAZ0WCTrGk",
     "Mohini":"https://www.youtube.com/watch?v=vvKO5suexeQ",
     "Shivalinga":"https://www.dailymotion.com/video/x5drjyu",
     "Kanchana 1":"https://www.imdb.com/video/vi921548825",
     "Kanchana 2":"https://www.imdb.com/video/vi1335671321",
     "Kanchana 3":"https://www.youtube.com/watch?v=-16MdQ9Blgk",
     "Aranmanai 1":"https://www.imdb.com/video/vi2734275353",
     "Aranmanai 2":"https://www.youtube.com/watch?v=OSH18HWQZRw",
     "Aranmanai 3":"https://www.youtube.com/watch?v=MRiK4WHaJb8",
     "Aval":"https://www.youtube.com/watch?v=Ft1KvQNteYY",
     "Devi 1":"https://www.youtube.com/watch?v=gWLhgenab28",
     "Devi 2":"https://www.youtube.com/watch?v=oC5GTqA-3_8",
     "Diya":"https://www.youtube.com/watch?v=MDP_SdBI2wE",
     "Airaa":"https://www.youtube.com/watch?v=V0JBOhkml14",
     "Cinderella":"https://www.youtube.com/watch?v=SqS4czryfdc",
     "Sultan":"https://www.youtube.com/watch?v=EWp7eDbJSCA",
     "Bahubali":"https://www.youtube.com/watch?v=EWp7eDbJSCA",
     "Bahubali 2":"https://www.youtube.com/watch?v=94BzBOpv42g",
     "Vivegam":"https://www.youtube.com/watch?v=yJdHR8nCYWk",
     "Spyder":"https://www.youtube.com/watch?v=GIzMJ3atybQ",
     "Theeran adikaram ondru":"https://www.youtube.com/watch?v=uLuGOOFORAs",
     "Petta":"https://www.youtube.com/watch?v=FCB0ZfQ9Rzs",
     "Darbar":"https://www.youtube.com/watch?v=1JlLi9pDaJE",
     "Sarkar":"https://www.youtube.com/watch?v=VkkyaodksT4",
     "Mersal":"https://www.youtube.com/watch?v=gQDo5QuZTaw",
     "Action":"https://www.youtube.com/watch?v=74FI1-yNOOg",
     "Kaala":"https://www.youtube.com/watch?v=mMCEvr3VWqQ",
     "Theri":"https://www.youtube.com/watch?v=ZK4uGLpkAKk",
     "2.0":"https://www.youtube.com/watch?v=jrETX2eDhL8",
     "Singam 1":"https://www.youtube.com/watch?v=WSoPFohbbWs",
     "Singam 2":"https://www.youtube.com/watch?v=W0tmFq4nwt8",
     "Singam 3":"https://www.youtube.com/watch?v=L5YMrYNSxiE",
     "Thupakki":"https://www.youtube.com/watch?v=s0O44Sn1hD4",
     "Maari":"https://www.youtube.com/watch?v=W3XFChOz-Z0",
     "Veeram":"https://www.youtube.com/watch?v=E2jIoTXQdxY",
     "Doctor":"https://www.youtube.com/watch?v=oQiH_Iw0kDs",
     "Anabelle Sethupathi":"https://www.youtube.com/watch?v=5ZjZbKI1m2s",
     "Kalakalappu":"https://www.youtube.com/watch?v=Rcclo_LBGd0",
     "Kalakalappu 2":"https://www.youtube.com/watch?v=0UM_FOOYVXs",
     "Sangali Bungali Kadhava Thorae":"https://www.youtube.com/watch?v=maJM53J6jjo",
     "Varutha Padatha Valibar Sangam":"https://www.youtube.com/watch?v=P-qYweRlYVg",
     "Tamil Padam 2.0":"https://www.youtube.com/watch?v=BPcEcDdEF30",
     "Nanban":"https://www.youtube.com/watch?v=oI4n3DibqkA",
     "Tenaliraman":"https://www.youtube.com/watch?v=ngGSjd9ctgY",
     "Kakki Sattai":"https://www.youtube.com/watch?v=leCsVj8SKyk",
     "Oru kal Oru Kannadi":"https://www.youtube.com/watch?v=8t-c0NIqoWc",
     "Bangalore Naatkal":"https://www.youtube.com/watch?v=qAtLkdR6KQE",
     "Monster":"https://www.youtube.com/watch?v=PMMZZuiymlg",
     "Naai Sekar":"https://www.youtube.com/watch?v=c6Y8-oJRwiU",
     "Mandela":"https://www.youtube.com/watch?v=ES1Oz7cW11M",
     "96":"https://www.youtube.com/watch?v=r0synl-lI4I",
     "Pyaar prema kadhal":"https://www.youtube.com/watch?v=NPJZZta_1p8",
     "Maara":"https://www.youtube.com/watch?v=Lv5KUKKwQEw",
     "Dev":"https://www.youtube.com/watch?v=AB2LXzNvUNo",
     "Thalli Pogathey":"https://www.youtube.com/watch?v=ukoc49LOzsA",
     "Kavan":"https://www.youtube.com/watch?v=y2mei-eRw2s",
     "Velan":"https://www.youtube.com/watch?v=FqSpkA_-S_0",
     "Enna solla pogirai":"https://www.youtube.com/watch?v=K8ngHnShirw",
     "Adithya Varma":"https://www.youtube.com/watch?v=MQEuFT5DUeY",
     "Biskoth":"https://www.youtube.com/watch?v=T6Y53rqv0vQ",
     "Enai Noki Paayum Thotta":"https://www.youtube.com/watch?v=2zyEs5tTaK8",
     "100% Kadhal":"https://www.youtube.com/watch?v=DS-5aQay_kA",
     "Kalavani 2":"https://www.youtube.com/watch?v=sa690ErhlEc",
     "Ok Kanmani":"https://www.youtube.com/watch?v=2mBG4vlhcCc",
     "Raja Rani":"https://www.youtube.com/watch?v=wZm38_0aIXk",
     "Kaadhali":"https://www.youtube.com/watch?v=duqAnrogMBg",
     "Super Machi":"https://www.youtube.com/watch?v=32rk3S5whMQ",
     "Chalte Chalte":"https://www.youtube.com/watch?v=aJ_yPbD6LKw",
     "Annapurnamma gari Manavadu":"https://www.youtube.com/watch?v=f55R29cfk00",
     "Mahanadhi":"https://www.youtube.com/watch?v=PLmBpf7UHJs",
     "Shyam Singha Roy":"https://www.youtube.com/watch?v=QliDRYaknmI",
     "Alavaikuntha purramuloo":"https://www.youtube.com/watch?v=SkENAjfVoNI",
     "Bharat ane nenu":"https://www.youtube.com/watch?v=KMWS5y2gZ6E",
     "Nuuvu Naaku Nachchav":"https://www.youtube.com/watch?v=ZSL2JRkyYoY",
     "Bommarillu":"https://www.youtube.com/watch?v=3BvfRARwT5k",
     "Pelli Choopulu":"https://www.youtube.com/watch?v=9v9nESxBpqU",
     "Okkadu":"https://www.youtube.com/watch?v=OlKmTiZ1Nmc",
     "Kshanam":"https://www.youtube.com/watch?v=OroFSmQQm1U",
     "Malli malli idhi rani roju":"https://www.youtube.com/watch?v=KXKZbb-loBQ",
     "Middle class abbayi":"https://www.youtube.com/watch?v=9V0hw6QjzSw",
     "Evaru":"https://www.youtube.com/watch?v=TfW6lil5uyc",
     "Hit":"https://www.youtube.com/watch?v=uYdsWe9iBAA",
     "Game over":"https://www.youtube.com/watch?v=2fliIDAIiPY",
     "V":"https://www.youtube.com/watch?v=eBcYKDUT8fs",
     "Awe":"https://www.youtube.com/watch?v=xOEscQChX7M",
     "7":"https://www.youtube.com/watch?v=VzajUuo4WwQ",
     "Nishabdham":"https://www.youtube.com/watch?v=OOotZ7Q4o8w",
     "U turn":"https://www.youtube.com/watch?v=HG7Lv384yTU",
     "Spyder":"https://www.youtube.com/watch?v=og1zP3u0b4k",
     "118":"https://www.youtube.com/watch?v=OHkz3YP4Kj0",
     "Yevadu":"https://www.youtube.com/watch?v=vBIRjqcr5AQ",
     "16 Extremes":"https://www.youtube.com/watch?v=CHasQbXxgYk",
     "Abhimanyudu":"https://www.youtube.com/watch?v=sM3u_l3IWl0",
     "Anaamika":"https://www.youtube.com/watch?v=bP5JilWa8gw",
     "Raahu":"https://www.youtube.com/watch?v=EJ6cuQeaZtg",
     "The house next door":"https://www.youtube.com/watch?v=odYx44CitAQ",
     "Ezra":"https://www.youtube.com/watch?v=4ecn22XHqHc",
     "Deyyam":"https://www.youtube.com/watch?v=A5724iiNoYs",
     "Maya":"https://www.youtube.com/watch?v=MhSITfcvy7Q",
     "Prema katha chithram 2":"https://www.youtube.com/watch?v=RJcXjj3EzfI",
     "Avunu":"https://www.youtube.com/watch?v=KIFJNawbIFQ",
     "Pisaasu":"https://www.youtube.com/watch?v=raHLv5JJ2A0",
     "Bhaagamathie":"https://www.youtube.com/watch?v=Aahj3atxdS4",
     "Tripura":"https://www.youtube.com/watch?v=rsbvr3an4Ko",
     "13B: Fear has a new address":"https://www.youtube.com/watch?v=-eWl5M-jqxs",
     "Bhoot":"https://www.youtube.com/watch?v=ELcRnZ3kP08",
     "Abinetri No 1":"https://www.youtube.com/watch?v=MtnJbH4LfV4",
     "Shaitan":"https://www.youtube.com/watch?v=-PYV3VH4xUM",
     "Jessie":"https://www.youtube.com/watch?v=Jhi-b5e63CQ",
     "Arundati":"https://www.youtube.com/watch?v=3OXhA30aJ7M",
     "Pushpa the rise":"https://www.youtube.com/watch?v=Q1NKMPhP8PY",
     "Akhanda":"https://www.youtube.com/watch?v=CWnu8pQRCkQ",
     "Narappa":"https://www.youtube.com/watch?v=GNJ-kT6gFhQ",
     "Rangasthalam":"https://www.youtube.com/watch?v=sueMmTm-M4Y",
     "Maha samudram":"https://www.youtube.com/watch?v=khbpC9joyoY",
     "Dhruva":"https://www.youtube.com/watch?v=r_yVN37aCYI",
     "Race Gurram":"https://www.youtube.com/watch?v=nda6eGtu8DI",
     "Red":"https://www.youtube.com/watch?v=M6hLhA6hsnw",
     "Naannaku prematho":"https://www.youtube.com/watch?v=Om69gF1iiT4",
     "Sye Raa Narasimha reddy":"https://www.youtube.com/watch?v=KyhrrdpA2YA",
     "Seetimaar":"https://www.youtube.com/watch?v=_Sufd-Dkrj4",
     "Makkhi":"https://www.youtube.com/watch?v=kVbBSqG7eNw",
     "Pokiri":"https://www.youtube.com/watch?v=nWgHIe6Sy_o",
     "Sahoo":"https://www.youtube.com/watch?v=lD0-ztCFydA",
     "Katamarayudu":"https://www.youtube.com/watch?v=XpAaOER_6iY",
     "Jathi ratnalu":"https://www.youtube.com/watch?v=Hgc07_BX4_8",
     "F2 Fun and Frustration":"https://www.youtube.com/watch?v=XttQbFKkeHQ",
     "Brochevarevura":"https://www.youtube.com/watch?v=S-ytHh7FFtg",
     "Nuvvu nakku nachav":"https://www.youtube.com/watch?v=ZSL2JRkyYoY",
     "Agent sai srinivas athreya":"https://www.youtube.com/watch?v=iPfVbR5oAWE",
     "Raja the great":"https://www.youtube.com/watch?v=o3Liy7yJkHs",
     "Anukunnati okati ayyinadhi okkati":"https://www.youtube.com/watch?v=KNiI-XSp03k",
     "Bhale bhale magadivoy":"https://www.youtube.com/watch?v=x3b3vvI6G18",
     "Nenu local":"https://www.youtube.com/watch?v=lylc7eY6yRU",
     "Radha":"https://www.youtube.com/watch?v=J_guI6Mi6g4",
     "Oh baby":"https://www.youtube.com/watch?v=D4x6CeRV5Bc",
     "Bheesma":"https://www.youtube.com/watch?v=8A9mJYprMl4",
     "DJ":"https://www.youtube.com/watch?v=fy-kooz9se4",
     "A Aa":"https://www.youtube.com/watch?v=V4KdbX1xvaI",
     "Deva dassu":"https://www.youtube.com/watch?v=CK_xo3UQIvU",
     "Most eligible bachelor":"https://www.youtube.com/watch?v=oFJxjVVovQo",
     "Varadu kaavalenu":"https://www.youtube.com/watch?v=vAxNeM5gIXg",
     "Tholi prema":"https://www.youtube.com/watch?v=-kFvrsAgp3M",
     "Upenna":"https://www.youtube.com/watch?v=fB3RcpbLvco",
     "Nenu sailaja":"https://www.youtube.com/watch?v=i916BRRHoTg",
     "Dear comrade":"https://www.youtube.com/watch?v=x_NEfuXTR1c",
     "Arjun reddy":"https://www.youtube.com/watch?v=aozErj9NqeE",
     "World famous lover":"https://www.youtube.com/watch?v=g8DNVJvE-rE",
     "Fidaa":"https://www.youtube.com/watch?v=AVtvjfoXNXc",
     "Nenu local":"https://www.youtube.com/watch?v=lylc7eY6yRU",
     "Middle class abbayi":"https://www.youtube.com/watch?v=9V0hw6QjzSw",
     "Jaanu":"https://www.youtube.com/watch?v=8sWRT2hGPcQ",
     "Majili":"https://www.youtube.com/watch?v=R9VF3m7UiLw",
     "Geetha govindam":"https://www.youtube.com/watch?v=qHqWRCxhcOk",
     "RX 100":"https://www.youtube.com/watch?v=IbPL4FUTvXY",
     "Taare zameen par":"https://www.youtube.com/watch?v=F-PAI2HnQUo",
     "3 idiots":"https://www.youtube.com/watch?v=K0eDlFX9GMc",
     "Zindagi na milegi dobara":"https://www.youtube.com/watch?v=FJrpcDgC3zU",
     "Queen":"https://www.youtube.com/watch?v=KGC6vl3lzf0",
     "Kapoor and sons":"https://www.youtube.com/watch?v=s7YYt9_KfsM",
     "Dil chahta hai":"https://www.youtube.com/watch?v=OBAcYSSUf6o",
     "Jab we met":"https://www.youtube.com/watch?v=WiMIxwX4MjI",
     "English vinglish":"https://www.youtube.com/watch?v=wmGVY4T88dc",
     "Barfi":"https://www.youtube.com/watch?v=nQ3FYUgSjC8",
     "Do dooni chaar":"https://www.youtube.com/watch?v=-Sq1d64nmlU",
     "Dil dhadakne do":"https://www.youtube.com/watch?v=QrT_fioqn4o",
     "Wake up sid":"https//www.youtube.com/watch?v=Ngimy3GpHS0",
     "Kuch kuch hota hai":"https://www.youtube.com/watch?v=83rVJ-rRPns",
     "Dear zindagi":"https://www.youtube.com/watch?v=VBM6TxgeIHY",
     "I am kalam":"https://www.youtube.com/watch?v=ieOfXPzRfTk",
     "Ittefaq":"https://www.youtube.com/watch?v=mvfvoCdPrII",
     "Talvar":"https://www.youtube.com/watch?v=aQNMsw8Ljjc",
     "Drishyam":"https://www.youtube.com/watch?v=AuuX2j14NBg",
     "Badla":"https://www.youtube.com/watch?v=mSlgu8AQAd4",
     "Te3n":"https://www.youtube.com/watch?v=SeBCB5ERnps",
     "A Wednesday":"https://www.youtube.com/watch?v=oII-vaL3mZg",
     "Talaash:the answer lies within":"https://www.youtube.com/watch?v=SMkKSyd8ieo",
     "Kahaani":"https://www.youtube.com/watch?v=rsjamVgPoI8",
     "Bell bottom":"https://www.youtube.com/watch?v=A6eZ49O67YQ",
     "Johnny gaddaar":"https://www.youtube.com/watch?v=iZCxKgD5yiw",
     "The body":"https://www.youtube.com/watch?v=4f9jIdg4rTQ",
     "Wazir":"https://www.youtube.com/watch?v=gdwM7xKOph0",
     "Batla house":"https://www.youtube.com/watch?v=dG3K6jB3iW8",
     "Bob biswas":"https://www.youtube.com/watch?v=5Etb02FzW7o",
     "Satyameva jayate":"https://www.youtube.com/watch?v=odXKXLG43co",
     "Roohi":"https://www.youtube.com/watch?v=mTT_V0t89MI",
     "Bhoot part1":"https://www.youtube.com/watch?v=ELcRnZ3kP08",
     "Chhoorii":"https://www.youtube.com/watch?v=BdgFSxIcEBg",
     "Haunted 3D":"https://www.youtube.com/watch?v=1g8a96rw-Jc",
     "Stree":"https://www.youtube.com/watch?v=gzeaGcLLl_A",
     "Bulbul":"https://www.youtube.com/watch?v=4MGReT9-cAg",
     "Machhli jal ki raani hai":"https://www.youtube.com/watch?v=sVoe6VlC-UY",
     "Lupt":"https://www.youtube.com/watch?v=FxhUuHzULcM",
     "1920":"https://www.youtube.com/watch?v=gugEXnglHP4",
     "Dybbuk":"https://www.youtube.com/watch?v=nD82ZhhZF_8",
     "Ghost stories":"https://www.youtube.com/watch?v=hsab-HJ7kqc",
     "Raat":"https://www.youtube.com/watch?v=Ar5RHRCl6ks",
     "Raaz":"https://www.youtube.com/watch?v=50Kolnu7bL4",
     "Laxmi":"https://www.youtube.com/watch?v=xw0gE8QA1W0",
     "3 A.M":"https://www.youtube.com/watch?v=Gb7NdefshDI",
     "URI:The surgical strike":"https://www.youtube.com/watch?v=VVY3do673Zc",
     "Baaghi 3":"https://www.youtube.com/watch?v=jQzDujMzfoU",
     "War":"https://www.youtube.com/watch?v=tQ0mzXRk-oM",
     "Antim: the final truth":"https://www.youtube.com/watch?v=XFKz1DACGdE",
     "Radhe":"https://www.youtube.com/watch?v=n5MVzhwupBY",
     "Commando 3":"https://www.youtube.com/watch?v=m-JIofHHU6s",
     "Khuda haafiz":"https://www.youtube.com/watch?v=q67l_GOUzGc",
     "krrish":"https://www.youtube.com/watch?v=3qa3L9rTEG0",
     "Sooryavanshi":"https://www.youtube.com/watch?v=u5r77-OQwa8",
     "The power":"https://www.youtube.com/watch?v=-q1TmdddcY8",
     "Ek tha tiger":"https://www.youtube.com/watch?v=SmUl0l8qBXw",
     "Baaghi":"https://www.youtube.com/watch?v=FV-3avN3Oxc",
     "Malang":"https://www.youtube.com/watch?v=sft5baUuzQs",
     "Mumbai saga":"https://www.youtube.com/watch?v=YTGO38DSIsc",
     "Chennai central":"https://www.youtube.com/watch?v=xEIh1awGwNs",
     "Hungama 2":"https://www.youtube.com/watch?v=RC8dHEENNHQ",
     "Minnal murali":"https://www.youtube.com/watch?v=Vctn-pq6MEs",
     "Indoo ki jawani":"https://www.youtube.com/watch?v=ZwTjZIsgQhg",
     "Chhalang":"https://www.youtube.com/watch?v=BY-0SbSF2dE",
     "Ginny weds sunny":"https://www.youtube.com/watch?v=WTJW2Ol1c0g",
     "pagal panti":"https://www.youtube.com/watch?v=3-7jehmURuM",
     "badhai ho":"https://www.youtube.com/watch?v=unAljCZMQYw",
     "Coolie No 1":"https://www.youtube.com/watch?v=XaZ7jAPdecc",
     "Made in china":"https://www.youtube.com/watch?v=eA6PFnSHo-E",
     "Luka chupi":"https://www.youtube.com/watch?v=SVj26LvQMPA",
     "good newwz":"https://www.youtube.com/watch?v=r9VJpqoAr84",
     "House full 4":"https://www.youtube.com/watch?v=gcHH34cEl3Y",
     "Andhadhun":"https://www.youtube.com/watch?v=2iVYI99VGaw",
     "Total dhamaal":"https://www.youtube.com/watch?v=fo9EhcwQXcM",
     "Befikre":"https://www.youtube.com/watch?v=p7X7mwcEJ-w",
     "Yeh jawaani hai deewani":"https://www.youtube.com/watch?v=Rbp2XUSeUNE",
     "Geharaaiyan":"https://www.youtube.com/watch?v=Yy8SKJygKD4",
     "Love aaj kal":"https://www.youtube.com/watch?v=4QvqHwH_je8",
     "Ae dil hai mushkil":"https://www.youtube.com/watch?v=Z_PODraXg4E",
     "Dil se":"https://www.youtube.com/watch?v=5C-8ScWuquw",
     "Rockstar":"https://www.youtube.com/watch?v=bD5FShPZdpw",
     "Aashiqui 1":"https://www.youtube.com/watch?v=iWIPGW21Q6w",
     "Aaashiqui 2":"https://www.youtube.com/watch?v=FyXXgpPqe6w",
     "Jab tak hai jaan":"https://www.youtube.com/watch?v=v0UXgoJ9Shg",
     "Raam leela":"https://www.youtube.com/watch?v=5DYk6G8Fu8o",
     "Fanaa":"https://www.youtube.com/watch?v=kofrlCHyiaU",
     "Student of the year":"https://www.youtube.com/watch?v=fivOhPjX9YM",
     "Kabir singh":"https://www.youtube.com/watch?v=RiANSSgCuJk",
     "Raabta":"https://www.youtube.com/watch?v=YXjYfpqg8Z0",
     "Jodhaa akbar":"https://www.youtube.com/watch?v=Ce-rrik4kT4",
     "Harry potter":"https://www.youtube.com/watch?v=VyHV0BRtdxo",
     "Cindrella":"https://www.youtube.com/watch?v=T1NeHRuPpoM",
     "Spider man":"https://www.youtube.com/watch?v=TYMMOjBUPMM",
     "Charlie and the chocolate factory":"https://www.youtube.com/watch?v=OFVGCUIXJls",
     "Enchanted":"https://www.youtube.com/watch?v=IJwUFq8uOr0",
     "The parent trap":"https://www.youtube.com/watch?v=PMAhVpgzmRU",
     "Inside out":"https://www.youtube.com/watch?v=yRUAzGQ3nSY",
     "Jumanji":"https://www.youtube.com/watch?v=2QKg5SZ_35I",
     "Alice in wonderland":"https://www.youtube.com/watch?v=9POCgSRVvf0",
     "Frozen":"https://www.youtube.com/watch?v=TbQm5doF_Uc",
     "Beauty and the beast":"https://www.youtube.com/watch?v=e3Nl_TCQXuw",
     "Tangled":"https://www.youtube.com/watch?v=JYKpIr1lSG0",
     "Home alone":"https://www.youtube.com/watch?v=jEDaVHmw7r4",
     "Aladdin":"https://www.youtube.com/watch?v=foyufD52aog",
     "Mulan":"https://www.youtube.com/watch?v=KK8FHdFluOQ",
     "Gone girl":"https://www.youtube.com/watch?v=2-_-1nJf8Vg",
     "Shutter island":"https://www.youtube.com/watch?v=v8yrZSkKxTA",
     "Prisoners":"https://www.youtube.com/watch?v=bpXfcTF6iVk",
     "The invisible man":"https://www.youtube.com/watch?v=WO_FJdiY9dA",
     "Don't breathe":"https://www.youtube.com/watch?v=76yBTNDB6vU",
     "Inception":"https://www.youtube.com/watch?v=YoHD9XEInc0",
     "The woman in the window":"https://www.youtube.com/watch?v=v_0GJg_Jnlo",
     "Tenet":"https://www.youtube.com/watch?v=AZGcmvrTX9M",
     "Wrath of man":"https://www.youtube.com/watch?v=EFYEni2gsK0",
     "Parasite":"https://www.youtube.com/watch?v=isOGD_7hNIY",
     "Nightcrawler":"https://www.youtube.com/watch?v=u1uP_8VJkDQ",
     "No time to die":"https://www.youtube.com/watch?v=BIhNsAtPbPI",
     "The sixth sense":"https://www.youtube.com/watch?v=AAs-1kNRfX8",
     "Black swan":"https://www.youtube.com/watch?v=5jaI1XOB-bs",
     "A quiet place 2":"https://www.youtube.com/watch?v=BpdDN9d9Jio",
     "A quiet place":"https://www.youtube.com/watch?v=WR7cc5t7tv8",
     "The conjuring":"https://www.youtube.com/watch?v=k10ETZ41q5o",
     "The nun":"https://www.youtube.com/watch?v=pzD9zGcUNrw",
     "Hereditary":"https://www.youtube.com/watch?v=YHxcDbai7aU",
     "IT":"https://www.youtube.com/watch?v=hAUTdjf9rko",
     "Insidious":"https://www.youtube.com/watch?v=zuZnRUcoWos",
     "Possessions of Hannah grace":"https://www.youtube.com/watch?v=RHAgri92JP8",
     "The witch":"https://www.youtube.com/watch?v=iQXmlf3Sefg",
     "Blumhouse's fantasy island":"https://www.youtube.com/watch?v=FDJDujWJhzw",
     "The curse of the weeping woman":"https://www.youtube.com/watch?v=zoIuCll9vmY",
     "Sinister":"https://www.youtube.com/watch?v=_kbQAJR9YWQ",
     "Anabelle comes home":"https://www.youtube.com/watch?v=bCxm7cTpBAs",
     "The night house 2":"https://www.youtube.com/watch?v=TwIJ2WOSk_g",
     "Malignant":"https://www.youtube.com/watch?v=Gczt0fhawDs",
     "The cabin in the woods":"https://www.youtube.com/watch?v=NsIilFNNmkY",
     "Free guy":"https://www.youtube.com/watch?v=X2m-08cOAbc",
     "Ghostbusters: afterlife":"https://www.youtube.com/watch?v=ahZFCF--uRY",
     "The hangover":"https://www.youtube.com/watch?v=tcdUhdOlz9M",
     "Due date":"https://www.youtube.com/watch?v=1p3NnJ_oiE0",
     "That's my boy":"https://www.youtube.com/watch?v=zertZQpKBHk",
     "Red notice":"https://www.youtube.com/watch?v=Pj0wz7zu3Ms",
     "21 jump street":"https://www.youtube.com/watch?v=RLoKtb4c4W0",
     "Jungle cruise":"https://www.youtube.com/watch?v=f_HvoipFcA8",
     "Bad teacher":"https://www.youtube.com/watch?v=GahC5cVsU6A",
     "Ted":"https://www.youtube.com/watch?v=9fbo_pQvU7M",
     "Central intelligence":"https://www.youtube.com/watch?v=0FKctBraQj0",
     "17 again":"https://www.youtube.com/watch?v=UQK5Hh0L1Sg",
     "Men in black":"https://www.youtube.com/watch?v=1Q4mhYF9aQQ",
     "Clueless":"https://www.youtube.com/watch?v=Mgjwq1ZzdPQ",
     "Last christmas":"https://www.youtube.com/watch?v=z9CEIcmWmtA",
     "Shang chi":"https://www.youtube.com/watch?v=8YjFbMbfXaQ",
     "Venom":"https://www.youtube.com/watch?v=u9Mv98Gr5pY",
     "Mission:impossible":"https://www.youtube.com/watch?v=Ohws8y572KE",
     "The dark knight":"https://www.youtube.com/watch?v=EXeTwQWrcwY",
     "Lucy":"https://www.youtube.com/watch?v=MVt32qoyhi0",
     "The hunger games: catching fire":"https://www.youtube.com/watch?v=mfmrPu43DF8",
     "Red notice":"https://www.youtube.com/watch?v=Pj0wz7zu3Ms",
     "Mad max:fury road":"https://www.youtube.com/watch?v=hEJnMQG9ev8",
     "The matrix":"https://www.youtube.com/watch?v=vKQi3bBA1y8",
     "The suicide squad":"https://www.youtube.com/watch?v=CmRih_VtVAs",
     "Nobody":"https://www.youtube.com/watch?v=wZti8QKBWPo",
     "Eternals":"https://www.youtube.com/watch?v=0WVDKZJkGlY",
     "Watchmen":"https://www.youtube.com/watch?v=wglmbroElU0",
     "Black widow":"https://www.youtube.com/watch?v=Fp9pNPdNwjI",
     "Jack reacher":"https://www.youtube.com/watch?v=Q-oxhxD32MM",
     "The notebook":"https://www.youtube.com/watch?v=yDJIcYE32NU",
     "The fault in our stars":"https://www.youtube.com/watch?v=9ItBvH5J6ss",
     "Me before you":"https://www.youtube.com/watch?v=Eh993__rOxA",
     "Call me by your name":"https://www.youtube.com/watch?v=Z9AYPxH5NTM",
     "Twilight":"https://www.youtube.com/watch?v=uxjNDE2fMjI",
     "After":"https://www.youtube.com/watch?v=rPTf0Gw5-Bg",
     "The lucky one":"https://www.youtube.com/watch?v=9w8lE83oYeM",
     "Titanic":"https://www.youtube.com/watch?v=kVrqfYjkTdQ",
     "Pride and prejuidice":"https://www.youtube.com/watch?v=1dYv5u6v55Y",
     "The shape of water":"https://www.youtube.com/watch?v=XFYWazblaUA",
     "The curious case of Benjamin button":"https://www.youtube.com/watch?v=iH6FdW39Hag",
     "The great gatsby":"https://www.youtube.com/watch?v=rARN6agiW7o",
     "The proposal":"https://www.youtube.com/watch?v=Z2lYA7L7PZY",
     "La La Land":"https://www.youtube.com/watch?v=0pdqf4P9MB8",
     "Gone with the wind":"https://www.youtube.com/watch?v=0X94oZgJis4"}
ans='yes'
while(ans=='yes'):
     name=input("Enter the movie name:")
     for i in dict:
          if(i==name):
               print("found")
               y=dict.get(i)
               webbrowser.open(y)
               break
     else:
          print("not found")
          ans=input("Do you want to continue?(yes/no):")
print("THANK YOU!")
        





































































