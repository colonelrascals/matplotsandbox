import matplotlib.pyplot as pyplot
import pandas as pd

raw_data = {
    'names': ['Patrick', 'Logan', 'Chris', 'Ehsan', 'Mike'],
    'jan_mem': [122, 35, 2, 111, 78],
    'feb_mem': [45, 156, 14, 67, 100],
    'march_mem': [102, 67, 14, 178, 70],

}

df = pd.DataFrame(raw_data, columns=[
                  'names', 'jan_mem', 'feb_mem', 'march_mem'])

df['total_mem'] = df['jan_mem'] + df['feb_mem'] + df['march_mem']

color = [(1, .4, .4), (1, .6, 1), (.5, .3, .7), (.2, .5, .1), (.4, .4, 1)]

pyplot.pie(df['total_mem'],
           labels=df['names'],
           colors=color,
           autopct='%1.1f%%')

pyplot.axis('equal')
pyplot.show()
