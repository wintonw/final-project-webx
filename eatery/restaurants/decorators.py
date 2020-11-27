from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_fuc):
    # logged in user no login & sign up page
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('restaurants:index')
        else:
            return view_fuc(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_fuc):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_fuc(request, *args, **kwargs)
            else:
                return HttpResponse("This page is not for you.")
        return wrapper_func
    return decorator


def admin_only(view_fuc):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('restaurant:index')

        if group == 'manager':
            return view_fuc(request, *args, **kwargs)
    return wrapper_func
