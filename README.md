# Law Degree Navigator 2025

A Python-based visualization tool designed for Kenyan law students and academic advisors to map out the prerequisite structure of LLB programs as mandated by the Council of Legal Education (CLE).

## Features
- **DAG Visualization**: Uses Directed Acyclic Graphs to show how Year 1 courses impact Year 4 eligibility.
- **KSL Path Finder**: Specifically highlights paths required to reach the Advocates Training Program (Kenya School of Law).
- **2025 Curriculum Mapping**: Pre-loaded with standard Kenyan university law modules.

## Installation
```bash
pip install -r requirements.txt
python navigator.py
```

## Usage
The script generates a high-resolution PNG (`llb_pathway_2025.png`) showing the dependencies between courses like Torts, Civil Procedure, and Evidence.