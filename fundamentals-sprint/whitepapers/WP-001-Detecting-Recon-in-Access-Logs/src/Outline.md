# WP-001 — Detecting Reconnaissance in Access Logs

## Abstract (120–180 words)
[Draft a brief summary of the problem, approach, and key findings.]

## Problem Statement
Web servers often face automated reconnaissance (link scraping, directory brute force, param fuzzing). We need practical signals in access logs that distinguish normal traffic from recon with low false positives.

## Background
- Log anatomy (common/combined format)
- Typical recon behaviors: many 404s, parameter spraying, strange user-agents

## Method / Approach
- Collect sample logs (real or synthetic)
- Use `logpeek` to compute top paths, status codes, and user-agents
- Define simple thresholds/ratios (e.g., 404 ratio, unique path rate)

## Results
- Table: sessions with 404 ratio > X%
- Figures: top paths, status distribution

## Limitations
- Shared IPs; NAT; benign bots; CDN effects

## Recommendations
- Baseline your 404 ratio; alert on deviations
- Track UA entropy; rate-limit anomaly bursts
- Store IP/session aggregates for 24–72h

## References
[1] OWASP, [2] Web log formats, [3] Research articles/CTI posts
