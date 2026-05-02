# 12-Weeks SQL PySpark

A hands-on learning repository for building practical SQL and PySpark skills through notebook-based exercises. The project combines SQL case studies with Apache Spark practice so each concept is tied to small, runnable examples.

## Repository Overview

This repository is organized around weekly practice and case-study notebooks. The current notebooks focus on analytics patterns that are common in data engineering, product analytics, and business reporting.

## Contents

| Notebook | Focus |
| --- | --- |
| `Project1-Case1.ipynb` | Daily active users and next-day login retention analysis |
| `Project1-Case2.ipynb` | Top product per category using ranking and aggregation logic |
| `Project1-Case3.ipynb` | Latest transaction per user with window functions |
| `Project1-Case4.ipynb` | Funnel analysis for view, cart, and purchase completion |
| `Spark.ipynb` | Apache Spark and PySpark fundamentals, including DataFrame operations |

## Skills Practiced

- SQL table creation, inserts, filtering, grouping, and ordering
- Aggregations with `COUNT`, `COUNT DISTINCT`, and grouped summaries
- Joins for behavioral and retention analysis
- Window functions such as `ROW_NUMBER` and `RANK`
- Funnel analysis using grouped event data
- PySpark DataFrame creation, transformations, deduplication, and column operations

## How to Use

Open the notebooks in a notebook environment that supports SQL magic commands and PySpark execution, such as Databricks, Jupyter with Spark configured, or another Spark-enabled notebook platform.

Recommended workflow:

1. Open one notebook at a time.
2. Run the setup cells to create sample tables or DataFrames.
3. Run the solution cells and review the output.
4. Modify the sample data to test edge cases and strengthen understanding.

## Project Goals

The goal of this repository is to document steady progress through SQL and PySpark practice while building a portfolio of clear, reviewable examples. Each notebook is intentionally small so the core idea is easy to understand, rerun, and expand.

## Status

Active learning repository. More SQL, PySpark, and data engineering exercises will be added over time.
