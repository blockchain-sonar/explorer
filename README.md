# Blockchain Sonar's Explorer

This is workspace branch of Blockchain Sonar's Explorer multi project repository based on [orphan](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---orphanltnew-branchgt) branches.

Branches (sub-projects):

* `docs` - Documentation
* `backend` - Sources of API service
* `frontend` - Sources of Web application

## Get Started

1. Clone the repository
	```shell
	git clone git@github.com:blockchain-sonar/explorer.git blockchain-sonar.explorer
	```
1. Enter into cloned directory
	```shell
	cd blockchain-sonar.explorer
	```
1. Initialize [worktree](https://git-scm.com/docs/git-worktree) by execute following commands
	```shell
	for BRANCH in backend docs frontend; do git worktree add "${BRANCH}" "${BRANCH}"; done
	```
1. Open VSCode Workspace
	```shell
	code "Blockchain Sonar Explorer.code-workspace" 
	```
