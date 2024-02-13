from setuptools import setup

package_name = 'pf3400_motion_control_example'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dmitrii Gusev',
    maintainer_email='dmitrii@industrialnext.ai',
    description='ROS2 version of the original PF3400 ROS1 package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example = pf3400_motion_control_example.example:main'
        ],
    },
)
