class Usuario:   
    def __init__(self,nombre,email):
        self.nombre= nombre
        self.email= email
        self.cuenta=0

    def hacer_deposito(self, cantidad):
        self.cuenta += cantidad
        return self
    def hacer_retiro(self, cantidad):
        self.cuenta -= cantidad
        return self

    def mostrar_balance_usuario(self):
        print(f"usuario:{self.nombre} balance:${self.cuenta}")
        return self

    def transferir_dinero(self,cantidad,usuario): 
        self.cuenta -= cantidad
        usuario.cuenta += cantidad
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()

raul= Usuario('Raul','raul.dojo@coding.com')
nicole= Usuario('Nicole','nicole22.dojo@coding.com')
malcom= Usuario('Malcom','malcom_W.dojo@coding.com')


raul.hacer_deposito(100).hacer_deposito(200).hacer_deposito(300).hacer_retiro(150).mostrar_balance_usuario()
print('---------------------')

nicole.hacer_deposito(650).hacer_deposito(1200).hacer_retiro(40).hacer_retiro(340).mostrar_balance_usuario()
print('---------------------')

malcom.hacer_deposito(921).hacer_retiro(22).hacer_retiro(45).hacer_retiro(180).mostrar_balance_usuario()
print('---------------------')
raul.transferir_dinero(500,malcom)


