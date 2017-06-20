# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses, Description, Comment

def index(request):
    courses = Courses.objects.all()
    description = Description.objects.all()
    print description
    context = {"courses": courses, "description":description}
    return render(request, 'first_app/index.html', context)

def newcourse(request):
    Courses.objects.create(name=request.POST['name'])
    course = Courses.objects.get(name=request.POST['name'])
    id = course.id
    Description.objects.create(description=request.POST['description'], course_id=id)
    return redirect('/')

def confirm(request, id):
    course = Courses.objects.get(id=id)
    id = course.id
    print id
    try:
        description = Description.objects.get(course_id=id)
    except: 
        pass
    context = {
        "id":course.id,
        "name":course.name,
        "description":description.description
    }
    return render(request, 'first_app/confirm.html', context)

def remove(request, id):
    Courses.objects.get(id=id).delete()
    return redirect('/')

def comments(request, id):
    course = Courses.objects.get(id=id)
    comments = Comment.objects.filter(course_id=id)
    context = {
        'name':course.name,
        'description':course.description,
        'id':id,
        'comments':comments,
        'course_id': course.id
    }
    print id
    return render(request, 'first_app/comments.html', context)

def addcomment(request, id):
    Comment.objects.create(comment=request.POST['comment'], course_id=id)
    course = Courses.objects.get(id=id)
    comments = Comment.objects.filter(course_id=id)
    context = {
        'name':course.name,
        'description':course.description,
        'course_id':course.id,
        'comments':comments
    }
    return render(request, 'first_app/comments.html', context)

# Create your views here.
