# Python Act

Heavily inspired by https://github.com/xingyaoww/code-act

## how-to

1. Run VLLM,

```bash
docker-compose up --build
```

2. Run Jupyter API,

```bash
docker image pull docker.io/xingyaoww/codeact-executor
python3 api.py --port 8081
```

3. Run Agent,

```bash
python3 agent.py \
--openai_base_url http://localhost:8005/v1 \
--jupyter_kernel_url http://localhost:8081/execute \
--model_name xingyaoww/CodeActAgent-Mistral-7b-v0.1
```