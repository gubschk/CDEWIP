import re

from chemdataextractor.doc import Paragraph
from chemdataextractor.model import Compound
from chemdataextractor.parse import I, Optional, R, W, merge
from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first

from custompropertymodel import BoilingPoint, MeltingPoint
from customregex import BpRegex, MpRegex


#example from github
class BpParser(BaseParser):
   
    root = BpRegex.bp

    def interpret(self, result, start, end):
        compound = Compound(
            boiling_points=[
                BoilingPoint(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound

        
# Melting Point parser
class MeltingPointParser(BaseParser):
    root = MpRegex.mp

    def interpret(self, result, start, end):
        compound = Compound(
            melting_points=[
                MeltingPoint(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound

Paragraph.parsers = [BpParser(), MeltingPointParser()]