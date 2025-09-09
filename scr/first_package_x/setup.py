from setuptools import find_packages, setup

package_name = 'first_package_x'

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
    maintainer='ffons',
    maintainer_email='ffons@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node_1 = first_package_x.first_talker_node:main",
            "draw_circle_turtle = first_package_x.draw_circles_node:main",
            "pose_suscriber = first_package_x.pose_suscriber:main",
            "turtle_controller  = first_package_x.turtle_controller_node:main"
        ],
    },
)
