#!/usr/bin/python3.1

import google.scholar
import unittest

class ScholarTest(unittest.TestCase):
  def test(self):
    engine = google.scholar.Engine("A. Einstein", 10, 3)
    print(engine)
    
    print("pages:")
    numPages = 0
    for page in engine:
      print(page[0:30])
      numPages += 1
    self.assertEqual(numPages, 3)  
    
    
unittest.main()
      
      
    
