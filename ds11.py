# %%
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns

df = pd.read_excel("Banana_Quality.xlsx")

sns.pairplot(df)
plt.show()

# %%
print(df.shape)
print(df.columns)
print(df.describe())
corr_matrix = df[['quality_score', 'ripeness_index', 'sugar_content_brix','firmness_kgf', 'length_cm', 'weight_g','tree_age_years', 'altitude_m', 'rainfall_mm', 'soil_nitrogen_ppm']].corr()

sns.heatmap(corr_matrix,annot=True)
plt.show()

# %%



