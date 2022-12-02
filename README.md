
## ArgusEyes

**ArgusEyes** is a system which allows data scientists to declaratively specify a variety of pipeline issues that they are concerned about. Subsequently, ArgusEyes can instrument, execute and screen the pipeline for the configured pipeline issues, as part of continuous integration processes. ArgusEyes detects complex issues by tracking record-level provenance and understanding the semantics of operations in ML pipelines. ArgusEyes was presented as an [abstract at CIDR'22](https://ssc.io/pdf/arguseyes.pdf).

We provide three example scenarios (Note that you have to locally install ArgusEyes first to execute them). You can run ArgusEyes to execute the pipeline and screen it for a particular issue issue:

### Label errors: detecting mislabeled image in a computer vision pipeline
 
  * Source code of the ML pipeline [mlinspect-computervision-sneakers.py](pipelines/mlinspect-computervision-sneakers.py)
  * Screening configuration: [mlinspect-computervision-sneakers-labelerrors.yaml](mlinspect-computervision-sneakers-labelerrors.yaml)
  * [Github workflow run detecting the label errors](https://github.com/amsterdata/arguseyes-demo/actions/runs/3602119501/jobs/6068693150)
  * Manual screening: `./eyes arguseyes/example_pipelines/mlinspect-computervision-sneakers-labelerrors.yaml`
  * Notebook for retrospective debugging: [retrospective_labelerrors.ipynb](retrospective_labelerrors.ipynb)

 
 
 - Spotting **data leakage** in a [price prediction pipeline](arguseyes/example_pipelines/mlflow-regression-nyctaxifare.py): <br/> `./eyes arguseyes/example_pipelines/mlflow-regression-nyctaxifare-dataleakage.yaml`
 
 
 - Adressing **fairness violations** in a [credit scoring pipeline](arguseyes/example_pipelines/openml-classification-incomelevel.py): <br/> `./eyes arguseyes/example_pipelines/openml-classification-incomelevel-fairness.yaml`

## Local setup

Prerequisite: Python 3.9

1. Clone this repository
2. Set up the environment

	`cd arguseyes` <br/>
	`python3.9 -m venv venv` <br/>
	`source venv/bin/activate` <br/>

3. Install graphviz

    `Linux: ` `apt-get install graphviz` <br/>
    `MAC OS: ` `brew install graphviz` <br/>
	
4. Install pip dependencies 

    `pip install -r requirements.txt` <br>
