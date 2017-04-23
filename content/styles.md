---
date: 2016-03-09T20:08:11+01:00
title: Styles
weight: 40
---

## Introduction

Vale is built around the notion of "styles," which are directories containing individual "rule" definitions&mdash;for example, you might have a structure like

```none
styles/
├── base/
│   ├── ComplexWords.yml
│   ├── SentenceLength.yml
│   ...
├── blog/
│   ├── TechTerms.yml
│   ...
└── docs/
    ├── Branding.yml
    ...
```

where *base*, *blog*, and *docs* are your styles. The [YAML](http://yaml.org/) files are rule definitions that include the following keys:

- The `type` of check you're extending;
- a `message` to be displayed to the user;
- the severity `level` of failing this check (suggestion, warning or error);
- the `scope` the check operates on (see [Formats](https://github.com/jdkato/vale/wiki/Formats) to learn about scoping); and
- check-specific data (see Check Types).

## Creating a style

`checks` provide a high-level way to extend Vale. They perform operations such as checking for consistency, counting occurrences and suggesting changes.

[Vale](https://github.com/jdkato/vale/tree/master/rule) and its reference styles, [The Economist](https://github.com/jdkato/vale/tree/master/styles/TheEconomist) and [`write-good`](https://github.com/jdkato/vale/tree/master/styles/write-good), provide examples of how you can write your own rules.

### existence

```yaml
extends: existence
message: "Consider removing '%s'"
ignorecase: true
level: warning
tokens:
  - appear to be
  - arguably
```

The most common extension point is the `existence` check. As its name implies, it looks for the *existence* of particular strings.

You may define these strings as elements of lists named either `tokens` or `raw`. The former converts its elements into a word-bounded group by default. For instance,

```yaml
message: "Consider removing '%s'"
tokens:
  - foo
  - bar
  - baz
```
becomes `\b(?:foo|bar|baz)\b`. You can also use the keys `ignorecase` and `nonword` to add `(?!)` and drop the word boundaries, respectively.

`raw`, on the other hand, simply concatenates its elements&mdash;so, something like

```yaml
raw:
  - '(?:foo)\sbar'
  - '(baz)'
```
becomes `(?:foo)\sbar(baz)`.

An `existence` expects its `message` to include a `%s` format specifier, which will be populated with the matched string. So, using the above example, "Consider removing 'foo'" will be printed if we find an occurrence of "foo."


### substitution

```yaml
extends: substitution
message: Consider using '%s' instead of '%s'
ignorecase: true
level: warning
swap:
  abundance: plenty
  accelerate: speed up
```

A `substitution` check associates a string with a preferred form. If we want to suggest the use of "plenty" instead of "abundance," for example, we'd write:

```yaml
swap:
  abundance: plenty
```

The keys  may be regular expressions, but they cannot include nested capture groups:

```yaml
swap:
  '(?:give|gave) rise to': lead to # this is okay
  '(give|gave) rise to': lead to # this is bad!
```

Like the `existence` check, `substitution` accepts the keys `ignorecase` and `nonword`.

A `substitution` check can have one or two `%s` format specifiers in its `message`. This allows us to do either of the following:

```yaml
message: "Consider using '%s' instead of '%s'"
# or
message: "Consider using '%s'"
```

### occurrence

```yaml
extends: occurrence
message: "Sentences should be less than 25 words"
scope: sentence
level: suggestion
max: 25
token: '\b(\w+)\b'
```

An `occurrence` check limits the number of times a particular token can appear in a given scope. In the example above, we're limiting the number of words per sentence.

This is the only check that doesn't accept a format specifier in its message.

### repetition

```yaml
extends: repetition
message: "'%s' is repeated!"
level: error
scope: paragraph
ignorecase: true
tokens:
  - '\b(\w+)\b'
```

A `repetition`  check  looks for repeated occurrences of its tokens. If `ignorecase` is set to `true`, it will convert all tokens to lower case for comparison purposes.

### consistency

```yaml
extends: consistency
message: "Inconsistent spelling of '%s'"
level: warning
scope: text
ignorecase: true
either:
  advisor: adviser
  centre: center
```

A `consistency` check will ensure that a key and its value (e.g., "advisor" and "adviser") don't both occur in its scope.

### conditional

```yaml
extends: conditional
message: "'%s' has no definition"
level: warning
scope: text
first: \b([A-Z]{3,5})\b
second: (?:\b[A-Z][a-z]+ )+\(([A-Z]{3,5})\)
exceptions:
  - ABC
```

A `conditional` check ensures that the existence of `first` implies the existence of `second`. For example, consider the following text:

> According to Wikipedia, the World Health Organization (WHO) is a specialized agency of the United Nations that is concerned with international public health. We can now use WHO because it has been defined, but we can't use DAFB because people may not know what it represents. We can use `DAFB` when it's presented as code, though.

Running `vale` on the above text with our example rule yields the following:

```none
test.md:1:224:vale.UnexpandedAcronyms:'DAFB' has no definition
```

A `conditional` check also takes an optional `exceptions` list. Any token listed as an exception will not be flagged.