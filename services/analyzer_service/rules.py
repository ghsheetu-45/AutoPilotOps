def analyze_api_health(response_time, http_status):
    if http_status != 200:
        return {
            "status": "DOWN",
            "severity": "CRITICAL",
            "reason": "API not reachable"
        }

    if response_time > 3:
        return {
            "status": "SLOW",
            "severity": "HIGH",
            "reason": "Response time above 3 seconds"
        }

    if response_time > 1:
        return {
            "status": "DEGRADED",
            "severity": "MEDIUM",
            "reason": "Response time above 1 second"
        }

    return {
        "status": "HEALTHY",
        "severity": "LOW",
        "reason": "API is healthy"
    }