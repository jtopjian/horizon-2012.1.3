# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Openstack, LLC
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import horizon


class Settings(horizon.Dashboard):
    name = _("Settings")
    slug = "settings"
    try:
        juju_panel = getattr(settings, 'ENABLE_JUJU_PANEL')
        if juju_panel == True:
            panels = ('user', 'project', 'ec2', 'juju')
        else:
            panels = ('user', 'project', 'ec2')
    except AttributeError:
            panels = ('user', 'project', 'ec2')

    default_panel = 'user'
    nav = False


horizon.register(Settings)
