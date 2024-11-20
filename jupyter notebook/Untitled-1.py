# %%
# Body mass index (BMI)
# input Weight
# Height 
# BMI (ask your seif your height)
# Weight
# calculate BMI
# Print BMI (My name is..., and my BMI is....)

# %%
# weight in kj/height in m and its square 

# %%
height = input("what is your height? ")

# %%
height = float(height)

# %%
weight = input("what is your weight?")

# %%
weight = float(weight)

# %%
name = input("what is your name?")

# %%
BMI = weight/height**2
BMI

# %%
print("My name is", name, "and my BMI is", BMI)

# %%
import seaborn as sns

# %%
import matplotlib.pyplot as plt

# %%
sns.set_theme(style="ticks", color_codes=True)

# %%
titanic = sns.load_dataset("titanic")

# %%
sns.catplot(x="sex", y= "survived", hue="class", kind="bar", data=titanic)

# %%
plt.show()

# %%
import seaborn as sns

# %%
import matplotlib.pyplot as plt

# %%
sns.set_theme(style="ticks", color_codes=True)

# %%
titanic = sns.load_dataset("titanic")

# %%
p1=sns.countplot(x='who', data=titanic, hue='alone')

# %%
p1.set_title("Plot for couting")

# %%
plt.show()

# %%
import seaborn as sns

# %%
import matplotlib.pyplot as plt

# %%
sns.set_theme(style="ticks", color_codes=True)

# %%
titanic = sns.load_dataset("titanic")

# %%
g=sns.FacetGrid(titanic,row="sex", hue="alone")

# %%
g=(g.map(plt.scatter, "age", "fare").add_legend())

# %%
plt.show()

# %%
titanic

# %%



