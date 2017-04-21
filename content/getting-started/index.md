---
date: 2016-03-09T00:11:02+01:00
title: Getting started
weight: 10
---

## Installation

Vale works on Windows, macOS and Linux. Installation is simple and there are a few options to choose from, as discussed below.

**Windows Installer**

The easiest way to install on Windows is to use the Windows Installer package, `vale.msi` (which you'll find on the [releases page](https://github.com/ValeLint/vale/releases)). 

You may be warned about the package coming from an "unidentified developer." If you're not comfortable with this, you can install manually (see below).

**Homebrew (macOS)**

The easiest way to install on macOS is through [Homebrew](https://brew.sh/):

```bash
$ brew tap ValeLint/vale
$ brew install vale
```

**Manually (Windows, macOS & Linux)**

Download a binary from the [releases page](https://github.com/ValeLint/vale/releases) for your OS. 

You can put it anywhere you want. If you're not sure how to get started, check out one of our guides below.

- [Getting Started with Vale (Windows)](#) (Coming soon.)
- [Getting Started with Vale (macOS)](https://jdkato.github.io/2017/02/26/getting-started-with-vale-mac.html)
- [Getting Started with Vale (Ubuntu)](#) (Coming soon.)

**Using Go (Windows, macOS & Linux)**

If you have [Go](https://golang.org/) installed and configured, you can install with `go get`:

```bash
$ go get github.com/ValeLint/vale
```

## Verifying Downloads

Releases are signed with my [public key](https://keybase.io/jdkato/key.asc) ([download link](https://jdkato.github.io/jdkato_gpg_key.asc)). To verify a release, you can do the following:

```bash
# after downloading my public key, we need to import it
$ gpg --import jdkato_gpg_key.asc
# verify the signature (replace "macOS-64bit.tar.gz" if necessary)
$ gpg --verify macOS-64bit.tar.gz.asc macOS-64bit.tar.gz
```
