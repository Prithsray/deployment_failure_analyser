def build_prompt(

    yaml_context,

    log_context,

    nodejs_analysis,

    config_analysis,

    log_analysis,

    rag_context,

    web_context
):

    return f"""
You are an expert AI DevOps assistant.

Analyze the deployment issue.

==================================================
CI/CD CONFIG
==================================================

{yaml_context}

==================================================
DEPLOYMENT LOGS
==================================================

{log_context}

==================================================
NODEJS ANALYSIS
==================================================

{nodejs_analysis}

==================================================
CONFIG ANALYSIS
==================================================

{config_analysis}

==================================================
LOG ANALYSIS
==================================================

{log_analysis}

==================================================
SIMILAR HISTORICAL FAILURES
==================================================

{rag_context}

==================================================
WEB SEARCH RESULTS
==================================================

{web_context}

==================================================
TASKS
==================================================

1. Explain issue in simple English

2. Identify root cause

3. Explain why deployment failed

4. Recommend fixes

5. Recommend GitHub Action changes

6. Mention confidence score

7. Keep answer concise but detailed

==================================================
OUTPUT FORMAT
==================================================

# Deployment Failure Analysis

## Root Cause

## Explanation

## Recommended Fix

## Suggested Pipeline Changes

## Confidence Score
"""