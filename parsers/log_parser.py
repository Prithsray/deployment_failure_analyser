COMMON_ERRORS = [

    "MODULE_NOT_FOUND",

    "ERR_REQUIRE_ESM",

    "Cannot use import statement outside module",

    "Cannot find module",

    "npm ERR!",

    "SyntaxError",

    "MIME type",

    "Refused to execute script"
]


def parse_logs(
    log_text
):

    detected_errors = []

    important_lines = []

    lines = log_text.splitlines()

    for line in lines:

        for err in COMMON_ERRORS:

            if err.lower() in line.lower():

                detected_errors.append(err)

                important_lines.append(line)

    return {

        "detected_errors":
            list(set(detected_errors)),

        "important_lines":
            important_lines[:20]
    }