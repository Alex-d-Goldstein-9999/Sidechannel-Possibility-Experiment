import tensorflow as tf

# Simple heavy matrix multiplication loop
def run_gpu_load(iterations=200):
    print("Running GPU load…")
    for _ in range(iterations):
        a = tf.random.uniform((2000, 2000))
        b = tf.random.uniform((2000, 2000))
        c = tf.matmul(a, b)
    print("Done.")

if __name__ == "__main__":
    run_gpu_load()
