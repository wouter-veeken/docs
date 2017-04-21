---
date: 2016-03-09T20:08:11+01:00
title: Configuration
weight: 30
---

## Basics

Vale looks for its configuration in a file named `.vale` or `_vale`. This file may be located in the current working directory, a parent directory or `$HOME`. If multiple config files are present, the closest one takes precedence.

The basic structure of a config file is as follows:

```ini
# Core settings
StylesPath = path/to/my/project/styles/directory
MinAlertLevel = warning # suggestion, warning or error

# Global settings (applied to every syntax)
[*]
# List of styles to load
BasedOnStyles = vale, MyCustomStyle
# Style.Rule = {YES, NO} to enable or disable a specific rule
vale.Editorializing = YES
...

# Syntax-specific settings
# These overwrite any conflicting global settings
[*.{md,txt}]
...
```

## Examples

Let's say we're working on a project with Python source code and reStructuredText documentation. Assuming we have styles named `base` (with general style rules) and `ProjectName` (with project-specific rules), we could have a config file like this:

```ini 
StylesPath = styles

[*.{rst,py}]
BasedOnStyles = base, ProjectName
```
If we have another style named `docs` with rules we only want to apply to our documentation, we could change it to:

```ini
[*.rst]
BasedOnStyles = base, ProjectName, docs

[*.py]
BasedOnStyles = base, ProjectName
docs.SomeRule = YES # there's actually one rule we want
```
