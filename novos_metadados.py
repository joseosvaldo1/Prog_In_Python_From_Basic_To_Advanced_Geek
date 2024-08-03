"""
Novos Recursos em Python:



"""

from importlib import metadata

# print(metadata.version('pip'))  # => 24.1.2

metadata_pip = metadata.metadata('pip')

print(list(metadata_pip))  # ['Metadata-Version', 'Name',
# 'Version', 'Summary', 'Author-email', 'License',
# 'Project-URL', 'Project-URL', 'Project-URL', 'Project-URL',
# 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
# 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
# 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python',
# 'Description-Content-Type', 'License-File', 'License-File', 'Description']

print(15*'-')

print(metadata_pip)

print(15*'-')

print(metadata_pip['Project-URL'])  # => Homepage, https://pip.pypa.io/
print(metadata_pip['Description-Content-Type'])  # => text/x-rst
print(metadata_pip['License'])  # => MIT

print(15*'-')

print(len(metadata.files('pip')))  # => 874

print(15*'-')

print(metadata.requires('pip'))  # => None

print(15*'-')

print(metadata.requires('django'))  # => ['asgiref <4,>=3.7.0',
# 'sqlparse >=0.3.1', 'tzdata ; sys_platform == "win32"',
# "argon2-cffi >=19.1.0 ; extra == 'argon2'", "bcrypt ;
# extra == 'bcrypt'"]

print(15*'-')

