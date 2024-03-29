# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-02-03 10:17:17
"""
import arcpy
def #  NOT  IMPLEMENTED# Function Body not implemented

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    data = "data"
    result_2_ = "D:\\2021\\Demo\\Demo.gdb\\result"

    for I_data_Dissolve2_GUID, Value in #  NOT  IMPLEMENTED(data_Dissolve2_2_, [["GUID", ""]], False):

        # Process: Dissolve (Dissolve) (management)
        data_Dissolve3 = "D:\\2021\\Demo\\Demo.gdb\\data_Dissolve3"
        arcpy.management.Dissolve(in_features=data, out_feature_class=data_Dissolve3, dissolve_field=["Type"], statistics_fields=[], multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")

        # Process: Calculate Field (Calculate Field) (management)
        data_Dissolve2_2_ = arcpy.management.CalculateField(in_table=data_Dissolve3, field="GUID", expression="SequentialNumber()", expression_type="PYTHON3", code_block="""# Calculates a sequential number
# More calculator examples at esriurl.com/CalculatorExamples
rec=0
def SequentialNumber():
    global rec
    pStart = 1
    pInterval = 1
    if (rec == 0):
        rec = pStart
    else:
        rec = rec + pInterval
    return rec""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

        # Process: Aggregate Polygons (Aggregate Polygons) (cartography)
        Value = "2"
        I_data_Dissolve2_GUID_Aggreg_Value_ = fr"D:\2021\Demo\Demo.gdb\I_data_Dissolve2_GUID_Aggreg_{Value}"
        I_data_Dissolve2_GUID_Aggreg_Value_Tbl = fr"D:\2021\Demo\Demo.gdb\I_data_Dissolve2_GUID_Aggreg_{Value}_Tbl"
        arcpy.cartography.AggregatePolygons(in_features=I_data_Dissolve2_GUID, out_feature_class=I_data_Dissolve2_GUID_Aggreg_Value_, aggregation_distance="100 Kilometers", minimum_area="0 SquareMeters", minimum_hole_size="0 SquareMeters", orthogonality_option="NON_ORTHOGONAL", barrier_features=[], out_table=I_data_Dissolve2_GUID_Aggreg_Value_Tbl, aggregate_field="Type")

        # Process: Append (Append) (management)
        result = arcpy.management.Append(inputs=[I_data_Dissolve2_GUID_Aggreg_Value_], target=result_2_, schema_type="TEST", field_mapping="", subtype="", expression="")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"D:\2021\Demo\Demo.gdb", workspace=r"D:\2021\Demo\Demo.gdb"):
        Model()
