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
from configuraciones import *

class Menu_niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self.name = ""
        self.manejador_niveles = Manejador_niveles(self._master)
        self.num_nivel = 1

        

        self.label_nombre = Label(self._slave, 50,0, 100, 50, "Insert name","Comic Sans MS",15, "black",r"Assets\UI\Table.png")

        self.txtNombre = TextBox(self._slave, x, y, 50,50, 150, 30, 
                                "gray", "white","red","blue", 2, 
                                "Comic Sans MS",15, "black")
        
        self.btn_save_name = Button(self._slave, x, y,
                                    200, 50,
                                    100,50, "black","white",
                                    self.btn_save_name_click, "",
                                    "Save name","Verdana", 15, "white"
                                     )
        
        self.btn_nivel_1 = Button(self._slave, x, y, 
                                  100,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, 1,
                                "1", "Verdana", 15, "white"
                                )
        
        self.btn_nivel_2 = Button(self._slave, x, y, 
                                  300,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, 2,
                                "2", "Verdana", 15, "white"
                                )
        
        self.btn_nivel_3 = Button(self._slave, x, y, 
                                  500,200,
                                100,50,
                                "red","blue",
                                self.entrar_nivel, 3,
                                "3", "Verdana", 15, "white"
                                )

        self.lista_widgets.append(self.btn_nivel_1)
        self.lista_widgets.append(self.btn_nivel_2)
        self.lista_widgets.append(self.btn_nivel_3)
        self.lista_widgets.append(self.txtNombre)
        self.lista_widgets.append(self.btn_save_name)
        self.lista_widgets.append(self.label_nombre)



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

    def btn_save_name_click(self, parametro):
        self.name = self.txtNombre.get_text()

    def entrar_nivel(self,num_nivel):
        if self.name != "":

            self.num_nivel = num_nivel
            nivel = self.manejador_niveles.get_nivel(f"nivel_{self.num_nivel}")
            form_contenedor_nivel = FormContenedorNivel(self._master, nivel,self.name)
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
    
    def iniciar_musica_nivel(self):
        music_ambiental_menu.stop()
        if self.num_nivel == 1:
            pass
        elif self.num_nivel ==2:
            pass
        elif self.num_nivel == 3:
            level_3_music.play()
            print("lbl3")
