from prefect.deployments import Deployment
from etl_web_to_gcs_q4 import etl_web_to_gcs
from prefect.filesystems import GitHub

github_block = GitHub.load("git-prefect-dezoom")

git_repo = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="git-flow2",
    # infrastructure=github_block,
)


if __name__ == "__main__":
    git_repo.apply()
