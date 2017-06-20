# CD_Django_TimeDisplay
Assignment: Time Display
Create a Django project called time_display_assignment according to the below wireframe.

In timedisplay's controller (views.py), create a method named index.

When you go to the URL localhost:8000 this should run the index method in your controller file, (views.py). Have that method render a template that displays the current date and time.

    from django.shortcuts import render, HttpResponse
    def yourMethodFromUrls(request):
    context = {
    "somekey":"somevalue"
    }
    return render(request,'appname/page.html', context)

The keys of your context dictionary are available to be accessed on your page.html.

    <div class="line">{{somekey}}</div>

The above line will print out “somevalue” on your HTML!

<img src="http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_3832/handouts/chapter3832_6613_time.png" alt="Coding Dojo Assignment Image">