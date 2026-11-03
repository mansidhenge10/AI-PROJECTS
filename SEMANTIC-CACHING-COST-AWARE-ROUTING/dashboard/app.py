
import streamlit as st
import sqlite3
import pandas as pd
import os

DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "metrics.db"
)

st.set_page_config(
    page_title="AI Routing Analytics",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Semantic Cache & Cost-Aware Routing")
st.caption("LLM Performance, Token Usage and Cache Analytics")

if not os.path.exists(DATABASE_PATH):
    st.warning("Metrics database not found.")
    st.stop()

connection = sqlite3.connect(DATABASE_PATH)

df = pd.read_sql_query(
    "SELECT * FROM request_metrics ORDER BY id DESC",
    connection
)

connection.close()

if df.empty:
    st.info("No requests recorded yet.")
    st.stop()

# Data preparation
df["prompt_tokens"] = df["prompt_tokens"].fillna(0)
df["completion_tokens"] = df["completion_tokens"].fillna(0)
df["total_tokens"] = df["total_tokens"].fillna(0)
df["latency_ms"] = df["latency_ms"].fillna(0)
df["actual_api_cost"] = df["actual_api_cost"].fillna(0)

total = len(df)
hits = int((df["source"] == "semantic_cache").sum())
misses = int((df["source"] == "ollama").sum())

hit_rate = (hits / total) * 100 if total else 0
avg_latency = df["latency_ms"].mean()
total_tokens = int(df["total_tokens"].sum())
avg_inference = df["inference_time_seconds"].mean()

# KPI metrics
st.subheader("Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", total)
col2.metric("Cache Hits", hits)
col3.metric("Cache Hit Rate", f"{hit_rate:.2f}%")
col4.metric("Average Latency", f"{avg_latency:.2f} ms")

st.divider()

# Cache performance
st.subheader("Cache Performance")

performance = pd.DataFrame({
    "Request Type": ["Cache Hits", "Cache Misses"],
    "Requests": [hits, misses]
})

st.bar_chart(performance.set_index("Request Type"))

# Model usage
st.subheader("Model Usage")

model_usage = (
    df["model"]
    .fillna("Semantic Cache")
    .value_counts()
)

st.bar_chart(model_usage)

st.divider()

# Token analytics
st.subheader("Token Analytics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Prompt Tokens",
    f"{int(df['prompt_tokens'].sum()):,}"
)

col2.metric(
    "Completion Tokens",
    f"{int(df['completion_tokens'].sum()):,}"
)

col3.metric(
    "Total Tokens",
    f"{total_tokens:,}"
)

# Latency analytics
st.subheader("Latency Analytics")

col1, col2 = st.columns(2)

col1.metric(
    "Average Request Latency",
    f"{avg_latency:.2f} ms"
)

col2.metric(
    "Average Model Inference",
    f"{avg_inference:.2f} seconds"
)

# Cost information
st.subheader("Inference Cost")

total_cost = df["actual_api_cost"].sum()

st.metric(
    "Actual API Cost",
    f"${total_cost:.4f}"
)

st.caption(
    "Local Ollama inference has zero API charges. "
    "Electricity and hardware costs are not included."
)

st.divider()

# Request history
st.subheader("Request History")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.caption("Dashboard data is loaded from the SQLite metrics database.")
