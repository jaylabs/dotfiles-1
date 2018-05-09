#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: vagrant_plugin
short_description: Manage vagrat plugins
description:
  - Manage vagrant plugins
version_added: 1.9
options:
  name:
    description:
      - The name of a vagrant plugin to install
    required: true
  version:
    description:
      - The version to be installed
    required: false
  executable:
    description:
      - The executable location for vagrant.
      - This is useful if vagrant is not in the PATH.
    required: false
  state:
    description:
      - The state of the vagrant plugin
    required: false
    default: present
    choices: [ "present", "absent", "latest" ]
'''

EXAMPLES = '''
description: Install "sahara" vagrant plugin.
- vagrant_plugin: name=sahara state=present

description: Update the plugin "sahara" to the latest version.
- vagrant_plugin: name=sahara state=latest

description: Remove the plugin "sahara".
- vagrant_plugin: name=sahara state=absent
'''

import re


class VagrantPlugin(object):
    def __init__(self, module, **kwargs):
        self.module = module
        self.name = kwargs['name']
        self.version = None

        if kwargs['version']:
            self.version = kwargs['version']

        if kwargs['executable']:
            self.executable = kwargs['executable']
        else:
            self.executable = module.get_bin_path('vagrant', True)


    def _exec(self, args, check_rc=True, append_name=True):
        if self.module.check_mode:
            return ''

        cmd = [self.executable, 'plugin'] + args
        if self.name and append_name:
            cmd.append(self.name)
        rc, out, err = self.module.run_command(cmd, check_rc=check_rc)
        return out

    def list(self):
        cmd = ['list']

        installed = dict()
        data = self._exec(cmd, check_rc=False, append_name=False)
        pattern = re.compile(r'^(\S+) +\((\S+)(?:\, +\S+)?\)')
        for dep in data.splitlines():
            m = pattern.match(dep)
            if m:
                installed[m.group(1)] = m.group(2)

        return installed

    def install(self):
        args = ['install']
        if self.version is not None:
            args.append('--plugin-version')
            args.append(self.version)
        return self._exec(args)

    def update(self):
        return self._exec(['update'])

    def uninstall(self):
        return self._exec(['uninstall'])


def main():
    arg_spec = dict(
        name=dict(default=None),
        version=dict(default=None),
        executable=dict(default=None),
        state=dict(default='present', choices=['present', 'absent', 'latest'])
    )
    module = AnsibleModule(
        argument_spec=arg_spec,
        supports_check_mode=True
    )

    name = module.params['name']
    version = module.params['version']
    executable = module.params['executable']
    state = module.params['state']

    if not name:
        module.fail_json(msg='name must be specified')

    apm = VagrantPlugin(
        module,
        name=name,
        version=version,
        executable=executable,
    )

    changed = False
    if state == 'present':
        installed = apm.list()
        if name not in installed:
            changed = True
            apm.install()
    elif state == 'latest':
        installed = apm.list()
        apm.version = None
        changed = True
        apm.install()
    else:
        installed = apm.list()
        if name in installed:
            changed = True
            apm.uninstall()

    module.exit_json(changed=changed)

# import module snippets
from ansible.module_utils.basic import *
main()
