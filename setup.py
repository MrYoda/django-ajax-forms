from setuptools import setup, find_packages

setup(
    name='django-ajax-forms',
    version='0.0.2',
    description='Provides support for doing validation using Ajax(currently with jQuery) using your existing Django forms.',
    author='Jonas Geiregat',
    author_email='jonas@geiregat.org',
    url='https://github.com/jonasgeiregat/django-ajax-forms',
    packages=[
            'ajax_forms',
            'ajax_forms.templatetags',
        ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    # Tells setuptools to download setuptools_git before running setup.py so
    # it can find the data files under Git version control.
    setup_requires=['setuptools_git', 'django'],
    zip_safe=False,
)
