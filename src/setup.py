from setuptools import setup
import setup_translate

pkg = 'Extensions.XPower'
setup(name='enigma2-plugin-extensions-xpower',
       version='1.59',
       description='remote PC power management for Win and linux',
       package_dir={pkg: 'XPower'},
       packages=[pkg],
       package_data={pkg: ['img/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
