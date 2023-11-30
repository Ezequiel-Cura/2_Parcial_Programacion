import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
from configuraciones import *


class Config_menu(Form):
    def __init__(self, screen, x, y, w, h, color_background,volumen, color_border="white", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)



        self.flag_play = True
        self.volumen = volumen

        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "blue", "white")

        porcentaje_volumen = f"{round(self.volumen * 100)}%"
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, porcentaje_volumen, 
                                   "Comic Sans MS", 15,"white", r"Assets\UI\Table.png")
        

        self.boton_home = Button_Image(screen=self._slave,
                                       master_x=   x,
                                       master_y=   y,
                                       x=   w- 70,
                                       y=  h- 70  ,
                                       w=  50,
                                       h=   50,
                                       path_image=r"Assets\UI\home.png",
                                       onclick=self.btn_home_click,
                                       onclick_param= ""
                                       )


        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.boton_home)
    


    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)



    def btn_home_click(self,parametro):
        self.end_dialog()

    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play.set_text("Play")
            self.btn_play._color_background = "blue" 
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "red"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play


    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        music_ambiental_menu.set_volume(self.volumen)
        