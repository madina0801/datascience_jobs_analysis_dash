from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Data Science Jobs Analysis', style={'textAlign':'center'}),
    dcc.Dropdown(df['Job Title'].unique(), 'Data Scientist', id='jobtitle-dropdown', style={'margin-bottom': '15px'}),
    dcc.RadioItems(
        id='companysize-radiobuttons',
        options=[
            {'label': size for size in df['Size'].unique()}
        ]
    ),
    dcc.Graph(id='salary-distribution-chart'),
    dcc.Graph(id='industry-chart')
])

@callback(
    Output('salary-distribution-chart', 'figure'),
    Input('jobtitle-dropdown', 'value')
)
def update_salary_distribution(job_title):
    dff = df[df['Job Title']==job_title]
    fig = px.box(
        dff,
        y='Salary Estimate',
        title=f'Salary Estimate for {job_title}',
        labels={'Salary Estimate': 'Estimated Salary'},
        template='plotly_dark'
    )
    return fig

@callback(
    Output('industry-chart', 'figure'),
    Input('jobtitle-dropdown', 'value')
)
def update_industry_chart(job_title):
    industry_count = df[df['Job Title']==job_title]['Industry'].value_counts().head(10)
    fig = px.bar(
        industry_count,
        x=industry_count.index,
        y=industry_count.values,
        title=f'Top 10 industries hiring for {job_title}',
        labels={'x': 'Industry', 'y': 'Number of jobs'},
        template='plotly_dark'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
