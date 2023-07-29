from setuptools import setup

setup(
    name="setup",
    version="2.3.0",
    description="Flask app template",
    author="Khoa",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["flask_singer_tap"],
    install_requires=[
        "requests==2.28.2",
        "Flask==2.3.0",
        "flask_sqlalchemy",
        "jsonpickle",
        "python-dotenv",
        "flask-restful",
        "jsonpickle",
        "celery==5.2.7",
        "flask_migrate",
        "psycopg2",
        "flask_security",
        "flask_socketio",
        "flask_bcrypt"
    ],
    extras_require={
        "test": [
            "pylint==2.13.4",
            "nose"
        ],
        "dev": [
            "ipdb"
        ]
    },
    # entry_points="""
    # [console_scripts]
    # tap-tiktok-ads=tap_tiktok_ads:main
    # """,
    # packages=["tap_tiktok_ads"],
    # package_data = {
    #     "schemas": ["tap_tiktok_ads/schemas/*.json"]
    # },
    # include_package_data=True,
)