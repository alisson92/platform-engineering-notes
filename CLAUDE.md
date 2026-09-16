# CLAUDE.md — platform-engineering-notes

Project context for future Claude Code sessions in this repository.

## What this repository is

A personal collection of Platform Engineering/SRE course notes, converted to Markdown to serve as versioned reference on GitHub. This is not a code project — there's no build, test, or deploy here.

## Language

All files in this repository (docs, filenames where practical, commit messages) are in **English** — this is the project's universal language standard, regardless of any Portuguese preference configured elsewhere for the user.

## Structure

- `courses/<course-slug>/` — one folder per course.
  - `<Course Name>.md` — the course's text transcript/summary.
  - `Module_N__<title>.md` — a module's slide content (from a source PPTX or PDF).
- `scripts/convert-to-md.py` — the script used for the initial conversion (txt/pptx/pdf → md). Kept around to reprocess future courses with the same pattern; not run automatically.

## Formatting conventions (follow when adding/editing content)

- **Course transcript (txt → md):** `# Course Title` at the top; the original `### Module N: ...` heading becomes `## Module N: ...`; the original `## ...` heading becomes `### ...`. In short, when converting by hand, bump every heading up one level relative to the source file.
- **Slides (pptx/pdf → md):** one `## Slide N` (or `## Page N` for PDF) per slide/page, with the slide's text as bullets and the presenter notes (when present) in a blockquote (`> **Presenter notes:**`).
- Plain Markdown, no front matter — this repo is read directly through the GitHub UI, not a static site generator.

## Important rules

- **Never commit completion certificates (PDF)** — they contain the author's full name. They're excluded via `.gitignore` on purpose; if a new certificate shows up, add its path to `.gitignore` instead of converting it.
- **Never commit videos (`.mp4`) or other raw media** — out of scope for a Markdown-only repository. Already covered by `*.mp4` in `.gitignore`.
- The content is derived from third-party courses (mostly platformengineering.org) — it's personal study material, not an official redistribution. When adding new courses, keep that same spirit (summary/transcript for personal reference, not republishing protected material beyond personal use).
- The repository is **private** on GitHub. Don't suggest making it public without flagging the copyright/PII considerations above.

## Workflow for adding a new course

1. Create `courses/<course-slug>/`.
2. If there's a source `.txt`/`.pptx`/`.pdf`, run `scripts/convert-to-md.py` (adjusting the input paths) or convert manually following the conventions above.
3. Exclude any certificate or raw video from the commit (`.gitignore` already covers the common patterns; add one-off exceptions if needed).
4. Check that the generated `.md` has a title (`#`) and a coherent heading hierarchy before committing.
