# import os
# os.makedirs('python1.4/glance/api')
# os.makedirs('python1.4/glance/cmd')
# os.makedirs('python1.4/glance/db')
# l=[]
# l.append(open('python1.4/glance/__init__.py', 'w'))
# l.append(open('python1.4/glance/api/__init__.py', 'w'))
# l.append(open('python1.4/glance/api/policy.py', 'w'))
# l.append(open('python1.4/glance/api/versions.py', 'w'))
# l.append(open('python1.4/glance/cmd/__init__.py', 'w'))
# l.append(open('python1.4/glance/cmd/manage.py', 'w'))
# l.append(open('python1.4/glance/db/__init__.py', 'w'))
# l.append(open('python1.4/glance/db/models.py', 'w'))
# map(lambda f:f.close(),l)
#可以导入glance这个包
# import glance   #在导入这个包的时候.默认执行的是这个包下的__init__.py
# import glance.api.policy
# glance.api.policy.get()
#这种方案是我们使用包使用最多的
# from glance.api import policy
# policy.get()


#错误示范     #在使用from这种形式的导包.import后面不允许出现
# from glance import api.policy
# # api.policy.get()
from ..cmd import manage
from glance.api import policy
policy.get()