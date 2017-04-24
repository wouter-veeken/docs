## Overview

Vale strives to be "syntax aware," which means that it's capable of both applying rules to and ignoring certain sections of text. The difficulty with this is supporting the many different writing formats: Markdown, AsciiDoc, reStructuredText, etc.

Fortunately, they all have something in common: they're designed, to varying degrees, for conversion into HTML. Vale uses this commonality to avoid having to do any parsing itself and to allow for straightforward integration of new formats. The strategy is as follows:

1. Use a third-party library to convert the markup to HTML;
2. use Go's [`html`](https://godoc.org/golang.org/x/net/html) package to tokenize the HTML; and
3. assign scopes to certain sections of text, which we then choose to either lint or ignore.

While this may sound like a roundabout approach, Vale is still quite performant:

| Project                | Files | Lines | Command                       | macOS  | Windows |
|:----------------------:|:-----:|:-----:|:-----------------------------:|:------:|:-------:|
| [You-Dont-Know-JS][p1] |  68   | 21464 |  `time vale --glob='*.md' .`  |  6.9s  |  6.6s   |
| [NLTK Book][p2]        |  45   | 36125 |  `time vale --glob='*.rst' .` |  18.2s |  15.5s  |
| [Django][p3]           |  2390 | 55101 |  `time vale --glob='*.py' .`  |  12.2s |  8.1s   |

The testing environments were (using Vale's built-in rules):

- macOS: v10.10.5, 2.9GHz Intel Core i7, 16GB DDR3
- Windows: v10, 3.10GHz Intel Core i5-3350, 8GB DDR3

## Scoping

Vale uses a scoping system to offer greater control over where certain rules apply. A scope is specified through a *selector* such as `paragraph.rst`, which indicates that the rule applies to all paragraphs in reStrucutredText files. Here are a few examples:

- `comment` matches all source code comments;
- `comment.line` matches all source code line comments;
- `heading.md` matches all Markdown headings; and
- `text.html` matches all HTML scopes.

## Markdown

Vale has built-in support for Github-flavored Markdown. By default, it ignores indented blocks, fenced blocks, and code spans.

## HTML

Vale has built-in support for HTML. By default, it ignores `script`, `style`, `pre`, `code`, and `tt` tags.

## reStructuredText

Vale supports reStructuredText through the external program [`rst2html`](http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py). If you have [Sphinx](http://www.sphinx-doc.org/en/stable/) or [docutils](http://docutils.sourceforge.net/) installed, you shouldn't need to install `rst2html` separately.

By default, it ignores literal blocks, inline literals, and `code-block`s.

## AsciiDoc

Vale supports AsciiDoc through the external program [AsciiDoctor](https://rubygems.org/gems/asciidoctor). By default, it ignores listing blocks and inline literals.

## Source code

|   Syntax   |          Extensions         |                                                        Tokens (scope)                                                       |
|----------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| C          | .c, .h                      | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| C#         | .cs, .csx                   | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| C++        | .cpp, .cc, .cxx, .hpp       | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| CSS        | .css                        | `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                                                            |
| Go         | .go                         | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| Haskell    | .hs                         | `--` (text.comment.line.ext), `{-` (text.comment.block.ext)                                                                 |
| Java       | .java, .bsh                 | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| JavaScript | .js                         | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| LESS       | .less                       | `//`(text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                               |
| Lua        | .lua                        | `--` (text.comment.line.ext), `--[[` (text.comment.block.ext)                                                               |
| Perl       | .pl, .pm, .pod              | `#` (text.comment.line.ext)                                                                                                 |
| PHP        | .php                        | `//` (text.comment.line.ext), `#` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext) |
| Python     | .py, .py3, .pyw, .pyi, .rpy | `#` (text.comment.line.ext), `"""` (text.comment.block.ext)                                                                 |
| R          | .r, .R                      | `#` (text.comment.line.ext)                                                                                                 |
| Ruby       | .rb                         | `#` (text.comment.line.ext), `^=begin` (text.comment.block.ext)                                                             |
| Sass       | .sass                       | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |
| Scala      | .scala, .sbt                | `//`(text.comment.line.ext),                                                                                                |
| Swift      | .swift                      | `//` (text.comment.line.ext), `/*...*/` (text.comment.line.ext), `/*` (text.comment.block.ext)                              |

[p1]: https://github.com/getify/You-Dont-Know-JS
[p2]: https://github.com/nltk/nltk_book
[p3]: https://github.com/django/django
