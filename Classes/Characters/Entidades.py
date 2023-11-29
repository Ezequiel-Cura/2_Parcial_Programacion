import pygame


class Entidades_Juego:
    def __init__(self,tamaño, posicion, dicc_animaciones):
        
        self.limit_count = 5
        self.que_hace = "idle"
        self.count = 0
        self.pasos_animacion = 0
        self.animaciones:dict | list = dicc_animaciones
        
        self.list_animaciones:list = Entidades_Juego.reescalalar_imagenesa(self.animaciones, tamaño[0], tamaño[1])

        if type(self.animaciones) == list:
            self.animacion_actual = self.list_animaciones
        else:
            self.animacion_actual:list[pygame.Surface] = self.list_animaciones["run"]

        self.rect:pygame.Rect = self.animacion_actual[0].get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.rectangulos: dict[str, pygame.Rect] = Entidades_Juego.obtener_rectangulos(self.rect, self.rect.width, self.rect.height)
        
        self.attack_delay = True
        self.jump_delay = True
        self.shoot_delay = True

    
    def draw(self, pantalla):
        pantalla.blit(self.plataforma["superficie"], self.plataforma["rectangulo"])

    def mover(self, pantalla):
        nueva_velocidad = self.velocidad
        # if self.que_hace == 2:
        if self.mirando_izq:
            nueva_velocidad *= -1
        new_x = self.rectangulos["principal"].x + nueva_velocidad 
        if new_x >= 0 and new_x <= pantalla.get_width() - self.rectangulos["principal"].width:
            for lado in self.rectangulos:
                self.rectangulos[lado].x += nueva_velocidad


    # def update(self, PANTALLA,plataformas, lista_enemigos):
    #     # 0 = Idle_der, 1 = Run_der, 2 = Jump_der, 3 = attack_der
    #     #   = Idle_izq,-1 = Run_izq, -2 = Jump_izq, -3 attack_izq

    #     if self.que_hace == "run":
   
    #         self.mover(PANTALLA)

    #     if self.que_hace == 3:
    #         self.attack(PANTALLA, lista_enemigos)
        
    #     if self.que_hace == 2:

    #         if not self.esta_aire:
    #             self.press_tecla_w = False
    #             self.saltar(plataformas)

    #     self.aplicar_gravedad()
    #     self.verificar_colision_piso(plataformas)
    #     self.verificar_colision_pared(plataformas)
  


    def animar_movimiento(self, pantalla):
        # self.animacion_actual = self.list_animaciones[self.que_hace]
        self.count += 1
        print(self.que_hace,"---------")
        if self.count > self.limit_count:
            self.pasos_animacion += 1
            self.count = 0

        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

        if self.mirando_izq == True:
            # nueva_lista = Entidades_Juego.rotar_imagen(self.animacion_actual[int(self.pasos_animacion)])
            pantalla.blit( pygame.transform.flip(self.animacion_actual[int(self.pasos_animacion)],True,False), (self.rectangulos["principal"].x , self.rectangulos["principal"].y ))
        else:
            pantalla.blit(self.animacion_actual[int(self.pasos_animacion)], (self.rectangulos["principal"].x , self.rectangulos["principal"].y ))

       

    @staticmethod
    def obtener_rectangulos(rectangulo:pygame.Rect, width:int, height:int):
        diccionario = {}
        if len(rectangulo) > 0 and isinstance(rectangulo, pygame.Rect):

            diccionario["principal"] = rectangulo
            diccionario["bottom"] = pygame.Rect(rectangulo.left, rectangulo.bottom - 12, rectangulo.width, height * 0.20)
            diccionario["right"] = pygame.Rect(rectangulo.right - 10, rectangulo.top, 10, rectangulo.height)
            diccionario["left"] = pygame.Rect(rectangulo.left, rectangulo.top, 10, rectangulo.height)
            diccionario["top"] = pygame.Rect(rectangulo.left, rectangulo.top , rectangulo.width, 12)

        return diccionario
    
    @staticmethod
    def reescalar_imagenes(lista_animaciones, ancho, alto):
        if type(lista_animaciones[0]) != list:
            
            lista = []
            
            for i in range(len(lista_animaciones)):
                img = lista_animaciones[i]
                img_res = pygame.transform.scale(img, (ancho, alto))
                lista.append(img_res)
            return lista
        
        else:

            list_temp = []
            for j in range(len(lista_animaciones)):
                lista = []
                for i in range(len(lista_animaciones[j])):
                    img = lista_animaciones[j][i]
                    # lista_animaciones[j][i] = pygame.transform.scale(img, (ancho, alto))
                    img_res = pygame.transform.scale(img, (ancho, alto))
                    lista.append(img_res)
                list_temp.append(lista)
            return list_temp
        
    def reescalalar_imagenesa(animaciones, ancho, alto):
        if type(animaciones) == list:
            lista = []
            for i in range(len(animaciones)):
                img = animaciones[i]
                img_res = pygame.transform.scale(img, (ancho, alto))
                lista.append(img_res)
            return lista
        
        else:
            temp_dict = {}
            for clave in animaciones:
                temp_list = []
                for i in range(len(animaciones[clave])):
                    img = animaciones[clave][i]
                    animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))
                    temp_list.append(pygame.transform.scale(img, (ancho, alto)))

                temp_dict[clave] = temp_list
            return temp_dict


    @staticmethod
    def rotar_imagen(imagenes:list):
        lista_imagenes = []
        for i in range(len(imagenes)):
            imagen_rotada = pygame.transform.flip(imagenes[i],True,False)
            lista_imagenes.append(imagen_rotada)
        
        return lista_imagenes