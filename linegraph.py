import matplotlib.pyplot as plt

years = [1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [2.750, 2.588, 3.018,
        2.654, 3.333, 4.001, 4.568, 4.853, 5.320, 5.725, 6.500, 6.700, 6.900, 7.346]

deaths = [1.2, 1.4, 1.2, 3.6, 2.4, 1.1, .9, .7, .6, .5, .4, .3, .25, .25]


lines = ply.plot(years, pops, years, death)

plt.grid(True)

plt.setp(lines, marker='o')
