import csv
import os
import sys

from github import Github


EWBANKKIT_SERVICES = [
    'apigatewayv2',
    'appmesh',
    'backup',
    'globalaccelerator',
    'kinesisanalytics',
    'kinesisanalyticsv2',
    'route53resolver'
]


def get_open_service_issues(writer, repo, service_name):
    for issue in repo.get_issues(state='open', labels=['service/%s' % (service_name)]):
        if issue.pull_request is not None:
            continue

        plus_ones = 0
        for reaction in issue.get_reactions():
            if reaction.content == '+1':
                plus_ones = plus_ones + 1

        writer.writerow([service_name, issue.html_url, issue.title, str(issue.created_at), str(plus_ones)])


def get_service_maintainer_issues(gh_token):
    gh = Github(gh_token)
    repo = gh.get_repo('hashicorp/terraform-provider-aws')
    csv_writer = csv.writer(sys.stdout)
    for service_name in EWBANKKIT_SERVICES:
        get_open_service_issues(csv_writer, repo, service_name)


if __name__ == "__main__":
    gh_token = os.environ.get("GITHUB_TOKEN")
    if gh_token is None:
        print('GITHUB_TOKEN not set')
    else:
        get_service_maintainer_issues(gh_token)
