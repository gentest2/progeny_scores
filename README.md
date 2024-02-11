# Progeny Scores

Progeny Scores is designed to download gene expression data from the Genialis Expressions data repository and compute PROGENy scores for specified datasets. It features both a Python library for programmatic access and a command-line interface for direct user interaction, catering to various user preferences and use cases.

The PROGENy scores are determined using a model that applies human-specific weights and considers the top 100 responsive genes ranked by their p-value.

## Installation

To install the Progeny Scores, follow these steps:
 
1. **Clone the Repository**:
 ```
git clone https://github.com/gentest2/progeny_scores.git
cd progeny_scores
 ```

2. **Install with pip**:

```
pip install -e .
```

3. **Verify Installation**:
```
python -c "import progeny_scores; print(progeny_scores.__version__)"
```

# Usage 

To use the Progeny Scores, you need to provide a 'slug', which is a unique name identifying a data collection on the Genialis Server. 

## Library Exmple

Returns a pandas DataFrame with PROGENy scores for every sample.


```python
from progeny_scores.analysis import get_progeny_scores

progeny_scores_df = get_progeny_scores('windrem-et-al-cell-2017')

print(progeny_scores_df)


```
## CLI Example
Returns a formatted table.

```
progeny-scores windrem-et-al-cell-2017
```



