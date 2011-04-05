#! /usr/bin/env python -w all

# Programname  - Short Description
# by Lucis d.o.o.  <luka.marinko@lucis.si>
# 

# Template based on Ayman Hourieh's from 
# http://aymanh.com/python-debugging-techniques 
import logging
import optparse

LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG}

def main():
  parser = optparse.OptionParser()
  parser.add_option('-l', '--logging-level', help='Logging level')
  parser.add_option('-f', '--logging-file', help='Logging file name')
  (options, args) = parser.parse_args()
  logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)
  logging.basicConfig(level=logging_level, filename=options.logging_file,
                      format='%(asctime)s %(levelname)s: %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')

  # Your program goes here.
  # You can access command-line arguments using the args variable.

if __name__ == '__main__':
  main()
