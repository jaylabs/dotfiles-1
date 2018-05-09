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
module: vscode
short_description: Manage Visual Studio Code extensions
description:
  - Manage Visual Studio Code extensions
version_added: 1.6
options:
  name:
    description:
      - The name of the extension to install
    required: true
  executable:
    description:
      - The executable location for code (vscode).
      - This is useful if vscode is not in the PATH.
    required: false
  state:
    description:
      - The state of the vscode
    required: false
    default: present
    choices: [ "present", "absent" ]
'''

EXAMPLES = '''
description: Install "donjayamanne.python" vscode extension.
- vscode: name=donjayamanne.python state=present

description: Remove the package "donjayamanne.python".
- vscode: name=donjayamanne.python state=absent
'''

import os

class Vscode(object):
    def __init__(self, module, **kwargs):
        self.module = module
        self.name = kwargs['name']

        if kwargs['executable']:
            self.executable = kwargs['executable']
        else:
            self.executable = module.get_bin_path('code', True)

    def _exec(self, args, run_in_check_mode=False, check_rc=True):
        if not self.module.check_mode or (self.module.check_mode and run_in_check_mode):
            cmd = [self.executable] + args
            if self.name:
                cmd.append(self.name)
            rc, out, err = self.module.run_command(cmd, check_rc=check_rc)
            return out
        return ''

    def list(self):
        cmd = ['--list-extensions']

        installed = list()
        missing = list()
        data = self._exec(cmd, True, False)
        for dep in data.splitlines():
            dep = dep.strip()
            if dep:
                installed.append(dep)
        if self.name not in installed:
            missing.append(self.name)

        return installed, missing

    def install(self):
        return self._exec(['--install-extension'])

    def uninstall(self):
        return self._exec(['--uninstall-extension'])


def main():
    arg_spec = dict(
        name=dict(default=None),
        version=dict(default=None),
        executable=dict(default=None),
        state=dict(default='present', choices=['present', 'absent'])
    )
    module = AnsibleModule(
        argument_spec=arg_spec,
        supports_check_mode=True
    )

    name = module.params['name']
    executable = module.params['executable']
    state = module.params['state']

    if not name:
        module.fail_json(msg='name must be specified')

    vscode = Vscode(module, name=name, executable=executable)

    changed = False
    if state == 'present':
        installed, missing = vscode.list()
        if len(missing):
            changed = True
            vscode.install()
    else: #absent
        installed, missing = vscode.list()
        if name in installed:
            changed = True
            vscode.uninstall()

    module.exit_json(changed=changed)

# import module snippets
from ansible.module_utils.basic import *
main()
