---
date: 2021-03-13T12:22:44+02:00
title: "Node Abhängigkeiten aus Themes"
tags:
- Hugo
- Themes
- Node
---
Since the [upgrade to a Hugo version above 0.75.0](/post/recent-hugo-version/) there is an enhancement in the form of the command [`hugo mod npm pack`](https://gohugo.io/commands/hugo_mod_npm_pack/) to merge the node dependencies of a theme with those of a project.

To use this new feature, the dependencies of a theme must be saved in a file `package.hugo.json` instead of` package.json`, it is sufficient to simply rename the file created by `npm` or` yarn`. A symlink alone doesn't work because Hugo's virtual filesystem (intentionally) doesn't work with symlinks.

<!--more-->

If it's just about merging the `dependencies` and` devDependencies` sections, that works very well. However, if you have defined special scripts (section `scripts` in` package.json`), e.g. to patch existing node libraries, the whole thing does not really help, because these sections (and all others that do not explicitly define dependencies) contribute the merge ignored.

There is a [Hugo Feature Request] (https://github.com/gohugoio/hugo/issues/8319), but it is not yet clear whether and if so, when this will be implemented.

Two solutions are possible:
* Create a patched Node dependency and publish it to it's own Node package repository - One can use [GitHub](https://docs.github.com/en/actions/guides/publishing-nodejs-packages) for building and distribution. Just make sure your project is using this registry.
* Build your own merging logic using [`jq`](https://stedolan.github.io/jq/):


An example for two files:
```
jq -s '.[0] * .[1]'  package.hugo.json themes/some-hugo-theme-with-npm-dependencies/package.hugo.json
```

An Example using multiple themes (This only works with BSD `find` - not on GitHub):
```
find . -name "package.hugo.json" -o -name "package.json" -depth 0 | xargs jq -s add > package.json
```
