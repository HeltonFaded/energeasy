def delete_disp(request,id):
     try:
          dispositivo = Dispositivos.objects.get(id=id)
          dispositivo.delete()
          messages.error(request, 'Dispositivo excluído com sucesso', extra_tags='warning-message')
          return redirect(reverse('clientes'))
     
     except:
          messages.warning(request, 'Dispositivo não encontrado', extra_tags='warning-message')
          return redirect(reverse('clientes'))
