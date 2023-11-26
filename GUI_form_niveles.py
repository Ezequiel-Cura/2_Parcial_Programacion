import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from manejador_niveles import Manejador_niveles

from GUI_form_contenedor_nivel import FormContenedorNivel

class Menu_niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.manejador_niveles = Manejador_niveles(self._master)

        self.btn_nivel_1 = Button(self._slave, x, y, 
                                  100,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, "nivel_uno",
                                "1", "Verdana", 15, "white"
                                )
        
        self.btn_nivel_2 = Button(self._slave, x, y, 
                                  300,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, "nivel_dos",
                                "2", "Verdana", 15, "white"
                                )
        
        self.btn_nivel_3 = Button(self._slave, x, y, 
                                  500,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, "nivel_tres",
                                "3", "Verdana", 15, "white"
                                )

        self.lista_widgets.append(self.btn_nivel_1)
        self.lista_widgets.append(self.btn_nivel_2)
        self.lista_widgets.append(self.btn_nivel_3)
        #Crear boton home
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

        self.lista_widgets.append(self.boton_home)

    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

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

    def btn_home_click(self,parametro):
        self.end_dialog()
    