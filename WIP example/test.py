from chemdataextractor import Document
from chemdataextractor.model import Compound
from chemdataextractor.doc import Heading
from customparser import Paragraph

#boiling point test 
d = Document(
    Heading(u'Synthesis of 2,4,6-trinitrotoluene (3a)'),
    Paragraph(u'The procedure was followed to yield a pale yellow solid (b.p. 240 °C)')
)
print("boiling point: ")
print(d.records.serialize())

#melting point test 
m = Document(
    Heading(u'Metal–organic frameworks: Molten MOFs'),
    Paragraph(u'When crystalline ZIF-4 is heated above its melting point 865 K and then cooled to room temperature, a melt-quenched glass is obtained.'),
    Paragraph(u'When crystalline ZIF-4 is heated above its melting point (866 K) and then cooled to room temperature, a melt-quenched glass is obtained.'),
    Paragraph(u'When crystalline ZIF-4 is heated above its (m.p. 867 K) and then cooled to room temperature, a melt-quenched glass is obtained.'),
    Paragraph(u'When crystalline ZIF-4 is heated above its (m.p. 868 K) and then cooled to room temperature, a melt-quenched glass is obtained.'), # of
    Paragraph(u'When crystalline ZIF-4 is heated above melting point (~869 K) and then cooled to room temperature, a melt-quenched glass is obtained.'), # ~
    Paragraph(u'When crystalline ZIF-4 is heated above its (m.p. - 870 K) and then cooled to room temperature, a melt-quenched glass is obtained.') # -
)
print("melting point: ")
print(m.records.serialize())
