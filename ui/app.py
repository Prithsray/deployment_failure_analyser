import streamlit as st
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from utils.file_loader import (
    load_file
)

from agents.orchestrator import (
    run_analysis
)

from agents.fix_mapper_agent import (
    map_errors_to_yaml
)

from parsers.log_parser import (
    parse_logs
)

from agents.chat_agent import (
    start_chat
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(

    page_title=
        "AI Deployment Failure Analyzer",

    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title(
    "AI Deployment Failure Analyzer"
)

st.markdown(
    """
Analyze:
- GitHub Actions YAML
- Deployment Logs
- NodeJS deployment failures
- AWS runtime issues
- ESM/CommonJS conflicts
"""
)

# =====================================================
# FILE UPLOADS
# =====================================================

config_file = st.file_uploader(

    "Upload Config File (.yml/.yaml/.json)",

    type=["yml", "yaml", "json"]
)

log_file = st.file_uploader(

    "Upload Deployment Logs (.txt/.log)",

    type=["txt", "log"]
)

# =====================================================
# ANALYZE BUTTON
# =====================================================

if st.button(
    "Analyze Deployment Failure"
):

    if (
        not config_file
        or not log_file
    ):

        st.error(
            "Please upload both files."
        )

    else:

        config_content = (
            config_file.read()
            .decode("utf-8")
        )

        log_content = (
            log_file.read()
            .decode("utf-8")
        )

        # ============================================
        # MAIN ANALYSIS
        # ============================================

        with st.spinner(
            "Analyzing deployment..."
        ):

            result = run_analysis(

                config_content,

                log_content,

                config_file.name
            )

        # ============================================
        # STORE CONTEXT IN SESSION STATE FOR CHAT
        # ============================================

        st.session_state["analysis_result"] = result["response"]
        st.session_state["config_content"]  = config_content
        st.session_state["log_content"]     = log_content

        # ============================================
        # DISPLAY RESULTS
        # ============================================

        st.success(
            "Analysis Complete"
        )

        st.subheader(
            "LLM Provider"
        )

        st.write(
            result["provider"]
        )

        st.subheader(
            "Deployment Analysis"
        )

        st.markdown(
            result["response"]
        )

        # ============================================
        # LINE-WISE FIXES
        # ============================================

        log_context = parse_logs(
            log_content
        )

        mapped_fixes = map_errors_to_yaml(

            log_context.get(
                "detected_errors",
                []
            ),

            config_content
        )

        st.subheader(
            "Line-wise YAML Fix Mapping"
        )

        for idx, item in enumerate(
            mapped_fixes,
            start=1
        ):

            with st.expander(
                f"Error {idx}: {item['error']}"
            ):

                st.markdown(
                    f"""
### Problem
{item['problem']}

### Recommended Fix
{item['recommended_fix']}
"""
                )

                related_yaml = item.get(
                    "related_yaml",
                    []
                )

                if related_yaml:

                    st.markdown(
                        "### YAML Lines To Change"
                    )

                    for line in related_yaml:

                        st.code(
                            f"Line {line['line_number']}: {line['content']}"
                        )

                replacement = item.get(
                    "replacement",
                    {}
                )

                if replacement:

                    st.markdown(
                        "### Suggested Change"
                    )

                    st.code(
                        f"""
FROM:
{replacement.get('from')}

TO:
{replacement.get('to')}
"""
                    )

# =====================================================
# CHAT SECTION
# =====================================================

st.divider()

st.subheader(
    "Ask Follow-up Questions"
)

user_query = st.text_input(
    "Ask deployment-related question"
)

if st.button(
    "Ask AI"
):

    if user_query:

        from utils.guardrails import (
            is_programming_related
        )

        from config.settings import (
            invoke_with_fallback
        )

        # ==========================================
        # GUARDRAIL CHECK
        # ==========================================

        if not is_programming_related(
            user_query
        ):

            st.warning(
                "Only programming and deployment-related queries are allowed."
            )

        else:

            analysis_context = st.session_state.get(
                "analysis_result",
                None
            )

            # ======================================
            # GUARD: ANALYSIS MUST RUN FIRST
            # ======================================

            if not analysis_context:

                st.warning(
                    "Please run an analysis first before asking questions."
                )

            else:

                config_ctx = st.session_state.get(
                    "config_content",
                    ""
                )

                log_ctx = st.session_state.get(
                    "log_content",
                    ""
                )

                # ==================================
                # CONTEXT-AWARE PROMPT
                # ==================================

                prompt = f"""
You are an AI DevOps assistant helping debug a deployment failure.

Deployment Analysis Context:
{analysis_context}

--- YAML CONFIG ---
{config_ctx}

--- DEPLOYMENT LOGS ---
{log_ctx}

User Question:
{user_query}

Answer clearly and concisely based on the context above.
"""

                response = invoke_with_fallback(
                    prompt
                )

                st.markdown(
                    f"**AI:** {response['response']}"
                )