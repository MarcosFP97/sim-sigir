# SEARCH SIMULATION FOR VERIFYING NEWS ACCURACY

In this code, we simulate different query generation strategies to examine their impact on search result quality. Our starting point is Study 5 from Aslett et al.'s data [1].

## INSTALLATION

```
pip install -r requirements.txt
```

## REPOSITORY STRUCTURE

All the main files of this repository are under 'src/' folder:

- data: it contains two csv files: the corpus of articles used in the simulation and a list of newsguard scores for several domains.
- sim.py: main file that models the entire simulation process.
- figs/plot.py: script that generates Fig. 4 in the paper for evaluating NewsGuard Scores at different rank positions. It also runs stats tests at this different rank positions.
- tests: folder that contains tests scripts for using Llama.
- sim_output: output of the simulations evaluated in the paper.
- analysis/stats_tests.py: script for computing the statistical tests reported in the paper.  

## PREREQUISITES


### LlaMa Model

We used an LLM for query generation. More specifically, a version of **Llama3**. To run the simulation ollama service needs to be up and running in the same environment:

```
ollama serve
```

We used the version `llama3:8b-instruct-q4_0` so you need to pull it first:

```
ollama pull model_version
```

### Bing Search API v7

To run searches, we used Bing official search API. You need to generate your search token first. Check [here](https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview).

## RUNNING SIMULATIONS

To run the simulation, the main file is `sim.py`. We need to provide as argument the different query generation strategies for the inital and subsequent search steps:

```
python sim.py gen1 gen2
```

## LICENSE

This project is licensed under the GPL-v3 License. See the `LICENSE` file for details.

## CITATION

Please cite our study.

## REFERENCES

[1] Kevin Aslett, Zeve Sanderson, William Godel, Nathaniel Persily, Jonathan Nagler, and Joshua A Tucker. 2024. Online searches to evaluate misinformation can increase its perceived veracity. Nature 625, 7995 (2024), 548–556.