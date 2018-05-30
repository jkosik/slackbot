ansible-py2-bootstrap
=========

This role is meant for installation of python2 on OS which doesn't ship with python2 by default (Ubuntu 16.04 Xenial and alikes).

This role will phase out once ansible supports python3.

Requirements
------------

The role assumes a Linux/Unix enviroment where `sudo` is installed and configured.

Make sure `gather_facts` is set to `no` in your playbook (default is `yes`).

Role Variables
--------------

There is no variable to be set.

Dependencies
------------

No dependencies

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

<pre>
    - hosts: servers
      become: yes
      gather_facts: no
      roles:
        - { role: ansible-py2-bootstrap, tags: [ "py2-bootstrap"] }
</pre>

`become: yes` is optional, since  all tasks are prefixed with `sudo`
`tags` is, of course, optional.

