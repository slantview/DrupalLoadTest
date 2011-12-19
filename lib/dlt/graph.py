"""
  Graph - A simple class for creating graph output from the DrupalLoadTest.
  
  == BEGIN LICENSE ==

  Licensed under the terms of any of the following licenses at your
  choice:

   - GNU General Public License Version 2 or later (the "GPL")
     http://www.gnu.org/licenses/gpl.html

   - GNU Lesser General Public License Version 2.1 or later (the "LGPL")
     http://www.gnu.org/licenses/lgpl.html

  == END LICENSE ==
"""
import dlt

class Graph(object):
  def __init__(self):
    x = 1
    
dlt.DrupalLoadTest.Graph = Graph