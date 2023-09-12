def gerenciar(request):
    dispositivo_list = Dispositivos.objects.all()
    return render(request, 'gerenciar.html',{'dispositivos': dispositivo_list})

def attDisp(request):
    idDispositivo= request.POST.get("id_dispositivo")
    dispositivo = Dispositivos.objects.filter(id=idDispositivo)
    dispositivoJson = json.loads(serializers.serialize('json',dispositivo))[0]['fields']
    idDisp = json.loads(serializers.serialize('json',dispositivo))[0]['pk']
    data = {'dispositivo': dispositivoJson,"idDisp": idDisp}

    return JsonResponse (data)
