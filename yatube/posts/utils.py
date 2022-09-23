from django.core.paginator import Paginator


def paginator_func(objects, limit, request):
    paginator = Paginator(objects, limit)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj
