import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json


def main():
    with open("results/generated_response.json", "r") as f:
        data = json.load(f)

    methods = ["fixed_length", "sentence_based", "semantic"]
    win_rate = [data["win_rate"][m] for m in methods]

    method_labels = ["Fixed Length", "Sentence Based", "Semantic"]

    fig_wr, ax_wr = plt.subplots(figsize=(6, 6))

    ax_wr.bar(method_labels, win_rate, color="steelblue", alpha=0.7)
    ax_wr.set_title("Win Rate")
    ax_wr.grid(axis="y", alpha=0.3)

    fig_mat, ax_mat = plt.subplots(figsize=(6, 6))

    pairwise_mat = np.zeros((3, 3))
    for i1, m1 in enumerate(methods):
        for i2, m2 in enumerate(methods):
            if m2 == m1:
                continue
            pairwise_mat[i1][i2] = data["pairwise"][m1][m2]

    sns.heatmap(
        pairwise_mat, annot=True, xticklabels=method_labels, yticklabels=method_labels
    )
    ax_mat.set_xlabel("Competing Method")
    ax_mat.set_ylabel("Winning Method")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
