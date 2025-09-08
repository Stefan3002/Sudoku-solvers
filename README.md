# Sudoku Solvers: From Brute Force to Logic

This repository contains the implementations and scripts used in the research study **"From Brute Force to Logic: Analyzing Diverse Approaches for Solving Sudoku Puzzles"**, authored by **Ștefan Secrieru, Claudia Iasmina Lazăr, and Roxana Andreea Goina**, presented at **SYNASC 2025**.  
The study delivers a comparative performance analysis of multiple well-known Sudoku-solving methods, using rigorous statistical techniques and large-scale benchmarks.

## 📋 Overview

The repository provides reproducible implementations of classic Sudoku-solving algorithms, together with scripts used for benchmarking and data collection.  
The goal is to evaluate **efficiency, stability, and scalability** of different solving approaches.

### Algorithms Covered

- **Depth-First Search (DFS / Backtracking)**
- **Breadth-First Search (BFS)**
- **Dancing Links (DLX)**
- **Constraint Satisfaction Problem (CSP) encoding**
- **Satisfiability (SAT) encoding**

Each algorithm was tested on:
- Classical *benchmark puzzles* (e.g., Al Escargot, Platinum Blonde, Easter Monster, Golden Nugget).
- A **large dataset** of 3 million Sudoku puzzles (sourced from [Kaggle](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings)).

## 📊 Benchmark Methodology

Performance was evaluated with a strong focus on reducing bias. The testing pipeline included:

- **Repeated measurements** to smooth hardware fluctuations.  
- **Warm-up rounds** to avoid cold-start and caching effects.  
- **Garbage collector management** (manual triggers, disabled during tests).  
- **Bootstrap resampling** (1000 samples) to calculate 95% confidence intervals for metrics.

### Key Metrics

- **Mean solving time** (ms)  
- **Median solving time** (ms)  
- **Standard deviation**  
- **Performance degradation (%)** across increasing puzzle difficulty  

Statistical tests used:
- **Mann–Whitney U test** (performance shifts by difficulty range).  
- Confidence intervals and effect analysis.  

Test environment:
- CPU: Intel® Core™ i7-11800H × 16  
- RAM: 16 GB  
- OS: Ubuntu 24.04.1 LTS  
- Language: Python (with [`PySAT`](https://pysathq.github.io/docs/html/) and [`python-constraint`](https://pypi.org/project/python-constraint/))  

## 📈 Results (Highlights)

- **SAT**: Fastest approach, *no performance degradation* across difficulties.  
- **DLX**: High performance, but with ~25% degradation at hardest puzzles.  
- **CSP**: Competitive on easy puzzles, but up to **200% slower** on hardest ones.  
- **DFS**: Moderate performance, easy to implement.  
- **BFS**: Worst performance, included mainly for educational contrast.  

Example: DLX recorded solving times in the range of **0.008–0.025 ms** on benchmark puzzles, while BFS required **>90 ms** on the hardest ones.

## 📁 Structure

Each folder corresponds to a solver implementation:

```
tests/         # Testing utils
solvers/       # All solvers used
utils/         # Scripts for benchmarking, bootstrapping, statistics
```

Benchmark results (tables and raw measurements) are included to reproduce the figures and findings of the paper.

## 📖 Citation

If you reference this work, please cite:

```bibtex
@inproceedings{secrieru2025sudoku,
  author    = {Ștefan Secrieru and Claudia Iasmina Lazăr and Roxana Andreea Goina},
  title     = {From Brute Force to Logic: Analyzing Diverse Approaches for Solving Sudoku Puzzles},
  booktitle = {Proceedings of the 27th International Symposium on Symbolic and Numeric Algorithms for Scientific Computing (SYNASC)},
  year      = {2025},
  note      = {Forthcoming},
}
```

## 📬 Contact

**Ștefan Secrieru**  
Email: stefan.secrieru@e-uvt.ro  
GitHub: [@Stefan3002](https://github.com/Stefan3002)

---

🔗 Related datasets & libraries:  
- [3 Million Sudoku puzzles dataset (Kaggle)](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings)  
- [PySAT library](https://pysathq.github.io/docs/html/)  
- [python-constraint](https://pypi.org/project/python-constraint/)  
