'''
This Python file accompanies the manuscript titled 
“Assessing the Relative Climate Impact of Carbon dioxide Utilization for Concrete, Chemical and Mineral Production” 
authored by Dr. Dwarakanath Ravikumar, Dr. Gregory Keoleian, Dr. Shelie Miller and Dr. Volker Sick.

This file contains code to generate and plot the distribution for the climate ROI for the CCU pathways as an inset in 
Figure 3 in the main manuscript. The climate ROI in the inset range between -2000 to +1000

@author: Dwarakanath Ravikumar
'''
import CO2_ROI_Constants
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
from CO2_ROI_Functions import f_get_climate_ROI_for_chemical_list,\
f_get_climate_ROI_for_concrete_list,\
f_get_climate_ROI_for_mineralization_without_compressive_strength_list, \
f_get_climate_ROI_for_mineralization_with_compressive_strength_list\

super_array=[]


climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
                                      
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

 
                                        
#climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC,\
#climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC\
#                                        =f_get_climate_ROI_for_chemical_list(\
#                                        CO2_ROI_Constants.Methane,\
#                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
#                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_mean, \
#                                        CO2_ROI_Constants.CO2_emissions_methane_conventional_sd,\
#                                        CO2_ROI_Constants.lognormal_distribution)
                                   
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
                                        
climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC,\
climate_ROI_DMC_Urea_transesterification_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DMC,\
                                        CO2_ROI_Constants.Urea_transesterification,\
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants.uniform_distribution)

climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC,\
climate_ROI_CO_Dry_Reforming_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.Dry_Reforming,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC,\
climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.CO,\
                                        CO2_ROI_Constants.reverseWater_Gas_Shift,\
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
climate_ROI_DME_NA_array_WITHOUT_EOC,\
climate_ROI_DME_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.DME,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_DME_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
climate_ROI_kerosene_NA_array_WITHOUT_EOC,\
climate_ROI_kerosene_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.Kerosene,\
                                        CO2_ROI_Constants.NA,\
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_kerosene_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)

climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.MeOH,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
positive_values_climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC.flatten()))))
positive_values_climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC = \
len(list(filter(lambda x: x>0,list(climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC.flatten()))))

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



Climate_ROI_Mineralization_With_Compressive_Strength_array, percentage_change_comp_strength_Mineralization_With_Compressive_Strength_array \
                                        =f_get_climate_ROI_for_mineralization_with_compressive_strength_list(\
                                        CO2_ROI_Constants.excel_sheet_name_mineralization_with_compressive_strength,\
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
                                        
positive_values_Climate_ROI_Mineralization_With_Compressive_Strength_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Mineralization_With_Compressive_Strength_array.flatten()))))

Climate_ROI_Mineralization_Without_Compressive_Strength_Flue_Gas_array \
                                       =f_get_climate_ROI_for_mineralization_without_compressive_strength_list(\
                                       CO2_ROI_Constants.excel_sheet_name_mineralization_without_compressive_strength_flue_gas,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_conventional_mineralization_without_compressive_strength_flue_gas_CO2_utilized,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_first_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_last_input_parameter,\
                                       CO2_ROI_Constants.column_name_CCU_mineralization_without_compressive_strength_flue_gas_CO2_utilized)
positive_values_Climate_ROI_Mineralization_Without_Compressive_Strength_Flue_Gas_array = \
len(list(filter(lambda x: x>0,list(Climate_ROI_Mineralization_Without_Compressive_Strength_Flue_Gas_array.flatten()))))



positive_values=[]

positive_values.append(positive_values_climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC)
positive_values.append(positive_values_climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC)
positive_values.append(positive_values_climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC)
positive_values.append(positive_values_Climate_ROI_Mineralization_Without_Compressive_Strength_Flue_Gas_array)
positive_values.append(positive_values_Climate_ROI_Mineralization_With_Compressive_Strength_array)

print(numpy.round(((numpy.array(positive_values)/CO2_ROI_Constants.number_of_samples)*100)))
                                      
#*********** KDE PLOT START ********************************

box_plot_fig=plt.figure(figsize=(30,20))

                                      
                                      
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)


sns.kdeplot(climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.DMC_Electrochemical_reduction_of_CO2_with_MeOH_WITHOUT_EOC_color)
sns.kdeplot(climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.DMC_Electrochemical_reduction_of_CO2_with_MeOH_WITH_EOC_color, linestyle="--") 

sns.kdeplot(climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.MeOH_Electrolytic_reduction_of_CO2_WITHOUT_EOC_color)
sns.kdeplot(climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width_WITH_EOC,shade=True,\
            color=CO2_ROI_Constants.MeOH_Electrolytic_reduction_of_CO2_WITH_EOC_color, linestyle="--") 

sns.kdeplot(Climate_ROI_Mineralization_With_Compressive_Strength_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.Mineralization_With_Compressive_Strength_Color)

sns.kdeplot(Climate_ROI_Mineralization_Without_Compressive_Strength_Flue_Gas_array.flatten(), vertical=True,\
            linewidth=CO2_ROI_Constants.kde_curve_width,shade=True,\
            color=CO2_ROI_Constants.Mineralization_Without_Compressive_Strength_Flue_Gas_Color)

#*********** KDE PLOT END ********************************
   

    
ax = plt.axes()
ax.set_xticks([])
ax.set_ylim(-2000,1000)
plt.yticks(fontsize=60)

box_plot_fig.savefig('kde_plot_outliers_fig.png')
#***************BOX PLOT AXES END ****************************






