## Using the CLI

`vale` is a command-line tool for linting prose against style guidelines. Its general usage information is below:

```none
$ vale --help
NAME:
   vale - A command-line linter for prose.

USAGE:
   vale [global options] command [command options] [arguments...]

VERSION:
   X.X.X

COMMANDS:
     dump-config, dc  Dumps configuration options to stdout and exits
     new              Generates a template for the given extension point
     help, h          Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --glob value     a glob pattern (e.g., --glob='*.{md,txt}') (default: "*")
   --output value   output style ("line" or "JSON") (default: "CLI")
   --no-wrap        don't wrap CLI output
   --no-exit        don't return a nonzero exit code on lint errors
   --sort           sort files by their name in output
   --ignore-syntax  lint all files line-by-line
   --help, -h       show help
   --version, -v    print the version
```
It can be run on single files or entire directories. You can also lint only files matching a particular glob:

```bash
$ vale --glob='*.{md,rst}' some-directory
```

Or exclude files matching a particular glob:


```bash
$ vale --glob='!*.min.js' some-directory
```

By default, the following rules are enforced:

<!-- vale off -->

| Rule           | Description                                                                        | Severity |
|:--------------:|:----------------------------------------------------------------------------------:|:--------:|
| Editorializing |  The use of adverbs or phrases to highlight something as particularly significant. | warning  |
| ComplexWords   |  The use of a complex word where a simpler one would do.                           | warning  |
| GenderBias     |  The unnecessary use of gender-specific language.                                  |   error  |
| Hedging        |  The use of phrases, like "in my opinion," that weaken meaning.                    | warning  |
| Redundancy     |  The use of phrases like "ATM machine."                                            |   error  |
| Repetition     |  Instances of repeated words, which are often referred to as lexical illusions.    |   error  |
| Uncomparables  |  The use of phrases like "very unique."                                            |   error  |
| Wordiness      |  The us of phrases like "in order to" and "due to the fact that."                  | warning  |

<!-- vale on -->

But Vale's true strength lies in its ability to support *your* style. See [Styles](https://valelint.github.io/styles/) for more information on creating your own style guide.

## Editor Integration

<!-- vale docs.Branding = NO -->

<p>
<a href="https://github.com/TimKam/atomic-vale"><img alt="Atom Logo" src="../img/atom.png" width="68" height="68"></a>

<a href="https://github.com/ValeLint/SubVale"><img alt="Sublime Text Logo" src="../img/sublime.png" width="64" height="64"></a>
</p>

<!-- vale docs.Branding = YES -->

[Editorializing]: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Editorializing
[ComplexWords]: http://www.plainlanguage.gov/howto/wordsuggestions/complexabstract.cfm

