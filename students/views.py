from django.shortcuts import render

def home(request):
    students = ['Arun', 'Rahul', 'Meena']

    return render(request, 'home.html', {'students': students})


def result(request, name):
    marks = {
        'Arun': 85,
        'Rahul': 90,
        'Meena': 95
    }

    student_mark = marks.get(name)

    return render(request, 'result.html', {
        'name': name,
        'mark': student_mark
    })