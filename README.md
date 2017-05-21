# Deploybot Client

A client to [Deploybot](https://www.deploybot.com) service.

# Install

```
pip install deploybot-cli
```

# Configuration

```
DEPLOYBOT_ACCOUNT="foo"
DEPLOYBOT_KEY="foo123bar456bar"
```

# Usage

```
- deploybot-cli --help
- deploybot-cli user
- deploybot-cli deploy [repository_id] [environment_id]
- deploybot-cli environment [repository_id]
- deploybot-cli repository 
- deploybot-cli server [repository_id] [environment_id]

```

# Test

```
python setup.py test
```