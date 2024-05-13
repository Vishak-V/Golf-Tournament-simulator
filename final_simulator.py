# Import Libraries

import pandas as pd

import numpy as np

import random

from datetime import datetime

 

## Set max row display, Lets me see if all the data is in the right order if needed, normally set to 10

pd.set_option('display.max_rows', 100)

 

# Get rid of the warnings (there are a lot of them) and let me see all the rows of data)

import warnings

warnings.filterwarnings("ignore")

 

 

 

 

def golf_simulator(player_1_name, player_2_name, course_name, num_of_sims):

   

    print(f'{player_1_name} vs {player_2_name}')

    print('----------------------------------')

    ##### Pull in all the data we need

    # Open the excel file

    xls = pd.ExcelFile('Mens Golf Datebase.xlsx')

 

    # Pull in the Stroke Log

    AUB1 = pd.read_excel(xls, 'Auburn (9.9.2023)')

    AUB2 = pd.read_excel(xls, 'Auburn (9.26.23)')

    AUB3 = pd.read_excel(xls, 'Auburn (10.8.23)')

    AUB4 = pd.read_excel(xls, 'Auburn (10.10.23)')

    AUB5 = pd.read_excel(xls, 'Auburn (10.17.23)')

 

    MIZ1 = pd.read_excel(xls, 'Mizzou (09.05.23)')

    MIZ2 = pd.read_excel(xls, 'Mizzou (9.19.23)')

    MIZ3 = pd.read_excel(xls, 'Mizzou (9.26.23)')

    MIZ4 = pd.read_excel(xls, 'Mizzou (10.10.23)')

    MIZ5 = pd.read_excel(xls, 'Mizzou (10.08.23)')

   

    # Concat the logs together

    database = pd.concat([AUB1, AUB2], ignore_index=True)

    database = pd.concat([database, AUB3], ignore_index=True)

    database = pd.concat([database, AUB4], ignore_index=True)

    database = pd.concat([database, AUB5] , ignore_index=True)

 

    database = pd.concat([database, MIZ1] , ignore_index=True)

    database = pd.concat([database, MIZ2] , ignore_index=True)

    database = pd.concat([database, MIZ3] , ignore_index=True)

    database = pd.concat([database, MIZ4] , ignore_index=True)

    database = pd.concat([database, MIZ5] , ignore_index=True)

   

    # GET THE PAR LOG

    index = pd.read_csv (‘Tornament Par.csv')

 

    # GET THE Course Rating

    #CR = pd.read_excel(xls, 'Tournament Info')

    #CR = CR[['Tournament', 'Rating', 'Slope']]

   

########################################################

   

    # Get Course information

    par_df = TP[['Course', 'Hole', 'Round', 'Par']]

    par_df = par_df.loc[par_df['Round'] == "Rd 1"]

    par_df = par_df.loc[par_df['Course'] == course_name]

    par_df.drop(par_df.loc[par_df['Hole']=='RD'].index, inplace=True)

    par_df.drop(par_df.loc[par_df['Hole']=='OUT'].index, inplace=True)

    par_df.drop(par_df.loc[par_df['Hole']=='IN'].index, inplace=True)

    par_df = par_df.drop(["Course"], axis=1)

    par_df = par_df.drop(["Round"], axis=1)

   

########################################################

 

    #### Create Hole Variables

    hole_lst_test = par_df['Par'].tolist()

   

    # Hole lst

    hole_1 = hole_lst_test[0]

    hole_2 = hole_lst_test[1]

    hole_3 = hole_lst_test[2]

    hole_4 = hole_lst_test[3]

    hole_5 = hole_lst_test[4]

    hole_6 = hole_lst_test[5]

    hole_7 = hole_lst_test[6]

    hole_8 = hole_lst_test[7]

    hole_9 = hole_lst_test[8]

   

    hole_10 = hole_lst_test[9]

    hole_11 = hole_lst_test[10]

    hole_12 = hole_lst_test[11]

    hole_13 = hole_lst_test[12]

    hole_14 = hole_lst_test[13]

    hole_15 = hole_lst_test[14]

    hole_16 = hole_lst_test[15]

    hole_17 = hole_lst_test[16]

    hole_18 = hole_lst_test[17]

 

########################################################

 

    par_lst = [hole_1, hole_2, hole_3,

               hole_4, hole_5, hole_6,

               hole_7, hole_8, hole_9,

               hole_10, hole_11, hole_12,

               hole_13, hole_14, hole_15,

               hole_16, hole_17, hole_18]

 

########################################################

    #### Merge the data sets and clean

    # Merge the datasets

    database_add = database.merge(TP, left_on=['Tournament', 'Round', 'Hole'],

                                      right_on=['Tournament', 'Round', 'Hole'])

   

    database_add = database_add.merge(CR, left_on='Tournament',

                                        right_on='Tournament')

 

    # Remove added info-

    database_add.drop(database_add.loc[database_add['Hole']=='RD'].index, inplace=True)

    database_add.drop(database_add.loc[database_add['Hole']=='OUT'].index, inplace=True)

    database_add.drop(database_add.loc[database_add['Hole']=='IN'].index, inplace=True)

 

 

 

    database_add = database_add.drop(["Men's HCP", "Team", "Tournament"], axis=1)

 

    # Add a column to show what hole we are on

    database_add['Side'] = database_add['Hole']

    database_add['Side']  = database_add['Side'] .replace("Hole 1", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 2", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 3", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 4", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 5", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 6", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 7", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 8", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 9", "Front 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 10", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 11", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 12", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 13", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 14", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 15", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 16", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 17", "Back 9")

    database_add['Side']  = database_add['Side'] .replace("Hole 18", "Back 9")

   

########################################################

 

    # Create Dataset of only Par 3's

    par_3_df = database_add.loc[database_add['Par'] == 3]

 

    # Create an index of the holes for when the data needs to be merged back

    par_3_df = par_3_df.reset_index()

    par_3_df['index1'] = par_3_df.index

    par_3_df = par_3_df.rename(columns={"index1": "Hole #"})

 

    # Creaet an empty list

    par_3_lst = []

 

    # iterate through the scores and name them based on par and score

    for score in par_3_df['Score']:

        if score == 1:

            result = "hole_in_one"

        if score == 2:

            result = "Birdie"

        if score == 3:

            result = "Par"

        if score == 4:

            result = "Bogey"

        if score == 5:

            result = "Double_Bogey"

        if score == 6:

            result = "Triple_Bogey"

        if score >= 7:

            result = "Quad_Bogey_+"

 

        # Add the result to the empty list through the itteration

        par_3_lst.append(result)      

 

    # Convert the list to a dataframe

    par_3_lst_df = pd.DataFrame(par_3_lst)

 

    # Clean up the new dataframe

    par_3_lst_df['index1'] = par_3_lst_df.index

    par_3_lst_df = par_3_lst_df.rename(columns={"index1": "Hole #"})

 

    # Merge and Clean the new dataframe

    par_3_df = par_3_df.merge(par_3_lst_df, left_on="Hole #", right_on="Hole #")

    par_3_df = par_3_df.rename(columns={0: "Score_Name"})

    par_3_df = par_3_df.drop(["Hole #"], axis=1)

       

########################################################

 

    # Create Dataset of only Par 4's

    par_4_df = database_add.loc[database_add['Par'] == 4]

 

    # Create an index of the holes for when the data needs to be merged back

    par_4_df = par_4_df.reset_index()

    par_4_df['index1'] = par_4_df.index

    par_4_df = par_4_df.rename(columns={"index1": "Hole #"})

 

    # Creaet an empty list

    par_4_lst = []

 

    # iterate through the scores and name them based on par and score

    for score in par_4_df['Score']:

        if score == 1:

            result = "hole_in_one"

        if score == 2:

            result = "Eagle"

        if score == 3:

            result = "Birdie"

        if score == 4:

            result = "Par"

        if score == 5:

            result = "Bogey"

        if score == 6:

            result = "Double_Bogey"

        if score == 7:

            result = "Triple_Bogey"

        if score >= 8:

            result = "Quad_Bogey_+"       

 

        # Add the result to the empty list through the itteration

        par_4_lst.append(result)      

 

    # Convert the list to a dataframe

    par_4_lst_df = pd.DataFrame(par_4_lst)

 

    # Clean up the new dataframe

    par_4_lst_df['index1'] = par_4_lst_df.index

    par_4_lst_df = par_4_lst_df.rename(columns={"index1": "Hole #"})

 

    # Merge and Clean the new dataframe

    par_4_df = par_4_df.merge(par_4_lst_df, left_on="Hole #", right_on="Hole #")

    par_4_df = par_4_df.rename(columns={0: "Score_Name"})

    par_4_df = par_4_df.drop(["Hole #"], axis=1)

   

########################################################

 

    # Create Dataset of only Par 5's

    par_5_df = database_add.loc[database_add['Par'] == 5]

 

    # Create an index of the holes for when the data needs to be merged back

    par_5_df = par_5_df.reset_index()

    par_5_df['index1'] = par_5_df.index

    par_5_df = par_5_df.rename(columns={"index1": "Hole #"})

 

    # Creaet an empty list

    par_5_lst = []

 

    # iterate through the scores and name them based on par and score

    for score in par_5_df['Score']:

        if score == 1:

            result = "hole_in_one"

        if score == 2:

            result = "Double_Eagle"

        if score == 3:

            result = "Eagle"

        if score == 4:

            result = "Birdie"

        if score == 5:

            result = "Par"

        if score == 6:

            result = "Bogey"

        if score == 7:

            result = "Double_Bogey"

        if score == 8:

            result = "Triple_Bogey"  

        if score >= 9:

            result = "Quad_Bogey_+"          

 

        # Add the result to the empty list through the itteration

        par_5_lst.append(result)      

 

    # Convert the list to a dataframe

    par_5_lst_df = pd.DataFrame(par_5_lst)

 

    # Clean up the new dataframe

    par_5_lst_df['index1'] = par_5_lst_df.index

    par_5_lst_df = par_5_lst_df.rename(columns={"index1": "Hole #"})

 

    # Merge and Clean the new dataframe

    par_5_df = par_5_df.merge(par_5_lst_df, left_on="Hole #", right_on="Hole #")

    par_5_df = par_5_df.rename(columns={0: "Score_Name"})

    par_5_df = par_5_df.drop(["Hole #"], axis=1)

       

########################################################

 

    # Merge the Datasets Together

    database_add = pd.concat([par_3_df, par_4_df], ignore_index=True)

    database_add = pd.concat([database_add, par_5_df], ignore_index=True)

    database_add['Count'] = 1

 

    # Remove the extremes

    database_add.drop(database_add.loc[database_add['Score_Name']== "hole_in_one"].index, inplace=True)

    database_add.drop(database_add.loc[database_add['Score_Name']== "Double_Eagle"].index, inplace=True)   

    database_add.drop(database_add.loc[database_add['Score_Name']== "Quad_Bogey_+"].index, inplace=True)

   

########################################################

 

    # Create adusted score

    database_add['adj_score'] = database_add['Score']

    Cleaned_Dataset = database_add.drop(["index", "Player ID", 

                                          "Count", "Course",

                                         "Rating", "Slope",

                                        ], axis=1) 

    

########################################################

 

    # Select Player 1

    player_1_df = Cleaned_Dataset.loc[Cleaned_Dataset['Player'] == player_1_name]

 

    # Clean the dataframe

    player_1_df = player_1_df.reset_index()

    player_1_df['Count'] = 1

 

    # Create list of outcomes grouped by scores

    player_1_count = player_1_df.groupby(["Player", "Side", "Score_Name", "Par", "adj_score"])["Count"].count().reset_index()

 

    # Create list of outcomes but not grouped by scores

    player_1_total = player_1_df.groupby(["Player", "Side", "Par"])["Count"].count().reset_index()

 

    # Merge the two datasets

    player_1_overview = player_1_count.merge(player_1_total, left_on=["Side", "Par"]

                                             , right_on=["Side", "Par"])

 

    # Create a rate column

    player_1_overview['Rate'] = player_1_overview['Count_x'] / player_1_overview['Count_y']

 

    # Clean the data

    player_1_overview = player_1_overview.rename(columns={"Count_x": "# of Outcome",

                                                          "Count_y": "# of Times",

                                                          "Player_x" : "Player"})

    player_1_overview = player_1_overview.drop(["Player_y"], axis=1)

 

    # Create the base dataframe that the hole data will be appended too

    player_1_sim_df = pd.DataFrame(index=np.arange(num_of_sims), columns=np.arange(1))

    player_1_sim_df['index1'] = player_1_sim_df.index

    player_1_sim_df = player_1_sim_df.drop([0], axis=1)

    player_1_sim_df = player_1_sim_df.rename(columns={"index1": "Sim #"})

    player_1_sim_df['Player 1'] = player_1_name

 

    # Create the loop for player 1

    counter = 0

    for par in par_lst:

        counter += 1

       

        # Calc for the front 9

        if counter <= 9:

            player_1 = player_1_overview.loc[player_1_overview['Side'] == 'Front 9']

            player_1 = player_1.loc[player_1['Par'] == par]

           

            # Create new input Data

            dict = {'Player' : [player_1_name, player_1_name],

                    'Side' : ['Front 9', 'Front 9'],

                    'Score_Name' : ['Hole_in_one', 'Quad_Bogey_+'],

                    'Par' : [par, par],

                    'adj_score' : [1, par + 4],

                    '# of Outcome' : [0, 0],

                    '# of Times' : [0, 0],

                    'Rate': [0.00011, 0.005]}

            df1 = pd.DataFrame(dict)

 

            # Create and concat the data for extream outcomes

            num_of_types = player_1['adj_score'].count()

            drop_rate = 0.00511/num_of_types

            player_1['Rate'] = player_1['Rate'] - drop_rate

            player_1 = pd.concat([player_1, df1], ignore_index=True)

           

            # Generate the input weights for the random choice generator

            player_1_score = player_1['adj_score'].tolist()

            player_1_weight = player_1['Rate'].tolist()

           

            # Create the simulations

            player_1_lst = random.choices(player_1_score, player_1_weight, k = num_of_sims)

            player_1_df = pd.DataFrame(player_1_lst)

            player_1_df['index1'] = player_1_df.index

            player_1_df = player_1_df.rename(columns={0: "Hole"+str(counter), "index1": "Sim #"})

           

            # Merge each hole to the main datasets

            player_1_sim_df = player_1_sim_df.merge(player_1_df, left_on="Sim #", right_on="Sim #")

           

        # Calc for the back 9

        elif counter >= 10:

            player_1 = player_1_overview.loc[player_1_overview['Side'] == 'Back 9']

            player_1 = player_1.loc[player_1['Par'] == par]

           

            # Create new input Data

            dict = {'Player' : [player_1_name, player_1_name],

                    'Side' : ['Back 9', 'Back 9'],

                    'Score_Name' : ['Hole_in_one', 'Quad_Bogey_+'],

                    'Par' : [par, par],

                    'adj_score' : [1, par + 4],

                    '# of Outcome' : [0, 0],

                    '# of Times' : [0, 0],

                    'Rate': [0.00011, 0.005]}

            df1 = pd.DataFrame(dict)

 

            # Create and concat the data for extream outcomes

            num_of_types = player_1['adj_score'].count()

            drop_rate = 0.00511/num_of_types

            player_1['Rate'] = player_1['Rate'] - drop_rate

            player_1 = pd.concat([player_1, df1], ignore_index=True)

           

            # Generate the input weights for the random choice generator

            player_1_score = player_1['adj_score'].tolist()

            player_1_weight = player_1['Rate'].tolist()

           

            # Create the simulations

            player_1_lst = random.choices(player_1_score, player_1_weight, k = num_of_sims)

            player_1_df = pd.DataFrame(player_1_lst)

            player_1_df['index1'] = player_1_df.index

            player_1_df = player_1_df.rename(columns={0: "Hole"+str(counter), "index1": "Sim #"})

           

            # Merge each hole to the main datasets

            player_1_sim_df = player_1_sim_df.merge(player_1_df, left_on="Sim #", right_on="Sim #")

    

            

    player_1_sim_df['Front_9'] = player_1_sim_df['Hole1']+player_1_sim_df['Hole2']+player_1_sim_df['Hole3']+player_1_sim_df['Hole4']+player_1_sim_df['Hole5']+player_1_sim_df['Hole6']+player_1_sim_df['Hole7']+player_1_sim_df['Hole8']+player_1_sim_df['Hole9']

    player_1_sim_df['Back_9'] = player_1_sim_df['Hole10']+player_1_sim_df['Hole11']+player_1_sim_df['Hole12']+player_1_sim_df['Hole13']+player_1_sim_df['Hole14']+player_1_sim_df['Hole15']+player_1_sim_df['Hole16']+player_1_sim_df['Hole17']+player_1_sim_df['Hole18']

    player_1_sim_df['Overall'] = player_1_sim_df['Front_9']+player_1_sim_df['Back_9']

   

    print(player_1_sim_df)

   

########################################################

 

    # Select Player 1

    player_2_df = Cleaned_Dataset.loc[Cleaned_Dataset['Player'] == player_2_name]

 

    # Clean the dataframe

    player_2_df = player_2_df.reset_index()

    player_2_df['Count'] = 1

 

    # Create list of outcomes grouped by scores

    player_2_count = player_2_df.groupby(["Player", "Side", "Score_Name", "Par", "adj_score"])["Count"].count().reset_index()

 

    # Create list of outcomes but not grouped by scores

    player_2_total = player_2_df.groupby(["Player", "Side", "Par"])["Count"].count().reset_index()

 

    # Merge the two datasets

    player_2_overview = player_2_count.merge(player_2_total, left_on=["Side", "Par"]

                                             , right_on=["Side", "Par"])

 

    # Create a rate column

    player_2_overview['Rate'] = player_2_overview['Count_x'] / player_2_overview['Count_y']

 

    # Clean the data

    player_2_overview = player_2_overview.rename(columns={"Count_x": "# of Outcome",

                                                          "Count_y": "# of Times",

                                                          "Player_x" : "Player"})

    player_2_overview = player_2_overview.drop(["Player_y"], axis=1)

 

    # Create the base dataframe that the hole data will be appended too

    player_2_sim_df = pd.DataFrame(index=np.arange(num_of_sims), columns=np.arange(1))

    player_2_sim_df['index1'] = player_2_sim_df.index

    player_2_sim_df = player_2_sim_df.drop([0], axis=1)

    player_2_sim_df = player_2_sim_df.rename(columns={"index1": "Sim #"})

    player_2_sim_df['Player 2'] = player_2_name

 

    # Create the loop for player 2

    counter = 0

    for par in par_lst:

        counter += 1

       

        # Calc for the front 9

        if counter <= 9:

            player_2 = player_2_overview.loc[player_2_overview['Side'] == 'Front 9']

            player_2 = player_2.loc[player_2['Par'] == par]

           

            # Create new input Data

            dict = {'Player' : [player_2_name, player_2_name],

                    'Side' : ['Front 9', 'Front 9'],

                    'Score_Name' : ['Hole_in_one', 'Quad_Bogey_+'],

                    'Par' : [par, par],

                    'adj_score' : [1, par + 4],

                    '# of Outcome' : [0, 0],

                    '# of Times' : [0, 0],

                    'Rate': [0.00011, 0.005]}

            df2 = pd.DataFrame(dict)

 

            # Create and concat the data for extream outcomes

            num_of_types = player_2['adj_score'].count()

            drop_rate = 0.00511/num_of_types

            player_2['Rate'] = player_2['Rate'] - drop_rate

            player_2 = pd.concat([player_2, df2], ignore_index=True)

           

            # Generate the input weights for the random choice generator

            player_2_score = player_2['adj_score'].tolist()

            player_2_weight = player_2['Rate'].tolist()

 

            # Create the simulations

            player_2_lst = random.choices(player_2_score, player_2_weight, k = num_of_sims)

            player_2_df = pd.DataFrame(player_2_lst)

            player_2_df['index1'] = player_2_df.index

            player_2_df = player_2_df.rename(columns={0: "Hole"+str(counter), "index1": "Sim #"})

           

            # Merge each hole to the main datasets

            player_2_sim_df = player_2_sim_df.merge(player_2_df, left_on="Sim #", right_on="Sim #")

           

        # Calc for the back 9

        elif counter >= 10:

            player_2 = player_2_overview.loc[player_2_overview['Side'] == 'Back 9']

            player_2 = player_2.loc[player_2['Par'] == par]

           

            # Create new input Data

            dict = {'Player' : [player_2_name, player_2_name],

                    'Side' : ['Back 9', 'Back 9'],

                    'Score_Name' : ['Hole_in_one', 'Quad_Bogey_+'],

                    'Par' : [par, par],

                    'adj_score' : [1, par + 4],

                    '# of Outcome' : [0, 0],

                    '# of Times' : [0, 0],

                    'Rate': [0.00011, 0.005]}

            df2 = pd.DataFrame(dict)

 

            # Create and concat the data for extream outcomes

            num_of_types = player_2['adj_score'].count()

            drop_rate = 0.00511/num_of_types

            player_2['Rate'] = player_2['Rate'] - drop_rate

            player_2 = pd.concat([player_2, df1], ignore_index=True)

           

            # Generate the input weights for the random choice generator

            player_2_score = player_2['adj_score'].tolist()

            player_2_weight = player_2['Rate'].tolist()

           

            # Create the simulations

            player_2_lst = random.choices(player_2_score, player_2_weight, k = num_of_sims)

            player_2_df = pd.DataFrame(player_2_lst)

            player_2_df['index1'] = player_2_df.index

            player_2_df = player_2_df.rename(columns={0: "Hole"+str(counter), "index1": "Sim #"})

           

            # Merge each hole to the main datasets

            player_2_sim_df = player_2_sim_df.merge(player_2_df, left_on="Sim #", right_on="Sim #")

       

    

    player_2_sim_df['Front_9'] = player_2_sim_df['Hole1']+player_2_sim_df['Hole2']+player_2_sim_df['Hole3']+player_2_sim_df['Hole4']+player_2_sim_df['Hole5']+player_2_sim_df['Hole6']+player_2_sim_df['Hole7']+player_2_sim_df['Hole8']+player_2_sim_df['Hole9']

    player_2_sim_df['Back_9'] = player_2_sim_df['Hole10']+player_2_sim_df['Hole11']+player_2_sim_df['Hole12']+player_2_sim_df['Hole13']+player_2_sim_df['Hole14']+player_2_sim_df['Hole15']+player_2_sim_df['Hole16']+player_2_sim_df['Hole17']+player_2_sim_df['Hole18']

    player_2_sim_df['Overall'] = player_2_sim_df['Front_9']+player_2_sim_df['Back_9']

   

    print(player_2_sim_df)

   

########################################################   

 

    hole_diff = player_1_sim_df-player_2_sim_df

    hole_diff['Player 1'] = player_1_input

    hole_diff['Player 2'] = player_2_input

 

    player_1_sim_df['Player (#)'] = "Player 1"

    player_2_sim_df['Player (#)'] = "Player 2"

   

    player_1_sim_df['Course'] = course_input

    player_2_sim_df['Course'] = course_input

    hole_diff['Course'] = course_input

   

    player_1_sim_df['Matchup'] = f'{player_1_input}_v_{player_2_input}' 

    player_2_sim_df['Matchup'] = f'{player_1_input}_v_{player_2_input}'

    hole_diff['Matchup'] = f'{player_1_input}_v_{player_2_input}'

   

    hole_diff = hole_diff[['Sim #', 'Player 1', 'Player 2', 'Course', 'Matchup',

                           'Hole1', 'Hole2', 'Hole3', 'Hole4', 'Hole5', 'Hole6', 'Hole7', 'Hole8', 'Hole9',

                           'Hole10', 'Hole11', 'Hole12', 'Hole13', 'Hole14', 'Hole15', 'Hole16', 'Hole17', 'Hole18',

                           'Front_9', 'Back_9', 'Overall',

            ]]

   

    player_1_sim_df['Sim #'] = player_1_sim_df['Sim #']+1

    player_2_sim_df['Sim #'] = player_2_sim_df['Sim #']+1

    hole_diff['Sim #'] = player_2_sim_df['Sim #']

   

    Player_1_df_final = player_1_sim_df

    Player_2_df_final = player_2_sim_df

    Player_1v2_df_final = hole_diff

 

    print(Player_1v2_df_final)

   

###########################################

   

    ## Create Player 1 Cleaned dataframe

    Player_1_df_final_H1 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H1['Hole'] = "Hole 1"

    Player_1_df_final_H1['Score'] = Player_1_df_final['Hole1']

 

    Player_1_df_final_H2 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H2['Hole'] = "Hole 2"

    Player_1_df_final_H2['Score'] = Player_1_df_final['Hole2']

 

    Player_1_df_final_H3 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H3['Hole'] = "Hole 3"

    Player_1_df_final_H3['Score'] = Player_1_df_final['Hole3']

 

    Player_1_df_final_H4 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H4['Hole'] = "Hole 4"

    Player_1_df_final_H4['Score'] = Player_1_df_final['Hole4']

 

    Player_1_df_final_H5 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H5['Hole'] = "Hole 5"

    Player_1_df_final_H5['Score'] = Player_1_df_final['Hole5']

 

    Player_1_df_final_H6 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H6['Hole'] = "Hole 6"

    Player_1_df_final_H6['Score'] = Player_1_df_final['Hole6']

 

    Player_1_df_final_H7 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H7['Hole'] = "Hole 7"

    Player_1_df_final_H7['Score'] = Player_1_df_final['Hole7']

 

    Player_1_df_final_H8 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H8['Hole'] = "Hole 8"

    Player_1_df_final_H8['Score'] = Player_1_df_final['Hole8']

 

    Player_1_df_final_H9 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H9['Hole'] = "Hole 9"

    Player_1_df_final_H9['Score'] = Player_1_df_final['Hole9']

 

    Player_1_df_final_H10 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H10['Hole'] = "Hole 10"

    Player_1_df_final_H10['Score'] = Player_1_df_final['Hole10']

 

    Player_1_df_final_H11 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H11['Hole'] = "Hole 11"

    Player_1_df_final_H11['Score'] = Player_1_df_final['Hole11']

 

    Player_1_df_final_H12 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H12['Hole'] = "Hole 12"

    Player_1_df_final_H12['Score'] = Player_1_df_final['Hole12']

 

    Player_1_df_final_H13 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H13['Hole'] = "Hole 13"

    Player_1_df_final_H13['Score'] = Player_1_df_final['Hole13']

 

    Player_1_df_final_H14 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H14['Hole'] = "Hole 14"

    Player_1_df_final_H14['Score'] = Player_1_df_final['Hole14']

 

    Player_1_df_final_H15 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H15['Hole'] = "Hole 15"

    Player_1_df_final_H15['Score'] = Player_1_df_final['Hole15']

 

    Player_1_df_final_H16 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H16['Hole'] = "Hole 16"

    Player_1_df_final_H16['Score'] = Player_1_df_final['Hole16']

 

    Player_1_df_final_H17 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H17['Hole'] = "Hole 17"

    Player_1_df_final_H17['Score'] = Player_1_df_final['Hole17']

 

    Player_1_df_final_H18 = Player_1_df_final[['Sim #', 'Course', 'Matchup', 'Player 1', "Player (#)"]]

    Player_1_df_final_H18['Hole'] = "Hole 18"

    Player_1_df_final_H18['Score'] = Player_1_df_final['Hole18']

 

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_H1, Player_1_df_final_H2], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H3], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H4], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H5], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H6], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H7], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H8], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H9], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H10], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H11], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H12], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H13], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H14], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H15], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H16], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H17], ignore_index=True)

    Player_1_df_final_cleaned = pd.concat([Player_1_df_final_cleaned, Player_1_df_final_H18], ignore_index=True)

 

    Player_1_df_final_cleaned = Player_1_df_final_cleaned.rename(columns={"Player 1": "Player (Name)"})

   

###########################################   

 

    ## Create Player 2 Cleaned dataframe

    Player_2_df_final_H1 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H1['Hole'] = "Hole 1"

    Player_2_df_final_H1['Score'] = Player_2_df_final['Hole1']

 

    Player_2_df_final_H2 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H2['Hole'] = "Hole 2"

    Player_2_df_final_H2['Score'] = Player_2_df_final['Hole2']

 

    Player_2_df_final_H3 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H3['Hole'] = "Hole 3"

    Player_2_df_final_H3['Score'] = Player_2_df_final['Hole3']

 

    Player_2_df_final_H4 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H4['Hole'] = "Hole 4"

    Player_2_df_final_H4['Score'] = Player_2_df_final['Hole4']

 

    Player_2_df_final_H5 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H5['Hole'] = "Hole 5"

    Player_2_df_final_H5['Score'] = Player_2_df_final['Hole5']

 

    Player_2_df_final_H6 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H6['Hole'] = "Hole 6"

    Player_2_df_final_H6['Score'] = Player_2_df_final['Hole6']

 

    Player_2_df_final_H7 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H7['Hole'] = "Hole 7"

    Player_2_df_final_H7['Score'] = Player_2_df_final['Hole7']

 

    Player_2_df_final_H8 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H8['Hole'] = "Hole 8"

    Player_2_df_final_H8['Score'] = Player_2_df_final['Hole8']

 

    Player_2_df_final_H9 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H9['Hole'] = "Hole 9"

    Player_2_df_final_H9['Score'] = Player_2_df_final['Hole9']

 

    Player_2_df_final_H10 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H10['Hole'] = "Hole 10"

    Player_2_df_final_H10['Score'] = Player_2_df_final['Hole10']

 

    Player_2_df_final_H11 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H11['Hole'] = "Hole 11"

    Player_2_df_final_H11['Score'] = Player_2_df_final['Hole11']

 

    Player_2_df_final_H12 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H12['Hole'] = "Hole 12"

    Player_2_df_final_H12['Score'] = Player_2_df_final['Hole12']

 

    Player_2_df_final_H13 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H13['Hole'] = "Hole 13"

    Player_2_df_final_H13['Score'] = Player_2_df_final['Hole13']

 

    Player_2_df_final_H14 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H14['Hole'] = "Hole 14"

    Player_2_df_final_H14['Score'] = Player_2_df_final['Hole14']

 

    Player_2_df_final_H15 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H15['Hole'] = "Hole 15"

    Player_2_df_final_H15['Score'] = Player_2_df_final['Hole15']

 

    Player_2_df_final_H16 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H16['Hole'] = "Hole 16"

    Player_2_df_final_H16['Score'] = Player_2_df_final['Hole16']

 

    Player_2_df_final_H17 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H17['Hole'] = "Hole 17"

    Player_2_df_final_H17['Score'] = Player_2_df_final['Hole17']

 

    Player_2_df_final_H18 = Player_2_df_final[['Sim #', 'Course', 'Matchup', 'Player 2', "Player (#)"]]

    Player_2_df_final_H18['Hole'] = "Hole 18"

    Player_2_df_final_H18['Score'] = Player_2_df_final['Hole18']

 

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_H1, Player_2_df_final_H2], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H3], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H4], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H5], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H6], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H7], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H8], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H9], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H10], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H11], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H12], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H13], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H14], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H15], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H16], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H17], ignore_index=True)

    Player_2_df_final_cleaned = pd.concat([Player_2_df_final_cleaned, Player_2_df_final_H18], ignore_index=True)

 

    Player_2_df_final_cleaned = Player_2_df_final_cleaned.rename(columns={"Player 2": "Player (Name)"})

   

###########################################   

    

    new_dataset = pd.concat([Player_1_df_final_cleaned, Player_2_df_final_cleaned], ignore_index=True)

    #new_dataset.to_csv("Output\_new_dataset_.csv", index=False)

    print(new_dataset)

   

###########################################   

    

    # Create Overview of difference

    Player_1v2_df_final_H1 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H1['Hole'] = "Hole 1"

    Player_1v2_df_final_H1['Par'] = hole_1

    Player_1v2_df_final_H1['Score'] = Player_1v2_df_final['Hole1']

 

    Player_1v2_df_final_H2 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H2['Hole'] = "Hole 2"

    Player_1v2_df_final_H2['Par'] = hole_2

    Player_1v2_df_final_H2['Score'] = Player_1v2_df_final['Hole2']

 

    Player_1v2_df_final_H3 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H3['Hole'] = "Hole 3"

    Player_1v2_df_final_H3['Par'] = hole_3

    Player_1v2_df_final_H3['Score'] = Player_1v2_df_final['Hole3']

 

    Player_1v2_df_final_H4 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H4['Hole'] = "Hole 4"

    Player_1v2_df_final_H4['Par'] = hole_4

    Player_1v2_df_final_H4['Score'] = Player_1v2_df_final['Hole4']

 

    Player_1v2_df_final_H5 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H5['Hole'] = "Hole 5"

    Player_1v2_df_final_H5['Par'] = hole_5

    Player_1v2_df_final_H5['Score'] = Player_1v2_df_final['Hole5']

 

    Player_1v2_df_final_H6 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H6['Hole'] = "Hole 6"

    Player_1v2_df_final_H6['Par'] = hole_6

    Player_1v2_df_final_H6['Score'] = Player_1v2_df_final['Hole6']

 

    Player_1v2_df_final_H7 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H7['Hole'] = "Hole 7"

    Player_1v2_df_final_H7['Par'] = hole_7

    Player_1v2_df_final_H7['Score'] = Player_1v2_df_final['Hole7']

 

    Player_1v2_df_final_H8 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H8['Hole'] = "Hole 8"

    Player_1v2_df_final_H8['Par'] = hole_8

    Player_1v2_df_final_H8['Score'] = Player_1v2_df_final['Hole8']

 

    Player_1v2_df_final_H9 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H9['Hole'] = "Hole 9"

    Player_1v2_df_final_H9['Par'] = hole_9

    Player_1v2_df_final_H9['Score'] = Player_1v2_df_final['Hole9']

 

    Player_1v2_df_final_H10 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H10['Hole'] = "Hole 10"

    Player_1v2_df_final_H10['Par'] = hole_10

    Player_1v2_df_final_H10['Score'] = Player_1v2_df_final['Hole10']

 

    Player_1v2_df_final_H11 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H11['Hole'] = "Hole 11"

    Player_1v2_df_final_H11['Par'] = hole_11

    Player_1v2_df_final_H11['Score'] = Player_1v2_df_final['Hole11']

 

    Player_1v2_df_final_H12 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H12['Hole'] = "Hole 12"

    Player_1v2_df_final_H12['Par'] = hole_12

    Player_1v2_df_final_H12['Score'] = Player_1v2_df_final['Hole12']

 

    Player_1v2_df_final_H13 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H13['Hole'] = "Hole 13"

    Player_1v2_df_final_H13['Par'] = hole_13

    Player_1v2_df_final_H13['Score'] = Player_1v2_df_final['Hole13']

 

    Player_1v2_df_final_H14 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H14['Hole'] = "Hole 14"

    Player_1v2_df_final_H14['Par'] = hole_14

    Player_1v2_df_final_H14['Score'] = Player_1v2_df_final['Hole14']

 

    Player_1v2_df_final_H15 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H15['Hole'] = "Hole 15"

    Player_1v2_df_final_H15['Par'] = hole_15

    Player_1v2_df_final_H15['Score'] = Player_1v2_df_final['Hole15']

 

    Player_1v2_df_final_H16 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H16['Hole'] = "Hole 16"

    Player_1v2_df_final_H16['Par'] = hole_16

    Player_1v2_df_final_H16['Score'] = Player_1v2_df_final['Hole16']

 

    Player_1v2_df_final_H17 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H17['Hole'] = "Hole 17"

    Player_1v2_df_final_H17['Par'] = hole_17

    Player_1v2_df_final_H17['Score'] = Player_1v2_df_final['Hole17']

 

    Player_1v2_df_final_H18 = Player_1v2_df_final[['Sim #', 'Course', 'Matchup', 'Player 1']]

    Player_1v2_df_final_H18['Hole'] = "Hole 18"

    Player_1v2_df_final_H18['Par'] = hole_18

    Player_1v2_df_final_H18['Score'] = Player_1v2_df_final['Hole18']

 

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_H1, Player_1v2_df_final_H2], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H3], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H4], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H5], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H6], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H7], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H8], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H9], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H10], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H11], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H12], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H13], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H14], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H15], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H16], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H17], ignore_index=True)

    Player_1v2_df_final_cleaned = pd.concat([Player_1v2_df_final_cleaned, Player_1v2_df_final_H18], ignore_index=True)

 

    Player_1v2_df_final_cleaned = Player_1v2_df_final_cleaned.rename(columns={"Player 1": "Player (Name)", "Score" : "Diff"})

    Player_1v2_df_final_cleaned['Tie'] = Player_1v2_df_final_cleaned['Diff'] == 0

    Player_1v2_df_final_cleaned['Player_2_win'] = Player_1v2_df_final_cleaned['Diff'] > 0

    Player_1v2_df_final_cleaned['Player_1_win'] = Player_1v2_df_final_cleaned['Diff'] < 0

   

    # Clean the data so we can repeate the process

    Player_1v2_df_final_cleaned['Player_1_win_num'] = np.where(Player_1v2_df_final_cleaned['Player_1_win'], -1, 0)

    Player_1v2_df_final_cleaned['Player_2_win_num'] = np.where(Player_1v2_df_final_cleaned['Player_2_win'], 1, 0)

    Player_1v2_df_final_cleaned['Player_tie_win_num'] = np.where(Player_1v2_df_final_cleaned['Tie'], 0, 0)

   

    Player_1v2_df_final_cleaned['Hole Result'] = Player_1v2_df_final_cleaned['Player_1_win_num'] + Player_1v2_df_final_cleaned['Player_2_win_num'] + Player_1v2_df_final_cleaned['Player_tie_win_num']

 

    Player_1v2_df_final_cleaned = Player_1v2_df_final_cleaned.drop(columns=['Tie', 'Player_1_win', 'Player_2_win',

                                                                            'Player_1_win_num', 'Player_2_win_num', 'Player_tie_win_num'])

   

    Player_1v2_df_final_cleaned['Simulation Winner Name'] = Player_1v2_df_final_cleaned['Hole Result'].apply(str)

    Player_1v2_df_final_cleaned['Simulation Winner Name'] = Player_1v2_df_final_cleaned['Simulation Winner Name'].str.replace("-1", player_1_input)

    Player_1v2_df_final_cleaned['Simulation Winner Name'] = Player_1v2_df_final_cleaned['Simulation Winner Name'].str.replace("0", "Tie")

    Player_1v2_df_final_cleaned['Simulation Winner Name'] = Player_1v2_df_final_cleaned['Simulation Winner Name'].str.replace("1", player_2_input)

   

    #Player_1v2_df_final_cleaned.to_csv("Output\_new_dataset_2_.csv", index=False)

   

###########################################

   

    Outcome_dataset = Player_1v2_df_final_cleaned.groupby(["Sim #"])["Hole Result"].sum().reset_index()

 

    Outcome_dataset = Outcome_dataset.rename(columns={"Hole Result": "Sim Result"})

 

    Outcome_dataset['Tie'] = Outcome_dataset['Sim Result'] == 0

    Outcome_dataset['Player_2_win'] = Outcome_dataset['Sim Result'] > 0

    Outcome_dataset['Player_1_win'] = Outcome_dataset['Sim Result'] < 0

 

    # Clean the data so we can repeate the process

    Outcome_dataset['Player_1_win_num'] = np.where(Outcome_dataset['Player_1_win'], -1, 0)

    Outcome_dataset['Player_2_win_num'] = np.where(Outcome_dataset['Player_2_win'], 1, 0)

    Outcome_dataset['Player_tie_win_num'] = np.where(Outcome_dataset['Tie'], 0, 0)

 

    Outcome_dataset['Simulation Winner'] = Outcome_dataset['Player_1_win_num'] + Outcome_dataset['Player_2_win_num'] + Outcome_dataset['Player_tie_win_num']

 

    Outcome_dataset = Outcome_dataset.drop(columns=['Tie', 'Player_1_win', 'Player_2_win',

                                                    'Player_1_win_num', 'Player_2_win_num', 'Player_tie_win_num'])

 

    Outcome_dataset['Course'] = course_input

    Outcome_dataset['Matchup'] = f'{player_1_input}_v_{player_2_input}'

    Outcome_dataset['Simulation Winner Name'] = Outcome_dataset['Simulation Winner'].apply(str)

   

    Outcome_dataset['Simulation Winner Name'] = Outcome_dataset['Simulation Winner Name'].str.replace("-1", player_1_input)

    Outcome_dataset['Simulation Winner Name'] = Outcome_dataset['Simulation Winner Name'].str.replace("0", "Tie")

    Outcome_dataset['Simulation Winner Name'] = Outcome_dataset['Simulation Winner Name'].str.replace("1", player_2_input)

   

    #Outcome_dataset.to_csv("Output\_new_dataset_3_.csv", index=False)       

    

 

    return Outcome_dataset

 

 

team_1_name = 'Auburn'

team_2_name = 'Mizzou'

course_input = 'Legend Trail Golf Club'

sims_input = 10

 

 

# Open the excel file

xls = pd.ExcelFile('Mens Golf Datebase.xlsx')

players = pd.read_excel(xls, 'Players')

 

team_1_lst = players.loc[players['Team'] == team_1_name]

team_1_lst = team_1_lst['Player'].tolist()

team_1_lst = team_1_lst[:2]

print(team_1_lst)

 

team_2_lst = players.loc[players['Team'] == team_2_name]

team_2_lst = team_2_lst['Player'].tolist()

team_2_lst = team_2_lst[:2]

print(team_2_lst)

 

# Start time counter

start_time = datetime.now()

 

counter = 0

for player_A in team_1_lst:

    for player_B in team_2_lst:

        print(f'{player_A} vs {player_B}')

        print(golf_simulator(player_1_name = player_A, player_2_name = player_B, course_name = course_input, num_of_sims = sims_input))

        counter += 1

       

# Get time to complete

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

   

print(counter)
