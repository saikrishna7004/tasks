from pytz import timezone
from django.utils.text import slugify
import random
import string

def questionAnswerSet(quesSetAll):
    quesSet = []
    for ques in quesSetAll:
        ansSet = []
        for ans in ques.answer_set.all().order_by('-answered_on'):
            ansSet.append({
                "title": ans.title,
                "desc": ans.desc,
                "answered_by": ans.answered_by,
                "answered_on": ans.answered_on.astimezone(timezone('Asia/Kolkata')),
                "updated_on": ans.updated_on.astimezone(timezone('Asia/Kolkata'))
            })
        quesSet.append({
            "id": ques.id,
            "title": ques.title,
            "desc": ques.desc,
            "posted_by": ques.posted_by.first_name,
            "posted_on": ques.posted_on.astimezone(timezone('Asia/Kolkata')),
            "updated_on": ques.updated_on.astimezone(timezone('Asia/Kolkata')),
            "answers": ansSet,
            "slug": ques.slug
        })
    return quesSet

def questionSet(quesSetAll):
    quesSet = []
    for ques in quesSetAll:
        quesSet.append({
            "id": ques.id,
            "title": ques.title,
            "desc": ques.desc,
            "posted_by": ques.posted_by.first_name,
            "posted_on": ques.posted_on.astimezone(timezone('Asia/Kolkata')),
            "updated_on": ques.updated_on.astimezone(timezone('Asia/Kolkata'))
        })
    return quesSet

def answerSet(ansSetAll):
    ansSet = []
    for ans in ansSetAll:
        ansSet.append({
            "id": ans.id,
            "desc": ans.desc,
            "answered_by": ans.answered_by.first_name,
            "answered_on": ans.answered_on.astimezone(timezone('Asia/Kolkata')),
            "updated_on": ans.updated_on.astimezone(timezone('Asia/Kolkata'))
        })
    return ansSet

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug