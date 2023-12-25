#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import importlib.util
import os
import sys

from django.core.exceptions import ImproperlyConfigured


def main():
    """Run administrative tasks."""
    django_env = os.environ.get('DJANGO_ENV', 'local')
    
    # check if the current environments settings module exists
    env_settings_module = f'pybox.settings.{django_env}'
    env_settings_module_found = importlib.util.find_spec(env_settings_module) is not None
    
    if env_settings_module_found:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', env_settings_module)
    else:
        raise ImproperlyConfigured(
            f'Could not find settings module {env_settings_module}'
        )
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
