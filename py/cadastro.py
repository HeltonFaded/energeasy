def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    
    elif request.method == "POST":
        KHW = request.POST.get('khw')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        icone = request.FILES.get('icone')
        tipo = request.POST.get('tipo')

        disp = Dispositivos(KHW=KHW, marca=marca, modelo=modelo, icone=icone, tipo=tipo)
        disp.save()
        messages.success(request, 'Dispositivo cadastrado com sucesso',extra_tags='success-message')
        return render(request, 'clientes.html', {'disp': disp})
