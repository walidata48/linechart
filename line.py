from dash import Dash, dcc, html
import plotly.express as px

app = Dash()


df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country',line_shape='spline', width=800, height=450, color_discrete_sequence=["rgba(67,24,255,0.85)", "rgba(106,210,255,0.85)"])
fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)',
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      title_x=0.5,
                      legend_title="",
                      #font_family="DM Sans, sans-serif",
                      margin_t=100

                      )
fig.update_layout(
    title=dict(text="<b>Investing in Health & Longevity</b><br><span style='margin: 5px; font-size: 15px;'>Here is the satisfactory result of economically empowered countries extend lifespan</span>", font=dict(size=26), xanchor='left',x=0.1, automargin=False, yref='container')
)
fig.update_xaxes(showgrid=False,)
fig.update_yaxes(showgrid=False,)
fig.update_traces(line = dict(width=4))
fig.add_annotation(
    text='<b>$90.8M',
                align='left',
                showarrow=False,
                xref='paper',
                yref='paper',
                x=0.07,
                y=0.9,
                font_size = 24
                
    )

fig.add_annotation(
    text='<br>Total spent launched health</br>education campaigns by <br>Australia & New Zealand Govt in 1972',
                align='left',
                xref='paper',
                yref='paper',
                x=0.07,
                y=0.76,
                font_size = 13,
                font_color = '#808080',
                showarrow=False
                                
    )


app.layout = html.Div([
    dcc.Graph(figure=fig)
], className='card')

app.run_server(debug=True, )