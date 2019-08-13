=====
Converter
=====

Quick start
-----------

1. Add "converter" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'converter',
    ]

2. Include the converter URLconf in your project urls.py like this::

    path('converter/', include('converter.urls')),

3. Run `python manage.py migrate` to create the converter models.

4. Start the development server and visit http://127.0.0.1:8000/admin/