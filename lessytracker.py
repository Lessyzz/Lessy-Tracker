import requests, threading, time, os
from riotwatcher import LolWatcher
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import ttk, messagebox
#from bs4 import BeautifulSoup

class LessyTracker():
    def __init__(self):
        # url = f"https://lessy.pythonanywhere.com/apikey"
        # response = requests.get(url)

        # self.api_key = BeautifulSoup(response.text, 'html.parser').get_text()
        self.api_key = "RGAPI-e21c2591-8fed-4824-b691-4aa49e0915de"
        self.watcher = LolWatcher(self.api_key)
        self.pid = os.getpid()

        self.champion_ids = []
        self.player_names = []
        self.champion_names = []
        self.spell1_names = []
        self.spell2_names = []

        self.ally_team_player_names = []
        self.ally_team_champion_names = []
        self.ally_team_spells_1 = []
        self.ally_team_spells_2 = []
        self.ally_champion_ids = []

        self.enemy_team_player_names = []
        self.enemy_team_champion_names = []
        self.enemy_team_spells_1 = []
        self.enemy_team_spells_2 = []
        self.enemy_champion_ids = []

        self.spell_cooldown = {
            "Ignite" : 180,
            "Cleanse" : 210,
            "Flash" : 300,
            "Teleport" : 360,
            "Exhaust" : 210,
            "Barrier" : 180,
            "Heal" : 240,
            "Ghost" : 210}

        self.region_list = ["TR1", "EUW1", "NA1", "EUN1", "RU1"]

        self.champion_id_list = {
    266: "Aatrox", 103: "Ahri", 84: "Akali", 166: "Akshan", 12: "Alistar", 32: "Amumu", 34: "Anivia", 1: "Annie",
    523: "Aphelios", 22: "Ashe", 136: "Aurelion Sol", 268: "Azir", 432: "Bard", 200: "Bel'Veth", 53: "Blitzcrank",
    63: "Brand", 201: "Braum", 51: "Caitlyn", 164: "Camille", 69: "Cassiopeia", 31: "Cho'Gath", 42: "Corki",
    122: "Darius", 131: "Diana", 119: "Draven", 36: "Dr. Mundo", 245: "Ekko", 60: "Elise", 28: "Evelynn",
    81: "Ezreal", 9: "Fiddlesticks", 114: "Fiora", 105: "Fizz", 3: "Galio", 41: "Gangplank", 86: "Garen",
    150: "Gnar", 79: "Gragas", 104: "Graves", 887: "Gwen", 120: "Hecarim", 74: "Heimerdinger", 420: "Illaoi",
    39: "Irelia", 427: "Ivern", 40: "Janna", 59: "Jarvan IV", 24: "Jax", 126: "Jayce", 202: "Jhin", 222: "Jinx",
    145: "Kai'Sa", 429: "Kalista", 43: "Karma", 30: "Karthus", 38: "Kassadin", 55: "Katarina", 10: "Kayle",
    141: "Kayn", 85: "Kennen", 121: "Kha'Zix", 203: "Kindred", 240: "Kled", 96: "Kog'Maw", 897: "K'Sante",
    7: "LeBlanc", 64: "Lee Sin", 89: "Leona", 876: "Lillia", 127: "Lissandra", 236: "Lucian", 117: "Lulu",
    99: "Lux", 54: "Malphite", 90: "Malzahar", 57: "Maokai", 11: "Master Yi", 902: "Milio", 21: "Miss Fortune",
    62: "Wukong", 82: "Mordekaiser", 25: "Morgana", 267: "Nami", 75: "Nasus", 111: "Nautilus", 518: "Neeko",
    76: "Nidalee", 895: "Nilah", 56: "Nocturne", 20: "Nunu & Willump", 2: "Olaf", 61: "Orianna", 516: "Ornn",
    80: "Pantheon", 78: "Poppy", 555: "Pyke", 246: "Qiyana", 133: "Quinn", 497: "Rakan", 33: "Rammus",
    421: "Rek'Sai", 526: "Rell", 888: "Renata Glasc", 58: "Renekton", 107: "Rengar", 92: "Riven", 68: "Rumble",
    13: "Ryze", 360: "Samira", 113: "Sejuani", 235: "Senna", 147: "Seraphine", 875: "Sett", 35: "Shaco",
    98: "Shen", 102: "Shyvana", 27: "Singed", 14: "Sion", 15: "Sivir", 72: "Skarner", 37: "Sona", 16: "Soraka",
    50: "Swain", 517: "Sylas", 134: "Syndra", 223: "Tahm Kench", 163: "Taliyah", 91: "Talon", 44: "Taric",
    17: "Teemo", 412: "Thresh", 18: "Tristana", 48: "Trundle", 23: "Tryndamere", 4: "Twisted Fate", 29: "Twitch",
    77: "Udyr", 6: "Urgot", 110: "Varus", 67: "Vayne", 45: "Veigar", 161: "Vel'Koz", 711: "Vex", 254: "Vi",
    234: "Viego", 112: "Viktor", 8: "Vladimir", 106: "Volibear", 19: "Warwick", 498: "Xayah", 101: "Xerath",
    5: "Xin Zhao", 157: "Yasuo", 777: "Yone", 83: "Yorick", 350: "Yuumi", 154: "Zac", 238: "Zed", 221: "Zeri",
    115: "Ziggs", 26: "Zilean", 142: "Zoe", 143: "Zyra"}

        self.spell_id_list = {21: "Barrier", 1: "Cleanse", 14: "Ignite", 3: "Exhaust", 4: "Flash", 
                              6: "Ghost", 7: "Heal", 11: "Smite", 12: "Teleport"}

        self.spell_name_links = {
            "Heal" : "https://static.wikia.nocookie.net/leagueoflegends/images/6/6e/Heal.png/revision/latest?cb=20180514003319",
            "Ghost" : "https://static.wikia.nocookie.net/leagueoflegends/images/a/ab/Ghost.png/revision/latest?cb=20180514003209",
            "Barrier" : "https://static.wikia.nocookie.net/leagueoflegends/images/c/cc/Barrier.png/revision/latest?cb=20180514002510",
            "Exhaust" : "https://static.wikia.nocookie.net/leagueoflegends/images/4/4a/Exhaust.png/revision/latest?cb=20180514003128",
            "Ignite" : "https://static.wikia.nocookie.net/leagueoflegends/images/f/f4/Ignite.png/revision/latest?cb=20180514003345",
            "Flash" : "https://static.wikia.nocookie.net/leagueoflegends/images/7/74/Flash.png/revision/latest?cb=20180514003149",
            "Smite" : "https://static.wikia.nocookie.net/leagueoflegends/images/0/05/Smite.png/revision/latest?cb=20180514003641",
            "Teleport" : "https://yt3.googleusercontent.com/Yy-AL-HAlzgPu82LhIsnOJhI23m8emJfMm4yBFYilDWfEQgM7rC_17UVx3xQPeNzrAV_Y-yz=s900-c-k-c0x00ffffff-no-rj",
            "Cleanse" : "https://yt3.googleusercontent.com/yChbG__l6RhGYE4F-O57aZS-wP-Lv6oDrQJMN9vXDppJGB5AqAb8By7LvJfRTQaq22Ot77QChw=s900-c-k-c0x00ffffff-no-rj"}

        self.first_gui()

    def move_app_root(self, e):
        self.root.geometry(f"+{e.x_root}+{e.y_root}")

    def move_app_first_interface(self, e):
        self.first_interface.geometry(f"+{e.x_root}+{e.y_root}")

    def back_C(self):
        self.root.destroy()

        self.champion_ids = []
        self.player_names = []
        self.champion_names = []
        self.spell1_names = []
        self.spell2_names = []

        self.ally_team_player_names = []
        self.ally_team_champion_names = []
        self.ally_team_spells_1 = []
        self.ally_team_spells_2 = []
        self.ally_champion_ids = []

        self.enemy_team_player_names = []
        self.enemy_team_champion_names = []
        self.enemy_team_spells_1 = []
        self.enemy_team_spells_2 = []
        self.enemy_champion_ids = []

        self.first_gui()

    def submit_C(self):
        self.nickname = self.nickname_E.get()
        self.region = self.region_CB.get()
        self.live_game_data()

    def spell_timer_command_1(self, spell, x, y):
        if spell != "Smite":
            self.time_label = Label(self.root, text = self.spell_cooldown[spell], background = "black", foreground = "red", font = "Courier 10 bold", width = 3)
            self.time_label.pack(), self.time_label.place(x = x, y = y)
            threading.Thread(target = self.spell_timer_command_2, args = (self.time_label, self.spell_cooldown[spell])).start()

    def spell_timer_command_2(self, label, timee):
        def asss(self):
            nonlocal timee
            timee -= 5
        while timee > 0:
            label.bind("<Button-1>", asss)
            label.config(text = timee)
            timee -= 1
            time.sleep(1)
        
        label.destroy()

    def get_character_image(self, label, character_id):
        link = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/{character_id}.png"
        response = requests.get(link)
        image = Image.open(BytesIO(response.content))
        image = image.resize((28, 28))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo

    def get_spell_image_from_link(self, label, spell):
        link = self.spell_name_links.get(spell)
        response = requests.get(link)
        image = Image.open(BytesIO(response.content))
        image = image.resize((26, 26))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo

    def first_gui(self):
        self.first_interface = Tk()
        self.first_interface.geometry(f"300x150+{int(self.first_interface.winfo_screenwidth() / 2)}+{int(self.first_interface.winfo_screenheight() / 2)}")
        self.first_interface.title("Lessy Tracker")
        self.first_interface.config(background = "black")
        self.first_interface.overrideredirect(True)
        self.first_interface.attributes('-topmost', True)
        self.first_gui_main()

    def first_gui_main(self):

        # Title bar

        self.title_bar_F = Frame(self.first_interface, background = "#F8D7FF", relief = "raised", bd = 0)
        self.title_bar_F.pack(fill = X)
        self.title_bar_F.bind("<B1-Motion>", self.move_app_first_interface)

        title_bar_L = Label(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "Lessy Tracker", font = "Courier 8 bold")
        title_bar_L.pack(side = "left", padx = 2, pady = 3)

        x_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "X", font = "Courier 8 bold", bd = 0, command = self.first_interface.destroy)
        x_B.pack(side = "right", padx = 5, pady = 3)

        # Labels

        nickname_L = Label(self.first_interface, background = "black", foreground = "green", text = "Nickname:", font = "Courier 10 bold")
        nickname_L.pack(), nickname_L.place(x = 20, y = 40)

        region_L = Label(self.first_interface, background = "black", foreground = "green", text = "Region:", font = "Courier 10 bold")
        region_L.pack(), region_L.place(x = 20, y = 80)

        self.nickname_E = Entry(self.first_interface, background = "black", foreground = "green", font = "Courier 10 bold", width = 17)
        self.nickname_E.pack(), self.nickname_E.place(x = 125, y = 40), self.nickname_E.focus()

        self.region_CB = ttk.Combobox(self.first_interface, value = self.region_list, width = 9, background = "black")
        self.region_CB.pack(), self.region_CB.place(x = 125, y = 80)

        submit_B = Button(self.first_interface, background = "black", foreground = "green", text = "Submit", width = 9, font = "Courier 10", command = self.submit_C)
        submit_B.pack(), submit_B.place(x = 125, y = 117)

        self.first_interface.mainloop()

    def live_game_data(self):
        try:
            player = self.watcher.summoner.by_name(self.region, self.nickname)
            id = player.get("id")

            url = f"https://{self.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{id}?api_key={self.api_key}"
            response = requests.get(url)

            if response.status_code == 200:
                self.first_interface.destroy()
                match_data = response.json()
            
            match_data_participants = match_data.get("participants")
        except:
            messagebox.showerror(title = "Lessy Tracker", message = 'Canlı maç verisine ulaşılamadı!')
        
        #print(match_data_participants)

        # Get player names
        for i in range(10):
            self.player_names.append(match_data_participants[i].get("summonerName"))


        # Get champion id's
        for i in range(10):
            self.champion_ids.append(match_data_participants[i].get("championId"))
        

        # Get champion names
        for i in range(10):
            self.champion_names.append(self.champion_id_list.get(match_data_participants[i].get("championId")))


        # Get spell ids_1
        for i in range(10):
            self.spell1_names.append(self.spell_id_list.get(match_data_participants[i].get("spell1Id")))
        

        # Get spell ids_2
        for i in range(10):
            self.spell2_names.append(self.spell_id_list.get(match_data_participants[i].get("spell2Id")))

        
        # Get player names, champion names and spells of teams
        if self.player_names.index(self.nickname) > 4:

            # Player names
            for i in self.player_names[5:10]:
                self.ally_team_player_names.append(i)

            for i in self.player_names[0:5]:
                self.enemy_team_player_names.append(i)


            # Champion names
            for i in self.champion_names[5:10]:
                self.ally_team_champion_names.append(i)

            for i in self.champion_names[0:5]:
                self.enemy_team_champion_names.append(i)


            # Champion id's
            for i in self.champion_ids[5:10]:
                self.ally_champion_ids.append(i)

            for i in self.champion_ids[0:5]:
                self.enemy_champion_ids.append(i)


            # Spell1 names
            for i in self.spell1_names[5:10]:
                self.ally_team_spells_1.append(i)
            
            for i in self.spell1_names[0:5]:
                self.enemy_team_spells_1.append(i)


            # Spell2 names
            for i in self.spell2_names[5:10]:
                self.ally_team_spells_2.append(i)

            for i in self.spell2_names[0:5]:
                self.enemy_team_spells_2.append(i)

        else:

            # Player names
            for i in self.player_names[0:5]:
                self.ally_team_player_names.append(i)

            for i in self.player_names[5:10]:
                self.enemy_team_player_names.append(i)        


            # Champion names
            for i in self.champion_names[0:5]:
                self.ally_team_champion_names.append(i)
                
            for i in self.champion_names[5:10]:
                self.enemy_team_champion_names.append(i)

            
            # Champion id's
            for i in self.champion_ids[0:5]:
                self.ally_champion_ids.append(i)

            for i in self.champion_ids[5:10]:
                self.enemy_champion_ids.append(i)
            

            # Spell1 names
            for i in self.spell1_names[0:5]:
                self.ally_team_spells_1.append(i)

            for i in self.spell1_names[5:10]:
                self.enemy_team_spells_1.append(i) 

            # Spell2 names
            for i in self.spell2_names[0:5]:
                self.ally_team_spells_2.append(i)
            
            for i in self.spell2_names[5:10]:
                self.enemy_team_spells_2.append(i)
        

        # print(self.player_names)
        # print(self.ally_team_player_names)
        # print(self.enemy_team_player_names)

        # print(self.champion_names)
        # print(self.ally_team_champion_names)
        # print(self.enemy_team_champion_names)

        # print(self.spell1_names)
        # print(self.ally_team_spells_1)
        # print(self.enemy_team_spells_1)

        # print(self.spell2_names)
        # print(self.ally_team_spells_2)
        # print(self.enemy_team_spells_2)
        
        # print(self.champion_ids)
        # print(self.ally_champion_ids)
        # print(self.enemy_champion_ids)

        self.gui_base()

    def gui_base(self):
        self.root = Tk()
        x_pos = int(self.root.winfo_screenwidth() / 6.4)
        y_pos = int(self.root.winfo_screenheight() / 1.270)
        self.root.geometry(f"125x225+{x_pos}+{y_pos + 2}")
        self.root.title("Lessy Tracker")
        self.root.config(background = "black")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.7)
        self.create_title_bar()

    def create_title_bar(self):
        self.title_bar_F = Frame(self.root, background = "#F8D7FF", relief = "raised", bd = 0)
        self.title_bar_F.pack(fill = X)
        self.title_bar_F.bind("<B1-Motion>", self.move_app_root)

        title_bar_L = Label(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "Lessy Tracker", font = "Courier 8 bold")
        title_bar_L.pack(side = "left", padx = 1, pady = 3)

        # x_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "X", font = "Courier 8 bold", bd = 0, command = lambda: os.system(f"taskkill /F /PID {self.pid}"))
        # x_B.pack(side = "right", padx = 2, pady = 3)

        # back_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "<-", font = "Courier 8 bold", bd = 0, command = self.back_C)
        # back_B.pack(side = "right", pady = 3)

        back_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "<-", font = "Courier 8 bold", bd = 0, command = self.back_C)
        back_B.pack(side = "right", padx = 2, pady = 3)
        self.gui_main()

    def gui_main(self):

        # Champion images
        y = 30
        for i in range(5):
            label = Label(self.root, background = "#F8D7FF")
            label.pack(), label.place(x = 5, y = y)
            threading.Thread(target = lambda: self.get_character_image(label , self.enemy_champion_ids[i])).start()
            y += 40

        # Spells

        self.f_champ_spell_1_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_1[0], 55, 35))
        self.f_champ_spell_1_L.pack(), self.f_champ_spell_1_L.place(x = 55, y = 30)

        self.f_champ_spell_2_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_2[0], 90, 35))
        self.f_champ_spell_2_L.pack(), self.f_champ_spell_2_L.place(x = 90, y = 30)


        self.s_champ_spell_1_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_1[1], 55, 75))
        self.s_champ_spell_1_L.pack(), self.s_champ_spell_1_L.place(x = 55, y = 70)

        self.s_champ_spell_2_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_2[1], 90, 75))
        self.s_champ_spell_2_L.pack(), self.s_champ_spell_2_L.place(x = 90, y = 70)


        self.t_champ_spell_1_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_1[2], 55, 115))
        self.t_champ_spell_1_L.pack(), self.t_champ_spell_1_L.place(x = 55, y = 110)

        self.t_champ_spell_2_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_2[2], 90, 115))
        self.t_champ_spell_2_L.pack(), self.t_champ_spell_2_L.place(x = 90, y = 110)


        self.fo_champ_spell_1_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_1[3], 55, 155))
        self.fo_champ_spell_1_L.pack(), self.fo_champ_spell_1_L.place(x = 55, y = 150)

        self.fo_champ_spell_2_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_2[3], 90, 155))
        self.fo_champ_spell_2_L.pack(), self.fo_champ_spell_2_L.place(x = 90, y = 150)


        self.fi_champ_spell_1_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_1[4], 55, 195))
        self.fi_champ_spell_1_L.pack(), self.fi_champ_spell_1_L.place(x = 55, y = 190)

        self.fi_champ_spell_2_L = Button(self.root, background = "#F8D7FF", command = lambda: self.spell_timer_command_1(self.enemy_team_spells_2[4], 90, 195))
        self.fi_champ_spell_2_L.pack(), self.fi_champ_spell_2_L.place(x = 90, y = 190)

        threading.Thread(target = lambda: self.get_spell_image_from_link(self.f_champ_spell_1_L, self.enemy_team_spells_1[0])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.s_champ_spell_1_L, self.enemy_team_spells_1[1])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.t_champ_spell_1_L, self.enemy_team_spells_1[2])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.fo_champ_spell_1_L, self.enemy_team_spells_1[3])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.fi_champ_spell_1_L, self.enemy_team_spells_1[4])).start()

        threading.Thread(target = lambda: self.get_spell_image_from_link(self.f_champ_spell_2_L, self.enemy_team_spells_2[0])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.s_champ_spell_2_L, self.enemy_team_spells_2[1])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.t_champ_spell_2_L, self.enemy_team_spells_2[2])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.fo_champ_spell_2_L, self.enemy_team_spells_2[3])).start()
        threading.Thread(target = lambda: self.get_spell_image_from_link(self.fi_champ_spell_2_L, self.enemy_team_spells_2[4])).start()

        self.root.mainloop()

run = LessyTracker()
