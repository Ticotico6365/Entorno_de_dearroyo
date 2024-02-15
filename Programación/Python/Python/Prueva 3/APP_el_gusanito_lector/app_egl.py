from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from conectamos_con_base_de_datos_EGL import *
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        #cargamos el archivo
        loadUi('APP_egl.ui', self)

        # CONECTAR BOTONES CON PAGINAS
        #para ver la tabla directamente
        self.bt_ver_tabla.clicked.connect(self.cargar_datos_tabla)
        #self.elige_tipo.currentIndexChanged.connect(self.cargar_datos_tabla_tipo())

        #dentro de crear elemento el boton para guardar
        self.bt_crear.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.crear))
        self.bt_guardar_insert.clicked.connect(self.crear_nuevo)

        #para el botón para eliminar el elemento
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.delete_2))
        self.bt_busca_delete.clicked.connect(self.eliminar_elemento)

        #Para los botones de editar
        self.bt_editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editar))
        self.bt_busca_edit.clicked.connect(self.mostrar_elemento)
        self.bt_guardar_edit.clicked.connect(self.crear_nuevo_editar)

    #CARGAR DATOS
    def cargar_datos_tabla(self):
        self.stackedWidget.setCurrentWidget(self.tabla)
        #carga de datos
        libros,columnas = extraer_datos()
        #establecer filas de la tabla
        self.tableWidget.setRowCount(len(libros))
        # Agregar datos a la tabla
        for fila, libro in enumerate(libros, start=0):
            for columna, campo_libro in enumerate(libro.values(), start=0):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(campo_libro)))
        self.tableWidget.resizeColumnsToContents()

    #CREAR
    def crear_nuevo(self):
        nuevo_libro = dict()
        nuevo_libro["portada"] = self.txt_portada_insert.toPlainText()
        nuevo_libro["nombre"] = self.txt_nombre_insert.toPlainText()
        nuevo_libro["autor"] = self.txt_autores_insert.toPlainText()
        nuevo_libro["precio"] = self.txt_precio_insert.value()
        nuevo_libro["ISBN"] = self.txt_isbn_insert.toPlainText()
        nuevo_libro["tipo"] = self.txt_tipo_insert.toPlainText()
        insertar_1_dato(nuevo_libro)

    #método para eliminar
    def eliminar_elemento(self):
        borrar_dato_id(self.txt_id_delete_2.value())

    #método para editar
    def mostrar_elemento(self):
        libro = buscar_libro_id(self.txt_id_edit_2.text())
        self.txt_portada_edit.insertPlainText(libro["portada"])
        self.txt_nombre_edit.insertPlainText(libro["nombre"])
        self.txt_autores_edit.insertPlainText(libro["autores"])
        self.txt_precio_edit.setValue(libro["precio"])
        self.txt_isbn_edit.insertPlainText(libro["isbn"])
        self.txt_tipo_edit.insertPlainText(libro["tipo"])
        #y borro
        borrar_dato_id(self.txt_id_edit_2.value())
    def crear_nuevo_editar(self):
        nuevo_libro = dict()
        nuevo_libro["portada"] = self.txt_portada_edit.toPlainText()
        nuevo_libro["nombre"] = self.txt_nombre_edit.toPlainText()
        nuevo_libro["autor"] = self.txt_autores_edit.toPlainText()
        nuevo_libro["precio"] = self.txt_precio_edit.value()
        nuevo_libro["ISBN"] = self.txt_isbn_edit.toPlainText()
        nuevo_libro["tipo"] = self.txt_tipo_edit.toPlainText()
        insertar_1_dato(nuevo_libro)

    def cargar_datos_tabla_tipo(self):
        self.stackedWidget.setCurrentWidget(self.tabla)
        #carga de datos
        libros,columnas = buscar_tipo(self.elige_tipo.currentText())
        #establecer filas de la tabla
        self.tableWidget.setRowCount(len(libros))
        # Agregar datos a la tabla
        for fila, libro in enumerate(libros, start=0):
            for columna, campo_libro in enumerate(libro.values(), start=0):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(campo_libro)))
        self.tableWidget.resizeColumnsToContents()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())