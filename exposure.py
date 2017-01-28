import arcpy
from arcpy import env  

env.workspace = r"C:/users/wfcla/Desktop/Classification_Automation"  

env.overwriteOutput = True  
  
buildings = "allbuildings_footprints"

slr1 = "SLR1"
slr2 = "SLR2"
slr3 = "SLR3"
slr4 = "SLR4"
slr5 = "SLR5"

cat1 = "Cat1"
cat2 = "Cat2"
cat3 = "Cat3"
cat4 = "Cat4"
cat5 = "Cat5"

slr_temp1 = 'slr_temp1'
slr_temp2 = 'slr_temp2'
slr_temp3 = 'slr_temp3'
slr_temp4 = 'slr_temp4'
slr_temp5 = 'slr_temp5'

cat_temp1 = 'cat_temp1'
cat_temp2 = 'cat_temp2'
cat_temp3 = 'cat_temp3'
cat_temp4 = 'cat_temp4'
cat_temp5 = 'cat_temp5'

#arcpy.MultiPatchFootprint_3d('Allbuildings', 'Allbuildings_fp.shp') 

# Add field allbuildings_footprints 

arcpy.AddField_management(buildings, "Category", "Double")
arcpy.AddField_management(buildings, "SLR", "Double")  
arcpy.AddField_management(buildings, "SLRarea", "Double")
arcpy.AddField_management(buildings,"PerSLR3", "Double")

#start of slr and cat analysis for field classifcation of exposure

buildings_fields = ["FID", "SLR"]
temp_fields = ["FID_allbui"]

arcpy.Intersect_analysis([buildings,slr5], slr_temp5) 

cur = arcpy.da.SearchCursor(slr_temp5, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '5'
		cur2.updateRow(row2)

arcpy.Delete_management("slr_temp5")  

arcpy.Intersect_analysis([buildings,slr4], slr_temp4) 

cur = arcpy.da.SearchCursor(slr_temp4, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '4'
		cur2.updateRow(row2)

arcpy.Delete_management("slr_temp4")  

arcpy.Intersect_analysis([buildings,slr3], slr_temp3) 

cur = arcpy.da.SearchCursor(slr_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '3'
		cur2.updateRow(row2)

arcpy.Delete_management("slr_temp3")  

arcpy.Intersect_analysis([buildings,slr2], slr_temp2) 

cur = arcpy.da.SearchCursor(slr_temp2, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '2'
		cur2.updateRow(row2)

arcpy.Delete_management("slr_temp2")  

arcpy.Intersect_analysis([buildings,slr1], slr_temp1) 

cur = arcpy.da.SearchCursor(slr_temp1, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '1'
		cur2.updateRow(row2)

arcpy.Delete_management("slr_temp1")  



arcpy.Intersect_analysis([buildings,cat5], cat_temp5) 

cur = arcpy.da.SearchCursor(cat_temp5, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '5'
		cur2.updateRow(row2)

arcpy.Delete_management("cat_temp5")  



arcpy.Intersect_analysis([buildings,cat4], cat_temp4) 

cur = arcpy.da.SearchCursor(cat_temp4, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '4'
		cur2.updateRow(row2)

arcpy.Delete_management("cat_temp4")  


cur = arcpy.da.SearchCursor(cat_temp3, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '3'
		cur2.updateRow(row2)

arcpy.Delete_management("cat_temp3")  


arcpy.Intersect_analysis([buildings,cat2], cat_temp2) 

cur = arcpy.da.SearchCursor(cat_temp2, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '2'
		cur2.updateRow(row2)

arcpy.Intersect_analysis([buildings,cat3], cat_temp3) 

arcpy.Delete_management("cat_temp2")  

arcpy.Intersect_analysis([buildings,cat1], cat_temp1) 

cur = arcpy.da.SearchCursor(cat_temp1, temp_fields)
for row in cur:
	cur2 = arcpy.da.UpdateCursor(buildings, buildings_fields)
	for row2 in cur2:
		if row[0] == row2[0]:
			row2[1] = '1'
		cur2.updateRow(row2)


arcpy.Delete_management("cat_temp1")  

