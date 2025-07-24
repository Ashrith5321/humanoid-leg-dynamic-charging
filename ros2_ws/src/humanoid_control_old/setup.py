from setuptools import setup, find_packages

package_name = 'humanoid_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),  # <--- this line is important
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ashrith Edukulla',
    maintainer_email='eashrith@gmail.com',
    description='ROS 2 package for humanoid leg control',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_leg = humanoid_control.scripts.move_leg_node:main',
        ],
    },
    include_package_data=True,
)

