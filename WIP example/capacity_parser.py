# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:07:39 2021

@author: Kristian
"""
from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.doc import Paragraph, Heading



#u in front of the string indicates that a unicode string is to be created
#We think the unicode is for symbols like the degree since it may not be recognized ASCII
d = Document(
    Heading(u'Synthesis of HKUST-1-AC'),
    Paragraph(u'The BET surface area and CO2 uptake capacity values for the HKUST-1–AC composite were 1381 m2 g−1 and 8.1 mmol g−1 (at 273 K and 1 bar), respectively, representing increases of 70% and 39%, respectively, over the reported values for HKUST-1')
)


from chemdataextractor.model import BaseModel, StringType, ListType, ModelType
import re
from chemdataextractor.parse import R, I, W, Optional, merge

class Capacity(BaseModel):
    value = StringType()
    units = StringType()
    
Compound.capacity = ListType(ModelType(Capacity))

prefix = (I(u'capacity') | I(u'CO2') + I(u'uptake')).hide()
#Left the optional in because if I take it out then there is a syntax error on line 33
units = (W(u'mmol g-1') + Optional(R(u'^[CFK]\.?$')))(u'units').add_action(merge)
value = R(u'^\d+(\.\d+)?$')(u'value')

cp = (prefix + value + units)(u'cp')


from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first

class CpParser(BaseParser):
    root = cp
    
    def interpret(self, result, start, end):
        compound = Compound(
            capacity=[
                Capacity(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound

Paragraph.parsers = [CpParser()]

print(d.records.serialize())
#It does not work...