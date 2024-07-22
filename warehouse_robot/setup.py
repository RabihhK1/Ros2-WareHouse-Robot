from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'warehouse_robot'

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
    maintainer='rabih',
    maintainer_email='rabih.h.kiwan@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stock_checker_server = warehouse_robot.stock_checker_server:main',
            'deliver_item_client = warehouse_robot.deliver_item_client:main',
       ],
    },
)