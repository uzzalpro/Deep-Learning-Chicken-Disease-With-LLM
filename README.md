# Deep-Learning-Chicken-Disease-With-LLM



#### Data Link: [Donwload Link](https://drive.google.com/file/d/1pV0DAdyjzsjk0HL7f8_5qiS_mVyjYk25/view?usp=sharing)

## Workflows

1. Update config.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-End-Deep-Learning-Project-Chicken-Disease
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Export the environment with azure blob store
```bash
export STORAGE_ACCOUNT_CONNECTION=<STORAGE_ACCOUNT_CONNECTION>
export STORAGE_ACCOUNT_CONTAINER=<STORAGE_ACCOUNT_CONTAINER>

```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## Using an LLM Agent with HuggingFace via LangChain Orchestration.
```bash
export HUGGINGFACEHUB_API_TOKEN=<HUGGINGFACEHUB_API_TOKEN>
```


# Azure-CICD-Deployment-with-Github-Actions

## 1. Login to Azure console.

