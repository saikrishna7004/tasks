from django.shortcuts import redirect, render, HttpResponse

from tasklist.funtions import answerSet, questionSet

from .models import Question, TaskInfo

# Create your views here.

def mytasks(request):
    return render(request, "tasklist.html")

def taskinfo(request, slug):
    if request.user.is_anonymous:
        return redirect("/login")
    sections = TaskInfo.objects.get(slug=slug).section_set.all()
    all_list = []
    for section in sections:
        all_list.append({"name": section.name, "ques_set": questionSet(section.question_set.all()), "id": section.id})
    # ques_list = questionSet(TaskInfo.objects.get(slug=slug).section_set.filter(id=id)[0].question_set.all())
    return render(request, "tasklist.html", {"all_list": all_list, "slug": slug})

def question(request, slug, id, id1):
    if request.user.is_anonymous:
        return redirect("/login")
    ques = questionSet([TaskInfo.objects.get(slug=slug).section_set.filter(id=id)[0].question_set.filter(id=id1)[0]])
    return render(request, "question.html", {"question": ques[0], "slug": slug, "ques_id": id1})

def answer(request, slug, id, id1):
    if request.user.is_anonymous:
        return redirect("/login")
    ques = questionSet([TaskInfo.objects.get(slug=slug).section_set.filter(id=id)[0].question_set.filter(id=id1)[0]])
    ans = answerSet(Question.objects.filter(id=id1)[0].answer_set.all().order_by("-answered_on"))

    return render(request, "answer.html", {"question": ques[0], "slug": slug, "answers": ans})

def answerPost(request, slug, id, id1):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method != "POST":
        return HttpResponse("Method not allowed - GET")
    ans = request.POST.get("desc")
    Question.objects.filter(id=id1)[0].answer_set.create(desc=ans, answered_by=request.user)
    return redirect("/tasks/"+slug+"/"+str(id)+"/"+str(id1)+"/"+"answer")


