# Deploybot Client

[![Build Status](https://travis-ci.org/mrprompt/deploybot-cli.svg?branch=master)](https://travis-ci.org/mrprompt/deploybot-cli)
[![Code Climate](https://codeclimate.com/github/mrprompt/deploybot-cli/badges/gpa.svg)](https://codeclimate.com/github/mrprompt/deploybot-cli)
[![Test Coverage](https://codeclimate.com/github/mrprompt/deploybot-cli/badges/coverage.svg)](https://codeclimate.com/github/mrprompt/deploybot-cli/coverage)
[![Issue Count](https://codeclimate.com/github/mrprompt/deploybot-cli/badges/issue_count.svg)](https://codeclimate.com/github/mrprompt/deploybot-cli)
[![GitHub issues](https://img.shields.io/github/issues/mrprompt/deploybot-cli.svg)](https://github.com/mrprompt/deploybot-cli/issues)
[![GitHub stars](https://img.shields.io/github/stars/mrprompt/deploybot-cli.svg)](https://github.com/mrprompt/deploybot-cli/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/mrprompt/deploybot-cli/master/LICENSE)

A client to [Deploybot](https://www.deploybot.com) service using [Deploybot-SDK](https://github.com/mrprompt/deploybot-sdk).

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
- deploybot help
- deploybot user list
- deploybot user get [user_id]
- deploybot deploy list [repository_id] [environment_id]
- deploybot deploy get [deploy_id]
- deploybot deploy trigger [deploy_id]
- deploybot environment list [repository_id]
- deploybot environment get [environment_id]
- deploybot repository list
- deploybot repository get [repository_id]
- deploybot server list [repository_id] [environment_id]
- deploybot server get [server_id]

```

# Test

```
python setup.py test
```
