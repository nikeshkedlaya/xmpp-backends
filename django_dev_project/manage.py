#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # so we can use xmpp_settings as if it were installed
    sys.path.insert(0, os.pardir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_dev_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
