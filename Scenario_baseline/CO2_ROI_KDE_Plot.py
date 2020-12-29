'''
This Python file accompanies the manuscript titled 
“Assessing the Relative Climate Impact of Carbon dioxide Utilization for Concrete, Chemical and Mineral Production” 
authored by Dr. Dwarakanath Ravikumar, Dr. Gregory Keoleian, Dr. Shelie Miller and Dr. Volker Sick.

This file contains code to generate and plot the distribution for the climate ROI for the CCU pathways in 
Figure 3 in the main manuscript. The climate ROI in the Figure 3 between -15 to +15

@author: Dwarakanath Ravikumar
'''
import CO2_ROI_Constants
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
from CO2_ROI_Functions import f_get_climate_ROI_for_chemical_list,\
f_get_climate_ROI_for_concrete_list,\
f_get_climate_ROI_for_mineralization_without_compressive_strength_list,\
f_get_climate_ROI_for_mineralization_with_compressive_strength_list

climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)

positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()))))
                
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        

positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()))))
                                       
                                 
climate_ROI_polyol_NA_array_WITHOUT_EOC,\
climate_ROI_polyol_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.polyol,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_polyol_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_polyol_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)

positive_values_climate_ROI_polyol_NA_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_polyol_NA_array_WITHOUT_EOC.flatten())))) 
positive_values_climate_ROI_polyol_NA_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_polyol_NA_array_WITH_EOC.flatten()))))
                                       
climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC,\
climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.Methane,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC.flatten())))) 
positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC.flatten()))))
                                   
climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC,\
climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Electrochemical_reduction_of_CO2_with_MeOH,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution)
                                        
positive_values_climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC.flatten())))) 
positive_values_climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC.flatten())))) 
                                        
                                      
climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC,\
climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Ethylene_carbonate_transesterification,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution)

positive_values_climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC.flatten())))) 
positive_values_climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITH_EOC.flatten())))) 
                                        
climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC,\
climate_ROI_DMC_Urea_transesterification_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Urea_transesterification,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution)
                                        
positive_values_climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_DMC_Urea_transesterification_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DMC_Urea_transesterification_array_WITH_EOC.flatten()))))

climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC,\
climate_ROI_CO_Dry_Reforming_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.Dry_Reforming,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)

positive_values_climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_CO_Dry_Reforming_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_CO_Dry_Reforming_array_WITH_EOC.flatten()))))

                                        
climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC,\
climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.reverseWater_Gas_Shift,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC.flatten()))))
                                        
climate_ROI_DME_NA_array_WITHOUT_EOC,\
climate_ROI_DME_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DME,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_DME_NA_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DME_NA_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_DME_NA_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_DME_NA_array_WITH_EOC.flatten()))))
                                        
climate_ROI_kerosene_NA_array_WITHOUT_EOC,\
climate_ROI_kerosene_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.Kerosene,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_kerosene_NA_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_kerosene_NA_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_kerosene_NA_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_kerosene_NA_array_WITH_EOC.flatten()))))

climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC.flatten()))))
                                        
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)


Climate_ROI_Concrete_Curing_OPC_only_array, percentage_change_comp_strength_Concrete_Curing_OPC_only_array\
                                       =f_get_climate_ROI_for_concrete_list(\
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
                                       
positive_values_Climate_ROI_Concrete_Curing_OPC_only_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Concrete_Curing_OPC_only_array.flatten()))))

Climate_ROI_Concrete_Curing_OPC_plus_SCM_array,percentage_change_comp_strength_Concrete_Curing_OPC_plus_SCM_array\
                                       =f_get_climate_ROI_for_concrete_list(\
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

positive_values_Climate_ROI_Concrete_Curing_OPC_plus_SCM_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten()))))

Climate_ROI_Concrete_Mixing_OPC_only_array,percentage_change_comp_strength_Concrete_Mixing_OPC_only_array\
                                       =f_get_climate_ROI_for_concrete_list(\
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

#print('*************************************')
#print(Climate_ROI_Concrete_Mixing_OPC_only_array)

positive_values_Climate_ROI_Concrete_Mixing_OPC_only_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten()))))


Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array, percentage_change_comp_strength_Concrete_Mixing_OPC_plus_SCM_array\
                                       =f_get_climate_ROI_for_concrete_list(\
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
                                       
positive_values_Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten()))))

Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array \
                                       =f_get_climate_ROI_for_mineralization_without_compressive_strength_list(\
                                       CO2_ROI_Constants.excel_sheet_name_mineralization_without_compressive_strength_CO2,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_CO2_CO2_utilized,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_CO2_CO2_utilized)
      
                                       
positive_values_Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array.flatten()))))

positive_values=[]


print('P11: formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P8: CO_Dry_Reforming_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P2:Concrete_Mixing_OPC_plus_SCM_array      :',numpy.round(((positive_values_Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array/CO2_ROI_Constants.number_of_samples)*100)))
print('P11: formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC      :',numpy.round(((positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P1: Concrete_Mixing_OPC_only_array      :',numpy.round(((positive_values_Climate_ROI_Concrete_Mixing_OPC_only_array/CO2_ROI_Constants.number_of_samples)*100)))
print('P15: CO_reverseWater_Gas_Shift_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P12: methane_Hydrogenation_of_CO2_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P16: MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P3: Concrete_Curing_OPC_only_array      :',numpy.round(((positive_values_Climate_ROI_Concrete_Curing_OPC_only_array/CO2_ROI_Constants.number_of_samples)*100)))
print('P4: Concrete_Curing_OPC_plus_SCM_array      :',numpy.round(((positive_values_Climate_ROI_Concrete_Curing_OPC_plus_SCM_array/CO2_ROI_Constants.number_of_samples)*100)))
print('P5: DME_NA_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_DME_NA_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P6: DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P15: CO_reverseWater_Gas_Shift_array_WITH_EOC      :',numpy.round(((positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P10: polyol_NA_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_polyol_NA_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P16: MeOH_Hydrogenation_of_CO2_array_WITH_EOC      :',numpy.round(((positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P12: methane_Hydrogenation_of_CO2_array_WITH_EOC      :',numpy.round(((positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P7: kerosene_NA_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_kerosene_NA_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P9: DMC_Urea_transesterification_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P17: formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC      :',numpy.round(((positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('P17: formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC      :',numpy.round(((positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC/CO2_ROI_Constants.number_of_samples)*100)))
print('Mineralization_Without_Compressive_Strength_CO2      :',numpy.round(((positive_values_Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array/CO2_ROI_Constants.number_of_samples)*100)))


positive_values.append(positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC)
positive_values.append(positive_values_Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array)
positive_values.append(positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC)
positive_values.append(positive_values_Climate_ROI_Concrete_Mixing_OPC_only_array)
positive_values.append(positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC)
positive_values.append(positive_values_Climate_ROI_Concrete_Curing_OPC_only_array)
positive_values.append(positive_values_Climate_ROI_Concrete_Curing_OPC_plus_SCM_array)
positive_values.append(positive_values_climate_ROI_DME_NA_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC)
positive_values.append(positive_values_climate_ROI_polyol_NA_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC)
positive_values.append(positive_values_climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC)
positive_values.append(positive_values_climate_ROI_kerosene_NA_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC)
positive_values.append(positive_values_Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array)

#print(numpy.round(((numpy.array(positive_values)/CO2_ROI_Constants.number_of_samples)*100)))             

                         
#*********** KDE PLOT START ********************************

kde_plot_fig=plt.figure(figsize=(30,20))

sns.kdeplot(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.formic_acid_Catalytic_reduction_of_CO2_with_H2_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.CO_Dry_Reforming_WITHOUT_EOC_color)

sns.kdeplot(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,color=CO2_ROI_Constants.concrete_Mixing_OPC_plus_SCM_color)

sns.kdeplot(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.formic_acid_Catalytic_reduction_of_CO2_with_H2_WITH_EOC_color, linestyle=(0,(5,5)))

sns.kdeplot(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,color=CO2_ROI_Constants.concrete_Mixing_OPC_only_color)

sns.kdeplot(climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.CO_reverseWater_Gas_Shift_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.methane_Hydrogenation_of_CO2_array_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.MeOH_Hydrogenation_of_CO2_WITHOUT_EOC_color)

sns.kdeplot(Climate_ROI_Concrete_Curing_OPC_only_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,color=CO2_ROI_Constants.concrete_Curing_OPC_only_color)

sns.kdeplot(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,color=CO2_ROI_Constants.concrete_Curing_OPC_plus_SCM_color)

sns.kdeplot(climate_ROI_DME_NA_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.DME_NA_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.DMC_Ethylene_carbonate_transesterification_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.CO_reverseWater_Gas_Shift_WITH_EOC_color, linestyle=(0,(5,5))) 

sns.kdeplot(climate_ROI_polyol_NA_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,color=CO2_ROI_Constants.polyol_NA_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.MeOH_Hydrogenation_of_CO2_WITH_EOC_color, linestyle=(0,(5,5)), alpha=0.5)

sns.kdeplot(climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.methane_Hydrogenation_of_CO2_array_WITH_EOC_color, linestyle=(0,(5,5)), alpha=0.5)

sns.kdeplot(climate_ROI_kerosene_NA_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.kerosene_NA_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.DMC_Urea_transesterification_WITHOUT_EOC_color)

sns.kdeplot(climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.formic_acid_Electrolytic_reduction_of_CO2_with_H2_WITHOUT_EOC_color)
sns.kdeplot(climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.formic_acid_Electrolytic_reduction_of_CO2_with_H2_WITH_EOC_color, linestyle="--") 

sns.kdeplot(Climate_ROI_Mineralization_Without_Compressive_Strength_CO2_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.Mineralization_Without_Compressive_Strength_CO2_Color)

#*********** KDE PLOT END ********************************
   

    
ax = plt.axes()
ax.set_xticks([])
ax.set_ylim(-15,15)
plt.yticks(fontsize=40)

kde_plot_fig.savefig('KDE_Plot.png')
#***************BOX PLOT AXES END ****************************






