from tkinter import *
from tkinter import ttk
import os, sys, time, threading

class Spell_Tracker():
    def __init__(self):
        self.speel_options = ["Flash", "Ignite", "Teleport", "Exhaust", "Smite", "Ghost", "Cleanse", "Heal", "Barrier"]
        self.gui_base()

    def gui_base(self):
        self.root = Tk()
        self.root.geometry("350x225+300+850")
        self.root.title("Spell Tracker")
        self.root.config(background = "black")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.7)
        self.gui_main()

    def move_app(self, e):
        self.root.geometry(f"+{e.x_root}+{e.y_root}")

    def back(self):
        self.back_B.destroy()
        self.root.geometry("350x225+300+850")
        self.title_bar_F.destroy()

        self.f_champ_L.destroy()
        self.s_champ_L.destroy()
        self.t_champ_L.destroy()
        self.fo_champ_L.destroy()
        self.fi_champ_L.destroy()

        self.f_champ_speel_CB_img_1_B.destroy()
        self.f_champ_speel_CB_img_2_B.destroy()

        self.s_champ_speel_CB_img_1_B.destroy()
        self.s_champ_speel_CB_img_2_B.destroy()

        self.t_champ_speel_CB_img_1_B.destroy()
        self.t_champ_speel_CB_img_2_B.destroy()

        self.fo_champ_speel_CB_img_1_B.destroy()
        self.fo_champ_speel_CB_img_2_B.destroy()

        self.fi_champ_speel_CB_img_1_B.destroy()
        self.fi_champ_speel_CB_img_2_B.destroy()

        self.gui_main()

    def gui_main(self):

        # Title bar

        self.title_bar_F = Frame(self.root, background = "#F8D7FF", relief = "raised", bd = 0)
        self.title_bar_F.pack(fill = X)
        self.title_bar_F.bind("<B1-Motion>", self.move_app)

        title_bar_L = Label(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "Spell Tracker", font = "Courier 8 bold")
        title_bar_L.pack(side = "left", padx = 5, pady = 3)

        x_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "X", font = "Courier 8 bold", bd = 0, command = self.root.destroy)
        x_B.pack(side = "right", padx = 5, pady = 3)

        # Labels

        self.f_champ_L = Entry(self.root, font = "Courier 10 bold", background = "black", fg = "red", width = 12)
        self.f_champ_L.pack(), self.f_champ_L.place(x = 10, y = 35)

        self.s_champ_L = Entry(self.root, font = "Courier 10 bold", background = "black", fg = "green", width = 12)
        self.s_champ_L.pack(), self.s_champ_L.place(x = 10, y = 75)

        self.t_champ_L = Entry(self.root, font = "Courier 10 bold", background = "black", fg = "yellow", width = 12)
        self.t_champ_L.pack(), self.t_champ_L.place(x = 10, y = 115)

        self.fo_champ_L = Entry(self.root, font = "Courier 10 bold", background = "black", fg = "purple", width = 12)
        self.fo_champ_L.pack(), self.fo_champ_L.place(x = 10, y = 155)

        self.fi_champ_L = Entry(self.root, font = "Courier 10 bold", background = "black", fg = "white", width = 12)
        self.fi_champ_L.pack(), self.fi_champ_L.place(x = 10, y = 195)

        # Spells

        # First
        self.f_champ_speel_CB_1 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.f_champ_speel_CB_1.pack(), self.f_champ_speel_CB_1.place(x = 130, y = 35)

        self.f_champ_speel_CB_2 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.f_champ_speel_CB_2.pack(), self.f_champ_speel_CB_2.place(x = 210, y = 35)

        # Second
        self.s_champ_speel_CB_1 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.s_champ_speel_CB_1.pack(), self.s_champ_speel_CB_1.place(x = 130, y = 75)

        self.s_champ_speel_CB_2 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.s_champ_speel_CB_2.pack(), self.s_champ_speel_CB_2.place(x = 210, y = 75)

        # Third
        self.t_champ_speel_CB_1 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.t_champ_speel_CB_1.pack(), self.t_champ_speel_CB_1.place(x = 130, y = 115)

        self.t_champ_speel_CB_2 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.t_champ_speel_CB_2.pack(), self.t_champ_speel_CB_2.place(x = 210, y = 115)

        # Forth
        self.fo_champ_speel_CB_1 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.fo_champ_speel_CB_1.pack(), self.fo_champ_speel_CB_1.place(x = 130, y = 155)

        self.fo_champ_speel_CB_2 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.fo_champ_speel_CB_2.pack(), self.fo_champ_speel_CB_2.place(x = 210, y = 155)

        # Fifth
        self.fi_champ_speel_CB_1 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.fi_champ_speel_CB_1.pack(), self.fi_champ_speel_CB_1.place(x = 130, y = 195)

        self.fi_champ_speel_CB_2 = ttk.Combobox(self.root, value = self.speel_options, width = 9, background = "black")
        self.fi_champ_speel_CB_2.pack(), self.fi_champ_speel_CB_2.place(x = 210, y = 195)

        # Button

        self.save_B = Button(self.root, font = "Courier 10 bold", background = "black", fg = "green", text = "Save", width = 5, command = self.save_c)
        self.save_B.pack(), self.save_B.place(x = 293, y = 112)

        self.root.mainloop()

    def save_c(self):
        self.f_get = self.f_champ_L.get()
        self.s_get = self.s_champ_L.get()
        self.t_get = self.t_champ_L.get()
        self.fo_get = self.fo_champ_L.get()
        self.fi_get = self.fi_champ_L.get()


        self.f_get_cb_1 = self.f_champ_speel_CB_1.get()
        self.f_get_cb_2 = self.f_champ_speel_CB_2.get()

        self.s_get_cb_1 = self.s_champ_speel_CB_1.get()
        self.s_get_cb_2 = self.s_champ_speel_CB_2.get()

        self.t_get_cb_1 = self.t_champ_speel_CB_1.get()
        self.t_get_cb_2 = self.t_champ_speel_CB_2.get()

        self.fo_get_cb_1 = self.fo_champ_speel_CB_1.get()
        self.fo_get_cb_2 = self.fo_champ_speel_CB_2.get()

        self.fi_get_cb_1 = self.fi_champ_speel_CB_1.get()
        self.fi_get_cb_2 = self.fi_champ_speel_CB_2.get()

        self.f_champ_L.destroy()
        self.s_champ_L.destroy()
        self.t_champ_L.destroy()
        self.fo_champ_L.destroy()
        self.fi_champ_L.destroy()

        self.f_champ_speel_CB_1.destroy()
        self.f_champ_speel_CB_2.destroy()
        self.s_champ_speel_CB_1.destroy()
        self.s_champ_speel_CB_2.destroy()
        self.t_champ_speel_CB_1.destroy()
        self.t_champ_speel_CB_2.destroy()
        self.fo_champ_speel_CB_1.destroy()
        self.fo_champ_speel_CB_2.destroy()
        self.fi_champ_speel_CB_1.destroy()
        self.fi_champ_speel_CB_2.destroy()

        self.save_B.destroy()
        self.create_interface()

    def create_interface(self):
        self.root.geometry("250x235+300+840")

        self.back_B = Button(self.title_bar_F, background = "#F8D7FF", foreground = "black", text = "<-", font = "Courier 8 bold", bd = 0, command = self.back)
        self.back_B.pack(side = "right", pady = 3)

        self.f_champ_L = Label(self.root, font = "Courier 12 bold", text = self.f_get, background = "black", width = 10, anchor = "w", fg = "red")
        self.f_champ_L.pack(), self.f_champ_L.place(x = 5, y = 38)
        
        self.s_champ_L = Label(self.root, font = "Courier 12 bold", text = self.s_get, background = "black", width = 10, anchor = "w", fg = "green")
        self.s_champ_L.pack(), self.s_champ_L.place(x = 5, y = 78)

        self.t_champ_L = Label(self.root, font = "Courier 12 bold", text = self.t_get, background = "black", width = 10, anchor = "w", fg = "yellow")
        self.t_champ_L.pack(), self.t_champ_L.place(x = 5, y = 118)

        self.fo_champ_L = Label(self.root, font = "Courier 12 bold", text = self.fo_get, background = "black", width = 10, anchor = "w", fg = "purple")
        self.fo_champ_L.pack(), self.fo_champ_L.place(x = 5, y = 158)

        self.fi_champ_L = Label(self.root, font = "Courier 12 bold", text = self.fi_get, background = "black", width = 10, anchor = "w", fg = "white")
        self.fi_champ_L.pack(), self.fi_champ_L.place(x = 5, y = 198)

        if getattr(sys, "frozen", False):
            path = os.path.dirname(sys.executable)
        elif __file__:
            path = os.path.dirname(__file__)

        # Spell images
        spell_path = path + "/Spells/"

        f_get_cb_1_im = PhotoImage(file = spell_path + self.f_get_cb_1 + ".png")
        f_get_cb_2_im = PhotoImage(file = spell_path + self.f_get_cb_2 + ".png")

        s_get_cb_1_im = PhotoImage(file = spell_path + self.s_get_cb_1 + ".png")
        s_get_cb_2_im = PhotoImage(file = spell_path + self.s_get_cb_2 + ".png")

        t_get_cb_1_im = PhotoImage(file = spell_path + self.t_get_cb_1 + ".png")
        t_get_cb_2_im = PhotoImage(file = spell_path + self.t_get_cb_2 + ".png")

        fo_get_cb_1_im = PhotoImage(file = spell_path + self.fo_get_cb_1 + ".png")
        fo_get_cb_2_im = PhotoImage(file = spell_path + self.fo_get_cb_2 + ".png")

        fi_get_cb_1_im = PhotoImage(file = spell_path + self.fi_get_cb_1 + ".png")
        fi_get_cb_2_im = PhotoImage(file = spell_path + self.fi_get_cb_2 + ".png")


        self.f_champ_speel_CB_img_1_B = Button(self.root, bg = "black", fg = "green", image = f_get_cb_1_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.f_get_cb_1, 270, 10))
        self.f_champ_speel_CB_img_1_B.pack(), self.f_champ_speel_CB_img_1_B.place(x = 170, y = 35)

        self.f_champ_speel_CB_img_2_B = Button(self.root, bg = "black", fg = "green", image = f_get_cb_2_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.f_get_cb_2, 310, 10))
        self.f_champ_speel_CB_img_2_B.pack(), self.f_champ_speel_CB_img_2_B.place(x = 210, y = 35)


        self.s_champ_speel_CB_img_1_B = Button(self.root, bg = "black", fg = "green", image = s_get_cb_1_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.s_get_cb_1, 270, 50))
        self.s_champ_speel_CB_img_1_B.pack(), self.s_champ_speel_CB_img_1_B.place(x = 170, y = 75)

        self.s_champ_speel_CB_img_2_B = Button(self.root, bg = "black", fg = "green", image = s_get_cb_2_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.s_get_cb_2, 310, 50))
        self.s_champ_speel_CB_img_2_B.pack(), self.s_champ_speel_CB_img_2_B.place(x = 210, y = 75)


        self.t_champ_speel_CB_img_1_B = Button(self.root, bg = "black", fg = "green", image = t_get_cb_1_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.t_get_cb_1, 270, 90))
        self.t_champ_speel_CB_img_1_B.pack(), self.t_champ_speel_CB_img_1_B.place(x = 170, y = 115)

        self.t_champ_speel_CB_img_2_B = Button(self.root, bg = "black", fg = "green", image = t_get_cb_2_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.t_get_cb_2, 310, 90))
        self.t_champ_speel_CB_img_2_B.pack(), self.t_champ_speel_CB_img_2_B.place(x = 210, y = 115)


        self.fo_champ_speel_CB_img_1_B = Button(self.root, bg = "black", fg = "green", image = fo_get_cb_1_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.fo_get_cb_1, 270, 130))
        self.fo_champ_speel_CB_img_1_B.pack(), self.fo_champ_speel_CB_img_1_B.place(x = 170, y = 155)

        self.fo_champ_speel_CB_img_2_B = Button(self.root, bg = "black", fg = "green", image = fo_get_cb_2_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.fo_get_cb_2, 310, 130))
        self.fo_champ_speel_CB_img_2_B.pack(), self.fo_champ_speel_CB_img_2_B.place(x = 210, y = 155)


        self.fi_champ_speel_CB_img_1_B = Button(self.root, bg = "black", fg = "green", image = fi_get_cb_1_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.fi_get_cb_1, 270, 170))
        self.fi_champ_speel_CB_img_1_B.pack(), self.fi_champ_speel_CB_img_1_B.place(x = 170, y = 195)

        self.fi_champ_speel_CB_img_2_B = Button(self.root, bg = "black", fg = "green", image = fi_get_cb_2_im, font = "Courier 8", border = False, command = lambda: self.spell_command(self.fi_get_cb_2, 310, 170))
        self.fi_champ_speel_CB_img_2_B.pack(), self.fi_champ_speel_CB_img_2_B.place(x = 210, y = 195)

        self.root.mainloop()

    def spell_command(self, spell, x, y):
        spell_cd = {"Ignite" : 180,
                    "Cleanse" : 210,
                    "Flash" : 300,
                    "Teleport" : 360,
                    "Exhaust" : 210,
                    "Barrier" : 180,
                    "Heal" : 240,
                    "Ghost" : 210}
        
        if spell != "Smite":
            self.time_label = Label(self.root, text = spell_cd[spell], background = "black", foreground = "red", font = "Courier 10 bold", width = 3)
            self.time_label.pack(), self.time_label.place(x = x - 100, y = y + 30)
            threading.Thread(target = self.spell_timer_command, args = (self.time_label, spell_cd[spell])).start()

    def spell_timer_command(self, label, timee):
        while timee > 0:
            label.config(text = timee)
            time.sleep(1)
            timee -= 1
        label.destroy()

run = Spell_Tracker()
