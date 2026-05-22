def map_yaml_lines(
    yaml_content
):

    line_map = []

    lines = yaml_content.splitlines()

    for idx, line in enumerate(lines):

        stripped = line.strip()

        if stripped:

            line_map.append(
                {
                    "line_number": idx + 1,
                    "content": stripped
                }
            )

    return line_map