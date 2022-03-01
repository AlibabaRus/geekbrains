import os

ROOT = os.path.dirname(__file__)
prog_n = 'my_project'
files = [os.path.join(prog_n, 'settings'), os.path.join(prog_n, 'mainapp'), os.path.join(prog_n, 'adminapp'), os.path.join(prog_n, 'authapp')]
for path in files:
    print(os.path.join(ROOT, path))
    os.makedirs(os.path.join(ROOT, path))