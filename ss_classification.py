import arcpy
from arcpy import env  

env.workspace = r"C:/users/wfcla/Desktop/Classification_Automation/"  
env.overwriteOutput = True  
  
multipatch = arcpy.GetParameterAsText(0)

buildings = arcpy.CreateScratchName("building_footprints",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

slr1 = arcpy.GetParameterAsText(1)
slr2 = arcpy.GetParameterAsText(2)
slr3 = arcpy.GetParameterAsText(3)
slr4 = arcpy.GetParameterAsText(4)
slr5 = arcpy.GetParameterAsText(5)



cat_temp1 = arcpy.CreateScratchName("temp1",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp2 = arcpy.CreateScratchName("temp2",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp3 = arcpy.CreateScratchName("temp3",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp4 = arcpy.CreateScratchName("temp4",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp5 = arcpy.CreateScratchName("temp5",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)



arcpy.MultiPatchFootprint_3d(multipatch, buildings)

# Add field allbuildings_footprints 


arcpy.AddField_management(multipatch, "Category", "Double")
arcpy.AddField_management(buildings, "Category", "Double")


buildings_fields = ["FID", "Category"]

multipatch_fields = ["OBJECTID", "Category"]


arcpy.Intersect_analysis([buildings,cat5], cat_temp5) 

cur = arcpy.da.SearchCursor(cat_temp5, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '5'
		cur2.updateRow(row2)

arcpy.Intersect_analysis([buildings,cat4], cat_temp4) 


cur = arcpy.da.SearchCursor(cat_temp4, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '4'
		cur2.updateRow(row2)

arcpy.Intersect_analysis([buildings,cat3], cat_temp3) 

cur = arcpy.da.SearchCursor(cat_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '3'
		cur2.updateRow(row2)


arcpy.Intersect_analysis([buildings,cat2], cat_temp2) 

cur = arcpy.da.SearchCursor(cat_temp2, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '2'
		cur2.updateRow(row2)



arcpy.Intersect_analysis([buildings,cat1], cat_temp1) 

cur = arcpy.da.SearchCursor(cat_temp1, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '1'
		cur2.updateRow(row2)


cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = row[1]
		cur2.updateRow(row2)
