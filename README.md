# Basic Django Celery Example

To try this out, follow these steps.

- Clone the repository and change directory into the cloned directory:

```bash
git clone git@github.com:stuartmaxwell/django-celery-example.git
cd django-celery-example
```

- Before you start, you'll need a Redis server. If you don't have one the easiest way is through Docker with the following command:

```bash
docker run --name my-redis-server -d -p 127.0.0.1:6379:6379 redis
```

- Create a virtual environment and activate it.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install the project requirements:

```bash
pip install .
```

- Add some email configuration to the `settings.py` file. I use Amazon SES but substitute with our own SMTP settings.

```python
# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = ""  # add your own settings here
EMAIL_PORT = ""  # add your own settings here
EMAIL_HOST_USER = ""  # add your own settings here
EMAIL_HOST_PASSWORD = ""  # add your own settings here
EMAIL_USE_TLS = True  # add your own settings here
DEFAULT_FROM_EMAIL = "you@example.com"  # your email address
```

- Run the database migrations and run the test server:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

- Then in a second terminal window, navigate to your project directory, activate the virtual environment again, and then launch the Celery process - it should print out some debug information and then a `ready` message to indicate it has connected to Redis successfully and is waiting for tasks:

```bash
python3 -m celery -A celery_project worker -l info -P solo
```

- Browse to <http://127.0.0.1:8000> and you should see a contact form. Try sending a message to see if it works.

- Switch back to your terminal windows with the Celery process and you'll see some updates. It can take several seconds to send the email, but that was all done by the celery process and didn't affect the page loading time after submitting the form.
