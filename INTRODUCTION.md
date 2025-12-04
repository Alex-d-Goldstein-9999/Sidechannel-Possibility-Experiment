# Introduction: GPU Side-Channel Attacks in Web Browsers

Most modern computing devices leverage graphics processing units, or GPUs. From web rendering to gaming to machine learning, GPUs have become an integral part of modern computing. As a result of their increased role in processing data, numerous microarchitectural features have been exposed by adversaries to carry out attacks on users, specifically side-channel attacks. Side-channel attacks are attacks that leverage indirect information leakage from a machine to infer what a person may be doing. Information such as timing, cache contention, and memory access patterns can be used to specifically pinpoint a person's activity on a machine. While CPUs have had decades to solidify their microarchitectural security, GPUs lack comparable protection and are more vulnerable to information leakage.

Modern GPUs rely on large shared caches, memory systems, and massively parallel execution units operating across multiple processes. These shared resources allow attackers to monitor changes in latency, memory contention, or scheduling behavior to infer the activity happening on the victim's co-running workloads. Design choices of GPUs that maximize throughput, such as batching, deterministic scheduling, and shared compute pipelines, also make GPU behavior highly observable and thus exploitable.

So what do web browsers have to do with this? Modern browser APIs like WebGL and WebGPU provide untrusted JavaScript code with direct access to a machine's GPU compute and memory resources. This allows attackers to run high-frequency GPU workloads through a webpage to probe the victim's shared hardware components and observe specific timing differences. Because GPU hardware is shared across tabs, attackers can infer timing signal leakage about other browser history or even native applications running concurrently within the same system.

Unfortunately, the browser was never designed to consider GPU sharing. As a result, malicious webpages can infer user behavior such as keystrokes, website rendering patterns, or even information within a machine learning model. Understanding the vulnerabilities of GPUs and how web browsers amplify these risks is fundamental to developing modern defenses with continued GPU integration.

## Our Demonstration

This project provides a simple, local demonstration of GPU side-channel attacks that can be run on your own computer. The demonstration consists of:

1. **A web-based attack scenario**: Two HTML pages that simulate an attacker and victim
2. **Timing measurements**: Real-time analysis of GPU operation timing to detect cross-tab activity
3. **Visual feedback**: Interactive demonstration showing how timing variations reveal concurrent GPU usage

The attack works by continuously measuring the time required to complete WebGL operations. When other browser tabs (or applications) use the GPU, these measurements show increased latency due to resource contention. By analyzing these timing patterns, an attacker can detect when the victim is performing GPU-intensive activities, even without direct access to the victim's tab.

This demonstration serves as a proof-of-concept that GPU side-channel attacks are not merely theoretical but can be practically demonstrated using standard web technologies available in modern browsers. The attack requires no special permissions, exploits hardware-level resource sharing, and works across browser tabs—highlighting the fundamental security challenges posed by shared GPU resources in modern computing systems.
