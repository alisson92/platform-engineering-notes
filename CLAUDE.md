# CLAUDE.md — platform-engineering-notes

Project context for future Claude Code sessions in this repository.

## What this repository is

A personal collection of Platform Engineering/SRE course notes, converted to Markdown to serve as versioned reference on GitHub. This is not a code project — there's no build, test, or deploy here.

## Language

**English is the default and mandatory language for this entire project.** Every file in this repository — course content, filenames (where practical), scripts, comments, commit messages, PR titles/descriptions, and any new file type added in the future — must be written in English, regardless of any Portuguese preference configured elsewhere for the user. This standard applies automatically to new files and new sections created going forward; don't ask for confirmation before defaulting to English here.

## Structure

- `courses/<course-slug>/` — one folder per course.
  - `<Course Name>.md` — the course's text transcript/summary.
  - `Module_N__<title>.md` — a module's slide content (from a source PPTX or PDF).
- `scripts/convert-to-md.py` — the script used for the initial conversion (txt/pptx/pdf → md). Kept around to reprocess future courses with the same pattern; not run automatically.

## Naming conventions

- **`<course-slug>`:** plain kebab-case, all lowercase, words separated by hyphens, no abbreviations that aren't already standard industry terms (e.g. `k8s`, `ci-cd` are fine; invented shorthand isn't). Example: `kubernetes-fundamentals`, `gitops-with-argocd`.
- **`Module_N__<title>.md`:** keep the existing format as-is — `Module_` prefix, `N` as the module number (no zero-padding, matches source numbering), double underscore, then `<title>` mirroring the module's original title from the source deck. Don't switch this to kebab-case; it's the established pattern across existing courses and changing it would require renaming every file already committed.

## Formatting conventions (follow when adding/editing content)

- **Course transcript (txt → md):** `# Course Title` at the top; the original `### Module N: ...` heading becomes `## Module N: ...`; the original `## ...` heading becomes `### ...`. In short, when converting by hand, bump every heading up one level relative to the source file.
- **Slides (pptx/pdf → md):** one `## Slide N` (or `## Page N` for PDF) per slide/page, with the slide's text as bullets and the presenter notes (when present) in a blockquote (`> **Presenter notes:**`).
- **Slides that are diagrams (architecture, flows, box-and-arrow visuals):** PDF-derived (`## Page N`) files are especially prone to this — python-pdf-style extraction flattens box/arrow layouts into an unreadable word soup, unlike the pptx path which extracts per-shape bullets more reliably. For these, also render each page/slide as a PNG and embed it right under the page heading with `![Page N](images/page-N.png)`, above the extracted text. The text stays for searchability; the image carries the actual diagram.
  - Single-deck course (one `.md` file): `courses/<course-slug>/images/page-N.png`.
  - Multi-module course (one `.md` per module, e.g. `gitops-for-platform-engineering`): `courses/<course-slug>/images/module-N/page-M.png`, to avoid page-number collisions across modules.
  - PNGs are not excluded by `.gitignore` (only the raw source `.pdf`/`.pptx`/`.txt` are), so they're versioned normally — no `.gitignore` change needed. Render with a small script (e.g. PyMuPDF `page.get_pixmap(dpi=120)`) rather than committing anything by hand. When adding a new course, check whether its slides are diagram-heavy (thin/title-only extracted text is the tell) before deciding text-only is enough.
- Plain Markdown, no front matter — this repo is read directly through the GitHub UI, not a static site generator.

## Important rules

- **Only `.md` is versioned.** `.gitignore` blanket-excludes `courses/**/*.pdf`, `*.pptx`, `*.ppt`, and `*.txt` — source decks/transcripts and completion certificates alike — so no per-course exception needs to be added when a new course comes in; the pattern already covers it.
- **Never commit videos (`.mp4`) or other raw media** — out of scope for a Markdown-only repository. Already covered by `*.mp4` in `.gitignore`.
- The content is derived from third-party courses (mostly platformengineering.org) — it's personal study material, not an official redistribution. When adding new courses, keep that same spirit (summary/transcript for personal reference, not republishing protected material beyond personal use).
- The repository is **private** on GitHub. Don't suggest making it public without flagging the copyright/PII considerations above.

## Workflow for adding a new course

1. Create `courses/<course-slug>/`.
2. If there's a source `.txt`/`.pptx`/`.pdf`, run `scripts/convert-to-md.py` (adjusting the input paths) or convert manually following the conventions above.
3. Source files and certificates are already covered by `.gitignore` by extension — no manual exclusion needed.
4. Check that the generated `.md` has a title (`#`) and a coherent heading hierarchy before committing (`scripts/check_md_structure.py` enforces this in CI).

## Commit and PR workflow

- Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for every commit message, same as the global preference — no restriction on type here (`feat`, `fix`, `docs`, `chore`, `refactor`, etc. all apply as appropriate).
- Even though this is a docs-only repo, pick the type that matches the actual change, not a default: `docs` for adding/editing course content, `chore` for repo maintenance (`.gitignore`, `scripts/`, this file), `fix` for correcting an error in already-committed content.
- Commit messages and PR titles/descriptions are in **English**, consistent with the repo's language standard — this overrides the global Portuguese-response preference, which only applies to conversation, not committed content.
- Keep commits scoped to one course or one concern at a time (e.g. don't mix adding a new course with an unrelated `.gitignore` fix in the same commit) to keep history easy to scan on GitHub.
