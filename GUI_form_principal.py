import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_config import Config_menu
from GUI_form_niveles import Menu_niveles


    
class FormPrincipal(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border = "black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        self.flag_play = True
        self.volumen = 0.2

        pygame.mixer.init()
        pygame.mixer.music.load(r"Assets\Music\Ambient 1.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        
        ##COMPLETAR


        self.btn_jugar = Button(self._slave, x, y, 400,200,
                                100,50,
                                "red","blue",
                                self.btn_jugar_click, "param",
                                "Jugar", "Verdana", 15, "white"
                                )
        
        self.btn_leader_board = Button(self._slave, x, y, 400, 300,
                                       100,50,
                                       "red","blue",
                                       self.btn_tabla_click, "param",
                                       "Leaderboard", "Verdana", 15, "white"
                                       )

        self.btn_config_sonidos = Button(self._slave, x, y,800, 400,
                                         100,50,
                                         "red","blue",
                                         self.btn_config_click, "param",
                                         "Config", "Verdana", 15, "white"
                                         )

        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_leader_board)
        self.lista_widgets.append(self.btn_config_sonidos)

        

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)


    def btn_jugar_click(self,param):
        menu_niveles = Menu_niveles(screen=self._master,
                                    x = 500,
                                    y = 100,
                                    w = 1000,
                                    h = 550,
                                    color_background= "gray",
                                    color_border= "white",
                                    active= True,
                                    )
        self.show_dialog(menu_niveles)

    def btn_config_click(self, param): 
        config_menu = Config_menu(screen=self._master,
                                    x = 500,
                                    y = 100,
                                    w = 1000,
                                    h = 550,
                                    volumen=self.volumen,
                                    color_background= "gray",
                                    color_border= "white",
                                    active= True,
                                   )

        self.show_dialog(config_menu)

    
    def btn_tabla_click(self, param):
        diccionario = [{"Jugador": "Mario", "Score": 100},
                      {"Jugador": "Mario", "Score": 100},
                      {"Jugador": "Mario", "Score": 100},
                      ]
        leaderboard_menu = FormMenuScore(screen=self._master,
                                    x = 500,
                                    y = 100,
                                    w = 1000,
                                    h = 550,
                                    color_background= "green",
                                    color_border= "gold",
                                    active= True,
                                    path_image= r"Assets\UI\Window.png",
                                    scoreboard= diccionario,
                                    margen_x= 10,
                                    margen_y = 100,
                                    espacio = 10
                                   )

        self.show_dialog(leaderboard_menu)


        # self.txtNombre = TextBox(self._slave, x, y, 50,50, 150, 30, 
        #                         "gray", "white","red","blue", 2, 
        #                         "Comic Sans MS",15, "black")
        # self.btn_tabla = Button_Image(self._slave, x,y ,225, 100, 50, 50, r"Assets\UI\Menu_BTN.png",
        #                               self.btn_tabla_click,"hoal")

        # self.lista_widgets.append(self.txtNombre)
        # self.lista_widgets.append(self.btn_tabla)
