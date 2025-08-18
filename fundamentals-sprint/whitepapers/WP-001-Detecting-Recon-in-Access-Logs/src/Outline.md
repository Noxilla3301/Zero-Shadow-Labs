# WP-001 — Detecting Reconnaissance in Access Logs

## Abstract (120–180 words)
Access logs can have specific indicators that can hint at / imply malicious activity. These factors can range from things like: logs of a user who seems to continuously be probing around on a web application, and keeps running into dead ends. Or, a user who's continuously running into specific errors like errors 404 (not found, server can't find the requested resource.) and 410 (gone, which means the target resource is no longer available at the origin server). These errors indicate anomalous activity, as a normal user wouldn't be constantly running into these walls if they were using the web application for its intended and regular use. A similar indication would be a user who continuously keeps hitting 'new paths' instead of browsing normally. Indications of malicious activity can vary, and the actual utility of said attacks can as well- ranging from manual to automated tactics (bots/scripts).

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
