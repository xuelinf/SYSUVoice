from django.conf.urls import patterns, url


urlpatterns = patterns(
    'panel.views',
    url(r'^$', 'index', name='index'),
    url(r'^user/all/$', 'user_manage', name="user_manage"),
    url(r'^user/(?P<uid>\d+)/edit/$', 'user_edit', name="user_edit"),
    url(r'^user/all/data-ss/$', 'user_table_ss', name="user_table_ss"),

    url(r'^node/all/$', 'node_manage', name="node_manage"),
    url(r'^node/create/$', 'node_create', name="node_create"),
    url(r'^node/all/data-ss/$', 'node_table_ss', name="node_table_ss"),
    url(r'^node/(?P<node_id>\d+)/edit/$', 'node_edit', name="node_edit"),

    # classify
    url(r'^classify/create/$', 'classify_create', name="classify_create"),
    url(r'^classify/all/$', 'classify_manage', name="classify_manage"),
    url(r'^classify/all/data-ss/$', 'classify_table_ss',
        name="classify_table_ss"),

    url(r'^topic/all/$', 'topic_manage', name="topic_manage"),
    url(r'^topic/all/data-ss/$', 'topic_table_ss', name="topic_table_ss"),
    url(r'^topic/(?P<topic_id>\d+)/$', 'topic_edit', name="topic_edit"),

    url(r'^ajax/node/$', 'node_title_ajax', name="node_title_ajax"),
    url(r'^ajax/topic/bulk-delete/$', 'topic_bulk_delete',
        name="topic_bulk_delete"),
    url(r'^ajax/node/bulk-delete/$', 'node_bulk_delete',
        name="node_bulk_delete"),
    url(r'^ajax/classify/bulk-delete/$', 'classify_bulk_delete',
        name="classify_bulk_delete"),
    url(r'^edit/success/$', 'edit_success', name="edit_success"),
)
