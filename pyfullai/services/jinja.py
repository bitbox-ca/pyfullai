from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader
from jinja2.sandbox import SandboxedEnvironment

env = Environment(
    loader=PackageLoader("pyfullai"),
    autoescape=True,
)

# Sandboxed environment for untrusted templates (user content, third-party systems).
# Prevents access to Python internals, attribute traversal, and dangerous operations.
sandbox_env = SandboxedEnvironment(
    loader=PackageLoader("pyfullai"),
    autoescape=True,
)
response_templates = Jinja2Templates(directory="pyfullai/templates")

# Use the primary environment inside of the Jinja2Templates wrapper.
response_templates.env = env
