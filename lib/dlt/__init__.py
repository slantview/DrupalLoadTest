"""
  dlt.__init__ - File for defining complete package listing.
  
  == BEGIN LICENSE ==

  Licensed under the terms of any of the following licenses at your
  choice:

   - GNU General Public License Version 2 or later (the "GPL")
     http://www.gnu.org/licenses/gpl.html

   - GNU Lesser General Public License Version 2.1 or later (the "LGPL")
     http://www.gnu.org/licenses/lgpl.html

  == END LICENSE ==
"""
import os, sys

LOG_NOTICE = 'notice'
LOG_WARN = 'warning'
LOG_ERROR = 'error'

class DrupalLoadTest(object):
  def __init__(self, options = {}):
    self.config = self.Config()
    self.graph = self.Graph()
    self.jmeter = self.Jmeter()
    
def log(msg, status = 'error'):
  print >>sys.stderr, "%s[%s]: %s" % (os.path.basename(sys.argv[0]), status, msg)
    
import dlt.config, dlt.graph, dlt.jmeter