from dash import Dash, html, dcc, Input, Output, State
from dash import dash_table
from datetime import date
import pandas as pd

to_do_app = Dash(__name__)

df = pd.read_csv('tasks.csv')


def add_task():
    return html.Div([
        html.Br(),
        html.Div(children='Enter a new task and a deadline date and press "Add task"'),
        html.Div(dcc.Input(id='input-on-submit', type='text', placeholder="Insert here task")),
        html.Br(),
        dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2025, 9, 19),
            initial_visible_month=date(2022, 4, 8),
            display_format='YYYY-MM-D',
            date=date(2022, 4, 8)
        ),
        html.Br(),
        html.Button('Add task', id='submit-val'),
    ])


@to_do_app.callback(
    Output('task-table', 'children'),
    Input(component_id='input-on-submit', component_property='value'),
    Input(component_id='my-date-picker-single', component_property='date')
)
# TODO: ADD task to dash_table.DataTable
def update_tasks(value, date):
    return html.Tr(html.Td({}), html.Td({}), format(value, date)) # wrong choice


def show_tasks(dataframe):
    # return html.Table([
    #     html.Thead(
    #         html.Tr([html.Th(col) for col in dataframe.columns])
    #     ),
    #     html.Tbody([
    #         html.Tr([
    #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
    #         ]) for i in range(len(dataframe))
    #     ])
    # ], id='task-table')

    return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='task-table')


to_do_app.layout = html.Div(children=[
    html.H1(children='To Do List Manager'),

    html.Div(children='''
        Organize your tasks with this to do list manager!
    '''),
    html.Br(),
    show_tasks(df),

    html.Br(),
    html.Br(),
    add_task()

])

if __name__ == '__main__':
    to_do_app.run_server(debug=True)

# TODO: Add delete option to task
# TODO: Save new task added in csv file
# TODO: SAVE LOCALLY
# dcc.Store(id='memory'),
#     # The local store will take the initial data
#     # only the first time the page is loaded
#     # and keep it until it is cleared.
#     dcc.Store(id='local', storage_type='local'),
#     # Same as the local store but will lose the data
#     # when the browser/tab closes.
# @app.callback(Output(store, 'data'),
#               Input('{}-button'.format(store), 'n_clicks'),
#               State(store, 'data'))
# def on_click(n_clicks, data):
#     if n_clicks is None:
#         # prevent the None callbacks is important with the store component.
#         # you don't want to update the store for nothing.
#         raise PreventUpdate
#
#     # Give a default data dict with 0 clicks if there's no data.
#     data = data or {'clicks': 0}
#
#     data['clicks'] = data['clicks'] + 1
#     return data
#
#
# # output the stored clicks in the table cell.
# @app.callback(Output('{}-clicks'.format(store), 'children'),
#               # Since we use the data prop in an output,
#               # we cannot get the initial data on load with the data prop.
#               # To counter this, you can use the modified_timestamp
#               # as Input and the data as State.
#               # This limitation is due to the initial None callbacks
#               # https://github.com/plotly/dash-renderer/pull/81
#               Input(store, 'modified_timestamp'),
#               State(store, 'data'))