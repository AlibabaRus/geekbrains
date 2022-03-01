import os

ROOT = os.path.dirname(__file__)
prog_n = 'my_project'
files_1 = [os.path.join(prog_n, 'settings', '__init__.py'), os.path.join(prog_n, 'settings', 'dev.py'),
           os.path.join(prog_n, 'settings', 'prod.py'),
           os.path.join(prog_n, 'mainapp', 'views.py'),
           os.path.join(prog_n, 'mainapp', '__init__.py'), os.path.join(prog_n, 'mainapp', 'models.py'),
           os.path.join(prog_n, 'mainapp', 'templates', 'mainapp', 'base.html'),
           os.path.join(prog_n, 'mainapp', 'templates', 'mainapp', 'index.html'),
           os.path.join(prog_n, 'authapp', 'views.py'),
           os.path.join(prog_n, 'authapp', '__init__.py'), os.path.join(prog_n, 'authapp', 'models.py'),
           os.path.join(prog_n, 'authapp', 'views.py'),
           os.path.join(prog_n, 'authapp', 'templates', 'authapp', 'base.html'),
           os.path.join(prog_n, 'authapp', 'templates', 'authapp', 'index.html')]
for path in files_1:
    os.makedirs(os.path.join(ROOT, path))