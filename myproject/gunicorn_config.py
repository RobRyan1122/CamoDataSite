# gunicorn_config.py

# Bind to all IP addresses on port 8000
bind = '0.0.0.0:8000'

# Number of worker processes
workers = 3

# Worker class (you can use 'gevent' for async workers if needed)
worker_class = 'sync'

# Access log file location
accesslog = '/var/log/gunicorn/access.log'

# Error log file location
errorlog = '/var/log/gunicorn/error.log'

# Daemonize the Gunicorn process (background mode)
daemon = False
