"""Render the actual CSV only; never run a new simulation."""
import csv
import math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    with open("results.csv", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("CSV contains no results")
    table = [r"\begin{tabular}{rrr}", r"\toprule", r"投针数 $N$ & 相交数 $K$ & $\widehat{\pi}$ \\", r"\midrule"]
    for row in rows:
        table.append(f"{int(row['n']):,} & {int(row['crossings']):,} & {float(row['pi_estimate']):.8f}" + r" \\")
    table.extend([r"\bottomrule", r"\end{tabular}"])
    Path("results-table.tex").write_text("\n".join(table) + "\n", encoding="utf-8")
    params = ["实际实验参数（各组分别初始化随机数生成器）："]
    for row in rows:
        params.append(f"$N={int(row['n'])}$，seed={int(row['seed'])}，针长 $L={float(row['needle_length']):g}$，线间距 $d={float(row['line_spacing']):g}$。" + r"\par")
    Path("results-params.tex").write_text("\n".join(params) + "\n", encoding="utf-8")
    ns = [int(row['n']) for row in rows]
    estimates = [float(row['pi_estimate']) for row in rows]
    fig, ax = plt.subplots(figsize=(7.2, 3.3), layout="constrained")
    ax.plot(ns, estimates, color="#0072B2", marker="o", label="Simulation estimate")
    ax.axhline(math.pi, color="#555555", linestyle="--", label="Reference pi")
    for n, value in zip(ns, estimates):
        ax.annotate(f"{value:.5f}", (n, value), xytext=(0, 8), textcoords="offset points", ha="center")
    ax.set_xscale("log")
    ax.margins(x=0.16)
    ax.set_xticks(ns, [f"{n:,}" for n in ns])
    ax.set(xlabel="Number of throws N (log scale)", ylabel="Estimated pi")
    lo, hi = min(estimates + [math.pi]), max(estimates + [math.pi])
    margin = max((hi-lo)*0.5, 0.01)
    ax.set_ylim(lo-margin, hi+margin)
    ax.grid(alpha=0.2)
    ax.legend(loc="best")
    fig.savefig("results.png", dpi=220, facecolor="white")
    plt.close(fig)
    errors = [abs(v-math.pi) for v in estimates]
    observation = "本次三组估计值分别为 " + "、".join(f"{v:.8f}" for v in estimates) + "；对应绝对误差为 " + "、".join(f"{e:.8f}" for e in errors) + "。"
    observation += "这些是固定种子下的实际结果；增加投针数并不保证每次误差单调减小，估计值也不要求恰好等于圆周率。"
    Path("results-observation.tex").write_text(observation + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
