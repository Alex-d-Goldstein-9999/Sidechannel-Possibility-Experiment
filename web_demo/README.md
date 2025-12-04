# GPU Side-Channel Attack Web Demo

This demonstration shows how a malicious webpage can detect GPU activity in other browser tabs using timing-based side-channel attacks.

## Overview

Modern browsers share GPU resources across all tabs. This demo exploits that sharing by:

1. **Attacker Page**: Continuously measures GPU operation timing using WebGL
2. **Victim Page**: Simulates user activity that triggers GPU usage
3. **Detection**: The attacker detects timing variations that indicate concurrent GPU usage

## How to Run

### Option 1: Using Python HTTP Server

```bash
# Navigate to the web_demo directory
cd web_demo

# Start the server
python3 server.py

# Open in your browser:
# - Attacker: http://localhost:8000/attacker.html
# - Victim:   http://localhost:8000/victim.html
```

### Option 2: Using Python's Built-in Server

```bash
cd web_demo
python3 -m http.server 8000
```

### Option 3: Open Directly

You can also open the HTML files directly in your browser, though some features may be limited due to CORS restrictions.

## Demonstration Steps

1. **Open the attacker page** (`attacker.html`) in one browser tab
2. **Click "Start Monitoring"** to begin the attack
3. **Open the victim page** (`victim.html`) in another browser tab
4. **Interact with the victim page**:
   - Click "Start Heavy GPU Load" button
   - Draw on the canvas
   - Move your mouse around
5. **Observe the attacker page** - it should detect the GPU activity through timing measurements

## What You'll See

- **Timing measurements**: Real-time graph showing GPU operation timing
- **Activity detection**: Status indicator changes when GPU activity is detected
- **Statistics**: Average timing, maximum timing, and jitter measurements
- **Visual feedback**: The attacker page will show warnings when activity is detected

## Technical Details

### Attack Mechanism

1. **High-frequency probes**: The attacker continuously performs WebGL operations and measures their completion time
2. **Baseline establishment**: First 100 samples establish a baseline timing
3. **Anomaly detection**: When timing exceeds 1.5x the baseline, activity is detected
4. **Shared resource contention**: GPU operations from other tabs cause measurable delays

### Why This Works

- All browser tabs share the same physical GPU hardware
- GPU operations are queued and scheduled deterministically
- Resource contention creates measurable timing differences
- JavaScript timing APIs (`performance.now()`) are precise enough to detect these differences

## Security Implications

This demonstration shows that:

- **Cross-tab inference**: Malicious websites can detect activity in other tabs
- **No permission required**: The attack works without any special permissions
- **Hardware-level vulnerability**: The issue stems from shared GPU hardware, not browser bugs
- **Real-world applicability**: Similar techniques could detect:
  - User interactions (mouse movements, clicks)
  - Website rendering patterns
  - Machine learning model inference
  - Video playback
  - Gaming activity

## Limitations of This Demo

- **Simplified**: Real attacks would use more sophisticated statistical analysis
- **Local only**: This demo runs locally; real attacks would be from remote websites
- **Detection only**: This demo detects activity but doesn't infer specific actions
- **Browser dependent**: Effectiveness varies by browser and GPU driver

## Related Work

This demo is inspired by research on:
- GPU side-channel attacks (e.g., "GPU-Zoom" attacks)
- Cross-origin timing attacks
- Microarchitectural side-channels
- Browser security and isolation

## Files

- `attacker.html` - The malicious page that performs the attack
- `victim.html` - The victim page that simulates user activity
- `server.py` - Simple HTTP server to serve the demo files
- `README.md` - This file

## Notes

- This is a **demonstration only** for educational purposes
- The attack works best when both tabs are visible and active
- Results may vary based on your GPU, browser, and system load
- Modern browsers are implementing mitigations, but the fundamental hardware issue remains
