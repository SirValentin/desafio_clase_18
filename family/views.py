from django.shortcuts import render
from family.models import Family

def create_family(request):
    # creamos 3 objetos de familia
    family_list = []
    new_family1 = Family.objects.create(name="Zoila Morales", age=44, date_of_birth="1978-07-13")
    new_family2 = Family.objects.create(name="Valentin Carvajal", age=56, date_of_birth="1966-04-07")
    new_family3 = Family.objects.create(name="Camila Carvajal", age=22, date_of_birth="2000-04-23")

    # agregamos los objetos a una lista para mandarlos por el context
    family_list.append(new_family1)
    family_list.append(new_family2)
    family_list.append(new_family3)
    context = {
        'family_list': family_list,
        'family_len': len(family_list)
    }
    return render(request, 'create_family.html', context=context)

def list_family(request):
    list_family = Family.objects.all
    context = {
        'family_list': list_family
    }
    return render(request, 'list_family.html', context=context)