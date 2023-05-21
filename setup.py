from setuptools import find_packages, setup

package_name = 'test_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shenoy',
    maintainer_email='shenoy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest', 'unittest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
