from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy


@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        # create new product
        return JsonResponse({'data': 'company post request'})


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(company.to_json(), safe=False)


@csrf_exempt
def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancies.all()
    vacancies_json = [p.to_json() for p in vacancies]

    return JsonResponse(vacancies_json, safe=False)


@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        # create new product
        return JsonResponse({'data': 'vacancy post request'})


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json(), safe=False)


@csrf_exempt
def vacancy_top(request):
    try:
        vacancies = Vacancy.objects.order_by("-salary")
        vacancies_json = [p.to_json() for p in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancies_json, safe=False)