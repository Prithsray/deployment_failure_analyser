ALLOWED_KEYWORDS = [

    # Programming
    "python",
    "javascript",
    "node",
    "nodejs",
    "npm",
    "module",
    "package",
    "dependency",

    # DevOps
    "deployment",
    "build",
    "pipeline",
    "ci",
    "cd",
    "github actions",

    # AWS
    "aws",
    "lambda",
    "cloudformation",
    "s3",
    "cloudfront",

    # Errors
    "error",
    "exception",
    "syntaxerror",
    "module_not_found",
    "err_require_esm",

    # Infra
    "docker",
    "yaml",
    "json",
    "runtime",

    # Logs
    "stack trace",
    "logs",
    "failed",
    "debug",
    "wrong",
    "step",
    "yml",
    "line"
]


BLOCKED_KEYWORDS = [

    "politics",
    "religion",
    "violence",
    "hack bank",
    "malware",
    "porn",
    "adult",
    "dating",
    "crypto scam"
]


def is_programming_related(
    text
):

    text = text.lower()

    # =====================================
    # BLOCKED CONTENT
    # =====================================

    for blocked in BLOCKED_KEYWORDS:

        if blocked in text:

            return False

    # =====================================
    # ALLOWED CONTENT
    # =====================================

    for keyword in ALLOWED_KEYWORDS:

        if keyword in text:

            return True

    return False