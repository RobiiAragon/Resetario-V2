import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import filedialog
from openpyxl.drawing.image import Image


def obtener_fecha_actual():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def crear_carpeta_con_fecha_actual():
    fecha_actual = obtener_fecha_actual()
    carpeta = os.path.join(os.getcwd(), "Recetarios", fecha_actual)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta


def hacer_preguntas():
    nombre = nombre_entry.get()
    if not nombre:
        nombre = " "  # Espacio en blanco
    edad = edad_entry.get()
    if not edad:
        edad = " "  # Espacio en blanco
    temp = temp_entry.get()
    if not temp:
        temp = " "  # Espacio en blanco
    ta = ta_entry.get()
    if not ta:
        ta = " "  # Espacio en blanco
    peso = peso_entry.get()
    if not peso:
        peso = " "  # Espacio en blanco
    fc = fc_entry.get()
    if not fc:
        fc = " "  # Espacio en blanco
    talla = talla_entry.get()
    if not talla:
        talla = " "  # Espacio en blanco
    fr = fr_entry.get()
    if not fr:
        fr = " "  # Espacio en blanco
    circun_abdom = circun_abdom_entry.get()
    if not circun_abdom:
        circun_abdom = " "  # Espacio en blanco
    id = id_entry.get()
    if not id:
        id = " "  # Espacio en blanco
    alergias = alergias_entry.get()
    if not alergias:
        alergias = " "  # Espacio en blanco
    tratamiento = tratamiento_entry.get()
    if not tratamiento:
        tratamiento = " "  # Espacio en blanco
    indicaciones_generales = indicaciones_generales_entry.get()
    if not indicaciones_generales:
        indicaciones_generales = " "  # Espacio en blanco
    proxima_cita = proxima_cita_entry.get()
    if not proxima_cita:
        proxima_cita = " "  # Espacio en blanco
    return nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita


def llenar_datos_en_plantilla(nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita):
    plantilla = openpyxl.load_workbook("receta.xlsx")
    hoja = plantilla.active

    hoja["J4"] = nombre
    hoja["J36"] = nombre
    hoja["H5"] = edad
    hoja["H37"] = edad
    # Fecha y hora automática en columna D4
    hoja["BB4"] = obtener_fecha_actual()
    # Fecha y hora automática en columna D34
    hoja["BB36"] = obtener_fecha_actual()
    hoja["R5"] = temp
    hoja["R37"] = temp
    hoja["H6"] = ta
    hoja["H38"] = ta
    hoja["R6"] = peso
    hoja["R38"] = peso
    hoja["H7"] = fc
    hoja["H39"] = fc
    hoja["R7"] = talla
    hoja["R39"] = talla
    hoja["H8"] = fr
    hoja["H40"] = fr
    hoja["L10"] = circun_abdom
    hoja["L42"] = circun_abdom
    hoja["H11"] = id
    hoja["H43"] = id
    hoja["I13"] = alergias
    hoja["I45"] = alergias
    hoja["AC6"] = tratamiento
    hoja["AC38"] = tratamiento
    hoja["O16"] = indicaciones_generales
    hoja["O48"] = indicaciones_generales
    hoja["AF22"] = proxima_cita
    hoja["AF54"] = proxima_cita

    # Cargar la imagen
    imagen = Image("receta.png")

    # Ajustar la imagen al tamaño de la celda deseada
    imagen.width = 750
    imagen.height = 990

    # Insertar la imagen en la celda deseada
    hoja.add_image(imagen, "A1")

    return plantilla


def guardar_plantilla_modificada(plantilla, carpeta, nombre_pdf):
    ruta_receta_modificada = os.path.join(carpeta, f"{nombre_pdf}.xlsx")
    plantilla.save(ruta_receta_modificada)
    return ruta_receta_modificada


def imprimir_mensaje_exito(carpeta):
    print("La receta modificada se ha guardado en la carpeta", carpeta)
    os.startfile(carpeta)


def generar_reporte():
    carpeta = crear_carpeta_con_fecha_actual()
    nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita = hacer_preguntas()
    plantilla = llenar_datos_en_plantilla(nombre, edad, temp, ta, peso, fc, talla, fr,
                                          circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita)
    ruta_receta_modificada = guardar_plantilla_modificada(
        plantilla, carpeta, nombre)
    imprimir_mensaje_exito(carpeta)


window = tk.Tk()
window.title("Generador de Reportes")
window.geometry("350x650")

nombre_label = tk.Label(window, text="Nombre:")
nombre_entry = tk.Entry(window)
edad_label = tk.Label(window, text="Edad:")
edad_entry = tk.Entry(window)
temp_label = tk.Label(window, text="Temp:")
temp_entry = tk.Entry(window)
ta_label = tk.Label(window, text="T.A.:")
ta_entry = tk.Entry(window)
peso_label = tk.Label(window, text="Peso:")
peso_entry = tk.Entry(window)
fc_label = tk.Label(window, text="F.C.:")
fc_entry = tk.Entry(window)
talla_label = tk.Label(window, text="Talla:")
talla_entry = tk.Entry(window)
fr_label = tk.Label(window, text="F.R.:")
fr_entry = tk.Entry(window)
circun_abdom_label = tk.Label(window, text="Circun. Abdom.:")
circun_abdom_entry = tk.Entry(window)
id_label = tk.Label(window, text="I.D.:")
id_entry = tk.Entry(window)
alergias_label = tk.Label(window, text="Alergias:")
alergias_entry = tk.Entry(window)
tratamiento_label = tk.Label(window, text="Tratamiento:")
tratamiento_entry = tk.Entry(window)
indicaciones_generales_label = tk.Label(window, text="Indicaciones Generales:")
indicaciones_generales_entry = tk.Entry(window)
proxima_cita_label = tk.Label(window, text="Próxima Cita:")
proxima_cita_entry = tk.Entry(window)
generar_button = tk.Button(
    window, text="Generar Reporte", command=generar_reporte)
mensaje_label = tk.Label(window, wraplength=350)

nombre_label.pack()
nombre_entry.pack()
edad_label.pack()
edad_entry.pack()
temp_label.pack()
temp_entry.pack()
ta_label.pack()
ta_entry.pack()
peso_label.pack()
peso_entry.pack()
fc_label.pack()
fc_entry.pack()
talla_label.pack()
talla_entry.pack()
fr_label.pack()
fr_entry.pack()
circun_abdom_label.pack()
circun_abdom_entry.pack()
id_label.pack()
id_entry.pack()
alergias_label.pack()
alergias_entry.pack()
tratamiento_label.pack()
tratamiento_entry.pack()
indicaciones_generales_label.pack()
indicaciones_generales_entry.pack()
proxima_cita_label.pack()
proxima_cita_entry.pack()
generar_button.pack()
mensaje_label.pack()

window.mainloop()