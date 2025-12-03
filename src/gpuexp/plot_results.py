import pandas as pd
import matplotlib.pyplot as plt

def plot(baseline="baseline.csv", gpu="with_gpu.csv"):
    base = pd.read_csv(baseline)["interval_ns"]
    gpu  = pd.read_csv(gpu)["interval_ns"]

    plt.figure(figsize=(12,6))
    plt.plot(base[:5000], label="Baseline", alpha=0.7)
    plt.plot(gpu[:5000], label="With GPU Load", alpha=0.7)
    plt.title("CPU Timer Jitter Under GPU Load")
    plt.xlabel("Sample Index")
    plt.ylabel("Interval (ns)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("timing_plot.png")
    plt.show()

if __name__ == "__main__":
    plot()
