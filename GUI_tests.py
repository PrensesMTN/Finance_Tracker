import tkinter
import tkinter.messagebox
import customtkinter
import tkinter as tk
from tkinter import messagebox
import csv
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

FRAME="frame"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PersioN Finance Tracker")
        self.geometry(f"{1000}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #  sidebar frame  widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PERSION", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_Ekle = customtkinter.CTkButton(self.sidebar_frame, text="INCOME", command="")
        self.sidebar_Ekle.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_Düzenle = customtkinter.CTkButton(self.sidebar_frame,text="OUT", command="")
        self.sidebar_Düzenle.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_Sil = customtkinter.CTkButton(self.sidebar_frame,text="Sil(Çoklu silme)", command="")
        self.sidebar_Sil.grid(row=4, column=0, padx=20, pady=10)        
        self.sidebar_Yenile = customtkinter.CTkButton(self.sidebar_frame,text="Yenile", command="")
        self.sidebar_Yenile.grid(row=5, column=0, padx=20, pady=10)


        # create main entry and button
#         self.entry_ara = customtkinter.CTkEntry(self, placeholder_text="Aramak istediğiniz ürünü giriniz.")
#         self.entry_ara.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         self.main_button_ara = customtkinter.CTkButton(master=self,text="ARA", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.open_input_dialog_event)
#         self.main_button_ara.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
# #
        # create treeview
        # self.vsb = customtkinter.CTkButton(master=self,text="ARA", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.open_input_dialog_event)
        # self.vsb.grid(row=1, column=1,sticky="nsew")
        
         
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


    def sidebar_button_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("sidebar_button click:", dialog.get_input())
 









if __name__ == "__main__":
    app = App()
    app.mainloop()
