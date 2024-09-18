from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Data Science Jobs Analysis', style={'textAlign':'center'}),
    dcc.Dropdown(df['Job Title'].unique(), 'Data Scientist', id='dropdown-selection'),
    dcc.Graph(id='salary-distribution-chart')
])

@callback(
    Output('salary-distribution-chart', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_salary_distribution(job_title):
    dff = df[df['Job Title']==job_title]
    fig = px.box(
        dff,
        y='Salary Estimate',
        title=f'Salary Estimate for {job_title}',
        labels={'Salary Estimate: Estimated Salary'},
        template='plotly_dark'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
