from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadIndicacoes(object):
    def setupUi(self, CadIndicacoes):
        CadIndicacoes.setObjectName("CadIndicacoes")
        CadIndicacoes.resize(405, 213)
        self.centralwidget = QtWidgets.QWidget(CadIndicacoes)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtId = QtWidgets.QLineEdit(self.centralwidget)
        self.edtId.setObjectName("edtId")
        self.verticalLayout.addWidget(self.edtId)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.edtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.edtNome.setEnabled(False)
        self.edtNome.setObjectName("edtNome")
        self.verticalLayout.addWidget(self.edtNome)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnNovo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNovo.setObjectName("btnNovo")
        self.verticalLayout_2.addWidget(self.btnNovo)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setObjectName("btnSalvar")
        self.verticalLayout_2.addWidget(self.btnSalvar)
        self.btnPesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesquisar.setObjectName("btnPesquisar")
        self.verticalLayout_2.addWidget(self.btnPesquisar)
        self.btnRemover = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemover.setEnabled(False)
        self.btnRemover.setObjectName("btnRemover")
        self.verticalLayout_2.addWidget(self.btnRemover)
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setObjectName("btnSair")
        self.verticalLayout_2.addWidget(self.btnSair)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        CadIndicacoes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CadIndicacoes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 22))
        self.menubar.setObjectName("menubar")
        CadIndicacoes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CadIndicacoes)
        self.statusbar.setObjectName("statusbar")
        CadIndicacoes.setStatusBar(self.statusbar)

        self.retranslateUi(CadIndicacoes)
        QtCore.QMetaObject.connectSlotsByName(CadIndicacoes)

    def retranslateUi(self, CadIndicacoes):
        _translate = QtCore.QCoreApplication.translate
        CadIndicacoes.setWindowTitle(_translate("CadIndicacoes", "Indicações"))
        self.label.setText(_translate("CadIndicacoes", "Id"))
        self.label_2.setText(_translate("CadIndicacoes", "Nome"))
        self.btnNovo.setText(_translate("CadIndicacoes", "&Novo"))
        self.btnSalvar.setText(_translate("CadIndicacoes", "&Salvar"))
        self.btnPesquisar.setText(_translate("CadIndicacoes", "&Pesquisar"))
        self.btnRemover.setText(_translate("CadIndicacoes", "&Remover"))
        self.btnSair.setText(_translate("CadIndicacoes", "Sai&r"))

    def set_mode(self, edit=True):
        self.edtId.setEnabled(not edit)
        self.edtNome.setEnabled(edit)

        self.btnNovo.setEnabled(not edit)
        self.btnSalvar.setEnabled(edit)
        self.btnPesquisar.setEnabled(not edit)
        self.btnRemover.setEnabled(edit)
        self.btnSair.setEnabled(not edit)