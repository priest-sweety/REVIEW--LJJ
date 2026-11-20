# Public release safety checklist

A public repository is readable worldwide, may be indexed and cloned, and is hard to retract. **Do not convert an unpublished project to Public merely because this template is public.**

- [ ] The content was created independently as generic teaching material, or every included source has explicit redistribution permission.
- [ ] No actual project name, research hypothesis, unpublished observation, clinical/cohort identifier, donor/sample identifier, institutional storage URI, raw data, analysis result, figure or internal report has leaked.
- [ ] No reference to a private repository, private branch, unpublished GitHub issue/PR, agent session, internal tool/service, email, or access-controlled source is present.
- [ ] No API key, token, SSH material, password, `.env`, credential, local config or secret-bearing workflow artifact exists.
- [ ] Repository **history** is new and independently reviewed: no fork provenance, copied `.git`, squashed private history, commits or tags imported from an unpublished study.
- [ ] Files, names, metadata, comments, Markdown, examples, tests, release notes, CI logs, GitHub issues and PR text have been reviewed (do not rely only on keyword scans).
- [ ] Licensing is compatible with redistribution of code, text, methods, references and third-party assets.
- [ ] The project owner and required collaborators/institution have explicitly approved publication.

**This standalone template:** includes generic placeholder text only and is intended to start from a fresh Git history. Do not copy the private study's Git tree into it.
