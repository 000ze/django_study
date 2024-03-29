#!/usr/bin/env python
import os
import sys
              #manage.py：一个命令行实用程序，可以让您以各种方式与此 Django 项目进行交互。你可以阅读所有的细节 manage.py 在 Django 的管理和 manage.py。
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
