import os

ROOT = os.path.dirname(__file__)
prog_n = 'templates'
files_1 = [os.path.join('settings', '__init__.py'), os.path.join('settings', 'dev.py'),
           os.path.join('settings', 'prod.py'),
           os.path.join('mainapp', 'views.py'),
           os.path.join('mainapp', '__init__.py'), os.path.join('mainapp', 'models.py'),
           os.path.join('mainapp', 'templates', 'mainapp', 'base.html'),
           os.path.join('mainapp', 'templates', 'mainapp', 'index.html'),
           os.path.join('authapp', 'views.py'),
           os.path.join('authapp', '__init__.py'), os.path.join('authapp', 'models.py'),
           os.path.join('authapp', 'views.py'),
           os.path.join('authapp', 'templates', 'authapp', 'base.html'),
           os.path.join('authapp', 'templates', 'authapp', 'index.html')]
for path in files_1:
    if path.split('.')[-1] == 'html':
        os.makedirs(os.path.join(ROOT, prog_n, path))
