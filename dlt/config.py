"""
  dlt.config - File for managing config for DrupalLoadTest.
  
  == BEGIN LICENSE ==

  Licensed under the terms of any of the following licenses at your
  choice:

   - GNU General Public License Version 2 or later (the "GPL")
     http://www.gnu.org/licenses/gpl.html

   - GNU Lesser General Public License Version 2.1 or later (the "LGPL")
     http://www.gnu.org/licenses/lgpl.html

  == END LICENSE ==
"""
import os
import sys
import ConfigParser
import dlt

# Our config file
CONFIG_FILE = os.getcwd() + '/config.cfg'

# Default configuration options.
CONFIG = {
  'Application': {},
  'Drupal': {}
}

class Config(object):
  def __init__(self):
    self.load()
    
  def load(self):
    """ Get the config file options and set them to the global config array. """
    
    cp = ConfigParser.ConfigParser()
    cp.readfp(open(CONFIG_FILE))

    CONFIG['Application']['host'] = cp.get('Application', 'host')
    CONFIG['Application']['port'] = cp.get('Application', 'port')
    CONFIG['Application']['max_threads'] = cp.get('Application', 'max_threads')
    CONFIG['Application']['jmx_file'] = cp.get('Application', 'jmx_file')
    CONFIG['Drupal']['user'] = cp.get('Drupal', 'user')
    CONFIG['Drupal']['pass'] = cp.get('Drupal', 'pass')
    CONFIG['Drupal']['base_path'] = cp.get('Drupal', 'base_path')
    
  def get(self):
    return CONFIG
    
dlt.DrupalLoadTest.Config = Config