def analyze_logs(
    log_context
):

    findings = []

    detected_errors = log_context.get(
        "detected_errors",
        []
    )

    for err in detected_errors:

        findings.append(
            f"Detected deployment error: {err}"
        )

    return findings