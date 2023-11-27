import json
import re

# CVS formato
# error | success , msg, funcion , archivo
#------------- CVS --------------------------------
def escritura_archivo_csv(tipo, msg:str, funcion:str, loc_archivo:str):
    
    try:
        with open("log_file.csv", "a") as archivo:
            log_info = f"{tipo},{msg},{funcion},{loc_archivo}\n"
            archivo.write(log_info)
    except Exception as argument:
        
        log_info = f"Error,{argument},escritura_archivo_csv,mod_archivos\n"
        archivo.write(log_info)
        print(f"An error occurred at escritura_archivo_csv: {argument}")

def lectura_archivo_csv():
    
    try:
        with open("jugador_datos.csv", "r") as archivo:
            lista_log = []
            for line in archivo:
                registro = re.split(",|\n",line)
                log = {}
                log["tipo"] = registro[0]
                log["msg"] = registro[1]
                log["funcion"] = registro[2]
                log["loc_archivo"] = registro[3]
                lista_log.append(log)
        return lista_log
    except Exception as argument:
        escritura_archivo_csv("Error", argument, "lectura_archivo_csv", "mod_archivos")
        print(f"An error occurred at lectura_archivo_csv: {argument}")



#------------- JSON DATOS JUEGO--------------------------------
def escritura_json(propiedad:str, dato: str | int ,data_json:dict,limpiar_propiedad:bool = False, inicia_partida:bool = False,palabra_adivininada:bool = False):
   
    try:
        with open("datos_juego.json", "w+") as archivo:
            if inicia_partida == True:
                data_json["lista_letras"] = []
                data_json["puntaje"] = 0
                data_json["vidas_restantes"] = 6
                json.dump(data_json,archivo,indent= 4)
            else:
                if palabra_adivininada == True:
                    data_json["lista_letras"] = []
                    json.dump(data_json,archivo,indent= 4)
                if propiedad == "lista_letras":
                    if limpiar_propiedad == True:
                        data_json["lista_letras"] = []
                    else:
                        data_json[propiedad].append(dato)
                else:
                    data_json[propiedad] = dato
                
                json.dump(data_json, archivo,indent=4)
            
    except Exception as argument:
        escritura_archivo_csv("Error", argument, "escritura_json", "mod_archivos")
        print(f"An error occurred at escritura_json: {argument}")
        

def lectura_json(propiedad:str= "" , objeto_total:bool=False):
  
    try:
        with open("datos_juego.json", "r") as archivo:
            data_json = json.load(archivo)
            
            if objeto_total == True:
                return data_json
            dato = data_json[propiedad]
            
        return dato
    except Exception as argument:
        escritura_archivo_csv("Error", argument, "lectura_json", "mod_archivos")
        print(f"An error occurred at lectura_json: {argument}")
    
# ----------------------- CSV PUNTAJE JUGADOR------------------------------------------

def escritura_csv_puntaje(nombre, puntaje, nivel):
   
    try:
        with open("Puntaje_jugador.csv", "a") as archivo:
            log_info = f"{nombre},{puntaje},{nivel}\n"
            archivo.write(log_info)


    except Exception as argument:
        escritura_archivo_csv("Error", argument, "escritura_csv_puntaje", "mod_archivos")
        print(f"An error occurred at escritura_json: {argument}")
        

def lectura_csv_puntaje(propiedad:str= "" , objeto_total:bool=False):
  
    try:
        with open("Puntaje_jugador.csv", "r") as archivo:
            puntaje_log = []
            for line in archivo:
                registro = re.split(",|\n",line)
                jugador = {}
                jugador["nombre"] = registro[0]
                jugador["puntaje"] = registro[1]
                jugador["nivel"] = registro[2]

                puntaje_log.append(jugador)
        return puntaje_log
      
    except Exception as argument:
        escritura_archivo_csv("Error", argument, "lectura_csv_puntaje", "mod_archivos")
        print(f"An error occurred at lectura_json: {argument}")
    