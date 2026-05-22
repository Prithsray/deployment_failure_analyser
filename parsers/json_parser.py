import json


def parse_json_config(
    file_content
):

    extracted = {

        "node_version": None,

        "aws_runtime": None,

        "steps": []
    }

    try:

        data = json.loads(
            file_content
        )

        pipeline = data.get(
            "pipeline",
            {}
        )

        extracted[
            "node_version"
        ] = pipeline.get(
            "node_version"
        )

        extracted[
            "aws_runtime"
        ] = pipeline.get(
            "aws_runtime"
        )

        extracted[
            "steps"
        ] = pipeline.get(
            "steps",
            []
        )

    except Exception as e:

        extracted[
            "parse_error"
        ] = str(e)

    return extracted