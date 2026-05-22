import typer

from utils.file_loader import (

    load_file,

    validate_config_file,

    validate_log_file
)

from utils.formatter import (

    print_header,

    print_section
)

from agents.orchestrator import (
    run_analysis
)

from agents.chat_agent import (
    start_chat
)

app = typer.Typer()


@app.command()
def analyze(

    config: str = typer.Option(
        ...,
        "--config"
    ),

    logs: str = typer.Option(
        ...,
        "--logs"
    )
):

    validate_config_file(
        config
    )

    validate_log_file(
        logs
    )

    print_header(
        "AI Deployment Failure Analyzer"
    )

    config_content = load_file(
        config
    )

    log_content = load_file(
        logs
    )

    result = run_analysis(

        config_content,

        log_content,

        config
    )

    print_section(
        "LLM Provider",
        result["provider"]
    )

    print_section(
        "Analysis",
        result["response"]
    )

    # ==========================================
    # CHAT MODE
    # ==========================================

    start_chat(
        result["response"]
    )


if __name__ == "__main__":
    app()