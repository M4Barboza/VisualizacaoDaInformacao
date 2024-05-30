import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('netflix_titles.csv', encoding='latin1')

duration_counts = df['duration'].value_counts()

top_durations = duration_counts.head(5)

labels = top_durations.index
sizes = top_durations.values
colors = ['lightpink', 'lightgrey', 'coral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Top 5 Durações de Conteúdo na Netflix')

plt.axis('equal')
plt.show()


##############################################################

df['date_added'] = pd.to_datetime(df['date_added'])

df = df.dropna(subset=['date_added'])

df['year_month_added'] = df['date_added'].dt.to_period('M')

type_counts = df.groupby(['year_month_added', 'type']
                         ).size().unstack(fill_value=0)

type_counts.plot(kind='line', marker='o')

plt.title('Adições Mensais de Filmes e Séries na Netflix')
plt.xlabel('Ano e Mês de Adição')
plt.ylabel('Número de Adições')

plt.legend(title='Tipo')

plt.tight_layout()

plt.show()

##############################################################

country_counts = df['country'].value_counts().reset_index()
country_counts.columns = ['country', 'count']

fig = go.Figure(data=go.Choropleth(
    locations=country_counts['country'],
    z=country_counts['count'],
    locationmode='country names',
    colorscale='Viridis',
    zmin=0,
    zmax=country_counts['count'].max(),
    colorbar_title="Filmes e Series na Netflix",
))

fig.update_layout(
    title_text='Filmes e Series na Netflix por País',
    geo_scope='world',
)

fig.show()
