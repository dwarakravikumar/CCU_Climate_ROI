1.	Introduction

The CCU_Climate_ROI code repository accompanies the manuscript titled “Assessing the Relative Climate Impact of Carbon dioxide Utilization for Concrete, Chemical and Mineral Production” authored by Dr. Dwarakanath Ravikumar, Dr. Gregory Keoleian, Dr. Shelie Miller and Dr. Volker Sick.

The code is used to determine and stochastically compare the climate return of investment (Climate ROI) of carbon, capture and utilization (CCU) for concrete, chemical and mineral production. The Climate ROI is quantified for 20 CCU pathways which includes 4 CCU concrete, 13 CCU chemical and 3 CCU mineral pathways. The Climate ROI is defined as the ratio of the net climate benefit generated per functional unit of the CCU pathway to the quantity of CO2 utilized per functional unit of the CCU pathway. In addition, the code is used to determine the key processes contributing to the net CO2 benefit of CCU concrete.

Beyond the baseline scenario (detailed above), the code quantifies and compares the climate ROI of the 20 CCU pathways in the scenarios wherein wind electricity and zero carbon heat is used to produce CCU concrete, chemicals and minerals.

The code was authored by Dr. Dwarakanath Ravikumar who can be contacted at dtriplic@nrel.gov

2.	Organization of the repository

The repository is organized into the following 3 folders 

Folder 1 - Scenario_baseline

This folder consists of the following files corresponding to the baseline scenario, whose results are presented in Figures 2, 3 and 4 in the main manuscript

CO2_ROI_Constants.py: This python file contains the constants required to quantify the climate ROI (Figure 3 manuscript) and the heat map analysis (Figures 4a and 4b manuscript), which is a stochastic comparison of the Climate ROI of the 20 CCU pathways.

Literature.xlsx: This file contains the life cycle inventory material and energy data for producing CCU concrete, chemicals and minerals. Please refer Section 2 of the supplementary information file accompanying the manuscript for more details. 

CO2_ROI_Heatmap_WITH_EOC.py and CO2_ROI_Heatmap_WITHOUT_EOC.py: These two python files plot the two heatmaps (Figure 4a and 4b manuscript), which stochastically compares the Climate ROI of the 20 CCU pathways. CO2_ROI_Heatmap_WITH_EOC.py quantifies the climate ROI and plots the heatmap after accounting for the environmental opportunity cost (EOC) of wind electricity, which is used to generate hydrogen in 7 CCU chemical pathways. The EOC of using wind electricity to generate the H2 is the CO2 that can potentially be avoided by offsetting fossil electricity when the wind electricity is instead supplied to the grid. CO2_ROI_Heatmap_WITHOUT_EOC.py plots the heatmap without accounting for the EOC.

CO2_ROI_KDE_Plot.py and CO2_ROI_KDE_Plot_Outliers.py: These two files plot the distribution of the Climate ROI (which is determined over 96,600 Monte Carlo runs) for the 20 CCU pathways. CO2_ROI_KDE_Plot.py plots the distribution of the climate ROI which are within the -15 to +15 in Figure 3 of the manuscript. CO2_ROI_KDE_Plot_Outliers.py plots the distribution of the climate ROI which are within the -1000 to -2000 as an inset plot in Figure 3 of the manuscript.

CO2_ROI_Proof_of_Concept.py:  This python file plots the scatter plot, the distribution of the Climate ROI and the heatmap for the two pathways – P11: Formic Acid and P2: Concrete – in Figure 2(a), Figure 2(b) and Figure 2(c) of the manuscript, respectively.

CO2_ROI_Delta_Index.py: This python file conducts a moment independent sensitivity analysis to determine the material and energy inventory items, which are the most significant drivers of the climate ROI of a CCU pathway (climate ROI hotspots). The moment independent sensitivity analysis calculates an  index value for each of the material and energy inventory items required to produce the CCU product and, thereby, contributes to the climate ROI of the CCU product. The inventory item with the highest  index value is the most significant contributor to the probability distribution function of the climate ROI.

CO2_ROI_Functions.py: This python file contains functions, which are required to determine the distributions for the Climate ROI, the heatmaps and the  indices from the moment independent sensitivity analysis.

Folder 2 - Scenario_wind_electricity

This folder consists of the following files, which are similar to those in the baseline scenario (above).

CO2_ROI_Constants.py: 

Literature.xlsx: 

CO2_ROI_Heatmap_WITH_EOC.py

CO2_ROI_Functions.py

The python files generate the heatmap in Supplementary Figure 2 in the supplementary information file for the scenario wherein wind electricity is used to produce CCU concrete, chemicals and minerals.


Folder 3 - Scenario_zero_carbon_heat

This folder consists of the following files, which are similar to those in the baseline scenario (above).

CO2_ROI_Constants.py

Literature.xlsx

CO2_ROI_Heatmap_WITH_EOC.py

CO2_ROI_Functions.py

The python files generate the heatmap in Supplementary Figure 3 in the supplementary information file for the scenario wherein zero carbon heat is used to produce CCU concrete, chemicals and minerals.



