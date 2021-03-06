#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException


from .ttypes import *

myInt = 1337

name = "Mark Zuckerberg"

states = [
  {
    "San Diego" : 3211000,
    "Sacramento" : 479600,
    "SF" : 837400,
  },
  {
    "New York" : 8406000,
    "Albany" : 98400,
  },
]

x = 1

y = 1000000

z = 1e+09

instagram = Internship(**{
  "weeks" : 12,
  "title" : "Software Engineer",
  "employer" :   3,
})

kRanges = [
  Range(**{
    "min" : 1,
    "max" : 2,
  }),
  Range(**{
    "min" : 5,
    "max" : 6,
  }),
]

internList = [
  Internship(**{
    "weeks" : 12,
    "title" : "Software Engineer",
    "employer" :     3,
  }),
  Internship(**{
    "weeks" : 10,
    "title" : "Sales Intern",
    "employer" :     0,
  }),
]

apostrophe = "'"

tripleApostrophe = "'''"

quotationMark = "\""

backslash = "\\"

escaped_a = "\x61"

char2ascii = {
  "'" : 39,
  "\"" : 34,
  "\\" : 92,
  "\x61" : 97,
}

