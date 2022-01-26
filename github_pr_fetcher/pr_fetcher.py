import requests
import json

# Acceptance Criteria
# - [x] Support fetching an individual PR via a PR number.
# - [x] Only ping Github once per script.
# - [x] Additionally print the author of a PR.
# - [x] Only iterate over the fetched PRs JSON once per script.
# - [ ] Test should not interact with the real Github API, but rather used mocked data.
# - [ ] Obtain 100% test coverage

# import json


class NotFoundException(Exception):
    pass


class HttpGitHubFetchPRGit:
    pr_query_url = "https://api.github.com/repos/bagaco-ramp-up/python-101/pulls"

    @staticmethod
    def get_github_all_pr():
        # pr_query_url = "https://api.github.com/repos/bagaco-ramp-up/python-101/pulls"
        pr_params = {
            "state": "all",
        }
        pull_request_data = requests.get(HttpGitHubFetchPRGit.pr_query_url, params=pr_params)
        if pull_request_data.status_code == 404:
            raise NotFoundException("Link not found")
        # print(pull_request_data)
        pull_request_dic = pull_request_data.json()
        # print(json.dumps(pull_request_dic, indent=4, sort_keys=True))
        # with open("github_pr_fetcher/pr_mock_data.json", "w") as new_file:
        #     json.dump(pull_request_dic, new_file)  # convert in to a string
        for i in range(0, len(pull_request_dic)):
            pull_request_title = pull_request_dic[i]["title"]
            pull_request_state = pull_request_dic[i]["state"]
            pull_request_number = pull_request_dic[i]["number"]
            # print(pull_request_number, " " + pull_request_title + " " + pull_request_state)
        return pull_request_dic


# /repos/{owner}/{repo}/pulls/{pull_number}
#  /repos/{owner}/{repo}/pulls
# https://api.github.com