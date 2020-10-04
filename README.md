libs:
python -m pip install Django==2.2.14
 -- https://django-rest-registration.readthedocs.io/en/latest/index.html --pip install django-rest-registration
 -- https://github.com/stefanfoulis/django-phonenumber-field  --pip install django-phonenumber-field
     -- https://github.com/django-money/django-money --pip install django-money
# -- URL=https://django-filter.readthedocs.io/en/master/guide/install.html  --pip install django-filter
# -- URL=https://django-recurrence.readthedocs.io/en/latest/index.html  --pip install django-recurrence
 -- https://django-registration.readthedocs.io/en/3.0.1/install.html --pip install django-registration
 -- pip install psycopg2,psycopg2-binary
 -- pip install rest_framework
 -- pip install Pillow
 
 -- https://github.com/python-social-auth/social-app-django --pip install social-auth-app-django
# -- https://github.com/django-notifications/django-notifications --pip install django-notifications-hq
# -- https://github.com/jarekwg/django-apscheduler  --pip install django-apscheduler
# -- https://github.com/jazzband/django-push-notifications  --pip install django-push-notifications
# -- https://github.com/jazzband/django-ical                --pip install django-ical


https://startbootstrap.com/snippets/login/


GIT:   
    rm -rf /var/showcase/
    mkdir /var/showcase
    cd /var/showcase
    git clone -b develop https://cheprasovstas:NQR4Cw6JwrVcJuM@github.com/cheprasovstas/showcase.git
GIT:  pull
    cd /var/showcase/showcase;
    git fetch origin develop;
    git pull origin develop;
    
GIT:  push
    cd /var/showcase/showcase;
    git push origin develop


virtualenv env

django commands start:
                cd /var/showcase;
                source ./env/bin/activate;
                cd /var/showcase/showcase/showcase/;
                python manage.py runserver 0.0.0.0:9000 &

                    env:
                        export SERVER_NAME=weekl-app.com;
                        export SERVER_PORT=9000;
                        export DATABASE_HOST=check-in.vps-cheprasov.host4g.ru;
                        export DATABASE_PORT=5432;
                        export DATABASE_USER=showcase;
                        export 'DATABASE_PASSWORD=!QW@1qw2';
                                                
                        set SERVER_NAME=weekl-app.com
                        set SERVER_PORT=9000
                        set DATABASE_HOST=check-in.vps-cheprasov.host4g.ru
                        set DATABASE_PORT=5432
                        set DATABASE_USER=showcase
                        set DATABASE_PASSWORD=!QW@1qw2
