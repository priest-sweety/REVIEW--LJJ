# Data governance and provenance

## Separate Git metadata from native data

**Do not commit:** FASTQ/BAM/CRAM/VCF, dense matrices or h5ad objects, identifiable patient or donor details, access credentials, license-restricted outputs, institution-only paths, unpublished figures, large intermediate artifacts or third-party content without redistribution rights.

**May be committed, only when authorized:** source accession IDs already public, non-sensitive sample aliases, schema specifications, small plain-text checksums, code, environment specifications, project documentation, and suitably licensed aggregate summaries. Private-only metadata belongs in controlled storage if a public release is planned.

## Register before analysis

Record: source authority, release/version, assay, reference build, permitted use, access authorization, sample-level metadata completeness, file fingerprint, verification status, and *safe alias* for the native storage location. A real full path may be stored only in approved private storage and never in a public example.

## Provenance chain

`source + authorization → native input + hash → transformation + environment → output + hash → result/figure → independent review`

Missing input is **not** a negative result. A downloaded file is **not** a scientifically validated sample. Avoid mixing donor/animal-level and cell/spot-level denominators.

## Before publication

Review the Git tree **and its history** for disclosure risks; inspect commits, filenames, figures, issue/PR text, workflows, and CI logs. A public-safe scaffold does not authorize releasing a project created from it. See [release checklist](PUBLIC_RELEASE_CHECKLIST.md).
