"""
Plot k-point convergence from pre-computed data.

Input:  kpoint-convergence.csv   (k_per_side, energy_ev)
Output: kpoint-convergence.png
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

HERE = Path(__file__).parent

df = pd.read_csv(HERE / "kpoint-convergence.csv")

E_ref = df["energy_ev"].iloc[-1]   # finest mesh as reference

fig, ax = plt.subplots(figsize=(3.4, 2.6))   # single-column width ≈ 3.4 in

ax.plot(
    df["k_per_side"], df["energy_ev"],
    "o-", color="#2c7bb6", linewidth=1.2,
    markersize=4, markerfacecolor="white", markeredgewidth=1.2,
)
ax.axhline(E_ref, color="gray", linewidth=0.8, linestyle="--", label="Converged value")

ax.set_xlabel(r"$k$-points per side")
ax.set_ylabel(r"Total energy (eV)")
ax.set_xticks(df["k_per_side"])
ax.xaxis.set_minor_locator(ticker.NullLocator())
ax.legend(fontsize=7, framealpha=0.5)
ax.tick_params(which="both", direction="in", top=True, right=True)

fig.tight_layout()
fig.savefig(HERE / "kpoint-convergence.png", dpi=300, bbox_inches="tight")
print("saved kpoint-convergence.png")
