'''
This Python file accompanies the manuscript titled 
“Assessing the Relative Climate Impact of Carbon dioxide Utilization for Concrete, Chemical and Mineral Production” 
authored by Dr. Dwarakanath Ravikumar, Dr. Gregory Keoleian, Dr. Shelie Miller and Dr. Volker Sick.

This python file contains constants which are required by the following files in the 'Scenario_baseline' folder
1. CO2_ROI_Heatmap_WITH_EOC.py
2. CO2_ROI_Heatmap_WITHOUT_EOC.py
3. CO2_ROI_KDE_Plot.py 
4. CO2_ROI_KDE_Plot_Outliers.py
5. CO2_ROI_Proof_of_Concept.py
6. CO2_ROI_Delta_Index.py   
7. CO2_ROI_Functions.py

@author: Dwarakanath Ravikumar
'''

excel_file = 'Literature.xlsx'
sheet_name='Concrete'
sheet_name_chemicals='Chemicals'
excel_column_conv_conc_strength_LB='Conventional - Compressive Strength LB'
excel_column_conv_conc_strength_UB='Conventional - Compressive Strength UB'
excel_column_CCU_conc_strength_LB='CCU - Compressive Strength LB'
excel_column_CCU_conc_strength_UB='CCU - Compressive Strength UB'
excel_column_CO2_utilized_LB='CO2 utilized - LB'
excel_column_CO2_utilized_UB='CO2 utilized - UB'
excel_column_CO2_cement='Cement'
font='Times New Roman'
fig_width=10
fig_height=15
number_of_products=20
number_of_products_for_proof_of_concept=2
font_size=24
font_style='normal'
font_weight='normal'
font_stretch='normal'
plot_columns=2
number_of_datasets_concrete_CO2_curing_OPC_only=50

number_of_samples=96600
number_of_input_parameters=31
number_of_byproducts=14
number_of_waste=12
output_image_name='CO2_ROI.png'
output_image_name_heatmap='Heatmap.png'
output_image_format='png'
cement_CO2_intensity_mean=0.948
cement_CO2_intensity_sd=0.15
scatter_dot_size=400
scatter_formic_acid_dot_size=200
scatter_concrete_mixing_dot_size=1
face_color='white'
spine_line_color='black'
spine_line_width= 2
kde_curve_width=1
kde_curve_width_WITH_EOC=5
xy_axis_width=0.5
xy_axis_color='grey'
subplot_wspace=0

concrete_Curing_OPC_only_color='rosybrown'
concrete_Curing_OPC_plus_SCM_color='red'
concrete_Mixing_OPC_only_color='darkred'
concrete_Mixing_OPC_plus_SCM_color='lightcoral'
formic_acid_Catalytic_reduction_of_CO2_with_H2_WITHOUT_EOC_color='green'
formic_acid_Catalytic_reduction_of_CO2_with_H2_WITH_EOC_color='green'
formic_acid_Electrolytic_reduction_of_CO2_with_H2_WITHOUT_EOC_color='magenta'
formic_acid_Electrolytic_reduction_of_CO2_with_H2_WITH_EOC_color='magenta'
polyol_NA_WITHOUT_EOC_color='blue'
polyol_NA_WITH_EOC_color='blue'
DMC_Ethylene_carbonate_transesterification_WITHOUT_EOC_color='saddlebrown'
DMC_Ethylene_carbonate_transesterification_WITH_EOC_color='saddlebrown'
DMC_Urea_transesterification_WITHOUT_EOC_color='black'
DMC_Urea_transesterification_WITH_EOC_color='black'
CO_Dry_Reforming_WITHOUT_EOC_color='orange'
CO_Dry_Reforming_WITH_EOC_color='orange'
CO_reverseWater_Gas_Shift_WITHOUT_EOC_color='deepskyblue'
CO_reverseWater_Gas_Shift_WITH_EOC_color='deepskyblue'
DME_NA_WITHOUT_EOC_color='lawngreen'
DME_NA_WITH_EOC_color='lawngreen'
kerosene_NA_WITHOUT_EOC_color='darkgray'
kerosene_NA_WITH_EOC_color='darkgray'
MeOH_Hydrogenation_of_CO2_WITHOUT_EOC_color='purple'
MeOH_Hydrogenation_of_CO2_WITH_EOC_color='purple'
MeOH_Electrolytic_reduction_of_CO2_WITHOUT_EOC_color='goldenrod'
MeOH_Electrolytic_reduction_of_CO2_WITH_EOC_color='goldenrod'
DMC_Electrochemical_reduction_of_CO2_with_MeOH_WITHOUT_EOC_color='olive'
DMC_Electrochemical_reduction_of_CO2_with_MeOH_WITH_EOC_color='olive'
methane_Hydrogenation_of_CO2_array_WITHOUT_EOC_color='teal'
methane_Hydrogenation_of_CO2_array_WITH_EOC_color='teal'
Mineralization_Without_Compressive_Strength_Flue_Gas_Color='silver'
Mineralization_Without_Compressive_Strength_CO2_Color='darkorange'
Mineralization_With_Compressive_Strength_Color='plum'

uniform_distribution='uniform'
lognormal_distribution='lognormal'

EOC_No='No'
EOC_Yes='Yes'

column_name_CCU_Product='CCU Product'
column_name_Production_Route='Production route'

column_name_CO2_Input='CO2 Input (kg)'
column_name_H2_Input='H2 Input (kg)'
column_name_H2O_as_analyte_Input='H2O as analyte Input (kg)'
column_name_H2O_for_cooling_Input='H2O for cooling Input (kg)'
column_name_NaOH_Input='NaOH Input (kg)'
column_name_HCl_Input='HCl Input (kg)'
column_name_NaCl_Input='NaCl Input (kg)'
column_name_Heat_for_CO2_capture_MJ='Heat for CO2 capture Input (MJ)'
column_name_Heat_for_CO2_capture_kWh_Th='Heat for CO2 capture Input (kWh-Th)'
column_name_Electricity_for_CO2_capture_kWh='Electricity for CO2 capture Input (kWh)'
column_name_electricity_for_H2='Electricity for H2 generation/Electrolytic reduction (kWh)'
column_name_Electricity_for_main_reaction_kWh_Input='Electricity Input for main reaction Input (kWh)'
column_name_Natural_Gas_kg_Input='Natural Gas Input (kg)'
column_name_Natural_Gas_m3_Input='Natural Gas Input (m3)'
column_name_Heat_kWh_Input='Heat Input (kWh)'
column_name_Heat_MJ_Input='Heat Input (MJ)'
column_name_Steam_MJ_Input='Steam Input (MJ)'
column_name_Steam_kg_Input='Steam Input (kg)'
column_name_Steam_kWh_Input='Steam Input (kWh)'
column_name_Methanol_Input='Methanol Input (kg)'
column_name_Ammonia_Input='Ammonia Input (kg)'
column_name_Ethylene_Oxide_Input='Ethylene Oxide Input (kg)'
column_name_Platinum_Input='Platinum Input (kg)'
column_name_Niobium_Input='Niobium Input (kg)'
column_name_Aniline_Input='Aniline Input (kg)'
column_name_Propylene_Input='Propylene Input (kg)'
column_name_Glycerol_Input='Glycerol Input (kg)'
column_name_Mono_Propylene_Glycol_Input='Mono Propylene Glycol Input (kg)'
column_name_Naptha_Burned_Input='Naptha Burned Input (kg)'
column_name_Refrigerant_Input='Refrigerant Input (kg)'
column_name_Activated_Carbon_Input='Activated Carbon Input (kg)'


column_name_H2_byproduct_output = 'H2 byproduct output (kg)'
column_name_O2_byproduct = 'O2 byproduct output (kg)'
column_name_Steam_kg_Byproduct = 'Steam output (kg)'
column_name_Steam_MJ_Byproduct = 'Steam output (MJ)'
column_name_Steam_kWth_Byproduct = 'Steam generated byproduct output (kWth)'
column_name_Heat_MJ_Byproduct = 'Heat output byproduct (MJ)'
column_name_Heat_kWh_Byproduct = 'Heat output byproduct (kWh)'
column_name_HCOONa_Byproduct = 'HCOONa output (kg)'
column_name_Na2CO3_Byproduct = 'Na2CO3 output (kg)'
column_name_Na2SO4_Byproduct = 'Na2SO4 output (kg)'
column_name_Ethylene_Glycol_Byproduct = 'Ethylene Glycol output (kg)'
column_name_Ethylene_Carbonate_Byproduct = 'Ethylene Carbonate output (kg)'
column_name_Naphtha_Byproduct = 'Naphtha output (kg)'
column_name_H2O_byproduct_output = 'H2O byproduct output (kg)'

column_name_CO2_emissions_waste='CO2 emissions waste (kg)'
column_name_Waste_water_waste='Waste water waste (kg)'
column_name_Flue_gas_waste='Flue gas waste (kg)'
column_name_zeolite_inert_landfill_waste = 'Waste zeolite inert landfill waste (kg)'
column_name_Methanol_waste='Methanol emissions waste (kg)'
column_name_O2_waste='O2 emissions waste (kg)'
column_name_N2_waste='N2 emissions waste (kg)'
column_name_H2O_waste='H2O emissions waste (kg)'
column_name_Ammonia_waste='Ammonia emissions waste (kg)'
column_name_Acetaldehyde_waste='Acetaldehyde emissions waste (kg)'
column_name_Aniline_waste='Aniline emissions waste (kg)'
column_name_CO_emissions_waste='CO emissions waste (kg)'

formic_acid='Formic Acid'
Catalytic_reduction_of_CO2_with_H2='Catalytic reduction of CO2 with H2'
Electrolytic_reduction_of_CO2='Electrolytic reduction of CO2'

MeOH='MeOH'
Hydrogenation_of_CO2='Hydrogenation of CO2'
Electrolytic_reduction_of_CO2='Electrolytic reduction of CO2'

CO='CO'
Dry_Reforming='Dry Reforming'
reverseWater_Gas_Shift='reverseWater-Gas-Shift'

DME='DME'
NA='NA1'

polyol='Polyol'
NA='NA1'

DMC='DMC'
Electrochemical_reduction_of_CO2_with_MeOH='Electrochemical reduction of CO2 with MeOH'
Ethylene_carbonate_transesterification='Ethylene carbonate transesterification'
Urea_transesterification='Urea transesterification'

Kerosene='Kerosene'
NA='NA1'

Methane='Methane'
Hydrogenation_of_CO2='Hydrogenation of CO2'

electricity_H2_electrolysis_kWh=58.3

Heat_to_electricity_LB=0.14
Heat_to_electricity_UB=0.25

Natural_gas_combined_cycle_elec_CO2_intensity_mean =0.458
Natural_gas_combined_cycle_elec_CO2_intensity_sd=0.036

CO2_Capture_Elec_Requirement_LB=0.016
CO2_Capture_Elec_Requirement_UB=0.036

CO2_Capture_Heat_Requirement_LB=3.60
CO2_Capture_Heat_Requirement_UB=4.43

#METHANOL MeOH CONSTANTS (all values per ton MeOH)
CO2_used_per_ton_CCU_MeOH_LB=1370
CO2_used_per_ton_CCU_MeOH_UB=1540

H2_used_per_ton_CCU_MeOH_LB=190
H2_used_per_ton_CCU_MeOH_UB=230

US_elec_CO2_intensity_LB=0.386
US_elec_CO2_intensity_UB=0.568

CO2_Capture_Heat_Requirement_LB=3.60
CO2_Capture_Heat_Requirement_UB=4.43

CO2_emissions_CCU_MeOH_without_H2_mean=19.9
CO2_emissions_CCU_MeOH_without_H2_sd=2.7

CO2_emissions_CCU_MeOH_with_H2_mean=716
CO2_emissions_CCU_MeOH_with_H2_sd=192

CO2_emissions_CCU_MeOH_with_env_opp_cost_mean=1160
CO2_emissions_CCU_MeOH_with_env_opp_cost_sd=198

CO2_emissions_Conv_MeOH_mean=537
CO2_emissions_Conv_MeOH_sd=63.1

#CO2_emissions_CO2_Capture_with_MEA_mean=0.221
#CO2_emissions_CO2_Capture_with_MEA_sd=0.022

CO2_emissions_CO2_Capture_with_MEA_mean=0.005
CO2_emissions_CO2_Capture_with_MEA_sd=0.0005

CO2_emissions_H2_Through_Electrolysis_mean=1.63
CO2_emissions_H2_Through_Electrolysis_sd=0.81

CO2_emissions_water_analyte_mean=0.0531
CO2_emissions_water_analyte_sd=0.015

CO2_emissions_water_cooling_mean=0.0014
CO2_emissions_water_cooling_sd=0.0003

CO2_emissions_NaOH_mean=1.36
CO2_emissions_NaOH_sd=0.088

CO2_emissions_HCl_mean=1.73
CO2_emissions_HCl_sd=0.341

CO2_emissions_NaCl_mean=0.252
CO2_emissions_NaCl_sd=0.08


CO2_emissions_heat_per_kWh_mean=0.413
CO2_emissions_heat_per_kWh_sd=0.0515

CO2_emissions_heat_per_MJ_mean=0.116
CO2_emissions_heat_per_MJ_sd=0.014

CO2_emissions_natural_gas_per_kg_mean=0.424
CO2_emissions_natural_gas_per_kg_sd=0.1

CO2_emissions_natural_gas_per_m3_mean=0.208
CO2_emissions_natural_gas_per_m3_sd=0.028

CO2_emissions_steam_per_kg_mean=0.234
CO2_emissions_steam_per_kg_sd=0.032

CO2_emissions_steam_per_MJ_mean=0.116
CO2_emissions_steam_per_MJ_sd=0.014


CO2_emissions_wind_electricity_mean=0.0279
CO2_emissions_wind_electricity_sd=0.0141

CO2_emissions_ammonia_mean=2.04
CO2_emissions_ammonia_sd=0.321

CO2_emissions_ethylene_oxide_mean=2.02
CO2_emissions_ethylene_oxide_sd=0.21

CO2_emissions_platinum_mean=27400
CO2_emissions_platinum_sd=3550

CO2_emissions_niobium_LB=12.5
CO2_emissions_niobium_UB=12.5

CO2_emissions_aniline_mean=5.48
CO2_emissions_aniline_sd=1.03

CO2_emissions_propylene_oxide_mean=5.15
CO2_emissions_propylene_oxide_sd=0.293

CO2_emissions_glycerol_mean=2.55
CO2_emissions_glycerol_sd=6.12

CO2_emissions_monopropylene_glycol_mean=4.68
CO2_emissions_monopropylene_glycol_sd=0.448

CO2_emissions_naphtha_mean=0.537
CO2_emissions_naphtha_sd=0.089

CO2_emissions_refrigerant_mean=101
CO2_emissions_refrigerant_sd=20.5

CO2_emissions_activated_carbon_mean=10.1
CO2_emissions_activated_carbon_sd=0.17

CO2_emissions_electricity_LB=0.386
CO2_emissions_electricity_UB=0.568

CO2_emissions_hydrogen_LB=11.2
CO2_emissions_hydrogen_UB=12

CO2_emissions_steam_mean=0.231
CO2_emissions_steam_sd=0.033

CO2_emissions_heat_mean=0.116
CO2_emissions_heat_sd=0.014

CO2_emissions_naphtha_mean=0.541
CO2_emissions_naphtha_sd=0.093

CO2_emissions_methane_mean=0.045
CO2_emissions_methane_sd=0.015

CO2_emissions_CO2_mean=1
CO2_emissions_CO2_sd=0

#***********CONVENTIONAL PRODUCT PRODUCTION PATHWAYS CO2 EMISSIONS *********
CO2_emissions_formic_acid_conventional_mean=3.2
CO2_emissions_formic_acid_conventional_sd=0.459

CO2_emissions_MeOH_conventional_mean=0.597
CO2_emissions_MeOH_conventional_sd=0.067

CO2_emissions_H2_conventional_LB = 11.2
CO2_emissions_H2_conventional_UB=12

CO2_emissions_O2_conventional_mean=0.609
CO2_emissions_O2_conventional_sd=0.0341

CO2_emissions_sodium_formate_conventional_mean=2.07    
CO2_emissions_sodium_formate_conventional_sd=0.2

CO2_emissions_soda_ash_conventional_mean=0.93    
CO2_emissions_soda_ash_conventional_sd=0.10

CO2_emissions_sodium_sulfate_conventional_mean=1.02   
CO2_emissions_sodium_sulfate_conventional_sd=0.104

CO2_emissions_ethylene_glycol_conventional_mean=1.86
CO2_emissions_ethylene_glycol_conventional_sd=0.369

CO2_emissions_ethylene_carbonate_conventional_mean=1.56
CO2_emissions_ethylene_carbonate_conventional_sd=0.205

CO2_emissions_naphtha_conventional_mean=0.541
CO2_emissions_naphtha_conventional_sd=0.093

CO2_emissions_water_conventional_mean=0.0014
CO2_emissions_water_conventional_sd=0.0003

CO2_emissions_CO_conventional_mean=2.1
CO2_emissions_CO_conventional_sd=0.165

CO2_emissions_DME_conventional_mean=1.31
CO2_emissions_DME_conventional_sd=0.142

CO2_emissions_DMC_conventional_LB=3.2
CO2_emissions_DMC_conventional_UB=3.2

CO2_emissions_polyol_conventional_mean=3.81
CO2_emissions_polyol_conventional_sd=0.051

CO2_emissions_kerosene_conventional_mean=0.577
CO2_emissions_kerosene_conventional_sd=0.099

#CO2_emissions_methane_conventional_mean=0.208
#CO2_emissions_methane_conventional_sd=0.028

CO2_emissions_methane_conventional_mean=0.045
CO2_emissions_methane_conventional_sd=0.015

#***********WASTE EMISSIONS CO2 EMISSIONS *********
CO2_emissions_waste_water_mean=0.4
CO2_emissions_waste_water_sd=0.11

CO2_emissions_waste_zeolite_mean=0.005
CO2_emissions_waste_zeolite_sd=0.001

#************CONCRETE INPUT INVENTORY CONSTANTS*********

excel_sheet_name_concrete='Concrete'
column_name_category='Category'
dataset_category_Curing_OPC_only='Curing OPC Only'
dataset_category_Curing_OPC_plus_SCM='Curing OPC+SCM'
dataset_category_Mixing_OPC_only='Mixing OPC Only'
dataset_category_Mixing_OPC_plus_SCM='Mixing OPC+SCM'
column_name_CCU_concrete_CO2_utilized='CCU CO2 utilized (kg/m3)'
column_name_CCU_first_input_parameter='CCU Cement (kg/m3)'
column_name_CCU_last_input_parameter='CCU Carbon curing (hours)'
column_name_CCU_Compressive_strength_range_LB='CCU Compressive strength range LB (MPa/m3)'
column_name_CCU_Compressive_strength_range_UB='CCU Compressive strength range UB (MPa/m3)'
column_name_CCU_CO2_Utilized_Duplicate='CCU CO2 Utilized Duplicate'
column_name_CCU_CO2_Utilized_Duplicate1='CCU CO2 Utilized Duplicate1'
column_name_CCU_CO2_Utilized_Duplicate2='CCU CO2 Utilized Duplicate2'
column_name_CCU_CO2_Utilized_Duplicate3='CCU CO2 Utilized Duplicate3'
column_name_CCU__CO2_utilized='CCU CO2 utilized (kg/m3)'

column_name_conventional_first_input_parameter='Conventional Cement (kg/m3)'
column_name_conventional_last_input_parameter='Conventional Carbon curing (hours)'
column_name_conventional_Compressive_strength_range_LB='Conventional Compressive strength range LB (MPa/m3)'
column_name_conventional_Compressive_strength_range_UB='Conventional Compressive strength range UB (MPa/m3)'
column_name_conventional_CO2_Utilized_Duplicate='Conventional CO2 Utilized Duplicate'
column_name_conventional_CO2_Utilized_Duplicate1='Conventional CO2 Utilized Duplicate1'
column_name_conventional_CO2_Utilized_Duplicate2='Conventional CO2 Utilized Duplicate2'
column_name_conventional_CO2_Utilized_Duplicate3='Conventional CO2 Utilized Duplicate3'
column_name_conventional_CO2_Utilized='Conventional CO2 utilized (kg/m3)'

number_of_input_parameters_concrete=9
Power_Required_CO2_Curing=38.8
injection_electricity=0.037
vaporization_electricity=0.0053

cement_CO2_intensity_mean=0.948
cement_CO2_intensity_sd=0.15

coarse_agg_CO2_intensity_mean=0.005
coarse_agg_CO2_intensity_sd=0.001

fine_agg_CO2_intensity_mean=0.004
fine_agg_CO2_intensity_sd=0.0004

water_CO2_intensity_mean=0.001
water_CO2_intensity_sd=0.0002

steam_curing_LB=39.55
steam_curing_UB=39.55

CCU_CO2_Curing_Elec_CO2_intensity_LB = 0.386
CCU_CO2_Curing_Elec_CO2_intensity_UB = 0.568

Pig_Iron_CO2_intensity_mean=2.18
Pig_Iron_CO2_intensity_sd=0.26

Coal_Elec_CO2_intensity_mean=1.24
Coal_Elec_CO2_intensity_sd=0.09

CCU_Injection_Elec_CO2_Intensity_LB = 0.386
CCU_Injection_Elec_CO2_Intensity_UB = 0.568

CCU_Vaporization_Elec_CO2_Intensity_LB = 0.386
CCU_Vaporization_Elec_CO2_Intensity_UB = 0.568

#************MINERALIZATION WITHOUT COMPRESSIVE STRENGTH CONSTANTS*********

excel_sheet_name_mineralization_without_compressive_strength_flue_gas='Mineral_No_Comp_Str_FlueGas'
excel_sheet_name_mineralization_without_compressive_strength_CO2='Mineral_No_Comp_Str_CO2'
excel_sheet_name_mineralization_with_compressive_strength='Mineral_WITH_Comp_Str_CO2'
number_of_input_parameters_mineralization_without_compressive_strength=25
number_of_input_parameters_mineralization_with_compressive_strength=25
conventional='conventional'
CCU='CCU'


column_name_CCU_mineralization_without_compressive_strength_flue_gas_CO2_utilized='CCU Flue Gas CO2 Emitted (kg)'
column_name_CCU_mineralization_without_compressive_strength_CO2_CO2_utilized='CCU CO2 Input (kg)'
column_name_CCU_mineralization_without_compressive_strength_flue_gas_first_input_parameter='CCU Cement (kg)'
column_name_CCU_mineralization_without_compressive_strength_CO2_first_input_parameter='CCU Cement (kg)'
column_name_CCU_mineralization_without_compressive_strength_flue_gas_last_input_parameter='CCU Carbon curing (hours)'
column_name_CCU_mineralization_without_compressive_strength_CO2_last_input_parameter='CCU Carbon curing (hours)'

column_name_conventional_mineralization_without_compressive_strength_flue_gas_CO2_utilized='Conventional Flue Gas CO2 Emitted (kg)'
column_name_conventional_mineralization_without_compressive_strength_CO2_CO2_utilized='Conventional CO2 Input (kg)'
column_name_conventional_mineralization_without_compressive_strength_flue_gas_first_input_parameter='Conventional Cement (kg)'
column_name_conventional_mineralization_without_compressive_strength_CO2_first_input_parameter='Conventional Cement (kg)'
column_name_conventional_mineralization_without_compressive_strength_flue_gas_last_input_parameter='Conventional Carbon curing (hours)'
column_name_conventional_mineralization_without_compressive_strength_CO2_last_input_parameter='Conventional Carbon curing (hours)'


column_name_conventional_mineralization_with_compressive_strength_first_input_parameter='Conventional Cement (kg)'
column_name_conventional_mineralization_with_compressive_strength_last_input_parameter='Conventional Carbon curing (hours)'
column_name_conventional_mineralization_with_compressive_strength_CO2_utilized='Conventional CO2 Input (kg)'
column_name_conventional_Compressive_strength_range_LB='Conventional Compressive strength range LB (MPa/m3)'
column_name_conventional_Compressive_strength_range_UB='Conventional Compressive strength range UB (MPa/m3)'
column_name_CCU_mineralization_with_compressive_strength_first_input_parameter='CCU Cement (kg)'
column_name_CCU_mineralization_with_compressive_strength_last_input_parameter='CCU Carbon curing (hours)'
column_name_CCU_mineralization_with_compressive_strength_CO2_utilized='CCU CO2 Input (kg)'
column_name_CCU_Compressive_strength_range_LB='CCU Compressive strength range LB (MPa/m3)'
column_name_CCU_Compressive_strength_range_UB='CCU Compressive strength range UB (MPa/m3)'


mineralization_electricity_CO2_Intensity_LB = 0.386
mineralization_electricity_CO2_Intensity_UB = 0.568

limestone_CO2_intensity_mean=0.00266
limestone_CO2_intensity_sd=0.0008

aluminum_CO2_intensity_mean=17
aluminum_CO2_intensity_sd=1.25

clay_CO2_intensity_mean=0.006
clay_CO2_intensity_sd=0.001

lignite_CO2_intensity_mean=0.525
lignite_CO2_intensity_sd=0.158

polystyrene_CO2_intensity_mean=3.61
polystyrene_CO2_intensity_sd=0.031

woodchips_CO2_intensity_mean=0.141
woodchips_CO2_intensity_sd=0.01

boron_CO2_intensity_mean=1.5
boron_CO2_intensity_sd=0

NH4Cl_CO2_intensity_mean=1.47
NH4Cl_CO2_intensity_sd=0.148

lime_CO2_intensity_mean=0.107
lime_CO2_intensity_sd=0.027

solid_waste_CO2_intensity_mean=0.005
solid_waste_CO2_intensity_sd=0.001

