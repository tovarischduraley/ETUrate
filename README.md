# ETUrate #
University teachers rating system. 
Teacher can be rated by his own students!

## Technology stack ##

This project uses:
> Django + HTML CSS templates
> 
> Redis
> 
> Celery
> 
> PostgreSQL 
> 
> Docker
> 
> Nginx


## Run ##

Put your settings to `settings.py` file

1. Install dependencies
```bash
pip3 install -r requirements.txt
```
2. Make migration
```bash
./manage.py migrate
```

3. Start server
```bash
./manage.py runserver
```

4. Start redis
```bash
redis-server
```

5. Start celerybeat schedule
```bash
celery -A RT beat
```

6. Start celery worker
```bash
celery -A RT worker -l INFO --pool=solo
```

## Screenshots ##

![index](/screenshots/index_page.png?raw=true)

![cathedras](/screenshots/cathedras.png?raw=true)

![teachers](/screenshots/teachers.png?raw=true)

![teacher](/screenshots/teacher.png?raw=true)

![admin_panel](/screenshots/admin_panel.png?raw=true)

![cathedra_control](/screenshots/cathedra_control.png?raw=true)

![registration](/screenshots/registration.png?raw=true)

![login](/screenshots/login.png?raw=true)

![password_reset](/screenshots/password_reset.png?raw=true)