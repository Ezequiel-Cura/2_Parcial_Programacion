import pygame

from UI.GUI_button_image import *
from UI.GUI_form import *

class FormContenedorNivel(Form):
    def __init__(self, screen:pygame.Surface, nivel):
        super().__init__(screen, 0,0, screen.get_width(), screen.get_height())
        nivel._slave = self._slave
        self.nivel = nivel


        #Crear boton home
        self.boton_home = Button_Image(screen=self._slave,
                                       master_x= self._w ,
                                       master_y= self._h ,
                                       x=  self._w - 70,
                                       y=  0,
                                       w=  50,
                                       h=  50,
                                       path_image=r"Assets\UI\home.png",
                                       onclick=self.btn_home_click,
                                       onclick_param= ""
                                       )

        # self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.boton_home)


    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()


    def btn_home_click(self,parametro):
        self.end_dialog()
    