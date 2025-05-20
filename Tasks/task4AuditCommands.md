# Install security tools
pip install bandit safety pip-audit

# Run them
bandit -r .
safety check
pip-audit
