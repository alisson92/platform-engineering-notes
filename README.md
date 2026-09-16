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

Only `.md` is versioned — it's the actual study content and the only thing worth keeping around. Everything else is scratch input for the conversion step and is excluded via [`.gitignore`](.gitignore), regardless of course:

- **Source decks/transcripts** (`.pdf`, `.pptx`, `.ppt`, `.txt`) — converted to `.md`, then irrelevant.
- **Completion certificates** (PDF) — also contain a full name; never converted, kept locally only.
- **Raw videos** (`.mp4`) — raw media, out of scope for a Markdown documentation repo.

## Known content quirk

The `Module_1`–`Module_4` slide files under `developer-portals-for-platform-engineers/` and `devops-modernization-for-platform-engineers/` are byte-for-byte identical ("Modernization fundamentals for platform engineers"), while each course's main transcript is distinct and consistent with its own title. The original slide decks were already deleted by the time this was noticed, so it can't be confirmed whether the two courses genuinely share that intro module or a conversion mix-up copied one deck into both folders. Documented here instead of "fixed" so it isn't mistaken for an unnoticed bug later.

## Content origin and use

The content here is derived from third-party courses (mostly from the [Platform Engineering](https://platformengineering.org/) community), transcribed and reorganized for personal study and reference. This repository is **not an official redistribution** of those courses — refer to the original source for the complete, up-to-date material.

## How it was converted

The original files (`.txt`, `.pptx`, `.pdf`) were converted to Markdown with `scripts/convert-to-md.py`, then removed after conversion. No need to reprocess anything — the `.md` files are now the source of truth.

To reuse the script for a new course, install its dependencies first:

```bash
pip install -r scripts/requirements.txt
```

It runs in dry-run mode by default (prints what it would do); pass `--apply` to actually write the `.md` files and delete the converted sources.
