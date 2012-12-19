from logging import getLogger
log = getLogger(__name__)

import os
from pylons import c
from ckan import authz
from ckan import logic
from ckan.logic import NotAuthorized
from ckan.lib import base
from ckan.lib.base import _
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes, IConfigurer, IDatasetForm, IAuthFunctions, IActions

class DatahubSuomi(SingletonPlugin):
    #implements(IRoutes, inherit=True)
    implements(IConfigurer, inherit=True)
    #implements(IDatasetForm, inherit=True)
    #implements(IAuthFunctions, inherit=True)  
    #implements(IActions, inherit=True)
    
    
    def update_config(self, config):
        rootdir = os.path.dirname(__file__)
        our_public_dir = os.path.join(rootdir, 'public')
        template_dir = os.path.join(rootdir, 'templates')
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])
