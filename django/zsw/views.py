from django.shortcuts import render, render_to_response


def hello(request):
    context = {'hello': 'Hello World!'}
    hello1 = "ffffffffffffff"
    # return render(request, 'hello.html', context)
    return render_to_response('zsw.html', locals())


def notice_del_confirm(request):
    hello2 = 'sssssssssssss'
    print(hello2)
    return render(request, 'hello.html', hello2)
