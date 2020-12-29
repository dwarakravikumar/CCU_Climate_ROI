"""
This file determines the delta indices through a moment independent sensitivity analysis for the inventory 
items required to produce a CCU product. The delta index is determined for inventory item for 
every dataset in every CCU pathway. The inventory item with the highest delta index has the greatest 
influence on the climate ROI
Th comment below each print statement denotes the parameter number with the greatest delta index. 
The "Literature.xlsx" file contains the parameter names of the parameter numbers.
"""
import CO2_ROI_Constants

from CO2_ROI_Functions import f_get_delta_indices_concrete1,\
                              f_get_delta_indices_chemical1,\
                              f_get_delta_indices_mineralization_without_compressive_strength,\
                              f_get_delta_indices_mineralization_with_compressive_strength

hotspot_array_formic_acid_Catalytic_reduction_of_CO2_with_H2=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_formic_acid_Catalytic_reduction_of_CO2_with_H2)
15,17,19,19,15,15,17

hotspot_array_CO_Dry_Reforming=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.Dry_Reforming,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_CO_Dry_Reforming)
#12, 12, 12



hotspot_array_concrete_Mixing_OPC_plus_SCM = f_get_delta_indices_concrete1(\
                                       CO2_ROI_Constants.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants.dataset_category_Mixing_OPC_plus_SCM,\
                                       CO2_ROI_Constants.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_CCU_concrete_CO2_utilized)

print(hotspot_array_concrete_Mixing_OPC_plus_SCM)
#parameter (OPC) - 21 times


hotspot_array_formic_acid_Catalytic_reduction_of_CO2_with_H2_With_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_formic_acid_Catalytic_reduction_of_CO2_with_H2_With_EOC)
#15,17,19,19,15,15,17

hotspot_array_concrete_Mixing_OPC_only = f_get_delta_indices_concrete1(\
                                       CO2_ROI_Constants.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants.dataset_category_Mixing_OPC_only,\
                                       CO2_ROI_Constants.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_CCU_concrete_CO2_utilized)

print(hotspot_array_concrete_Mixing_OPC_only)
#parameter 1, 10 (OPC) - 8 times

hotspot_array_CO_reverseWater_Gas_Shift=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.reverseWater_Gas_Shift,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_CO_reverseWater_Gas_Shift)
#2, 2, 2, 2

hotspot_array_Methane_Hydrogenation_of_CO2=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.Methane,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_Methane_Hydrogenation_of_CO2)
#2, 2, 11, 2, 2, 11, 2, 2

hotspot_array_MeOH_Hydrogenation_of_CO2=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_MeOH_Hydrogenation_of_CO2)
#without EOC [47. 36. 47. 47.  1. 33.  4.  4. 15. 47.  1. 47. 47. 35. 47. 47.  3.  3. 3.  3. 47.  3.]
#with EOC [58. 59. 59. 59. 59. 59. 59. 59. 58. 59. 59. 59. 59. 59. 59. 59. 58. 58.58. 58. 59. 58.]

hotspot_array_concrete_Curing_OPC_only = f_get_delta_indices_concrete1(\
                                       CO2_ROI_Constants.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants.dataset_category_Curing_OPC_only,\
                                       CO2_ROI_Constants.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_CCU_concrete_CO2_utilized)

print(hotspot_array_concrete_Curing_OPC_only)
#parameter 1, 10 (OPC) - 17 times, parameter 18 (carbon curing) - 28 times

hotspot_array_concrete_Curing_OPC_plus_SCM = f_get_delta_indices_concrete1(\
                                       CO2_ROI_Constants.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants.dataset_category_Curing_OPC_plus_SCM,\
                                       CO2_ROI_Constants.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants.column_name_CCU_concrete_CO2_utilized)

print(hotspot_array_concrete_Curing_OPC_plus_SCM)
#parameter 5,15 (SCM) - 15 times

hotspot_array_DME_NA=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.DME,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_DME_NA)
#13,37,13

hotspot_array_DMC_Ethylene_carbonate_transesterification=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Ethylene_carbonate_transesterification,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_DMC_Ethylene_carbonate_transesterification)
#17

hotspot_array_CO_reverseWater_Gas_Shift_with_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.reverseWater_Gas_Shift,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_CO_reverseWater_Gas_Shift_with_EOC)
#12, 12, 12, 12

hotspot_array_Polyol_NA=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.polyol,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_polyol_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_polyol_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_Polyol_NA)
#26, 26, 26
#
hotspot_array_formic_acid_Electrolytic_reduction_of_CO2=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_formic_acid_Electrolytic_reduction_of_CO2)
#without EOC 17,17,17,15,15,15,15,17,17,17,17,17,17
#With EOC [17. 17. 59. 15. 15. 15. 15. 17. 17. 59. 59. 59. 59.]

hotspot_array_MeOH_Hydrogenation_of_CO2_with_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_MeOH_Hydrogenation_of_CO2_with_EOC)
#2, 11, 11, 11, 11, 11, 11, 11, 2, 11, 11, 11, 11, 11, 11, 11, 2, 2, 2, 2, 11, 2

hotspot_array_Methane_Hydrogenation_of_CO2_with_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.Methane,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_Methane_Hydrogenation_of_CO2_with_EOC)
#2, 2, 11, 2, 2, 11, 2, 2

hotspot_array_formic_acid_Electrolytic_reduction_of_CO2_with_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_formic_acid_Electrolytic_reduction_of_CO2_with_EOC)
#17,17,17,15,15,15,15,17,17,17,17,17,17

hotspot_array_kerosene_NA=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.Kerosene,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_kerosene_NA)
#17

hotspot_array_DMC_Urea_transesterification=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Urea_transesterification,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_DMC_Urea_transesterification)
#17

hotspot_array_DMC_Electrochemical_reduction_of_CO2_with_MeOH=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Electrochemical_reduction_of_CO2_with_MeOH,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_DMC_Electrochemical_reduction_of_CO2_with_MeOH)
#17,17

 

hotspot_array_MeOH_Electrolytic_reduction_of_CO2=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_No)
print(hotspot_array_MeOH_Electrolytic_reduction_of_CO2)
#17

hotspot_array_MeOH_Electrolytic_reduction_of_CO2_with_EOC=f_get_delta_indices_chemical1(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution,\
                                        CO2_ROI_Constants.EOC_Yes)
print(hotspot_array_MeOH_Electrolytic_reduction_of_CO2_with_EOC)
#17

#Delta Indices for mineralization. CO2 used for curing, WITHOUT compressive strength
f_get_delta_indices_mineralization_without_compressive_strength(CO2_ROI_Constants.excel_sheet_name_mineralization_without_compressive_strength_CO2,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_CO2_utilized,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_CO2_utilized)
#[ 1.  1.  1.  5. 17.  9.  5.]


#Delta Indices for mineralization. Flue gas used for curing, WITHOUT compressive strength
f_get_delta_indices_mineralization_without_compressive_strength(\
                                       CO2_ROI_Constants.excel_sheet_name_mineralization_without_compressive_strength_flue_gas,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_CO2_utilized,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_CO2_utilized)    
#[ 5. 13.  5. 13.  5.  5.  5.  5.  5.  5.  5. 13. 15. 15.]  

#Delta Indices for mineralization. WITH compressive strength
f_get_delta_indices_mineralization_with_compressive_strength(CO2_ROI_Constants.excel_sheet_name_mineralization_with_compressive_strength,\
                                        CO2_ROI_Constants.column_name_conventional_mineralization_with_compressive_strength_first_input_parameter,\
                                        CO2_ROI_Constants.column_name_conventional_mineralization_with_compressive_strength_last_input_parameter,\
                                        CO2_ROI_Constants.column_name_conventional_mineralization_with_compressive_strength_CO2_utilized,\
                                        CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_LB,\
                                        CO2_ROI_Constants.column_name_conventional_Compressive_strength_range_UB,\
                                        CO2_ROI_Constants.column_name_CCU_mineralization_with_compressive_strength_first_input_parameter,\
                                        CO2_ROI_Constants.column_name_CCU_mineralization_with_compressive_strength_last_input_parameter,\
                                        CO2_ROI_Constants.column_name_CCU_mineralization_with_compressive_strength_CO2_utilized,\
                                        CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_LB,\
                                        CO2_ROI_Constants.column_name_CCU_Compressive_strength_range_UB)
#[25. 25. 25. 25. 25.]











