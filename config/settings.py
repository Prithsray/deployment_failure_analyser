import os
import httpx

from langchain_openai import (
    ChatOpenAI
)

from langchain_ollama import (
    ChatOllama
)


# =====================================================
# HTTP CLIENT
# =====================================================

http_client = httpx.Client(
    verify=False,
    timeout=120
)


# =====================================================
# PRIMARY CLOUD LLM
# =====================================================

PRIMARY_LLM = ChatOpenAI(

    base_url="https://genailab.tcs.in",

    model="azure_ai/genailab-maas-DeepSeek-V3-0324",

    api_key='sk-LMT_wLg-A0Ui2ibM_0F60g',

    http_client=http_client,

    temperature=0
)


# =====================================================
# OLLAMA FALLBACK
# =====================================================

FALLBACK_LLM = ChatOllama(

    base_url="http://localhost:11434",

    model="llama-3.2-3b-it:latest",

    temperature=0
)


# =====================================================
# SAFE INVOCATION
# =====================================================

def invoke_with_fallback(
    prompt
):

    try:

        response = PRIMARY_LLM.invoke(
            prompt
        )

        return {
            "provider":
                "TCS DeepSeek",

            "response":
                response.content
        }

    except Exception as e:

        print(
            f"\nPrimary LLM failed: {str(e)}"
        )

        print(
            "\nSwitching to Ollama..."
        )

        response = FALLBACK_LLM.invoke(
            prompt
        )

        return {
            "provider":
                "Ollama Devstral",

            "response":
                response.content
        }