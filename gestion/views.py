from contextvars import Context
from pipes import Template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
#
from django.views import generic
from .forms import AgendaForm
from datetime import datetime, timedelta
from .mixins import MedicoMixin
# Create your views here.


def index(request):
    especialidades = Especialidades.objects.all()
    contexto = {
        "especialidades": especialidades,  
        }
    return render(request,'index.html', contexto)

class AgendaCrear(MedicoMixin,generic.View):
    template_name = 'gestion/crear_agenda.html'
    form_class = AgendaForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            hospital = form.cleaned_data['hospital']
            especialidad = form.cleaned_data['especialidad']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            hora_inicio = form.cleaned_data['hora_inicio']
            hora_fin = form.cleaned_data['hora_fin']
            fecha_inicio_str = fecha_inicio.strftime("%Y-%m-%d")
            fecha_fin_str = fecha_fin.strftime("%Y-%m-%d")
            hora_inicio_str = hora_inicio.strftime("%H:%M:%S")
            hora_fin_str = hora_fin.strftime("%H:%M:%S")
            fecha_inicio = datetime.strptime(fecha_inicio_str + " " + hora_inicio_str, "%Y-%m-%d %H:%M:%S")
            fecha_fin = datetime.strptime(fecha_fin_str + " " + hora_fin_str, "%Y-%m-%d %H:%M:%S")
            intervalo = form.cleaned_data['intervalo']
            intervalo = int(intervalo)
            # dias de la semana 
            dias = form.cleaned_data['days']
            print(dias)
            print(fecha_inicio.strftime("%A"))
            #dias entre fecha inicio y fecha fin
            print(hora_fin)
            print(hora_inicio)
            horas = timedelta(hours=hora_fin.hour, minutes=hora_fin.minute, seconds=hora_fin.second) - timedelta(hours=hora_inicio.hour, minutes=hora_inicio.minute, seconds=hora_inicio.second)
            minutos = horas.total_seconds() / 60
            cantidad_turnos = int(minutos / intervalo)

            while fecha_inicio <= fecha_fin:
                if fecha_inicio.strftime("%A") in dias:
                    for i in range(cantidad_turnos):
                        fecha_turno = fecha_inicio + timedelta(minutes=intervalo * i)
                        turno = Agenda.objects.create(
                            user=user,
                            hospital=hospital,
                            especialidad=especialidad,
                            fecha = fecha_turno,
                        )
                        turno.save()
                fecha_inicio = fecha_inicio + timedelta(days=1)
            return redirect('gestion:lista_agenda')

        return render(request, self.template_name, {'form': form})


class AgentaLista(MedicoMixin,generic.ListView):
    template_name = 'gestion/lista_agenda.html'
    context_object_name = 'agendas'

    def get_queryset(self):
        user = self.request.user
        # para filtrar por fecha actual 
        # fecha__gte=datetime.now(),
        query_agenda = Agenda.objects.filter(user=user).order_by('fecha')
        print(query_agenda)
        return query_agenda
    