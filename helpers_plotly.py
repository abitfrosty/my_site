import pandas as pd
import plotly.graph_objs as go

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    
    df_train = pd.read_csv('/var/www/webApp/webApp/extras/plotly_titanic/titanic_train.csv')
    
    
    # First chart plots Passenger Age distribution
    age_data = df_train[['Age']]
    x = age_data['Age'].to_list()
    
    graph_one = []    
    graph_one.append(
      go.Histogram(
      x = x
      )
    )

    layout_one = dict(title = 'Passenger Age distribution',
                xaxis = dict(title = 'Passenger Age'),
                yaxis = dict(title = 'Passenger Count'),
                )

    # Second chart plots Passenger Class distribution
    
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


    # Third chart plots Passenger Sex distribution
    
    sex_data = df_train[['Sex']].groupby('Sex').size()
    values = sex_data.to_list()
    labels = sex_data.index.to_list()
    
    graph_three = []
    graph_three.append(
      go.Pie(
      values = values,
      labels = labels
      )
    )

    layout_three = dict(title = 'Passenger Sex distribution')
    
    # Fourth chart shows distribution of embarkation by price
    
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
    
    # Append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
