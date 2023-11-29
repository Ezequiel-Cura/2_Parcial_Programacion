import pygame

from UI.GUI_button_image import *
from UI.GUI_form import *
from manejador_niveles import Manejador_niveles
from Classes.Niveles.Nivel_2 import Nivel_2


class FormContenedorNivel(Form):
    def __init__(self, screen:pygame.Surface, nivel,name):
        super().__init__(screen, 0,0, screen.get_width(), screen.get_height())
        self.name = name
        nivel._slave = self._slave
        self.nivel = nivel
        self.pause_game_var = False

        self.puntaje_niveles = 0

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
        
        self.btn_pause_game = Button_Image(screen=self._slave,
                                       master_x= self._w ,
                                       master_y= self._h ,
                                       x=  self._w - 140,
                                       y=  0,
                                       w=  50,
                                       h=  50,
                                       path_image=r"Assets\UI\pause.png",
                                       onclick=self.pause_game,
                                       onclick_param= ""
                                       )

        # self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.btn_pause_game)


    def update(self, lista_eventos):
        if not self.pause_game_var:

            res = self.nivel.update(lista_eventos,self.name)
            # print(res)
            if res:
                if res["que_hacer"] == "Menu":
                    self.btn_home_click("hola")
                elif res["que_hacer"] == "Siguiente Nivel":

                    self._slave.fill("black")
                    print("Siguiente Nivel")
                    self.btn_home_click("")
                    self.nivel = Nivel_2(self._master)

        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        
        self.draw()

    def pause_game(self,param):
        self.pause_game_var = not self.pause_game_var

    def btn_home_click(self,parametro):
        self.end_dialog()
    