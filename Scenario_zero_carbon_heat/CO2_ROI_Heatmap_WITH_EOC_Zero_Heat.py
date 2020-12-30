"""
This file contains code to generate a heatmap to visualize the results from comparing the
climate ROI of alternate CCU pathways

@author: purpledwarak
"""
import CO2_ROI_Constants_Zero_Heat
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np
from matplotlib.ticker import PercentFormatter
from CO2_ROI_Functions import f_get_outranking_calculator,\
f_get_climate_ROI_for_chemical_list, f_get_climate_ROI_for_concrete_list

super_array=[]

rcParams['font.family'] = 'Arial'
#rcParams['font.sans-serif'] = ['Tahoma']


climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.formic_acid,\
                                        CO2_ROI_Constants_Zero_Heat.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)


                                      
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.formic_acid,\
                                        CO2_ROI_Constants_Zero_Heat.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                        
                                 
climate_ROI_polyol_NA_array_WITHOUT_EOC,\
climate_ROI_polyol_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.polyol,\
                                        CO2_ROI_Constants_Zero_Heat.NA,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_polyol_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_polyol_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)

 
                                        
climate_ROI_methane_Hydrogenation_of_CO2_array_WITHOUT_EOC,\
climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.Methane,\
                                        CO2_ROI_Constants_Zero_Heat.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_methane_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_methane_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                   
climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITHOUT_EOC,\
climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.DMC,\
                                        CO2_ROI_Constants_Zero_Heat.Electrochemical_reduction_of_CO2_with_MeOH,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants_Zero_Heat.uniform_distribution)
                                        
                                      
climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC,\
climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.DMC,\
                                        CO2_ROI_Constants_Zero_Heat.Ethylene_carbonate_transesterification,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants_Zero_Heat.uniform_distribution)
                                        
climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC,\
climate_ROI_DMC_Urea_transesterification_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.DMC,\
                                        CO2_ROI_Constants_Zero_Heat.Urea_transesterification,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_LB, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DMC_conventional_UB,\
                                        CO2_ROI_Constants_Zero_Heat.uniform_distribution)

climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC,\
climate_ROI_CO_Dry_Reforming_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.CO,\
                                        CO2_ROI_Constants_Zero_Heat.Dry_Reforming,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                        
climate_ROI_CO_reverseWater_Gas_Shift_array_WITHOUT_EOC,\
climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.CO,\
                                        CO2_ROI_Constants_Zero_Heat.reverseWater_Gas_Shift,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_CO_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_CO_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                        
climate_ROI_DME_NA_array_WITHOUT_EOC,\
climate_ROI_DME_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.DME,\
                                        CO2_ROI_Constants_Zero_Heat.NA,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DME_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_DME_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                        
climate_ROI_kerosene_NA_array_WITHOUT_EOC,\
climate_ROI_kerosene_NA_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.Kerosene,\
                                        CO2_ROI_Constants_Zero_Heat.NA,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_kerosene_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_kerosene_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)

climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.MeOH,\
                                        CO2_ROI_Constants_Zero_Heat.Hydrogenation_of_CO2,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)
                                        
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITHOUT_EOC, \
climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants_Zero_Heat.MeOH,\
                                        CO2_ROI_Constants_Zero_Heat.Electrolytic_reduction_of_CO2,\
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_MeOH_conventional_mean, \
                                        CO2_ROI_Constants_Zero_Heat.CO2_emissions_MeOH_conventional_sd,\
                                        CO2_ROI_Constants_Zero_Heat.lognormal_distribution)


Climate_ROI_Concrete_Curing_OPC_only_array, percentage_change_comp_strength_Concrete_Curing_OPC_only_array\
                                       =f_get_climate_ROI_for_concrete_list(\
                                       CO2_ROI_Constants_Zero_Heat.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants_Zero_Heat.dataset_category_Curing_OPC_only,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_concrete_CO2_utilized)

Climate_ROI_Concrete_Curing_OPC_plus_SCM_array,percentage_change_comp_strength_Concrete_Curing_OPC_plus_SCM_array\
                                       =f_get_climate_ROI_for_concrete_list(\
                                       CO2_ROI_Constants_Zero_Heat.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants_Zero_Heat.dataset_category_Curing_OPC_plus_SCM,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_concrete_CO2_utilized)

Climate_ROI_Concrete_Mixing_OPC_only_array,percentage_change_comp_strength_Concrete_Mixing_OPC_only_array\
                                       =f_get_climate_ROI_for_concrete_list(\
                                       CO2_ROI_Constants_Zero_Heat.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants_Zero_Heat.dataset_category_Mixing_OPC_only,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_concrete_CO2_utilized)

Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array, percentage_change_comp_strength_Concrete_Mixing_OPC_plus_SCM_array\
                                       =f_get_climate_ROI_for_concrete_list(\
                                       CO2_ROI_Constants_Zero_Heat.excel_sheet_name_concrete,\
                                       CO2_ROI_Constants_Zero_Heat.dataset_category_Mixing_OPC_plus_SCM,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_first_input_parameter, \
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_conventional_CO2_Utilized,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_first_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_last_input_parameter,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_LB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_Compressive_strength_range_UB,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_CO2_Utilized_Duplicate,\
                                       CO2_ROI_Constants_Zero_Heat.column_name_CCU_concrete_CO2_utilized)

#***************HEATMAP OUTRANKING PLOT START ****************************

#It is important to note that the ROI arrays below are appended in the descending order based on
#the climate ROI
#The  arrays of the products at the top (appended first) have the greatest ROI.
#Do NOT change this order as this order helps achieve the 'green' rows on top versus 'red' 
#rows at the bottom for the heatmap

super_array.append(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()) 
super_array.append(climate_ROI_CO_Dry_Reforming_array_WITHOUT_EOC.flatten())
super_array.append(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten()) 
super_array.append(climate_ROI_DMC_Ethylene_carbonate_transesterification_array_WITHOUT_EOC.flatten()) 
super_array.append(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten())  
super_array.append(Climate_ROI_Concrete_Curing_OPC_only_array.flatten()) 
super_array.append(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten())
super_array.append(climate_ROI_formic_acid_Electrolytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()) 
super_array.append(climate_ROI_CO_reverseWater_Gas_Shift_array_WITH_EOC.flatten()) 
super_array.append(climate_ROI_DME_NA_array_WITHOUT_EOC.flatten()) 
super_array.append(climate_ROI_kerosene_NA_array_WITHOUT_EOC.flatten()) 
super_array.append(climate_ROI_polyol_NA_array_WITHOUT_EOC.flatten()) 
super_array.append(climate_ROI_DMC_Urea_transesterification_array_WITHOUT_EOC.flatten()) 
super_array.append(climate_ROI_MeOH_Hydrogenation_of_CO2_array_WITH_EOC.flatten()) 
super_array.append(climate_ROI_methane_Hydrogenation_of_CO2_array_WITH_EOC.flatten())
super_array.append(climate_ROI_MeOH_Electrolytic_reduction_of_CO2_array_WITH_EOC.flatten())
super_array.append(climate_ROI_DMC_Electrochemical_reduction_of_CO2_with_MeOH_array_WITH_EOC.flatten()) 




#get the outranking % scores which are included in the heatmap
outranking_array=f_get_outranking_calculator(super_array)

matrix = np.zeros(outranking_array.shape, dtype=bool)
np.fill_diagonal(matrix, True)

#Uncomment the following two lines for triangular heatmap
#matrix = np.zeros_like(outranking_array, dtype=np.bool)
#matrix[np.triu_indices_from(matrix)] = True

heatmap_fig=plt.figure(figsize=(40,40))

#Properties for the colorbar. Make the colorbar horizontal (orientation), make it the same 
#dimensions as the heatmap (shrink), decrease space between x-axis of heatmap and colorbar (pad) 
#and decrease height when compared to length of colorbar (aspect)
cbar_kws1={ 'orientation': 'horizontal', 'shrink': 1, 'pad':0.01, 'aspect':44}

ax3 = sns.heatmap(outranking_array, linewidth=2,linecolor='black', annot = True, \
                  cmap= 'RdYlGn',square=False, annot_kws={'size':48, 'weight': 'bold'},fmt=".0%",\
                  mask=matrix,cbar_kws=cbar_kws1)

#Set the increments for the colorbar in increments of 20% from 0 to 100%
cbar = ax3.collections[0].colorbar
cbar.set_ticks([0,0.2,0.4,0.6,0.8, 1])
cbar.ax.xaxis.set_major_formatter(PercentFormatter(1, 0))
cbar.ax.tick_params(labelsize=52)
#cbar.ax.tick_params(weight='bold')


ax = plt.axes()
#ax3.xaxis.set_ticks_position('top')
ax.set_xticks([])
ax.set_yticks([])

heatmap_fig.savefig('heatmap_WITH_EOC_Zero_Heat.png')
#***************HEATMAP OUTRANKING  PLOT END ****************************


