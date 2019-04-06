from django.shortcuts import redirect


def staff_required(func):
    def wrap(request, *args, **kwargs):

        if request.user.is_authenticated and request.user.is_staff:
            return func(request, *args, **kwargs)
        elif request.user.is_authenticated:
            return redirect("shop:index")
        else:
            return redirect("account:login")

    return wrap
