import pandas as pd
import plotly.graph_objs as go

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    
    df_train = pd.read_csv('extras/plotly_titanic/titanic_train.csv')
    
    
    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = [0, 1, 2, 3, 4, 5],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Chart One',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    
    pclass_data = df_train[['Pclass', 'PassengerId']].groupby(by='Pclass').count().rename(columns={'PassengerId': 'Count'}).T.iloc[0]
    x = pclass_data.index.to_list()
    y = pclass_data.to_list()

    graph_two = []
    graph_two.append(
      go.Bar(
      x = x,
      y = y,
      )
    )

    layout_two = dict(title = 'Passenger class by Fare',
                xaxis = dict(title = 'Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)', tickformat = ',d',),
                yaxis = dict(title = 'Passenger Fare (British pound)',),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )
    
# fourth chart shows rural population vs arable land
    
    emb_fare_data = df_train[['Embarked', 'Fare']]
    x = emb_fare_data['Embarked'].to_list()
    y = emb_fare_data['Fare'].to_list()
    
    graph_four = []
    graph_four.append(
      go.Scatter(
      x = x,
      y = y,
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Port of Embarkation by Fare',
                xaxis = dict(title = 'Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)'),
                yaxis = dict(title = 'Passenger Fare (British pound)'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
