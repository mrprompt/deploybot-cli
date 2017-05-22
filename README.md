# Deploybot Client

[![Build Status](https://travis-ci.org/mrprompt/deploybot-cli.svg?branch=master)](https://travis-ci.org/mrprompt/deploybot-cli)
[![Code Climate](https://codeclimate.com/github/mrprompt/deploybot-cli/badges/gpa.svg)](https://codeclimate.com/github/mrprompt/deploybot-cli)
[![Test Coverage](https://codeclimate.com/github/mrprompt/deploybot-cli/badges/coverage.svg)](https://codeclimate.com/github/mrprompt/deploybot-cli/coverage)

A client to [Deploybot](https://www.deploybot.com) service.

# Install

```
pip install deploybot-cli
```

# Configuration

```
DEPLOYBOT_ACCOUNT="foo"
DEPLOYBOT_KEY="foo123bar456bar"
COLUMN_WIDTH=15 (optional - default = 32)
COLUMN_STYLE="block" (optional - default = fancy_grid, availables = round, fancy_grid, grid, clean and block)
```

# Usage

```
- deploybot-cli help
- deploybot-cli user list
- deploybot-cli deploy list [repository_id] [environment_id]
- deploybot-cli environment list [repository_id]
- deploybot-cli repository list
- deploybot-cli server list [repository_id] [environment_id]

```

# Test

```
python setup.py test
```