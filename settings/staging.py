from .prod import *  # noqa: ignore=F405

ALLOWED_HOSTS = ["staging.eval.ai", "beta-staging.eval.ai"]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "https://evalai.s3.amazonaws.com",
    "https://staging-evalai.s3.amazonaws.com",
    "https://staging.eval.ai",
    "https://beta-staging.eval.ai",
)
