import yaml


def parse_yaml(
    file_content
):

    extracted = {

        "node_version": None,

        "steps": []
    }

    try:

        data = yaml.safe_load(
            file_content
        )

        jobs = data.get(
            "jobs",
            {}
        )

        for _, job in jobs.items():

            steps = job.get(
                "steps",
                []
            )

            for step in steps:

                extracted[
                    "steps"
                ].append(step)

                if (
                    "uses" in step
                    and "setup-node"
                    in step["uses"]
                ):

                    extracted[
                        "node_version"
                    ] = (
                        step.get(
                            "with",
                            {}
                        ).get(
                            "node-version"
                        )
                    )

    except Exception as e:

        extracted[
            "parse_error"
        ] = str(e)

    return extracted