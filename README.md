# Platform Engineering Notes

Personal reference collection of study notes on **Platform Engineering** (SRE/DevOps), organized by course and converted to Markdown for easy versioning, search, and reading directly on GitHub.

## Structure

Each course lives in its own folder under `courses/`:

```
courses/
└── <course-slug>/
    ├── <Course Name>.md              # course transcript/summary
    └── Module_N__<title>.md          # module N slides (when the course has a presentation)
```

- The `<Course Name>.md` files come from the course's text transcript (originally `.txt`).
- The `Module_N__*.md` files come from each module's slides (`.pptx`). Each slide is a `## Slide N` section, with the slide's text/bullets and, when present, the **presenter notes** (narrated video transcript) in a blockquote.
- Some courses (e.g. GitOps) have their content as PDF instead of PPTX — in that case, each PDF page becomes a `## Page N` section.

## What is NOT versioned

See [`.gitignore`](.gitignore):

- **Completion certificates** (PDF) — contain a full name, kept locally only.
- **Raw videos** (`.mp4`) — raw media, out of scope for a Markdown documentation repo.

## Content origin and use

The content here is derived from third-party courses (mostly from the [Platform Engineering](https://platformengineering.org/) community), transcribed and reorganized for personal study and reference. This repository is **not an official redistribution** of those courses — refer to the original source for the complete, up-to-date material.

## How it was converted

The original files (`.txt`, `.pptx`, `.pdf`) were converted to Markdown with a Python script using the `pypdf` and `python-pptx` libraries, then removed after conversion. No need to reprocess anything — the `.md` files are now the source of truth.
