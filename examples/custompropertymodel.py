from chemdataextractor.model import BaseModel, StringType, ListType, ModelType
from chemdataextractor.model import Compound

class BoilingPoint(BaseModel):
    value = StringType()
    units = StringType()
    
Compound.boiling_points = ListType(ModelType(BoilingPoint))

class MeltingPoint(BaseModel):
    value = StringType()
    units = StringType()
    
Compound.melting_points = ListType(ModelType(MeltingPoint))