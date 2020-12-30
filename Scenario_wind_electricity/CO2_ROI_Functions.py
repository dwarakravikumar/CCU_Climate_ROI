from matplotlib.ticker import FormatStrFormatter
import math
import CO2_ROI_Constants_Wind_Elec
import numpy as np
import pandas as pd
import statistics
from SALib.analyze import delta
from SALib.analyze import sobol

def f_get_axis_limits(xticks,yticks):
    
        if(abs(min(xticks))>abs(max(xticks))):
            x_axis_upper_limit=-min(xticks)
            x_axis_lower_limit=min(xticks)
            
        if(abs(min(xticks))<abs(max(xticks)) or abs(min(xticks))==abs(max(xticks))):
            x_axis_upper_limit=max(xticks)
            x_axis_lower_limit=-max(xticks)
            
        if(abs(min(yticks))>abs(max(yticks))):
            y_axis_upper_limit=-min(yticks)
            y_axis_lower_limit=min(yticks)
            
        if(abs(min(yticks))<abs(max(yticks))or abs(min(yticks))==abs(max(yticks))):
            y_axis_upper_limit=max(yticks)
            y_axis_lower_limit=-max(yticks)
            
        return x_axis_lower_limit, x_axis_upper_limit, y_axis_lower_limit, y_axis_upper_limit
    
def f_set_axis_format(axis, facecolor, spinecolor, linewidth,ticks_font):
    
        axis.set_facecolor(facecolor)
        axis.spines['left'].set_color(spinecolor)
        axis.spines['right'].set_color(spinecolor)
        axis.spines['top'].set_color(spinecolor)
        axis.spines['bottom'].set_color(spinecolor)
        
        axis.spines['left'].set_linewidth(linewidth)
        axis.spines['right'].set_linewidth(linewidth)
        axis.spines['top'].set_linewidth(linewidth)
        axis.spines['bottom'].set_linewidth(linewidth)
                
        axis.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
        axis.yaxis.set_major_formatter(FormatStrFormatter('%0.2f'))
                        
        for label in axis.get_xticklabels():
            label.set_fontproperties(ticks_font)
        
        for label in axis.get_yticklabels():
            label.set_fontproperties(ticks_font) 
        
        return axis
    
    
def f_get_yaxis_limits(y_axis_lower_limit1,y_axis_upper_limit1,y_axis_lower_limit2,y_axis_upper_limit2):
        
        if(y_axis_upper_limit1>y_axis_upper_limit2):
            y_axis_upper_limit2=y_axis_upper_limit1
        
        if(y_axis_upper_limit2>y_axis_upper_limit1):
            y_axis_upper_limit1=y_axis_upper_limit2  
            
        if(y_axis_lower_limit1<y_axis_lower_limit2):
            y_axis_lower_limit2=y_axis_lower_limit1
        
        if(y_axis_lower_limit2<y_axis_lower_limit1):
            y_axis_lower_limit1=y_axis_lower_limit2  
            
        return y_axis_lower_limit1,y_axis_upper_limit1,y_axis_lower_limit2,y_axis_upper_limit2
    
def f_set_axis_bounds(axis,x_axis_lower_limit, x_axis_upper_limit, y_axis_lower_limit, y_axis_upper_limit):
    
        axis.spines["left"].set_position(("data", x_axis_lower_limit))
        axis.spines["right"].set_position(("data", x_axis_upper_limit))
        axis.spines["bottom"].set_position(("data", y_axis_lower_limit))
        axis.spines["top"].set_position(("data", y_axis_upper_limit))
        
        axis.spines["bottom"].set_bounds(x_axis_lower_limit, x_axis_upper_limit)
        axis.spines["top"].set_bounds(x_axis_lower_limit, x_axis_upper_limit)
        axis.spines["left"].set_bounds(y_axis_lower_limit, y_axis_upper_limit)
        axis.spines["right"].set_bounds(y_axis_lower_limit, y_axis_upper_limit)
        
        return axis
    
def f_draw_xy_axis(axis,x_axis_lower_limit, x_axis_upper_limit, y_axis_lower_limit, y_axis_upper_limit, line_width, line_color):
        axis.plot([0,0],[y_axis_lower_limit, y_axis_upper_limit],color=line_color, linewidth=line_width)
        axis.plot([x_axis_lower_limit, x_axis_upper_limit],[0, 0],color=line_color, linewidth=line_width)
        
def f_get_conventional_MeOH_CO2_intensity():
        m1 = math.log((CO2_ROI_Constants_Wind_Elec.CO2_emissions_Conv_MeOH_mean**2)/math.sqrt(CO2_ROI_Constants_Wind_Elec.CO2_emissions_Conv_MeOH_sd**2+CO2_ROI_Constants_Wind_Elec.CO2_emissions_Conv_MeOH_mean**2))
        sd1= math.sqrt(math.log(CO2_ROI_Constants_Wind_Elec.CO2_emissions_Conv_MeOH_sd**2/(CO2_ROI_Constants_Wind_Elec.CO2_emissions_Conv_MeOH_mean**2)+1))
        conventional_MeOH_CO2_intensity_array_array=np.random.lognormal(m1, sd1, CO2_ROI_Constants_Wind_Elec.number_of_samples)
        return conventional_MeOH_CO2_intensity_array_array
    
def f_get_CCU_MeOH_CO2_intensity_without_H2():
    m1 = math.log((CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_without_H2_mean**2)/math.sqrt(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_without_H2_sd**2+CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_without_H2_mean**2))
    sd1= math.sqrt(math.log(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_without_H2_sd**2/(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_without_H2_mean**2)+1))
    CCU_MeOH_CO2_intensity_without_H2_array_array=np.random.lognormal(m1, sd1, CO2_ROI_Constants_Wind_Elec.number_of_samples)
    return CCU_MeOH_CO2_intensity_without_H2_array_array

def f_get_CCU_MeOH_CO2_intensity_with_H2():
    m1 = math.log((CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_H2_mean**2)/math.sqrt(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_H2_sd**2+CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_H2_mean**2))
    sd1= math.sqrt(math.log(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_H2_sd**2/(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_H2_mean**2)+1))
    CCU_MeOH_CO2_intensity_with_H2_array_array=np.random.lognormal(m1, sd1, CO2_ROI_Constants_Wind_Elec.number_of_samples)
    return CCU_MeOH_CO2_intensity_with_H2_array_array

def f_get_CCU_MeOH_CO2_intensity_with_env_opp_cost():
    m1 = math.log((CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_env_opp_cost_mean**2)/math.sqrt(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_env_opp_cost_sd**2+CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_env_opp_cost_mean**2))
    sd1= math.sqrt(math.log(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_env_opp_cost_sd**2/(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CCU_MeOH_with_env_opp_cost_mean**2)+1))
    CCU_MeOH_CO2_intensity_with_env_opp_cost_array_array=np.random.lognormal(m1, sd1, CO2_ROI_Constants_Wind_Elec.number_of_samples)
    return CCU_MeOH_CO2_intensity_with_env_opp_cost_array_array

def f_get_CO2_used_per_ton_CCU_MeOH():
    CO2_used_per_ton_CCU_MeOH_array_array=np.random.uniform(CO2_ROI_Constants_Wind_Elec.CO2_used_per_ton_CCU_MeOH_LB,CO2_ROI_Constants_Wind_Elec.CO2_used_per_ton_CCU_MeOH_UB,CO2_ROI_Constants_Wind_Elec.number_of_samples)
    return CO2_used_per_ton_CCU_MeOH_array_array

#def f_get_outranking_calculator(array1, array2):
#    
#    first_lesser_than_second=0
#    
#    for first_array_counter, second_array_counter in zip(array1, array2):
#        if (first_array_counter<second_array_counter):
#            first_lesser_than_second=first_lesser_than_second=+1
#            
#    return first_lesser_than_second

def f_get_outranking_calculator(super_array):
    
    outranking_array=[]
    
    
    for i in range(len(super_array)):
  
      for j in range(0,len(super_array)):
                
        first_higher_CO2_ROI_than_second=0
        
        for first_array_counter, second_array_counter in zip (super_array[i], super_array[j]):
                    
            if (first_array_counter>second_array_counter):
                        
                first_higher_CO2_ROI_than_second=first_higher_CO2_ROI_than_second+1
                        
        outranking_array.append((first_higher_CO2_ROI_than_second/CO2_ROI_Constants_Wind_Elec.number_of_samples))
        
 
    return np.array(outranking_array).reshape(CO2_ROI_Constants_Wind_Elec.number_of_products,CO2_ROI_Constants_Wind_Elec.number_of_products)

def f_get_outranking_calculator_for_proof_of_concept(super_array):
    
    outranking_array=[]
    
    
    for i in range(len(super_array)):
  
      for j in range(0,len(super_array)):
                
        first_higher_CO2_ROI_than_second=0
        
        for first_array_counter, second_array_counter in zip (super_array[i], super_array[j]):
                    
            if (first_array_counter>second_array_counter):
                        
                first_higher_CO2_ROI_than_second=first_higher_CO2_ROI_than_second+1
                        
        outranking_array.append((first_higher_CO2_ROI_than_second/CO2_ROI_Constants_Wind_Elec.number_of_samples))
        
 
    return np.array(outranking_array).reshape(CO2_ROI_Constants_Wind_Elec.number_of_products_for_proof_of_concept,CO2_ROI_Constants_Wind_Elec.number_of_products_for_proof_of_concept)


def f_harmonize_literature_data(df):
    
    df.fillna(0, inplace=True)
    
#If the value for the heat or electricity required to capture CO2 is mentioned, then set the value of CO2 required (kg) to zero
# to prevent double counting   
    df.loc[(df[CO2_ROI_Constants_Wind_Elec.column_name_Heat_for_CO2_capture_MJ] != 0) | \
           (df[CO2_ROI_Constants_Wind_Elec.column_name_Heat_for_CO2_capture_kWh_Th] != 0)\
              | (df[CO2_ROI_Constants_Wind_Elec.column_name_Electricity_for_CO2_capture_kWh] != 0), CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input]=0
#If the value for the electricity required to generate H2 is mentioned, then set the value of H2 required (kg) to zero
# to prevent double counting          
    df.loc[(df[CO2_ROI_Constants_Wind_Elec.column_name_electricity_for_H2] != 0), CO2_ROI_Constants_Wind_Elec.column_name_H2_Input]=0
    
    
    return df

#def f_harmonize_concrete_literature_data(df):
#    
#    df.fillna(0, inplace=True)
#    df.replace('NA',0)
#    
#    return df

def f_get_lognormal_distribution(mean, sd, number_of_samples):
    
    m1 = math.log((mean**2)/math.sqrt(sd**2+mean**2))
    sd1= math.sqrt(math.log(sd**2/(mean**2)+1))
    lognormal_distribution=np.random.lognormal(m1, sd1, number_of_samples)
    
    return lognormal_distribution

def f_get_uniform_distribution(LB, UB, number_of_samples):

    uniform_distribution=np.random.uniform(LB, UB,number_of_samples)
    
    return uniform_distribution

def f_get_chemical_input_inventory_CO2_intensity_array(number_of_samples,number_of_columns):
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix=np.zeros((number_of_samples,number_of_columns))

    CO2_energy_penalty=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_sd,number_of_samples)
    
    #The energy penalty from column 0 is applicable only when the energy requirements for carbon capture are not provided in the dataset in 
    #columns 7,8,9. This is made sure through the harmonization which sets column 0 to zero when energy values for carbon capture
    #are provided in columns 7,8,9.
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,0] = CO2_energy_penalty
    
    CO2_H2_Generation=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_Through_Electrolysis_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_Through_Electrolysis_sd,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,1] =CO2_H2_Generation
    
    CO2_water_analyte=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_analyte_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_analyte_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,2] =CO2_water_analyte
    
    CO2_water_cooling=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_cooling_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_cooling_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,3] =CO2_water_cooling
    
    CO2_NaOH=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaOH_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaOH_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,4] =CO2_NaOH
    
    CO2_HCl=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_HCl_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_HCl_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,5] =CO2_HCl
    
    CO2_NaCl=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaCl_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaCl_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,6] =CO2_NaCl
    
    Heat_to_electricity_array=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.Heat_to_electricity_LB, CO2_ROI_Constants_Wind_Elec.Heat_to_electricity_UB,number_of_samples)
    US_elec_CO2_intensity_array=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_LB, CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_UB,number_of_samples)
            
    #The following three columns (7,8,9) account for the CO2 emissions from the energy penalty, which is compensated by an external power plant.
    #The following three columns will will come into play when the correspoding energy values in the "literature_review_input_inventory_array"
    #are provided in the dataset. In case it the energy values are not provided by the dataset, the code uses the generaic of the energy requirement for
    # carbon capture from a literature review and as a result the values in column 0 (above) come into play. Alternately, either the energy penalty values are
    #calculated from columns 7,8, 9 or from column 0. This is made sure through the harmonization which sets column 0 to zero when energy values for carbon capture
    #are provided in columns 7,8,9.
       
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,7] = US_elec_CO2_intensity_array*Heat_to_electricity_array*0.277
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,8] = US_elec_CO2_intensity_array*Heat_to_electricity_array
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,9] = US_elec_CO2_intensity_array*.1
    
    CO2_wind_electricity=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,10] =CO2_wind_electricity
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,11] =US_elec_CO2_intensity_array
    
    CO2_natural_gas_per_kg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_kg_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_kg_sd,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,12] = CO2_natural_gas_per_kg
    
    CO2_natural_gas_per_m3=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_m3_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_m3_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,13] = CO2_natural_gas_per_m3
    
    CO2_heat_per_MJ=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,14] = CO2_heat_per_MJ*3.6
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,15] = CO2_heat_per_MJ
    
    CO2_steam_per_MJ=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,16] = CO2_steam_per_MJ
    
    CO2_steam_per_kg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,17] = CO2_steam_per_kg
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,18] = CO2_steam_per_MJ*3.6
    
    CO2_MeOH=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_MeOH_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_MeOH_conventional_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,19] = CO2_MeOH
    
    CO2_ammonia=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ammonia_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ammonia_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,20] = CO2_ammonia
    
    CO2_ethylene_oxide=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_oxide_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_oxide_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,21] = CO2_ethylene_oxide
    
    CO2_platinum=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_platinum_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_platinum_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,22] = CO2_platinum
    
    CO2_niobium=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_niobium_LB, CO2_ROI_Constants_Wind_Elec.CO2_emissions_niobium_UB,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,23] =CO2_niobium
    
    CO2_aniline=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_aniline_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_aniline_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,24] = CO2_aniline
    
    CO2_propylene_oxide=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_propylene_oxide_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_propylene_oxide_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,25] = CO2_propylene_oxide
    
    CO2_glycerol=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_glycerol_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_glycerol_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,26] = CO2_glycerol
    
    CO2_monopropylene_glycol=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_monopropylene_glycol_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_monopropylene_glycol_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,27] = CO2_monopropylene_glycol
    
    CO2_naphtha=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,28] = CO2_naphtha
    
    CO2_refrigerant=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_refrigerant_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_refrigerant_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,29] = CO2_refrigerant
    
    CO2_activated_carbon=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_activated_carbon_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_activated_carbon_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,30] = CO2_activated_carbon
    
    #Column 31 is a dummy column consisting of 1's. This column is multiplied by the CO2 utilized divided by nine to account for the 10% of 
    #the emissions which are not captured by the MEA system.
    ones_array=f_get_uniform_distribution(1, 1, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,31] = ones_array
    
    
    return Monte_Carlo_input_inventory_CO2_intensity_matrix


def f_get_chemical_input_inventory_CO2_intensity_for_sensitvity_analysis_array(number_of_samples,number_of_columns):
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix=np.zeros((number_of_samples,number_of_columns))

    CO2_energy_penalty=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_sd,number_of_samples)
    
    #The energy penalty from column 0 is applicable only when the energy requirements for carbon capture are not provided in the dataset in 
    #columns 7,8,9. This is made sure through the harmonization which sets column 0 to zero when energy values for carbon capture
    #are provided in columns 7,8,9.
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,0] = CO2_energy_penalty
    
    CO2_H2_Generation=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_Through_Electrolysis_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_Through_Electrolysis_sd,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,1] =CO2_H2_Generation
    
    CO2_water_analyte=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_analyte_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_analyte_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,2] =CO2_water_analyte
    
    CO2_water_cooling=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_cooling_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_cooling_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,3] =CO2_water_cooling
    
    CO2_NaOH=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaOH_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaOH_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,4] =CO2_NaOH
    
    CO2_HCl=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_HCl_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_HCl_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,5] =CO2_HCl
    
    CO2_NaCl=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaCl_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_NaCl_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,6] =CO2_NaCl
    
    Heat_to_electricity_array=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.Heat_to_electricity_LB, CO2_ROI_Constants_Wind_Elec.Heat_to_electricity_UB,number_of_samples)
    US_elec_CO2_intensity_array=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_LB, CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_UB,number_of_samples)
            
    #The following three columns (7,8,9) account for the CO2 emissions from the energy penalty, which is compensated by an external power plant.
    #The following three columns will will come into play when the correspoding energy values in the "literature_review_input_inventory_array"
    #are provided in the dataset. In case it the energy values are not provided by the dataset, the code uses the generaic of the energy requirement for
    # carbon capture from a literature review and as a result the values in column 0 (above) come into play. Alternately, either the energy penalty values are
    #calculated from columns 7,8, 9 or from column 0. This is made sure through the harmonization which sets column 0 to zero when energy values for carbon capture
    #are provided in columns 7,8,9.
       
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,7] = US_elec_CO2_intensity_array*Heat_to_electricity_array*0.277
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,8] = US_elec_CO2_intensity_array*Heat_to_electricity_array
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,9] = US_elec_CO2_intensity_array*.1
    
    CO2_wind_electricity=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,10] =CO2_wind_electricity
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,11] =US_elec_CO2_intensity_array
    
    CO2_natural_gas_per_kg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_kg_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_kg_sd,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,12] = CO2_natural_gas_per_kg
    
    CO2_natural_gas_per_m3=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_m3_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_natural_gas_per_m3_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,13] = CO2_natural_gas_per_m3
    
    
    CO2_heat_per_kWh=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_kWh_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_kWh_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,14] = CO2_heat_per_kWh
    
    CO2_heat_per_MJ=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,15] = CO2_heat_per_MJ
    
    CO2_steam_per_MJ=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,16] = CO2_steam_per_MJ
    
    CO2_steam_per_kg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,17] = CO2_steam_per_kg
    
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,18] = CO2_steam_per_MJ*3.6
    
    CO2_MeOH=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_MeOH_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_MeOH_conventional_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,19] = CO2_MeOH
    
    CO2_ammonia=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ammonia_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ammonia_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,20] = CO2_ammonia
    
    CO2_ethylene_oxide=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_oxide_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_oxide_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,21] = CO2_ethylene_oxide
    
    CO2_platinum=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_platinum_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_platinum_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,22] = CO2_platinum
    
    CO2_niobium=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_niobium_LB, CO2_ROI_Constants_Wind_Elec.CO2_emissions_niobium_UB,number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,23] =CO2_niobium
    
    CO2_aniline=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_aniline_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_aniline_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,24] = CO2_aniline
    
    CO2_propylene_oxide=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_propylene_oxide_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_propylene_oxide_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,25] = CO2_propylene_oxide
    
    CO2_glycerol=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_glycerol_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_glycerol_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,26] = CO2_glycerol
    
    CO2_monopropylene_glycol=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_monopropylene_glycol_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_monopropylene_glycol_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,27] = CO2_monopropylene_glycol
    
    CO2_naphtha=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,28] = CO2_naphtha
    
    CO2_refrigerant=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_refrigerant_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_refrigerant_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,29] = CO2_refrigerant
    
    CO2_activated_carbon=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_activated_carbon_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_activated_carbon_sd, number_of_samples)
    Monte_Carlo_input_inventory_CO2_intensity_matrix[:,30] = CO2_activated_carbon
   
    
    return Monte_Carlo_input_inventory_CO2_intensity_matrix



def f_get_monte_carlo_byproducts_CO2_intensity_matrix(number_of_samples,number_of_columns):
    
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix=np.zeros((number_of_samples,number_of_columns))
    
    CO2_H2_conventional=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_conventional_LB, CO2_ROI_Constants_Wind_Elec.CO2_emissions_H2_conventional_UB, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,0] = CO2_H2_conventional
    
    CO2_O2_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_O2_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_O2_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,1] = CO2_O2_conventional
    
    CO2_steam_kg_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_kg_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,2] = CO2_steam_kg_conventional
    
    CO2_steam_MJ_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_steam_per_MJ_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,3] = CO2_steam_MJ_conventional
    
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,4] = CO2_steam_MJ_conventional*0.277

    CO2_heat_MJ_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_heat_per_MJ_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,5] = CO2_heat_MJ_conventional
    
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,6] = CO2_heat_MJ_conventional*3.6
    
    CO2_sodium_formate_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_sodium_formate_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_sodium_formate_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,7] = CO2_sodium_formate_conventional
    
    CO2_sodium_carbonate_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_soda_ash_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_soda_ash_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,8] = CO2_sodium_carbonate_conventional
    
    CO2_sodium_sulfate_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_sodium_sulfate_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_sodium_sulfate_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,9] = CO2_sodium_sulfate_conventional
    
    CO2_ethylene_glycol_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_glycol_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_glycol_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,10] = CO2_ethylene_glycol_conventional
    
    CO2_ethylene_carbonate_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_carbonate_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_ethylene_carbonate_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,11] = CO2_ethylene_carbonate_conventional
    
    CO2_naphtha_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_naphtha_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,12] = CO2_naphtha_conventional
    
    CO2_water_conventional=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_conventional_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_water_conventional_sd, number_of_samples)
    Monte_Carlo_conventional_pathway_CO2_intensity_matrix[:,13] = CO2_water_conventional
    
    return Monte_Carlo_conventional_pathway_CO2_intensity_matrix
    
def f_get_monte_carlo_waste_CO2_intensity_matrix(number_of_samples,number_of_columns):
    
    Monte_Carlo_waste_CO2_intensity_matrix=np.zeros((number_of_samples,number_of_columns))
    
    CO2_waste_CO2_emissions=f_get_uniform_distribution(1, 1, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,0] = CO2_waste_CO2_emissions
    
    CO2_waste_water_emissions=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_waste_water_mean,CO2_ROI_Constants_Wind_Elec.CO2_emissions_waste_water_sd, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,1] = CO2_waste_water_emissions
    
    CO2_flue_gas_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,2] = CO2_flue_gas_emissions
    
    CO2_waste_zeolite_emissions=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_waste_zeolite_mean,CO2_ROI_Constants_Wind_Elec.CO2_emissions_waste_zeolite_sd, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,3] = CO2_waste_zeolite_emissions
    
    CO2_waste_methanol_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,4] = CO2_waste_methanol_emissions
    
    CO2_waste_O2_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,5] = CO2_waste_O2_emissions
    
    CO2_waste_N2_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,6] = CO2_waste_N2_emissions
    
    CO2_waste_H2O_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,7] = CO2_waste_H2O_emissions
    
    CO2_waste_ammonia_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,8] = CO2_waste_ammonia_emissions
    
    CO2_waste_acetaldehyde_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,9] = CO2_waste_acetaldehyde_emissions

    CO2_waste_aniline_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,10] = CO2_waste_aniline_emissions
    
    CO2_waste_carbon_monoxide_emissions=f_get_uniform_distribution(0,0, number_of_samples)
    Monte_Carlo_waste_CO2_intensity_matrix[:,11] = CO2_waste_carbon_monoxide_emissions
    
    return Monte_Carlo_waste_CO2_intensity_matrix

def f_get_monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix(number_of_samples,number_datasets_formic_acid_catalytic_reduction_CO2_with_H2, mean, sd, distribution_type):
    
    if(distribution_type==CO2_ROI_Constants_Wind_Elec.lognormal_distribution):
        monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix=f_get_lognormal_distribution(mean,sd, (number_of_samples,number_datasets_formic_acid_catalytic_reduction_CO2_with_H2))
    
    elif(distribution_type==CO2_ROI_Constants_Wind_Elec.uniform_distribution):
        monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix=f_get_uniform_distribution(mean,sd, (number_of_samples,number_datasets_formic_acid_catalytic_reduction_CO2_with_H2))
        
    return monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix

def f_get_climate_ROI_for_chemical_list(CCU_chemical_name,\
                                        CCU_chemical_production_route,\
                                        CO2_emissions_chemicals_conventional_pathway_mean, \
                                        CO2_emissions_chemicals_conventional_pathway_sd,\
                                        distribution_type):
    
    excel_tab_df = pd.read_excel(CO2_ROI_Constants_Wind_Elec.excel_file, sheet_name=CO2_ROI_Constants_Wind_Elec.sheet_name_chemicals)
    
    #filter the rows for the specific chemical and production route
    CCU_input_inventory_un_harmonized_df = \
    excel_tab_df[(excel_tab_df[CO2_ROI_Constants_Wind_Elec.column_name_CCU_Product]==CCU_chemical_name) & \
                 (excel_tab_df[CO2_ROI_Constants_Wind_Elec.column_name_Production_Route]==CCU_chemical_production_route)]
    
    #get the CO2 utilized for this chemical from the original and unhamronized data. 
    #The CO2 values will be used to calculate the climate ROI 
    CO2_Utilized_list=CCU_input_inventory_un_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input].values.tolist()
    
   
    #In the harmonization, the CO2 utiilized value in the dataset is set to zero when the energy values for carbon capture
    # are provided in the dataset. This is done to avoid double counting as the energy penalty is either calculated from the
    #energy values for carbon capture provided in the study OR from the CO2 utilized value
    CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df = f_harmonize_literature_data(excel_tab_df)
    CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df = \
    CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[\
    (CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CCU_Product]==CCU_chemical_name) \
    & \
    (CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_Production_Route]==CCU_chemical_production_route)]
    
    #Get the number of datasets for a specific chemical and produciton route
    number_of_datasets_for_CCU_chemical=CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.shape[0]
    
    #Get the CO2 internsity of the inventory items used to produce the chemical through the CCU pathway
    CCU_input_inventory_CO2_intensity_array=\
    f_get_chemical_input_inventory_CO2_intensity_array(int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical)),CO2_ROI_Constants_Wind_Elec.number_of_input_parameters+1)
    
    #Get the inventory items, which were used to produce the chemical through the CCU pathway
    CCU_input_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters+1))
    CCU_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters]=np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc[:,CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input:CO2_ROI_Constants_Wind_Elec.column_name_Activated_Carbon_Input].values.tolist())
    #Add an extra column to the inventory array account for the 10% of the CO2 emissions not captured by the MEA system
    CCU_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters]=np.array(CCU_input_inventory_un_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input].values.tolist())/9
    
    CCU_input_inventory_CO2_emissions_array=CCU_input_inventory_CO2_intensity_array.dot(np.transpose(CCU_input_inventory_array))
    
    #Get the CO2 intensity of the byproducts (produced along with the CCU chemical)
    CCU_byproducts_CO2_intensity_array=f_get_monte_carlo_byproducts_CO2_intensity_matrix(int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical)),CO2_ROI_Constants_Wind_Elec.number_of_byproducts)
    #Get the values of the byproducts that were produced along with the chemical
    CCU_byproduct_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,CO2_ROI_Constants_Wind_Elec.number_of_byproducts))
    CCU_byproduct_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_byproducts]=np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc[:,CO2_ROI_Constants_Wind_Elec.column_name_H2_byproduct_output:CO2_ROI_Constants_Wind_Elec.column_name_H2O_byproduct_output].values.tolist())
    CCU_byproduct_CO2_emissions_array=CCU_byproducts_CO2_intensity_array.dot(np.transpose(CCU_byproduct_inventory_array))
    
    #Get the CO2 intensity of the waste emissions from the CCU production process
    CCU_waste_CO2_intensity_array=f_get_monte_carlo_waste_CO2_intensity_matrix(int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical)),CO2_ROI_Constants_Wind_Elec.number_of_waste)
    
    #Get the values of the wastes that were produced along with the chemical
    CCU_waste_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,CO2_ROI_Constants_Wind_Elec.number_of_waste))
    
    CCU_waste_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_waste]=\
    np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc\
    [:,CO2_ROI_Constants_Wind_Elec.column_name_CO2_emissions_waste:CO2_ROI_Constants_Wind_Elec.column_name_CO_emissions_waste].values.tolist())
    
    CCU_waste_CO2_emissions_array=CCU_waste_CO2_intensity_array.dot(np.transpose(CCU_waste_inventory_array))
    
    #Obtain the CO2 emissions from producing the chemical conventionally
    conventional_pathway_CO2_intensity_array=f_get_monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix\
    (int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical)),\
     number_of_datasets_for_CCU_chemical, CO2_emissions_chemicals_conventional_pathway_mean,\
     CO2_emissions_chemicals_conventional_pathway_sd,distribution_type)
    
    #The first column contains the H2 required (kg) and the second column contains the electrcity which was used to generate the 
    #After harmonization, the dataset either containes the H2 requirement in kg or the electrcity used for H2 electrolysis in kWh
    H2_inventory_array=np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df\
                                [[CO2_ROI_Constants_Wind_Elec.column_name_H2_Input,\
                                  CO2_ROI_Constants_Wind_Elec.column_name_electricity_for_H2]].values.tolist())
    
    #calculate the delta in the CO2 intensity between the US grid and wind electricity
    wind_elec_CO2_intensity_array=\
    np.array(f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_mean, \
    CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_sd, int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical))))
    
    US_elec_CO2_intensity_array=np.array(f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_LB, \
    CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_UB,int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical))))
    
    delta_elec_CO2_intensity_array=US_elec_CO2_intensity_array-wind_elec_CO2_intensity_array
    
    #The first column in EOC array will be multipied by the H2 values (kg) from the H2 inventory array
    EOC_array=np.zeros((2,int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical))))
    EOC_array[0:,]=delta_elec_CO2_intensity_array*CO2_ROI_Constants_Wind_Elec.electricity_H2_electrolysis_kWh
    #The second column will be multipied by the electrcity required for H2 generation (kWh) from the H2 inventory array
    EOC_array[1:,]=delta_elec_CO2_intensity_array
    
    #Calculate the CO2 values of the environmental opportunity cost (EOC)
    CO2_EOC_array= np.transpose(H2_inventory_array.dot(EOC_array))
    
    #Calculate the climate ROI. The numerator consists of the SUM of CO2 emissions from 
    # (i) producing the chemical through the conventional pathway
    # (ii) byproducts which are produced along with the chenical in the CCU pathway
    #MINUS the CO2 emissions from 
    # (i) producing the chemical through the CCU pathway
    # (ii) waste emissions from the CCU production production pathway
    # (iii) environemental opportunity cost 
    #The denominator consists of the CO2 utilized in producing the product
    
    climate_ROI_array_WITHOUT_EOC=\
    (conventional_pathway_CO2_intensity_array\
     +CCU_byproduct_CO2_emissions_array\
     -CCU_input_inventory_CO2_emissions_array\
     -CCU_waste_CO2_emissions_array)/np.array(CO2_Utilized_list)
    
    climate_ROI_array_WITH_EOC=\
    (conventional_pathway_CO2_intensity_array\
     +CCU_byproduct_CO2_emissions_array\
     -CCU_input_inventory_CO2_emissions_array\
     -CCU_waste_CO2_emissions_array-CO2_EOC_array)/np.array(CO2_Utilized_list)
    
   
    return climate_ROI_array_WITHOUT_EOC, climate_ROI_array_WITH_EOC

def f_harmonize_concrete_literature_data (df):
    

    df.fillna(0, inplace=True)
    df.replace(to_replace =['NA','No'], value=0)

    #The following three lines of code ensure that the 
    #(i) 'CCU SCM (kg/m3)' column will contain only the values of the slag inventory 
    # (ii) 'CCU SCM Type' column will contain only the fly ash nventory value.
    #This ensures that we can multiply the 'CCU SCM (kg/m3)' by the slag CO2 intensity value
    #and the 'CCU SCM Type' column by the fly ash CO2 intensity value
    
    #If the 'CCU SCM Type' column is fly ash populate it with the inventory value of fly ash from the 
    #'CCU SCM (kg/m3)' column
    df.loc[(df['CCU SCM Type'] == 'Fly Ash'), 'CCU SCM Type']=df['CCU SCM (kg/m3)']
    
    #Since the fly ash inventory value has been duplicated in the 'CCU SCM Type' column (previous line of
    #code) replace the original fly ash inventory value in the 'CCU SCM (kg/m3)' with zero
    df.loc[(df['CCU SCM Type']==df['CCU SCM (kg/m3)']),'CCU SCM (kg/m3)']=0
    
    #Since the 'CCU SCM Type' column is supposed to contain only the numerical values of the 'fly ash'
    #inventory, replace the 'Slag' entries with zero
    df.loc[(df['CCU SCM Type']=='Slag'),'CCU SCM Type']=0
    
    #If the 'Conventional SCM Type' column is fly ash populate it with the inventory value of fly ash from the 
    #'CCU SCM (kg/m3)' column
    df.loc[(df['Conventional SCM Type'] == 'Fly Ash'), 'Conventional SCM Type']=df['Conventional SCM (kg/m3)']
    
    #Since the fly ash inventory value has been duplicated in the 'Conventional SCM Type' column (previous line of
    #code) replace the original fly ash inventory value in the 'Conventional SCM (kg/m3)' with zero
    df.loc[(df['Conventional SCM Type']==df['Conventional SCM (kg/m3)']),'Conventional SCM (kg/m3)']=0
    
    #Since the 'Conventional SCM Type' column is supposed to contain only the numerical values of the 'fly ash'
    #inventory, replace the 'Slag' entries with zero
    df.loc[(df['Conventional SCM Type']=='Slag'),'Conventional SCM Type']=0
    
    return df

def f_duplicate_CO2_Utilization_column(df,column_name_CO2_Utilized_Duplicate,column_name_concrete_CO2_utilized):
    #Add three columns to the dataframe which contain the CO2 utilized value.
    #This duplication is required for the matrix mutiplication to determine the CO2 emissions from the following three 
    #processes which are dependent on the CO2 utilized 
    #(1) CO2 injection
    #(2) CO2 vaporization
    #(3) 10% not captured at the power plant

    for i in range(1,4):
        df.insert(len(df.columns),column_name_CO2_Utilized_Duplicate+str(i),df[column_name_concrete_CO2_utilized]) 

    return df

def f_get_concrete_compressive_strength_distribution(df,number_of_samples,column_name_Compressive_strength_range_LB,\
                                                     column_name_Compressive_strength_range_UB):
       
    #The code geenrates a uniform distribution of the compressive strenght through the equation
    #uniform distribution=LB+(UB-LB)*UD(0,1), where LB and UB are the lower and upper bounds
    #of the compressive strength and UD is a uniform distribution between 0 and 1
    comp_strength_UB_minus_LB_array=np.array([(df[column_name_Compressive_strength_range_UB]-df[column_name_Compressive_strength_range_LB]).tolist()])

    uniform_distribution_zero_to_one=np.array([f_get_uniform_distribution(0,1,number_of_samples)])

    comp_strength_delta_array=np.transpose(comp_strength_UB_minus_LB_array)*uniform_distribution_zero_to_one
    
    comp_strength_LB_array=np.array([df[column_name_Compressive_strength_range_LB].tolist()])
    
    comp_strength_distribution_array=np.transpose(comp_strength_LB_array)+comp_strength_delta_array
    
    
    return comp_strength_distribution_array  
 
            
def f_get_concrete_input_inventory_CO2_intensity_matrix(number_of_samples,number_of_columns):
    
      
    concrete_input_inventory_CO2_intensity_matrix=np.zeros((number_of_samples,number_of_columns))

    CO2_cement=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.cement_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.cement_CO2_intensity_sd,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,0] = CO2_cement
  
 
    CO2_coarse_agg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.coarse_agg_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.coarse_agg_CO2_intensity_sd,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,1] = CO2_coarse_agg
    
    CO2_fine_agg=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.fine_agg_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.fine_agg_CO2_intensity_sd,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,2] = CO2_fine_agg
    
    CO2_water=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.water_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.water_CO2_intensity_sd,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,3] = CO2_water

    CO2_Slag=7.7*f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.Pig_Iron_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.Pig_Iron_CO2_intensity_sd, number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,4] = CO2_Slag

    CO2_fly_ash=22.7*f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.Coal_Elec_CO2_intensity_mean, CO2_ROI_Constants_Wind_Elec.Coal_Elec_CO2_intensity_sd, number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,5] = CO2_fly_ash
    
    CO2_energy_penalty=f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_mean, CO2_ROI_Constants_Wind_Elec.CO2_emissions_CO2_Capture_with_MEA_sd,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,6] = CO2_energy_penalty
    
    CO2_steam_curing_CO2_emissions=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.steam_curing_LB, CO2_ROI_Constants_Wind_Elec.steam_curing_UB,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,7] = CO2_steam_curing_CO2_emissions
    
    Power_Required_CO2_Curing=CO2_ROI_Constants_Wind_Elec.Power_Required_CO2_Curing
    CCU_CO2_Curing_CO2_intensity_array=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CCU_CO2_Curing_Elec_CO2_intensity_LB,CO2_ROI_Constants_Wind_Elec.CCU_CO2_Curing_Elec_CO2_intensity_UB,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,8] = Power_Required_CO2_Curing*CCU_CO2_Curing_CO2_intensity_array
    
    CO2_CO2_Injection=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CCU_Injection_Elec_CO2_Intensity_LB,CO2_ROI_Constants_Wind_Elec.CCU_Injection_Elec_CO2_Intensity_UB,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,9] = CO2_CO2_Injection
    
    CO2_CO2_Vaporization=f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.CCU_Vaporization_Elec_CO2_Intensity_LB,CO2_ROI_Constants_Wind_Elec.CCU_Vaporization_Elec_CO2_Intensity_UB,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,10] = CO2_CO2_Vaporization
    
    #Represents the 10% of the CO2 emissions that is not captured by the MEA system
    CO2_CO2_Not_Captured=f_get_uniform_distribution(1/9,1/9,number_of_samples)
    concrete_input_inventory_CO2_intensity_matrix[:,11] = CO2_CO2_Not_Captured
    
    return concrete_input_inventory_CO2_intensity_matrix

def f_get_climate_ROI_for_concrete_list(excel_sheet_name,\
                                        dataset_category,\
                                        column_name_conventional_concrete_first_input_parameter,\
                                        column_name_conventional_concrete_last_input_parameter,\
                                        column_name_conventional_Compressive_strength_range_LB,\
                                        column_name_conventional_Compressive_strength_range_UB,\
                                        column_name_conventional_CO2_Utilized_Duplicate,\
                                        column_name_conventional_concrete_CO2_utilized,\
                                        column_name_CCU_concrete_first_input_parameter,\
                                        column_name_CCU_concrete_last_input_parameter,\
                                        column_name_CCU_Compressive_strength_range_LB,\
                                        column_name_CCU_Compressive_strength_range_UB,\
                                        column_name_CCU_CO2_Utilized_Duplicate,\
                                        column_name_CCU_concrete_CO2_utilized):
    
    concrete_un_harmonized_df = pd.read_excel(CO2_ROI_Constants_Wind_Elec.excel_file, excel_sheet_name)
    
    concrete_harmonized_df = f_harmonize_concrete_literature_data(concrete_un_harmonized_df)
    
    #Filter the rows for the specific concrete dataset catgory
    concrete_input_inventory_harmonized_df = \
    concrete_harmonized_df.loc[concrete_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_category].isin([dataset_category])]
    
    #Get the CO2 utilized for concrete. The CO2 values will be used to calculate the climate ROI 
    CO2_Utilized_CCU_concrete_array=\
    np.transpose(np.array([concrete_input_inventory_harmonized_df[column_name_CCU_concrete_CO2_utilized].values.tolist()]))
    
    #Get the number of datasets in a specific catagory of CCU concrete
    number_of_datasets_for_CCU_concrete=concrete_input_inventory_harmonized_df.shape[0]
    
    concrete_input_inventory_harmonized_df=\
    f_duplicate_CO2_Utilization_column(concrete_input_inventory_harmonized_df,\
                                       column_name_CCU_CO2_Utilized_Duplicate,column_name_CCU_concrete_CO2_utilized)
    
    concrete_input_inventory_harmonized_df=\
    f_duplicate_CO2_Utilization_column(concrete_input_inventory_harmonized_df,\
                                       column_name_conventional_CO2_Utilized_Duplicate,column_name_conventional_concrete_CO2_utilized)
    
    #Get the CO2 intensity of the inventory items used to produce conventiona/CCU concrete
    #(same for conventional and CCU concrete)
    concrete_input_inventory_CO2_intensity_array=f_get_concrete_input_inventory_CO2_intensity_matrix(\
                                                    int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_concrete)),\
                                                    CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3)
    
    #Get the compressive strength distribution for CCU concrete
    CCU_comp_strength_distribution = f_get_concrete_compressive_strength_distribution(concrete_input_inventory_harmonized_df,\
                                                                                  int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_concrete)),\
                                                                                  column_name_CCU_Compressive_strength_range_LB,\
                                                                                  column_name_CCU_Compressive_strength_range_UB)

    #Get the compressive strength distribution for conventional concrete
    conventional_comp_strength_distribution = f_get_concrete_compressive_strength_distribution(concrete_input_inventory_harmonized_df,\
                                                                                  int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_concrete)),\
                                                                                  column_name_conventional_Compressive_strength_range_LB,\
                                                                                  column_name_conventional_Compressive_strength_range_UB)

   
    percentage_change_comp_strength=((CCU_comp_strength_distribution-conventional_comp_strength_distribution)\
                                    /CCU_comp_strength_distribution)*100
    
    #Get the inventory items, which were used to produce CCU concrete
    CCU_concrete_input_inventory_array=np.zeros((number_of_datasets_for_CCU_concrete,\
                                                 CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3))
    CCU_concrete_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete]=\
        np.array(concrete_input_inventory_harmonized_df.loc[:,column_name_CCU_concrete_first_input_parameter:\
                                                        column_name_CCU_concrete_last_input_parameter].values.tolist())
        
    #Get the inventory items, which were used to produce conventional concrete
    conventional_concrete_input_inventory_array=np.zeros((number_of_datasets_for_CCU_concrete,\
                                                 CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3))
    
    conventional_concrete_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete]=\
        np.array(concrete_input_inventory_harmonized_df.loc[:,column_name_conventional_concrete_first_input_parameter:\
                                                        column_name_conventional_concrete_last_input_parameter].values.tolist())

   #Append the last three columns which are required to account for the CO2 emissions from (1)CO2 injection
   #(2) CO2 vaporization and (3)10% not captured at the power plant
    CCU_concrete_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete:\
                                       CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3]=\
                                       np.array(concrete_input_inventory_harmonized_df[\
                                      [CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate1,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate2,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate3]].values.tolist())
    
    #Append the last three columns which are required to account for the CO2 emissions from (1)CO2 injection
    #(2) CO2 vaporization and (3)10% not captured at the power plant
    conventional_concrete_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete:\
                                       CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3]=\
                                       np.array(concrete_input_inventory_harmonized_df[\
                                      [CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate1,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate2,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate3]].values.tolist())
    

    conventional_concrete_kg_CO2_per_MPa=(conventional_concrete_input_inventory_array.dot(np.transpose(concrete_input_inventory_CO2_intensity_array)))/conventional_comp_strength_distribution
    
    CCU_concrete_kg_CO2_per_MPa = (CCU_concrete_input_inventory_array.dot(np.transpose(concrete_input_inventory_CO2_intensity_array)))/CCU_comp_strength_distribution
  
    Climate_ROI_Concrete_array=(conventional_concrete_kg_CO2_per_MPa-CCU_concrete_kg_CO2_per_MPa)/CO2_Utilized_CCU_concrete_array
    
   
    return Climate_ROI_Concrete_array, percentage_change_comp_strength



def f_get_delta_indices_chemical(CCU_chemical_name,CCU_chemical_production_route,\
                                        CO2_emissions_chemicals_conventional_pathway_mean, \
                                        CO2_emissions_chemicals_conventional_pathway_sd,\
                                        distribution_type,\
                                        EOC_Included):
    
    excel_tab_df = pd.read_excel(CO2_ROI_Constants_Wind_Elec.excel_file, sheet_name=CO2_ROI_Constants_Wind_Elec.sheet_name_chemicals)
    
    #filter the rows for the specific chemical and production route
    CCU_input_inventory_un_harmonized_df = \
    excel_tab_df[(excel_tab_df[CO2_ROI_Constants_Wind_Elec.column_name_CCU_Product]==CCU_chemical_name) & \
                 (excel_tab_df[CO2_ROI_Constants_Wind_Elec.column_name_Production_Route]==CCU_chemical_production_route)]
    

    
    #get the CO2 utilized for this chemical from the original and unhamronized data. 
    #The CO2 values will be used to calculate the climate ROI 
    CO2_Utilized_array=\
        np.transpose(np.array([CCU_input_inventory_un_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input].values.tolist()]))
    
   
    #In the harmonization, the CO2 utiilized value in the dataset is set to zero when the energy values for carbon capture
    # are provided in the dataset. This is done to avoid double counting as the energy penalty is either calculated from the
    #energy values for carbon capture provided in the study OR from the CO2 utilized value
    CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df = f_harmonize_literature_data(excel_tab_df)
    CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df = \
        CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[\
            (CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CCU_Product]\
             ==CCU_chemical_name) \
            & \
            (CCU_input_byproduct_waste_inventory_ALL_chemcials_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_Production_Route]\
             ==CCU_chemical_production_route)]
    
    #Get the number of datasets for a specific chemical and produciton route
    number_of_datasets_for_CCU_chemical=CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.shape[0]
    
    print('number_of_datasets_for_CCU_chemical:',number_of_datasets_for_CCU_chemical)
    
#    tt= (int(round(CO2_ROI_Constants_Wind_Elec.number_of_samples/number_of_datasets_for_CCU_chemical)))
    
#    print('CO2_Utilized_array:',CO2_Utilized_array)
    
#    CO2_Utilized_array = np.repeat(CO2_Utilized_array,repeats=[tt],axis=0)
    
    #Get the CO2 internsity of the inventory items used to produce the chemical through the CCU pathway
    CCU_input_inventory_CO2_intensity_array=\
    f_get_chemical_input_inventory_CO2_intensity_array\
    (CO2_ROI_Constants_Wind_Elec.number_of_samples,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters+1)
    
    print('CCU_input_inventory_CO2_intensity_array.shape:',CCU_input_inventory_CO2_intensity_array.shape)
#    print('CCU_input_inventory_CO2_intensity_array:',CCU_input_inventory_CO2_intensity_array)
    
    #Get the inventory items, which were used to produce the chemical through the CCU pathway
    CCU_input_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters+1))
    CCU_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters]=\
    np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc[:,CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input:CO2_ROI_Constants_Wind_Elec.column_name_Activated_Carbon_Input].values.tolist())

    #Add an extra column to the inventory array account for the 10% of the CO2 emissions not captured by the MEA system
    CCU_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters]=np.array(CCU_input_inventory_un_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input].values.tolist())/9

    #CCU_input_inventory_array = np.repeat(CCU_input_inventory_array,repeats=[tt],axis=0)
    
    #Obtain the CO2 emissions from producing the chemical conventionally
    conventional_pathway_CO2_intensity_array=\
        f_get_monte_carlo_chemical_conventional_pathway_CO2_intensity_matrix(\
        CO2_ROI_Constants_Wind_Elec.number_of_samples,\
        1, CO2_emissions_chemicals_conventional_pathway_mean,\
        CO2_emissions_chemicals_conventional_pathway_sd,distribution_type)
        
    #The first column contains the H2 required (kg) and the second column contains the electrcity which was used to generate the 
    #After harmonization, the dataset either contains the H2 requirement in kg or the electrcity used for H2 electrolysis in kWh
    H2_inventory_array=np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df\
                            [[CO2_ROI_Constants_Wind_Elec.column_name_H2_Input,\
                              CO2_ROI_Constants_Wind_Elec.column_name_electricity_for_H2]].values.tolist())
        
    #Get the CO2 intensity of the waste emissions from the CCU production process
    CCU_waste_CO2_intensity_array=\
            f_get_monte_carlo_waste_CO2_intensity_matrix(CO2_ROI_Constants_Wind_Elec.number_of_samples,CO2_ROI_Constants_Wind_Elec.number_of_waste)
            
    #calculate the delta in the CO2 intensity between the US grid and wind electricity
    wind_elec_CO2_intensity_array=\
        np.transpose(np.array([f_get_lognormal_distribution(CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_mean, \
        CO2_ROI_Constants_Wind_Elec.CO2_emissions_wind_electricity_sd,\
        CO2_ROI_Constants_Wind_Elec.number_of_samples)]))
        
    US_elec_CO2_intensity_array=\
        np.transpose(np.array([f_get_uniform_distribution(CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_LB, \
        CO2_ROI_Constants_Wind_Elec.US_elec_CO2_intensity_UB,CO2_ROI_Constants_Wind_Elec.number_of_samples)]))
    
    delta_elec_CO2_intensity_array=US_elec_CO2_intensity_array-wind_elec_CO2_intensity_array
        
    most_important_input_parameter_array=np.zeros(number_of_datasets_for_CCU_chemical)  
    
    for i in range(number_of_datasets_for_CCU_chemical):
    
#        print('CCU_input_inventory_array.shape:',np.array([CCU_input_inventory_array[i]]).shape)
#        print('CCU_input_inventory_array[i]:',np.array([CCU_input_inventory_array[i]]))
        
        CCU_input_inventory_CO2_emissions_array=\
            CCU_input_inventory_CO2_intensity_array*np.array([CCU_input_inventory_array[i]])
        
#        print('CCU_input_inventory_CO2_emissions_array.shape:',CCU_input_inventory_CO2_emissions_array.shape)
        
        #Get the CO2 intensity of the byproducts (produced along with the CCU chemical)
        CCU_byproducts_CO2_intensity_array\
            =f_get_monte_carlo_byproducts_CO2_intensity_matrix(CO2_ROI_Constants_Wind_Elec.number_of_samples,\
             CO2_ROI_Constants_Wind_Elec.number_of_byproducts)
       
    
        #Get the values of the byproducts that were produced along with the chemical
        CCU_byproduct_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,\
                                                CO2_ROI_Constants_Wind_Elec.number_of_byproducts))
        CCU_byproduct_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_byproducts]=\
                 np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc\
                 [:,CO2_ROI_Constants_Wind_Elec.column_name_H2_byproduct_output:CO2_ROI_Constants_Wind_Elec.column_name_H2O_byproduct_output].values.tolist())
       
#        print('CCU_byproduct_inventory_array.shape', CCU_byproduct_inventory_array.shape)
#        print('CCU_byproduct_inventory_array', CCU_byproduct_inventory_array)
    #    CCU_byproduct_inventory_array = np.repeat(CCU_byproduct_inventory_array,repeats=[tt],axis=0)
    
    
#        print('CCU_byproducts_CO2_intensity_array.shape', CCU_byproducts_CO2_intensity_array.shape)
#        print('CCU_byproducts_CO2_intensity_array', CCU_byproducts_CO2_intensity_array)
        
        CCU_byproduct_CO2_emissions_array=\
            CCU_byproducts_CO2_intensity_array*np.array([CCU_byproduct_inventory_array[i]])
        
    
#        print('CCU_byproduct_CO2_emissions_array.shape', CCU_byproduct_CO2_emissions_array.shape)
        

        #Get the values of the wastes that were produced along with the chemical
        CCU_waste_inventory_array=np.zeros((number_of_datasets_for_CCU_chemical,CO2_ROI_Constants_Wind_Elec.number_of_waste))
        
        CCU_waste_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_waste]=\
        np.array(CCU_input_byproduct_waste_inventory_for_specific_chemical_harmonized_df.loc\
        [:,CO2_ROI_Constants_Wind_Elec.column_name_CO2_emissions_waste:CO2_ROI_Constants_Wind_Elec.column_name_CO_emissions_waste].values.tolist())
        
    #    CCU_waste_inventory_array = np.repeat(CCU_waste_inventory_array,repeats=[tt],axis=0)
        
#        print('CCU_waste_CO2_intensity_array.shape', CCU_waste_CO2_intensity_array.shape)
#        print('CCU_waste_CO2_intensity_array', CCU_waste_CO2_intensity_array)
        
#        print('CCU_waste_inventory_array.shape', CCU_waste_inventory_array.shape)
#        print('CCU_waste_inventory_array', CCU_waste_inventory_array)
        
        CCU_waste_CO2_emissions_array=CCU_waste_CO2_intensity_array*np.array([CCU_waste_inventory_array[i]])
        
#        print('CCU_waste_CO2_emissions_array.shape', CCU_waste_CO2_emissions_array.shape)
#        print('CCU_waste_CO2_emissions_array', CCU_waste_CO2_emissions_array)
        

        
#        print('conventional_pathway_CO2_intensity_array.shape', conventional_pathway_CO2_intensity_array.shape)
#        print('conventional_pathway_CO2_intensity_array', conventional_pathway_CO2_intensity_array)
        

           
#        print('np.array([H2_inventory_array[0]]).shape', np.array([H2_inventory_array[i]]).shape)
#        print('np.array([H2_inventory_array[0]])', np.array([H2_inventory_array[i]]))
    
    #    H2_inventory_array = np.repeat(H2_inventory_array,repeats=[tt],axis=0)
        

        
        #The first column in EOC array will be multipied by the H2 values (kg) from the H2 inventory array
        EOC_array=np.zeros((CO2_ROI_Constants_Wind_Elec.number_of_samples,2))
          
        EOC_array[:,0]=(delta_elec_CO2_intensity_array*CO2_ROI_Constants_Wind_Elec.electricity_H2_electrolysis_kWh)[:,0]
        #The second column will be multipied by the electrcity required for H2 generation (kWh) from the H2 inventory array
        EOC_array[:,1]=(delta_elec_CO2_intensity_array)[:,0]
    
        
#        print('EOC_array.shape', EOC_array.shape)
#        print('EOC_array', EOC_array)
        
        #Calculate the CO2 values of the environmental opportunity cost (EOC)
        CO2_EOC_array= np.array([H2_inventory_array[i]])*EOC_array
        
#        print('CO2_EOC_array.shape', CO2_EOC_array.shape)
#        print('CO2_EOC_array', CO2_EOC_array)
    
        
        input_array= \
            np.hstack((\
                       CCU_input_inventory_CO2_emissions_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters],\
                       CCU_byproduct_CO2_emissions_array,\
                       CCU_waste_CO2_emissions_array))
    #    input_array= np.hstack((CCU_input_inventory_CO2_emissions_array,CCU_byproduct_CO2_emissions_array,CCU_waste_CO2_emissions_array))
        
#        print('input_array.shape    :')
#        print(input_array.shape)
#        print('input_array    :')
#        print(np.sum(input_array, axis=1))
#        print('conventional_pathway_CO2_intensity_array.shape    :', conventional_pathway_CO2_intensity_array.shape)
#        print('CCU_input_inventory_CO2_emissions_array.shape    :', CCU_input_inventory_CO2_emissions_array.shape)
#        print('CCU_input_inventory_CO2_intensity_array    :')
#        print(np.sum(CCU_input_inventory_CO2_intensity_array, axis=1))
        
#        print('CCU_byproduct_CO2_emissions_array    :')
#        print(np.sum(CCU_byproduct_CO2_emissions_array, axis=1))
        
#        print('CCU_waste_CO2_emissions_array    :')
#        print(np.sum(CCU_waste_CO2_emissions_array, axis=1))
#        print('CCU_byproduct_CO2_emissions_array.shape    :', CCU_byproduct_CO2_emissions_array.shape)
#        print('CCU_waste_CO2_emissions_array.shape    :', CCU_waste_CO2_emissions_array.shape)
#        print('np.array([CO2_Utilized_array[0]]).shape    :', np.array([CO2_Utilized_array[i]]))
        
        
        if(EOC_Included==CO2_ROI_Constants_Wind_Elec.EOC_No): 
            output_array= \
                    np.hstack((\
                               conventional_pathway_CO2_intensity_array/np.array([CO2_Utilized_array[i]]),\
                               -CCU_input_inventory_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                               CCU_byproduct_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                               -CCU_waste_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                               ))
               
            
               
        else:    
             output_array= \
                np.hstack((\
                           conventional_pathway_CO2_intensity_array/np.array([CO2_Utilized_array[i]]),\
                           -CCU_input_inventory_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                           CCU_byproduct_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                           -CCU_waste_CO2_emissions_array/np.array([CO2_Utilized_array[i]]),\
                           -CO2_EOC_array/np.array([CO2_Utilized_array[i]])\
                           ))


    #    output_array= np.hstack((-CCU_input_inventory_CO2_emissions_array,CCU_byproduct_CO2_emissions_array,-CCU_waste_CO2_emissions_array))
        
#        print('output_array.shape    :', output_array.shape)
    
        
        output_array1=np.sum(output_array,axis=1)
#        print('output_array1    :')
        print(output_array1)
        
        
        x_problem = {
        'num_vars':57,
        'names':   [
    #                'CO2 utilized',\
    #                'conventional emissions',\
                    CO2_ROI_Constants_Wind_Elec.column_name_CO2_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2O_as_analyte_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2O_for_cooling_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_NaOH_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_HCl_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_NaCl_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_for_CO2_capture_MJ,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_for_CO2_capture_kWh_Th,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Electricity_for_CO2_capture_kWh,\
                    CO2_ROI_Constants_Wind_Elec.column_name_electricity_for_H2,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Electricity_for_main_reaction_kWh_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Natural_Gas_kg_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Natural_Gas_m3_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_kWh_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_MJ_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_MJ_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_kg_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_kWh_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Methanol_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Ammonia_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Ethylene_Oxide_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Platinum_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Niobium_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Aniline_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Propylene_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Glycerol_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Mono_Propylene_Glycol_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Naptha_Burned_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Refrigerant_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Activated_Carbon_Input,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2_byproduct_output,\
                    CO2_ROI_Constants_Wind_Elec.column_name_O2_byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_kg_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_MJ_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Steam_kWth_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_MJ_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Heat_kWh_Byproduct ,\
                    CO2_ROI_Constants_Wind_Elec.column_name_HCOONa_Byproduct ,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Na2CO3_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Na2SO4_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Ethylene_Glycol_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Ethylene_Carbonate_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Naphtha_Byproduct,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2O_byproduct_output,\
                    CO2_ROI_Constants_Wind_Elec.column_name_CO2_emissions_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Waste_water_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Flue_gas_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_zeolite_inert_landfill_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Methanol_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_O2_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_N2_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_H2O_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Ammonia_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Acetaldehyde_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_Aniline_waste,\
                    CO2_ROI_Constants_Wind_Elec.column_name_CO_emissions_waste\
                    ],
                
        }
                
       
        Si = delta.analyze(x_problem,input_array,output_array1,conf_level=0.95, print_to_console=False)
            
        performance = Si['delta']
        print(performance)
        print(list(performance).index(max(list(performance)))+1)
        
        most_important_input_parameter_array[i]=list(performance).index(max(list(performance)))+1

    
    return most_important_input_parameter_array
    
def f_get_delta_indices_concrete(excel_sheet_name,\
                                        dataset_category,\
                                        column_name_conventional_concrete_first_input_parameter,\
                                        column_name_conventional_concrete_last_input_parameter,\
                                        column_name_conventional_Compressive_strength_range_LB,\
                                        column_name_conventional_Compressive_strength_range_UB,\
                                        column_name_conventional_CO2_Utilized_Duplicate,\
                                        column_name_conventional_concrete_CO2_utilized,\
                                        column_name_CCU_concrete_first_input_parameter,\
                                        column_name_CCU_concrete_last_input_parameter,\
                                        column_name_CCU_Compressive_strength_range_LB,\
                                        column_name_CCU_Compressive_strength_range_UB,\
                                        column_name_CCU_CO2_Utilized_Duplicate,\
                                        column_name_CCU_concrete_CO2_utilized):
    
    concrete_un_harmonized_df = pd.read_excel(CO2_ROI_Constants_Wind_Elec.excel_file, excel_sheet_name)
    
    concrete_harmonized_df = f_harmonize_concrete_literature_data(concrete_un_harmonized_df)
    
    #Filter the rows for the specific concrete dataset catgory
    concrete_input_inventory_harmonized_df = \
    concrete_harmonized_df.loc[concrete_harmonized_df[CO2_ROI_Constants_Wind_Elec.column_name_category].isin([dataset_category])]
    
    #Get the CO2 utilized for concrete. The CO2 values will be used to calculate the climate ROI 
    CO2_Utilized_CCU_concrete_array=\
    np.transpose(np.array([concrete_input_inventory_harmonized_df[column_name_CCU_concrete_CO2_utilized].values.tolist()]))
    
    #Get the number of datasets in a specific catagory of CCU concrete
    number_of_datasets_for_CCU_concrete=concrete_input_inventory_harmonized_df.shape[0]
    
    concrete_input_inventory_harmonized_df=\
    f_duplicate_CO2_Utilization_column(concrete_input_inventory_harmonized_df,\
                                       column_name_CCU_CO2_Utilized_Duplicate,column_name_CCU_concrete_CO2_utilized)
    
    concrete_input_inventory_harmonized_df=\
    f_duplicate_CO2_Utilization_column(concrete_input_inventory_harmonized_df,\
                                       column_name_conventional_CO2_Utilized_Duplicate,column_name_conventional_concrete_CO2_utilized)
    
    #Get the CO2 intensity of the inventory items used to produce conventiona/CCU concrete
    #(same for conventional and CCU concrete)
    concrete_input_inventory_CO2_intensity_array=f_get_concrete_input_inventory_CO2_intensity_matrix(\
                                                    CO2_ROI_Constants_Wind_Elec.number_of_samples,\
                                                    CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3)
    

   
    #Get the compressive strength distribution for CCU concrete
    CCU_comp_strength_distribution = f_get_concrete_compressive_strength_distribution(concrete_input_inventory_harmonized_df,\
                                                                                  CO2_ROI_Constants_Wind_Elec.number_of_samples,\
                                                                                  column_name_CCU_Compressive_strength_range_LB,\
                                                                                  column_name_CCU_Compressive_strength_range_UB)

    #Get the compressive strength distribution for conventional concrete
    conventional_comp_strength_distribution = f_get_concrete_compressive_strength_distribution(concrete_input_inventory_harmonized_df,\
                                                                                  CO2_ROI_Constants_Wind_Elec.number_of_samples,\
                                                                                  column_name_conventional_Compressive_strength_range_LB,\
                                                                                  column_name_conventional_Compressive_strength_range_UB)

   
#    percentage_change_comp_strength=((CCU_comp_strength_distribution-conventional_comp_strength_distribution)\
#                                    /CCU_comp_strength_distribution)*100
    
    #Get the inventory items, which were used to produce CCU concrete
    CCU_concrete_input_inventory_array=np.zeros((number_of_datasets_for_CCU_concrete,\
                                                 CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3))
    CCU_concrete_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete]=\
        np.array(concrete_input_inventory_harmonized_df.loc[:,column_name_CCU_concrete_first_input_parameter:\
                                                        column_name_CCU_concrete_last_input_parameter].values.tolist())


    #Get the inventory items, which were used to produce conventional concrete
    conventional_concrete_input_inventory_array=np.zeros((number_of_datasets_for_CCU_concrete,\
                                                 CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3))
    
    conventional_concrete_input_inventory_array[:,0:CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete]=\
        np.array(concrete_input_inventory_harmonized_df.loc[:,column_name_conventional_concrete_first_input_parameter:\
                                                        column_name_conventional_concrete_last_input_parameter].values.tolist())


    #Append the last three columns which are required to account for the CO2 emissions from (1)CO2 injection
   #(2) CO2 vaporization and (3)10% not captured at the power plant
    CCU_concrete_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete:\
                                       CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3]=\
                                       np.array(concrete_input_inventory_harmonized_df[\
                                      [CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate1,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate2,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_CCU_CO2_Utilized_Duplicate3]].values.tolist())
    
    #Append the last three columns which are required to account for the CO2 emissions from (1)CO2 injection
    #(2) CO2 vaporization and (3)10% not captured at the power plant
    conventional_concrete_input_inventory_array[:,CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete:\
                                       CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3]=\
                                       np.array(concrete_input_inventory_harmonized_df[\
                                      [CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate1,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate2,\
                                       CO2_ROI_Constants_Wind_Elec.column_name_conventional_CO2_Utilized_Duplicate3]].values.tolist())
    

#    conventional_concrete_kg_CO2_per_MPa=(conventional_concrete_input_inventory_array.dot(np.transpose(concrete_input_inventory_CO2_intensity_array)))/conventional_comp_strength_distribution
#    
#    CCU_concrete_kg_CO2_per_MPa = (CCU_concrete_input_inventory_array.dot(np.transpose(concrete_input_inventory_CO2_intensity_array)))/CCU_comp_strength_distribution
#  
#    Climate_ROI_Concrete_array=(conventional_concrete_kg_CO2_per_MPa-CCU_concrete_kg_CO2_per_MPa)/CO2_Utilized_CCU_concrete_array
    
#    print('Climate_ROI_Concrete_array.shape: ', Climate_ROI_Concrete_array.shape)

    concrete_input_inventory_CO2_intensity_array=f_get_concrete_input_inventory_CO2_intensity_matrix(\
                                                    CO2_ROI_Constants_Wind_Elec.number_of_samples,\
                                                    CO2_ROI_Constants_Wind_Elec.number_of_input_parameters_concrete+3)
    
 
#    print('**********************')
#    print('concrete_input_inventory_CO2_intensity_array    ',concrete_input_inventory_CO2_intensity_array)
#    print('conventional_concrete_input_inventory_array    ',conventional_concrete_input_inventory_array)
#    print('conventional_comp_strength_distribution  ',conventional_comp_strength_distribution)
#    print('conventional_comp_strength_distribution.shape  ',np.array([conventional_comp_strength_distribution[0]]).shape)
#    
#        
#    print('product  ',concrete_input_inventory_CO2_intensity_array*conventional_concrete_input_inventory_array[0])
    
    most_important_input_parameter_array=np.zeros(number_of_datasets_for_CCU_concrete)  
    
    for i in range(number_of_datasets_for_CCU_concrete):
    
        conventional_kg_CO2_per_MPa=(concrete_input_inventory_CO2_intensity_array*conventional_concrete_input_inventory_array[i])/np.transpose(np.array([conventional_comp_strength_distribution[i]]))
        CCU_kg_CO2_per_MPa=(concrete_input_inventory_CO2_intensity_array*CCU_concrete_input_inventory_array[i])/np.transpose(np.array([CCU_comp_strength_distribution[i]]))
        
        Climate_ROI_Concrete=(np.sum(conventional_kg_CO2_per_MPa,axis=1)-np.sum(CCU_kg_CO2_per_MPa,axis=1))/CO2_Utilized_CCU_concrete_array[i]
        
        output_array=Climate_ROI_Concrete
        
    #    obtain the Co2 emissions of the 9 input parameters. Remove the 3 extra columns were added
    #    during the harmonization for Co2 inhjection, vaportization and 10% Co2 emissions during Co2 capture
        conventional_kg_CO2_per_MPa_input_columns=conventional_kg_CO2_per_MPa[:,0:9]
        CCU_kg_CO2_per_MPa_input_columns=CCU_kg_CO2_per_MPa[:,0:9]
        
      
        input_array=np.hstack((conventional_kg_CO2_per_MPa_input_columns,CCU_kg_CO2_per_MPa_input_columns))
        
        x_problem = {
        'num_vars':18,
        'names':   []
        }
        
        Si = delta.analyze(x_problem,input_array,output_array,conf_level=0.95, print_to_console=False)
        
        performance = Si['delta']
#    print(performance)
#        print('i    ',i)
        print("index  :", list(performance).index(max(list(performance)))+1)
        
        most_important_input_parameter_array[i]=(list(performance).index(max(list(performance))))+1

    
    return most_important_input_parameter_array
    

    
#    return Climate_ROI_Concrete_array, percentage_change_comp_strength  
        
