from chemdataextractor.parse import R, I, W, Optional, merge
import re

class BpRegex: 
  prefix = (R(u'^b\.?p\.?$', re.I) | I(u'boiling') + I(u'point')).hide()#u-createsunicodestring
  units = (W(u'°') + Optional(R(u'^[CFK]\.?$')))(u'units').add_action(merge)
  value = R(u'^\d+(\.\d+)?$')(u'value')
  bp = (prefix + value + units)(u'bp')

class MpRegex: 
  prefix = (R(u'^b\.?p\.?$', re.I) | I(u'boiling') + I(u'point')).hide()#u-createsunicodestring
  units = (W(u'°') + Optional(R(u'^[CFK]\.?$')))(u'units').add_action(merge)
  value = R(u'^\d+(\.\d+)?$')(u'value')
  mp = (prefix + value + units)(u'bp')