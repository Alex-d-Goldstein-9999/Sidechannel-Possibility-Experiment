import time
import sys
import csv

def run_probe(duration_sec=5, outfile=sys.argv[1]):
    data = []
    start = time.perf_counter_ns()
    last = start
    
    while True:
        now = time.perf_counter_ns()
        interval = now - last
        data.append(interval)
        last = now

        if (now - start) / 1e9 >= duration_sec:
            break

    with open(outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["interval_ns"])
        for v in data:
            w.writerow([v])

    print(f"Saved {len(data)} samples to {outfile}")

if __name__ == "__main__":
    run_probe()
