import os


ALLOWED_CONFIG_EXTENSIONS = [

    ".json",

    ".yml",

    ".yaml"
]


ALLOWED_LOG_EXTENSIONS = [

    ".txt",

    ".log"
]


def validate_config_file(
    path
):

    extension = os.path.splitext(
        path
    )[1].lower()

    if (
        extension
        not in ALLOWED_CONFIG_EXTENSIONS
    ):

        raise ValueError(
            "Only .json, .yml and .yaml config files allowed."
        )


def validate_log_file(
    path
):

    extension = os.path.splitext(
        path
    )[1].lower()

    if (
        extension
        not in ALLOWED_LOG_EXTENSIONS
    ):

        raise ValueError(
            "Only .txt and .log files allowed."
        )


def load_file(
    path
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()