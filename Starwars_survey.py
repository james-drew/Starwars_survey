
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np

star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")

# remove rows is no ResondentID
star_wars = star_wars.dropna(subset=['RespondentID'])

# convert Yes/No to bool
yesno = {
    "Yes": True,
    "No": False
}

star_wars['Have you seen any of the 6 films in the Star Wars franchise?'] = star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].map(yesno)

star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'] = star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].map(yesno)

# convert film watchs to bool
filmwatch = {
    "Star Wars: Episode I  The Phantom Menace": True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    np.NaN: False,
}
for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(filmwatch)

# rename film watch columns
filmname = {
    star_wars.columns[3]:'seen_1',
    star_wars.columns[4]:'seen_2',
    star_wars.columns[5]:'seen_3',
    star_wars.columns[6]:'seen_4',
    star_wars.columns[7]:'seen_5',
    star_wars.columns[8]:'seen_6'
}
star_wars = star_wars.rename(columns=filmname)

# rename rating cols
ratingname = {
    star_wars.columns[9]:'ranking_1',
    star_wars.columns[10]:'ranking_2',
    star_wars.columns[11]:'ranking_3',
    star_wars.columns[12]:'ranking_4',
    star_wars.columns[13]:'ranking_5',
    star_wars.columns[14]:'ranking_6'
}
star_wars = star_wars.rename(columns=ratingname)

# convert rating cols to float
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)


# In[173]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# find means
ranking_means = []
for col in star_wars.columns[9:15]:
    ranking_means.append(star_wars[col].mean())

# find sums
seen_sums = []
for col in star_wars.columns[3:9]:
    seen_sums.append(star_wars[col].sum())

# plot on bar
ind = np.arange(6)
width = 0.5
fig,ax = plt.subplots()
means = ax.bar(ind, ranking_means, width)
sums = ax.bar(ind+0.5,seen_sums,0.35)




# In[184]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]

# find means
males_ranks = []
females_ranks = []
for col in star_wars.columns[9:15]:
    males_ranks.append(males[col].mean())
    females_ranks.append(females[col].mean())

# find sums
male_sums = []
female_sums = []
for col in star_wars.columns[3:9]:
    male_sums.append(males[col].sum())
    female_sums.append(females[col].sum())

# plot ranks + sums
ind = np.arange(6) + 0.3
width = 0.3
fig,ax = plt.subplots(1,2)
m_ranks = ax[0].bar(ind, males_ranks, width)
f_ranks = ax[0].bar(ind+0.3,females_ranks,0.3,color='y')

m_sums = ax[1].bar(ind, male_sums, width)
f_sums = ax[1].bar(ind+0.3,female_sums,0.3,color='y')

