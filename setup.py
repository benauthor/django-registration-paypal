from distutils.core import setup

setup(
        name="django-registration-paypal",
        version="0.1.0",
        author="Dusty Phillips",
        author_email="dusty@archlinux.ca",
        packages=['paypal_registration'],
        url="",
        license="LICENSE.txt",
        description="django-registration backend to support paypal payments",
        long_description=open('README.txt').read(),
)
