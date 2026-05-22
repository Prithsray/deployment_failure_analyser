import re


def analyze_nodejs_patterns(
    log_text,
    yaml_context
):

    findings = []

    if (
        "ERR_REQUIRE_ESM"
        in log_text
    ):

        findings.append(
            {
                "type":
                    "ESM_CONFLICT",

                "severity":
                    "HIGH"
            }
        )

    if (
        "Cannot use import statement outside module"
        in log_text
    ):

        findings.append(
            {
                "type":
                    "COMMONJS_ESM_CONFLICT",

                "severity":
                    "HIGH"
            }
        )

    module_match = re.findall(
        r"Cannot find module '(.*?)'",
        log_text
    )

    if module_match:

        findings.append(
            {
                "type":
                    "MODULE_NOT_FOUND",

                "modules":
                    module_match
            }
        )

    return findings