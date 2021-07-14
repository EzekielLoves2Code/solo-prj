from django.shortcuts import render, redirect

def index(request):
    # if 'userid' not in request.session:
    #     return redirect('/')
    # user = User.objects.get(id=request.session['userid'])
    context = {
        # 'user': user,
        'all_ideas': Idea.objects.all()
    }
    return render(request, 'dashboard.html', context)
# def view(request, idea_id):
#     context ={
#         'idea': Idea.objects.get(id=idea_id),
#         'current_user':User.objects.get(id=request.session['userid'])
#     }
#     return render(request, 'viewidea.html', context)


def remove(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    idea.delete()
    return redirect('/ideas')


# def editpage(request, idea_id):
#     context = {
#         'show': Show.objects.get(id=show_id)
#     }
#     return render(request, 'editidea.html', context)






# Create your views here.
