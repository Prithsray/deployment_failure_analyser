import os

from parsers.yaml_parser import (
    parse_yaml
)

from parsers.json_parser import (
    parse_json_config
)

from parsers.log_parser import (
    parse_logs
)

from parsers.nodejs_parser import (
    analyze_nodejs_patterns
)

from agents.rag_agent import (
    retrieve_similar_failures
)

from agents.config_agent import (
    analyze_config
)

from agents.log_agent import (
    analyze_logs
)

from agents.web_agent import (
    search_web_context
)

from prompts.analysis_prompt import (
    build_prompt
)

from config.settings import (
    invoke_with_fallback
)


def run_analysis(
    config_content,
    log_content,
    config_path
):

    extension = os.path.splitext(
        config_path
    )[1].lower()

    # ==========================================
    # CONFIG PARSING
    # ==========================================

    if extension in [
        ".yml",
        ".yaml"
    ]:

        config_context = parse_yaml(
            config_content
        )

    elif extension == ".json":

        config_context = parse_json_config(
            config_content
        )

    else:

        raise ValueError(
            "Unsupported config format."
        )

    # ==========================================
    # LOG PARSING
    # ==========================================

    log_context = parse_logs(
        log_content
    )

    nodejs_analysis = analyze_nodejs_patterns(
        log_content,
        config_context
    )

    config_analysis = analyze_config(
        config_context
    )

    log_analysis = analyze_logs(
        log_context
    )

    rag_results = retrieve_similar_failures(
        str(log_context)
    )

    web_results = search_web_context(
        " ".join(
            log_context.get(
                "detected_errors",
                []
            )
        )
    )

    prompt = build_prompt(

        yaml_context=config_context,

        log_context=log_context,

        nodejs_analysis=nodejs_analysis,

        config_analysis=config_analysis,

        log_analysis=log_analysis,

        rag_context=rag_results,

        web_context=web_results
    )

    return invoke_with_fallback(
        prompt
    )