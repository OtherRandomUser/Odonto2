from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadTomografias(object):
    def setupUi(self, CadTomografias):
        CadTomografias.setObjectName("CadTomografias")
        CadTomografias.resize(1119, 824)
        self.centralwidget = QtWidgets.QWidget(CadTomografias)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edtPaciente = QtWidgets.QLineEdit(self.centralwidget)
        self.edtPaciente.setEnabled(False)
        self.edtPaciente.setObjectName("edtPaciente")
        self.horizontalLayout_2.addWidget(self.edtPaciente)
        self.btnLimparPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimparPaciente.setEnabled(False)
        self.btnLimparPaciente.setObjectName("btnLimparPaciente")
        self.horizontalLayout_2.addWidget(self.btnLimparPaciente)
        self.btnPesqPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesqPaciente.setEnabled(False)
        self.btnPesqPaciente.setObjectName("btnPesqPaciente")
        self.horizontalLayout_2.addWidget(self.btnPesqPaciente)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtAluno = QtWidgets.QLineEdit(self.centralwidget)
        self.edtAluno.setEnabled(False)
        self.edtAluno.setObjectName("edtAluno")
        self.horizontalLayout_3.addWidget(self.edtAluno)
        self.btnLimparAluno = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimparAluno.setEnabled(False)
        self.btnLimparAluno.setObjectName("btnLimparAluno")
        self.horizontalLayout_3.addWidget(self.btnLimparAluno)
        self.btnPesqAluno = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesqAluno.setEnabled(False)
        self.btnPesqAluno.setObjectName("btnPesqAluno")
        self.horizontalLayout_3.addWidget(self.btnPesqAluno)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.edtValor = QtWidgets.QLineEdit(self.centralwidget)
        self.edtValor.setEnabled(False)
        self.edtValor.setObjectName("edtValor")
        self.verticalLayout.addWidget(self.edtValor)
        self.chkEntregue = QtWidgets.QCheckBox(self.centralwidget)
        self.chkEntregue.setEnabled(False)
        self.chkEntregue.setObjectName("chkEntregue")
        self.verticalLayout.addWidget(self.chkEntregue)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.edtEntrega = QtWidgets.QLineEdit(self.centralwidget)
        self.edtEntrega.setEnabled(False)
        self.edtEntrega.setObjectName("edtEntrega")
        self.verticalLayout.addWidget(self.edtEntrega)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.edtMotivo = QtWidgets.QLineEdit(self.centralwidget)
        self.edtMotivo.setEnabled(False)
        self.edtMotivo.setObjectName("edtMotivo")
        self.verticalLayout.addWidget(self.edtMotivo)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.cboTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cboTipo.setEnabled(False)
        self.cboTipo.setObjectName("cboTipo")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.verticalLayout.addWidget(self.cboTipo)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.cboEspecializacao = QtWidgets.QComboBox(self.centralwidget)
        self.cboEspecializacao.setEnabled(False)
        self.cboEspecializacao.setObjectName("cboEspecializacao")
        self.cboEspecializacao.addItem("")
        self.cboEspecializacao.addItem("")
        self.cboEspecializacao.addItem("")
        self.cboEspecializacao.addItem("")
        self.verticalLayout.addWidget(self.cboEspecializacao)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.edtRegiao = QtWidgets.QLineEdit(self.centralwidget)
        self.edtRegiao.setEnabled(False)
        self.edtRegiao.setObjectName("edtRegiao")
        self.verticalLayout.addWidget(self.edtRegiao)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.edtElemento = QtWidgets.QLineEdit(self.centralwidget)
        self.edtElemento.setEnabled(False)
        self.edtElemento.setObjectName("edtElemento")
        self.verticalLayout.addWidget(self.edtElemento)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.cboProporcao = QtWidgets.QComboBox(self.centralwidget)
        self.cboProporcao.setEnabled(False)
        self.cboProporcao.setObjectName("cboProporcao")
        self.cboProporcao.addItem("")
        self.cboProporcao.addItem("")
        self.cboProporcao.addItem("")
        self.cboProporcao.addItem("")
        self.cboProporcao.addItem("")
        self.verticalLayout.addWidget(self.cboProporcao)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.cboAlvo = QtWidgets.QComboBox(self.centralwidget)
        self.cboAlvo.setEnabled(False)
        self.cboAlvo.setObjectName("cboAlvo")
        self.cboAlvo.addItem("")
        self.cboAlvo.addItem("")
        self.verticalLayout.addWidget(self.cboAlvo)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.cboResolucao = QtWidgets.QComboBox(self.centralwidget)
        self.cboResolucao.setEnabled(False)
        self.cboResolucao.setObjectName("cboResolucao")
        self.cboResolucao.addItem("")
        self.cboResolucao.addItem("")
        self.cboResolucao.addItem("")
        self.verticalLayout.addWidget(self.cboResolucao)
        self.btnParametrizacao = QtWidgets.QPushButton(self.centralwidget)
        self.btnParametrizacao.setObjectName("btnParametrizacao")
        self.verticalLayout.addWidget(self.btnParametrizacao)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        CadTomografias.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CadTomografias)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 22))
        self.menubar.setObjectName("menubar")
        CadTomografias.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CadTomografias)
        self.statusbar.setObjectName("statusbar")
        CadTomografias.setStatusBar(self.statusbar)

        self.retranslateUi(CadTomografias)
        QtCore.QMetaObject.connectSlotsByName(CadTomografias)

    def retranslateUi(self, CadTomografias):
        _translate = QtCore.QCoreApplication.translate
        CadTomografias.setWindowTitle(_translate("CadTomografias", "MainWindow"))
        self.label.setText(_translate("CadTomografias", "Id"))
        self.label_2.setText(_translate("CadTomografias", "Paciente"))
        self.btnLimparPaciente.setText(_translate("CadTomografias", "Limpar"))
        self.btnPesqPaciente.setText(_translate("CadTomografias", "Pesquisar"))
        self.label_3.setText(_translate("CadTomografias", "Aluno"))
        self.btnLimparAluno.setText(_translate("CadTomografias", "Limpar"))
        self.btnPesqAluno.setText(_translate("CadTomografias", "Pesquisar"))
        self.label_4.setText(_translate("CadTomografias", "Valor"))
        self.chkEntregue.setText(_translate("CadTomografias", "Entregue"))
        self.label_5.setText(_translate("CadTomografias", "Data de Entrega"))
        self.label_6.setText(_translate("CadTomografias", "Motivo"))
        self.label_7.setText(_translate("CadTomografias", "Tipo"))
        self.cboTipo.setItemText(0, _translate("CadTomografias", "Maxila"))
        self.cboTipo.setItemText(1, _translate("CadTomografias", "Mandibula"))
        self.cboTipo.setItemText(2, _translate("CadTomografias", "ATM"))
        self.cboTipo.setItemText(3, _translate("CadTomografias", "Segmento"))
        self.cboTipo.setItemText(4, _translate("CadTomografias", "Elemento"))
        self.label_8.setText(_translate("CadTomografias", "Especialização"))
        self.cboEspecializacao.setItemText(0, _translate("CadTomografias", "Nanhuma"))
        self.cboEspecializacao.setItemText(1, _translate("CadTomografias", "Ramos Mandibulares"))
        self.cboEspecializacao.setItemText(2, _translate("CadTomografias", "Oclusao"))
        self.cboEspecializacao.setItemText(3, _translate("CadTomografias", "Abertura"))
        self.label_9.setText(_translate("CadTomografias", "Região"))
        self.label_10.setText(_translate("CadTomografias", "Elemento"))
        self.label_11.setText(_translate("CadTomografias", "Proporção"))
        self.cboProporcao.setItemText(0, _translate("CadTomografias", "5x5"))
        self.cboProporcao.setItemText(1, _translate("CadTomografias", "6x8"))
        self.cboProporcao.setItemText(2, _translate("CadTomografias", "8x8"))
        self.cboProporcao.setItemText(3, _translate("CadTomografias", "8x15"))
        self.cboProporcao.setItemText(4, _translate("CadTomografias", "13x15"))
        self.label_12.setText(_translate("CadTomografias", "Alvo"))
        self.cboAlvo.setItemText(0, _translate("CadTomografias", "Alvo"))
        self.cboAlvo.setItemText(1, _translate("CadTomografias", "Dente"))
        self.label_13.setText(_translate("CadTomografias", "Resolução"))
        self.cboResolucao.setItemText(0, _translate("CadTomografias", "Baixa"))
        self.cboResolucao.setItemText(1, _translate("CadTomografias", "Média"))
        self.cboResolucao.setItemText(2, _translate("CadTomografias", "Alta"))
        self.btnParametrizacao.setText(_translate("CadTomografias", "Parametrização"))
        self.btnNovo.setText(_translate("CadTomografias", "&Novo"))
        self.btnSalvar.setText(_translate("CadTomografias", "&Salvar"))
        self.btnPesquisar.setText(_translate("CadTomografias", "&Pesquisar"))
        self.btnRemover.setText(_translate("CadTomografias", "&Remover"))
        self.btnSair.setText(_translate("CadTomografias", "Sai&r"))


    def set_mode(self, edit=True):
        self.edtId.setEnabled(not edit)
        self.btnPesqPaciente.setEnabled(edit)
        self.btnLimparPaciente.setEnabled(edit)
        self.btnPesqAluno.setEnabled(edit)
        self.btnLimparAluno.setEnabled(edit)
        self.edtValor.setEnabled(edit)
        self.chkEntregue.setEnabled(edit)
        self.edtEntrega.setEnabled(edit)
        self.edtMotivo.setEnabled(edit)
        self.cboTipo.setEnabled(edit)
        self.cboEspecializacao.setEnabled(edit)
        self.edtRegiao.setEnabled(edit)
        self.edtElemento.setEnabled(edit)
        self.cboProporcao.setEnabled(edit)
        self.cboAlvo.setEnabled(edit)
        self.cboResolucao.setEnabled(edit)
        self.btnParametrizacao.setEnabled(edit)

        self.btnNovo.setEnabled(not edit)
        self.btnSalvar.setEnabled(edit)
        self.btnPesquisar.setEnabled(not edit)
        self.btnRemover.setEnabled(edit)
        self.btnSair.setEnabled(not edit)