import clr
# Import Revit API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
# Import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


levels = []
builtInParam = BuiltInParameter.LEVEL_PARAM

for f in UnwrapElement(IN[0]):
	lv = f.get_Parameter(builtInParam).AsElementId()
	for l in UnwrapElement(IN[1]):
		if(l.Id == lv):
			levels.append(l.Name)

OUT = levels