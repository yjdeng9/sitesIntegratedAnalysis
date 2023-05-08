



# 做一个卡方检验
from scipy.stats import chi2_contingency
import numpy as np

kf_data = np.array([[1, 2, 3], [4, 5, 6]])
chi2_contingency(kf_data)
