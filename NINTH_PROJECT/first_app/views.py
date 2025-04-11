from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Cookie
def home(request):
    response = render(request, 'home.html')
    # response.set_cookie('name', 'Ishrakul Tahmid', max_age=10) # Cookie will expire in 10 seconds
    response.set_cookie('name', 'Ishrakul Tahmid', expires=datetime.now(datetime.timezone.utc) + timedelta(days=7)) # Cookie will expire in 7 days
    return response
def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

# Session
# Session is a dictionary-like object that stores data on the server side. It is used to store data that is specific to a user and is not shared with other users.
# Session data is stored on the server side and is identified by a session ID that is sent to the client as a cookie. The session ID is used to retrieve the session data from the server when the client makes a request.

def set_session(request):
    data = {
        'name': 'Ishrakul Tahmid',
        'age': 22,
        'country': 'Bangladesh'
    }
    request.session.update(data) # Update the session data with the new data
    print(request.session.get_session_cookie_age()) # Print the session cookie age in seconds
    print(request.session.get_expiry_age()) # Print the session expiry age in seconds
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest') # Default value is 'Guest' if the key does not exist
        age = request.session.get('age')
        country = request.session.get('country')
        request.session.modified = True # Mark the session as modified to update the expiry time
        return render(request, 'get_session.html', {'name': name, 'age': age, 'country': country})
    else:
        return HttpResponse('Session data not found. Please set the session data first.')

def delete_session(request):
    # del request.session['name'] # Delete the session data with the key 'name'
    request.session.flush() # Delete all session data
    return render(request, 'delete_session.html')