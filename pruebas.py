import ListaErrores as lalista



lista =lalista.ListaError()

error = lalista.Error('semantico','javier','prueba',5,5)
error1 = lalista.Error('semantico1','javier','prueba',5,5)
error2 = lalista.Error('semantico2','javier','prueba',5,5)
error3 = lalista.Error('semantico3','javier','prueba',5,5)
error4 = lalista.Error('semantico4','javier','prueba',5,5)
error5 = lalista.Error('semantico5','javier','prueba',5,5)
error6 = lalista.Error('semantico6','javier','prueba',5,5)
error7 = lalista.Error('semantico7','javier','prueba',5,5)

lista.AddError(error)
lista.AddError(error1)
lista.AddError(error2)
lista.AddError(error3)
lista.AddError(error4)
lista.AddError(error5)
lista.AddError(error6)
lista.AddError(error7)

datos = lista.ObtenerLista()

for data in datos:
    print(data.tipo)


