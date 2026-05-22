def analyze_config(
    yaml_context
):

    findings = []

    node_version = yaml_context.get(
        "node_version"
    )

    if node_version:

        findings.append(
            f"Pipeline uses NodeJS {node_version}"
        )

    if not node_version:

        findings.append(
            "NodeJS version not explicitly configured."
        )

    return findings