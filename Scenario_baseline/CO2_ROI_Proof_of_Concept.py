'''
This Python file accompanies the manuscript titled 
“Assessing the Relative Climate Impact of Carbon dioxide Utilization for Concrete, Chemical and Mineral Production” 
authored by Dr. Dwarakanath Ravikumar, Dr. Gregory Keoleian, Dr. Shelie Miller and Dr. Volker Sick.

This file contains code to generate the scatter plot, the distribution of the Climate ROI and the heatmap 
for the two pathways – P11: Formic Acid and P2: Concrete – in Figure 2(a), Figure 2(b) and Figure 2(c) of the manuscript, respectively 

@author: Dwarakanath Ravikumar
'''
import CO2_ROI_Constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams
import pandas as pd
from matplotlib.ticker import PercentFormatter
from CO2_ROI_Functions import f_get_climate_ROI_for_chemical_list, \
f_get_climate_ROI_for_concrete_list,\
f_get_outranking_calculator_for_proof_of_concept

rcParams['font.family'] = 'Arial'

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

climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC,\
climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC\
                                        =f_get_climate_ROI_for_chemical_list(\
                                        CO2_ROI_Constants.formic_acid,\
                                        CO2_ROI_Constants.Catalytic_reduction_of_CO2_with_H2,\
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_mean, \
                                        CO2_ROI_Constants.CO2_emissions_formic_acid_conventional_sd,\
                                        CO2_ROI_Constants.lognormal_distribution)
                                        
positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array = \
len(list(filter(lambda x: x>0,list(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITHOUT_EOC.flatten()))))


positive_values=[]


#positive_values.append(positive_values_Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array)
positive_values.append(positive_values_Climate_ROI_Concrete_Mixing_OPC_only_array)
#positive_values.append(positive_values_Climate_ROI_Concrete_Curing_OPC_only_array)
#positive_values.append(positive_values_Climate_ROI_Concrete_Curing_OPC_plus_SCM_array)
positive_values.append(positive_values_climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array)

print(np.round(((np.array(positive_values)/CO2_ROI_Constants.number_of_samples)*100)))  

                                 
                                       
#*********** SCATTER PLOT START ********************************

scatter_plot_concept_fig=plt.figure(figsize=(30,40))
x_axis_array=[]
#x_axis_array=list(percentage_change_comp_strength_Concrete_Curing_OPC_only_array.flatten())
#(x_axis_array).extend(list(percentage_change_comp_strength_Concrete_Curing_OPC_plus_SCM_array.flatten()))
#(x_axis_array).extend(list(percentage_change_comp_strength_Concrete_Mixing_OPC_only_array.flatten()))
(x_axis_array).extend(list(percentage_change_comp_strength_Concrete_Mixing_OPC_plus_SCM_array.flatten()))
(x_axis_array).extend(len(list(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()))*[0])


y_axis_array=[]
#y_axis_array=list(Climate_ROI_Concrete_Curing_OPC_only_array.flatten())
#(y_axis_array).extend(list(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten()))
#(y_axis_array).extend(list(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten()))
(y_axis_array).extend(list(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten()))
(y_axis_array).extend(list(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()))

color_array=[]
#color_array=len(Climate_ROI_Concrete_Curing_OPC_only_array.flatten())*[CO2_ROI_Constants.concrete_Curing_OPC_only_color]
#color_array.extend(len(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten())*[CO2_ROI_Constants.concrete_Curing_OPC_plus_SCM_color])
#color_array.extend(len(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten())*[CO2_ROI_Constants.concrete_Mixing_OPC_only_color])
color_array.extend(len(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten())*[CO2_ROI_Constants.concrete_Mixing_OPC_plus_SCM_color])
color_array.extend(len(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten())*[CO2_ROI_Constants.formic_acid_Catalytic_reduction_of_CO2_with_H2_WITH_EOC_color])



size_array=[]
(size_array).extend(CO2_ROI_Constants.scatter_concrete_mixing_dot_size*np.ones(len(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten())))
(size_array).extend(CO2_ROI_Constants.scatter_formic_acid_dot_size*np.ones(len(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten())))

fc_array=[]
fc_array.extend(len(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten())*[CO2_ROI_Constants.concrete_Mixing_OPC_plus_SCM_color])
fc_array.extend(len(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten())*['none'])

ec_array=[]
ec_array.extend(len(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten())*[CO2_ROI_Constants.concrete_Mixing_OPC_plus_SCM_color])
ec_array.extend(len(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten())*[CO2_ROI_Constants.formic_acid_Catalytic_reduction_of_CO2_with_H2_WITH_EOC_color])



Concrete_Mixing_OPC_only_array_scatter_plot = {\
         'x_axis_array': x_axis_array,\
        'y_axis_array': y_axis_array,\
        'color_array':color_array,\
        'size_array':size_array,\
        'fc_array':fc_array,\
        'ec_array':ec_array\
        }

df_scatter_plot_data = pd.DataFrame(Concrete_Mixing_OPC_only_array_scatter_plot, columns = ['x_axis_array', 'y_axis_array','color_array','size_array','fc_array','ec_array'])


plt.scatter(x='x_axis_array',\
               y='y_axis_array',\
               data=df_scatter_plot_data,\
               s='size_array',\
               facecolors='fc_array',\
               c='color_array',\
               marker="s")
               

ax = plt.axes()
ax.set_ylim(-100,100)
ax.set_xlim(-100,100)
ax.set_ylabel('')
ax.set_xlabel('')
plt.yticks(fontsize=60)
plt.xticks(fontsize=60)
ax.axhline(y=0, color='black',linewidth=0.5)
ax.axvline(x=0, color='black',linewidth=0.5)
ax.tick_params(pad=20)
scatter_plot_concept_fig.savefig('Proof_of_Concept_Scatter_Plot.png')


#*********** SCATTER PLOT END ********************************


#*************** KDE PLOT START ****************************

kde_plot_fig=plt.figure(figsize=(30,40))

#sns.kdeplot(Climate_ROI_Concrete_Curing_OPC_only_array.flatten(), vertical=True,linewidth=CO2_ROI_Constants.kde_curve_width, shade=True,color=CO2_ROI_Constants.concrete_Curing_OPC_only_color)
#sns.kdeplot(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten(), vertical=True,linewidth=CO2_ROI_Constants.kde_curve_width, shade=True,color=CO2_ROI_Constants.concrete_Curing_OPC_plus_SCM_color)
#sns.kdeplot(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten(), vertical=True,linewidth=CO2_ROI_Constants.kde_curve_width, shade=True,color=CO2_ROI_Constants.concrete_Mixing_OPC_only_color)
sns.kdeplot(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten(), vertical=True,linewidth=CO2_ROI_Constants.kde_curve_width, shade=True,color=CO2_ROI_Constants.concrete_Mixing_OPC_plus_SCM_color)
sns.kdeplot(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten(), vertical=True,linewidth=CO2_ROI_Constants.kde_curve_width, shade=True,color=CO2_ROI_Constants.formic_acid_Catalytic_reduction_of_CO2_with_H2_WITH_EOC_color)


ax = plt.axes()
ax.set_xticks([])
ax.set_ylim(-100,100)
plt.yticks(fontsize=60)
ax.axhline(y=0, color='black',linewidth=0.5)
#ax.axvline(y=0, color='black',linewidth=0.5)

kde_plot_fig.savefig('Proof_of_Concept_KDE_Plot.png')

#*************** KDE PLOT END ****************************



super_array=[]

#It is important to note that the ROI arrays below are appended in the descending order based on
#the climate ROI
#The  arrays of the products at the top (appended first) have the greatest ROI.
#Do NOT change this order as this order helps achieve the 'green' rows on top versus 'red' 
#rows at the bottom for the heatmap

super_array.append(Climate_ROI_Concrete_Mixing_OPC_plus_SCM_array.flatten())
super_array.append(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()) 
 
#super_array.append(climate_ROI_formic_acid_Catalytic_reduction_of_CO2_with_H2_array_WITH_EOC.flatten()) 
#super_array.append(Climate_ROI_Concrete_Mixing_OPC_only_array.flatten())  
#super_array.append(Climate_ROI_Concrete_Curing_OPC_only_array.flatten()) 
#super_array.append(Climate_ROI_Concrete_Curing_OPC_plus_SCM_array.flatten())



#get the outranking % scores which are included in the heatmap
outranking_array=f_get_outranking_calculator_for_proof_of_concept(super_array)

matrix = np.zeros(outranking_array.shape, dtype=bool)
np.fill_diagonal(matrix, True)

#Uncomment the following two lines for triangular heatmap
#matrix = np.zeros_like(outranking_array, dtype=np.bool)
#matrix[np.triu_indices_from(matrix)] = True

heatmap_fig=plt.figure(figsize=(30,10))

#Properties for the colorbar. Make the colorbar horizontal (orientation), make it the same 
#dimensions as the heatmap (shrink), decrease space between x-axis of heatmap and colorbar (pad) 
#and decrease height when compared to length of colorbar (aspect)
cbar_kws1={ 'orientation': 'horizontal', 'shrink': 1, 'pad':0.03, 'aspect':40}

ax3 = sns.heatmap(outranking_array, linewidth=2,linecolor='black', annot = True, \
                  cmap= 'RdYlGn',square=False, annot_kws={'size':52, 'weight': 'bold'},fmt=".0%",\
                  mask=matrix,cbar_kws=cbar_kws1)

#Set the increments for the colorbar in increments of 20% from 0 to 100%
cbar = ax3.collections[0].colorbar
cbar.set_ticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.71])
cbar.ax.xaxis.set_major_formatter(PercentFormatter(1, 0))
cbar.ax.tick_params(labelsize=52)
#cbar.ax.tick_params(weight='bold')


ax = plt.axes()
#ax3.xaxis.set_ticks_position('top')
ax.set_xticks([])
ax.set_yticks([])

heatmap_fig.savefig('Proof_of_Concept_heatmap.png')
#***************HEATMAP OUTRANKING  PLOT END ****************************

