from services.analyzer_service.rules import analyze_api_health


def analyze(monitor_result: dict):
    response_time = monitor_result.get("response_time_ms") / 1000
    http_status = monitor_result.get("http_status")

    return analyze_api_health(response_time, http_status)