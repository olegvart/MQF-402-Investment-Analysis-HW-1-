import numpy as np
import pandas as pd

# 1. LOAD DATA (change the path if your file is somewhere else, e.g. "data/Portfolios_Formed_on_Size_daily.txt")
df = pd.read_csv("data/Portfolios_Formed_on_Size_daily.txt", sep="\t", index_col=0).dropna(how="all")
df.columns = [c.strip() for c in df.columns]

# 2. OWN OLS FUNCTION (no stats packages allowed)
def ols(y, X, L=10):
    n, k = X.shape
    XtXi = np.linalg.inv(X.T @ X)
    b = XtXi @ X.T @ y                      # coefficients
    e = y - X @ b                           # residuals
    se = np.sqrt(np.diag(e @ e / (n - k) * XtXi))            # classical SE
    S0 = (X * e[:, None]).T @ (X * e[:, None])
    se_white = np.sqrt(np.diag(XtXi @ S0 @ XtXi))            # White SE
    S = S0.copy()
    for l in range(1, L + 1):                                # Newey-West SE
        G = (X[l:] * e[l:, None]).T @ (X[:-l] * e[:-l, None])
        S += (1 - l / (L + 1)) * (G + G.T)
    se_nw = np.sqrt(np.diag(XtXi @ S @ XtXi))
    r2 = 1 - e @ e / ((y - y.mean()) @ (y - y.mean()))
    return b, se, se_white, se_nw, r2

# 3. RUN Q3: market return today on Decile i return yesterday
vw = df["vwretd"].values
for d in ["1-Dec", "2-Dec", "3-Dec"]:
    x = df[d].values
    y = vw[1:]                                       # today's market return
    X = np.column_stack([np.ones(len(y)), x[:-1]])   # constant + yesterday's decile return
    b, se, sew, sen, r2 = ols(y, X)
    print(d, "c=%.4f phi=%.4f t_classical=%.2f t_White=%.2f t_NW=%.2f R2=%.4f"
          % (b[0], b[1], b[1]/se[1], b[1]/sew[1], b[1]/sen[1], r2))
