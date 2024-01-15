# End-to-End-Classification-with-Mlflow

```
## Workflows

1. Update config.yaml
2. Update secrets.yamn [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
```

#### cmd
```
- mlflow ui
```

### dagshbub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/timothyafolami/End-to-End-Classification-with-Mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=username \
MLFLOW_TRACKING_PASSWORD= your password \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/timothyafolami/End-to-End-Classification-with-Mlflow.mlflow 

export MLFLOW_TRACKING_USERNAME=username

export MLFLOW_TRACKING_PASSWORD= your password

```
