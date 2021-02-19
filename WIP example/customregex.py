from chemdataextractor.parse import R, I, W, Optional, merge
import re


class Obstructions: #Class for bracket
  bracket = Optional(R(u'\('))
  curlLine = Optional(R(u'\~'))
  of =  Optional(W(u'of'))
  hyphen = Optional(R(u'\-'))
  all = bracket + curlLine + of + hyphen

class BpRegex: 
  prefix = (R(u'^b\.?p\.?$', re.I) | I(u'boiling') + I(u'point')).hide()#u-createsunicodestring
  units = (W(u'°') + Optional(R(u'^[CFK]\.?$')))(u'units').add_action(merge)
  value = R(u'^\d+(\.\d+)?$')(u'value')
  bp = (prefix + value + units)(u'bp')

class MpRegex: 
  prefix = (R(u'^m\.?p\.?$', re.I) | I(u'melting') + I(u'point')).hide()#u-createsunicodestring
  units = Optional(R(u'^[CFK]\.?$'))(u'units').add_action(merge)
  value = R(u'^\d+(\.\d+)?$')(u'value')
  mp = (prefix + Obstructions.all + value + units)(u'mp')
