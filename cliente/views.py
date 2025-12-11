from django.shortcuts import render

# Create your views here.
from models import Cliente
def cadastrar_cliente(request):
    if request.method == 'POST':
         codcli = request.POST.get('codcli')
         nome = request.POST.get('nome')
         telefone = request.POST.get('telefone')
         cliente = Cliente(codcli, nome, telefone)
         return HttpResponse(f"Cliente cadastrado com sucesso! <br> Código: "
                            f"{cliente.codcli} <br> Nome: {cliente.nome} "
                            f"<br> Telefone: {cliente.telefone}")
         return render(request, 'formcliente.html')