# analyze_system.py (updated with adaptive per-cauldron tolerance)

import statistics
from collections import defaultdict

def remove_outliers(data, threshold=2.0):
    """
    Remove outliers using IQR (Interquartile Range) method.
    Outliers are values beyond threshold * IQR from Q1/Q3.
    """
    if len(data) < 4:
        return data
    
    sorted_data = sorted(data)
    q1_idx = len(sorted_data) // 4
    q3_idx = 3 * len(sorted_data) // 4
    q1 = sorted_data[q1_idx]
    q3 = sorted_data[q3_idx]
    iqr = q3 - q1
    
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered if len(filtered) > 0 else data

def compute_adaptive_tolerance(tickets):
    """
    Compute per-cauldron adaptive tolerance based on standard deviation of discrepancies.
    Uses 2σ rule with a minimum of 10% and a maximum of 30%.
    Excludes outliers and suspicious tickets from calculation.
    """
    discrepancies_by_cauldron = defaultdict(list)
    for t in tickets:
        cid = t.get('cauldron_id')
        d = t.get('pct_discrepancy')
        # Only include non-suspicious tickets for tolerance calculation
        status = t.get('discrepancy_status', '')
        if d is not None and status not in ['suspicious', 'over-reported', 'under-reported', 'no-drain-match']:
            discrepancies_by_cauldron[cid].append(abs(d))  # Use absolute value

    tolerance_by_cauldron = {}
    for cid, diffs in discrepancies_by_cauldron.items():
        if len(diffs) > 3:  # Minimum sample size
            # Remove outliers before calculating standard deviation
            clean_diffs = remove_outliers(diffs)
            if len(clean_diffs) > 1:
                sigma = statistics.stdev(clean_diffs)
                tol = max(0.10, min(0.30, 2 * sigma))  # Clamp between 10%-30%
            else:
                tol = 0.15  # fallback default
        else:
            tol = 0.15  # fallback for insufficient data
        tolerance_by_cauldron[cid] = tol
    return tolerance_by_cauldron

def apply_tolerance(tickets, tolerance_by_cauldron):
    for t in tickets:
        cid = t.get('cauldron_id')
        tol = tolerance_by_cauldron.get(cid, 0.15)
        d = t.get('pct_discrepancy')
        if d is None:
            t['discrepancy_status'] = 'no-data'
        elif d > tol:
            t['discrepancy_status'] = 'suspicious'
        else:
            t['discrepancy_status'] = 'match'
        t['tolerance_used'] = tol
    return tickets

def summarize_results(tickets, tolerance_by_cauldron):
    print("Adaptive per-cauldron tolerances:")
    for cid, tol in sorted(tolerance_by_cauldron.items()):
        print(f"  {cid}: {tol*100:.1f}%")

    total = len(tickets)
    suspicious = sum(t['discrepancy_status']=='suspicious' for t in tickets)
    print(f"\nSummary: {suspicious}/{total} suspicious ({suspicious/total*100:.1f}%)\n")

def run_adaptive_analysis(tickets):
    tolerance_by_cauldron = compute_adaptive_tolerance(tickets)
    tickets = apply_tolerance(tickets, tolerance_by_cauldron)
    summarize_results(tickets, tolerance_by_cauldron)
    return tickets, tolerance_by_cauldron

# Example usage (assuming you already have tickets with pct_discrepancy computed):
# tickets, tolerance_map = run_adaptive_analysis(tickets)