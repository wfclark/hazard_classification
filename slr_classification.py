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


slr_temp1 = arcpy.CreateScratchName("temp1",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)
slr_temp2 = arcpy.CreateScratchName("temp2",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

slr_temp3 = arcpy.CreateScratchName("temp3",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

slr_temp4 = arcpy.CreateScratchName("temp4",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

slr_temp5 = arcpy.CreateScratchName("temp5",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp1 = arcpy.CreateScratchName("temp6",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp2 = arcpy.CreateScratchName("temp7",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp3 = arcpy.CreateScratchName("tem8",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp4 = arcpy.CreateScratchName("temp9",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

cat_temp5 = arcpy.CreateScratchName("temp10",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)


arcpy.MultiPatchFootprint_3d(multipatch, buildings)

# Add field allbuildings_footprints 



arcpy.AddField_management(multipatch, "SLR", "Double")  
arcpy.AddField_management(multipatch, "SLRarea", "Double")
arcpy.AddField_management(multipatch,"PerSLR3", "Double")
arcpy.AddField_management(multipatch,"area", "Double")




arcpy.AddField_management(buildings, "SLR", "Double")  
arcpy.AddField_management(buildings, "SLRarea", "Double")
arcpy.AddField_management(buildings,"PerSLR3", "Double")
arcpy.AddField_management(buildings,"area", "Double")





buildings_fields = ["FID", "SLR", "SLRarea", "PerSLR3", "Category", "Area"]

multipatch_fields = ["OBJECTID", "SLR", "SLRarea", "PerSLR3", "Category", "Area"]

temp_fields = ["FID_buildi", "SLRarea"]


#start of slr and cat analysis for field classifcation of exposure


with arcpy.da.UpdateCursor(buildings, ["SHAPE@AREA", "area"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

arcpy.Intersect_analysis([buildings, slr5], slr_temp5) 

cur = arcpy.da.SearchCursor(slr_temp5, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '5'
		cur2.updateRow(row2)

with arcpy.da.UpdateCursor(slr_temp5, ["SHAPE@AREA", "SLRarea"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

cur = arcpy.da.SearchCursor(slr_temp5, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[1]
		cur2.updateRow(row2)




arcpy.Intersect_analysis([buildings,slr4], slr_temp4) 

cur = arcpy.da.SearchCursor(slr_temp4, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '4'
		cur2.updateRow(row2)

with arcpy.da.UpdateCursor(slr_temp4, ["SHAPE@AREA", "SLRarea"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

cur = arcpy.da.SearchCursor(slr_temp4, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[1]
		cur2.updateRow(row2)



arcpy.Intersect_analysis([buildings,slr3], slr_temp3) 

cur = arcpy.da.SearchCursor(slr_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '3'
		cur2.updateRow(row2)

with arcpy.da.UpdateCursor(slr_temp3, ["SHAPE@AREA", "SLRarea"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)
        

cur = arcpy.da.SearchCursor(slr_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[1]
		cur2.updateRow(row2)


cur = arcpy.da.SearchCursor(slr_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[3] = row[1]/row2[5]
		cur2.updateRow(row2)



arcpy.Intersect_analysis([buildings,slr2], slr_temp2) 

cur = arcpy.da.SearchCursor(slr_temp2, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '2'
		cur2.updateRow(row2)


with arcpy.da.UpdateCursor(slr_temp2, ["SHAPE@AREA", "SLRarea"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)
        
cur = arcpy.da.SearchCursor(slr_temp2, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[1]
		cur2.updateRow(row2)


arcpy.Intersect_analysis([buildings,slr1], slr_temp1) 

cur = arcpy.da.SearchCursor(slr_temp1, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '1'
		cur2.updateRow(row2)


with arcpy.da.UpdateCursor(slr_temp1, ["SHAPE@AREA", "SLRarea"]) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)
        
cur = arcpy.da.SearchCursor(slr_temp1, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[1]
		cur2.updateRow(row2)
    
arcpy.Delete_management("temp1")
arcpy.Delete_management("temp2")  
arcpy.Delete_management("temp3")  
arcpy.Delete_management("temp4")  
arcpy.Delete_management("temp5")  


cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = row[1]
		cur2.updateRow(row2)

cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[2] = row[2]
		cur2.updateRow(row2)

cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[3] = row[3]
		cur2.updateRow(row2)

cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[4] = row[4]
		cur2.updateRow(row2)

cur = arcpy.da.SearchCursor(buildings, buildings_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(multipatch, multipatch_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[5] = row[5]
		cur2.updateRow(row2)

