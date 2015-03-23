# pylukinlib

General python functions, modules and blueprints used by me in different projects.

## The name pylukinlib?

Written in python, it's a library and I have nicked myself Arlukin. Figure out
the rest by yourself =)


## BUILD

# Start a virtualbox
vagrant up
vagrant ssh

# Test if it works
/vagrant/example/flask-login.py

# See: https://packaging.python.org/en/latest/distributing.html#requirements-for-packaging-and-distributing

cat >> ~/.pypirc << EOF
[distutils]
index-servers=pypi

[pypi]
repository: https://pypi.python.org/pypi
username: arlukin
EOF

cd /vagrant
source /usr/local/pythonenv/pylukinlib/bin/activate
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*