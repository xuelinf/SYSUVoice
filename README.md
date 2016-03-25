# About

A Forum(BBS) based on Django, forked from [FairyBBS](https://github.com/ericls/FairyBBS).

It looks like:

Topics

![][1]

Nodes

![][2]

Mange

![][3]

Tested on Django 1.8.6

# Features

Major features:

1. Whole user manage system, contains registration, login, change password, retrieve;
2. Users can create topics, append topics, have comments on topics.
3. Send notifications when others @YOU in anywhere.
4. Markdown supported, whether in topics or comments.
5. A convenient administrator page, can manage users, topics, nodes. 
6. A simple keyword search egine, one can search some specific topics.

# How to Run

1. Firstly, make sure all the relevant requirements installed.
2. Do some configure in SYSUVoice/settings.py.

        # About database setting
        DATABASES = {
            'default': {
                'ENGINE': '',
                'NAME': '',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        }

        # Settings about email adress(used when reset password). 
        EMAIL_USE_TLS = True
        EMAIL_HOST = 'smtp.qq.com'
        EMAIL_PORT = 25
        EMAIL_HOST_USER = 'xxxxxxxxx@qq.com'
        EMAIL_HOST_PASSWORD = 'xxxxxxx'
3. Start corresponding database service.
4. Change directory SYSUVoice/ , run `python manage.py runserver`.  Just looks like the followings:

        $ python manage.py runserver
        Performing system checks...
        
        System check identified no issues (0 silenced).
        March 25, 2016 - 15:10:30
        Django version 1.8.6, using settings 'SYSUVoice.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.


[1]: Demo/topic.png
[2]: Demo/nodes.png
[3]: Demo/manage.png

