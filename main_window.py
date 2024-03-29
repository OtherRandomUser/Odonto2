from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_main_window import Ui_MainWindow
from cad_indicacoes import CadIndicacoes
from cad_alunos import CadAlunos
from cad_pacientes import CadPacientes
from cad_panoramicas import CadPanoramicas
from cad_tomografias import CadTomografias

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__setupEvents()

    def __setupEvents(self):
        def on_cad_indicacoes():
            indicacoes = CadIndicacoes()
            indicacoes.show()

        def on_cad_alunos():
            alunos = CadAlunos()
            alunos.show()

        def on_cad_pacientes():
            pacientes = CadPacientes()
            pacientes.show()

        def on_cad_panoramicas():
            panoramicas = CadPanoramicas()
            panoramicas.show()

        def on_cad_tomografias():
            tomografias = CadTomografias()
            print("Teste")
            tomografias.show()

        self.ui.actionIndica_es.triggered.connect(on_cad_indicacoes)
        self.ui.actionAlunos.triggered.connect(on_cad_alunos)
        self.ui.actionPacientes.triggered.connect(on_cad_pacientes)
        self.ui.actionPanoramicas.triggered.connect(on_cad_panoramicas)
        self.ui.actionTomografias.triggered.connect(on_cad_tomografias)

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                self.close()