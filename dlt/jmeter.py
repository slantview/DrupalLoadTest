"""
  Jmeter - A simple class for interacting with Jmeter.
  
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
import dlt

OPTIONS = {}

class Jmeter(object):
  def __init__(self):
    self.env = os.environ
    try:
      if (not self.env['JMETER_HOME']):
        if (os.access('/usr/bin/jmeter')):
          self.env['JMETER_HOME'] = '/usr'
        else:
          dlt.log('Unable to locate jmeter.  Please install jmeter or set JMETER_HOME to correct location.', dlt.LOG_ERROR)
    except Exception, e:
      print e
        
  def setOption(self, name, value = None):
    if name is not None and value is not None:
      OPTIONS[name] = value
    elif (name is not None):
      OPTIONS[name] = ''
  
  def run(self):
    args = []
    args.append(self.env['JMETER_HOME'] + '/bin/jmeter')
    for key in OPTIONS.keys():
      args.append('-' + key + '' + OPTIONS[key]);
    status = os.spawnv(os.P_WAIT, args[0], args)
    if status > 0:
      raise Error, "%s exited with code %d" % (args[0], status)
    elif status < 0:
      raise Error, "%s killed by signal %d" % (args[0], -status)
        
dlt.DrupalLoadTest.Jmeter = Jmeter