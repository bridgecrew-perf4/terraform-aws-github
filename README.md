# GitHub API Tools

GitHub API tools for [`terraform-provider-aws`](https://github.com/hashicorp/terraform-provider-aws).

## Setup

```console
$ pyenv virtualenv 3.8.7 387-github-api
$ echo "387-github-api" > .python-version
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Run

```console
$ export GITHUB_TOKEN="..."
$ python get_service_maintainer_issues.py
```
