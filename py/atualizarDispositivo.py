def atualiza_Disp(request, id):
        dispositivo = get_object_or_404(Dispositivos, id=id)

        tipo = request.POST.get('tipo')
        marca = request.POST.get('marca')
        potencia = request.POST.get('potencia')
        modelo = request.POST.get('modelo')

        dispositivo.tipo = tipo
        dispositivo.marca = marca
        dispositivo.KHW = potencia
        dispositivo.modelo = modelo
        icone = request.FILES.get('icone')
        if icone:
            dispositivo.icone = icone

    

        dispositivo.save()

        data = {'status': '200', 'message': 'Dispositivo atualizado com sucesso'}
        redirect(reverse('clientes'))
        messages.success(request, 'Dispositivo atualizado com sucesso',extra_tags='success-message')
        return JsonResponse(data)
