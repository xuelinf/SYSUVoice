# encoding=utf-8

from account.models import profile
from forum.models import node, topic, post
import os
sitename = u'SYSUBBS'


links = {}
nodes = node.objects.all()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_PATH = os.path.join(BASE_DIR, 'static/upload')
user_count = profile.objects.count()
topic_count = topic.objects.filter(deleted=False).count()
post_count = post.objects.filter(deleted=False).count()

site_off = False
