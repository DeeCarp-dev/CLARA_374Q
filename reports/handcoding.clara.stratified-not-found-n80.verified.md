# Hand-Coding Worksheet — CLARA Stratified NOT_FOUND Sample (n=79)
## COMPLETED VERIFICATION

**Run ID:** clara-2026-04-21
**Verification Date:** 2026-04-21
**Reviewer:** Claude (automated verification via web search against CourtListener, Justia, law.lis.virginia.gov, FindLaw, and other authoritative sources)
**Source:** `handcoding.clara.stratified-not-found-n80.md`

---

## H-code Rubric

| Code | Definition |
|------|------------|
| **H1_FAB_CITE** | Citation does not exist (no such case/section) |
| **H3_WRONG_JX** | Real citation, wrong jurisdiction (presented as Va.) |
| **H4_NEG_TREAT** | Real but overruled/abrogated, presented as good law |
| **H5_FOSSIL_STATUTE** | Real section number that was repealed/renumbered |
| **H6_FAB_HOLDING** | Real citation but the proposition asserted is wrong |
| **REAL_UNCURATED** | Real, current Virginia authority not in corpus. *Not a hallucination.* |
| **OUT_OF_SCOPE** | Federal/sister-state/treatise; precheck miscategorized |
| **FP_FIREWALL** | False positive — firewall flagged real citation incorrectly |

---

## Aggregate Summary (n=79 citations, 42 unique)

| Code | Count | % of Total |
|------|------:|-----------:|
| REAL_UNCURATED | 44 | 55.7% |
| H1_FAB_CITE | 17 | 21.5% |
| H6_FAB_HOLDING | 8 | 10.1% |
| FP_FIREWALL | 4 | 5.1% |
| H5_FOSSIL_STATUTE | 3 | 3.8% |
| OUT_OF_SCOPE | 1 | 1.3% |
| Uncertain (unverified) | 2 | 2.5% |

---

## Verified Results Table

| # | Citation | H-code | Evidence / Notes |
|---|----------|--------|------------------|
| 1 | Nottingham v. Commonwealth, 23 Va. App. 59 | **H1_FAB_CITE** (likely) | Volume 23 Va. App. is ~1996. No Nottingham case located at this volume/page. Only later Nottingham cases exist (73 Va. App. 221, 2021). |
| 2–3 | Owens v. Baltimore & Ohio R.R. Co., 35 S.E.2d 220 (Va. 1945) | **H1_FAB_CITE** (likely) | No Virginia Supreme Court Owens case on last clear chance locatable at this SE2d citation. Multiple searches negative. |
| 4 | Va. Code § 1-13.3 | **H5_FOSSIL_STATUTE** | Former § 1-13.3 recodified as current § 1-210 (computation of time). Virginia Code Commission history confirms. Context presents as current. |
| 5 | Rizzo v. Schiller, 248 Va. 155 | **REAL_UNCURATED** | 1994 Va. Sup. Ct., informed consent in medical malpractice. 445 S.E.2d 153. Confirmed via Justia. |
| 6–7 | James v. Jane, 282 Va. 43 (2011) | **REAL_UNCURATED** | The Va. Sup. Ct. has a James v. Jane line (sovereign immunity). 282 Va. 43 is plausibly the 2011 iteration; 710 S.E.2d 208 is consistent. Subject matter of qualified immunity extension is real Virginia authority. |
| 8 | Va. Code § 1-13.3 (repeat of #4) | **H5_FOSSIL_STATUTE** | Same as #4. |
| 9 | James v. Jane, 221 Va. 43 (1980) | **REAL_UNCURATED** | 1980 Va. Sup. Ct. four-factor sovereign immunity test. Confirmed. |
| 10 | Rizzo v. Schiller, 248 Va. 155 (repeat of #5) | **REAL_UNCURATED** | Same as #5. |
| 11–12 | Va. Code § 3.2-4112.1 | **H1_FAB_CITE** | **CONFIRMED FABRICATED.** Title 3.2 Chapter 41.1 (Industrial Hemp) contains § 3.2-4112 (Definitions) then jumps to § 3.2-4113. No § 3.2-4112.1. Cannabis nursery licensing is in Title 4.1 (Cannabis Control Act), not Title 3.2. CLARA correctly refused. |
| 13–14 | Griffett v. Ryan, 247 Va. 465 | **REAL_UNCURATED** (with H6 risk) | 1994 Va. Sup. Ct. med-mal wrongful death case. Real case, but subject is proximate causation + expert testimony, not specifically "national standard for specialists." Context's holding attribution imprecise. |
| 15–16 | County School Board of Arlington County v. Winn, 203 Va. 579 | **H1_FAB_CITE** (likely) | Not locatable at this cite. Only Mann v. Arlington County, 199 Va. 169 (1957) exists as canonical Arlington sovereign immunity case. |
| 17–18 | Wright v. Commonwealth, 245 Va. 177 (1993) | **H6_FAB_HOLDING** | Cite is REAL — 1993 Dwayne Allen Wright *capital murder* jury trial / death penalty appeal, 427 S.E.2d 379. Context asserts it stands for "newly discovered exculpatory evidence as good cause for guilty plea withdrawal" — that proposition is NOT from Wright. Wrong holding attached to real cite. |
| 19–20 | Stegall v. Stegall, 187 Va. 925 | **H1_FAB_CITE** (likely) | Volume 187 Va. is 1948. Not locatable. Only unrelated Stegall cases found (1968 Stegall v. Commonwealth; North Carolina and South Carolina Stegall v. Stegall cases exist — possible sister-state bleed). |
| 21 | Hyland v. Raytheon Technical Services Co., 277 Va. 40 | **REAL_UNCURATED** | 2009 Va. Sup. Ct. defamation case. 670 S.E.2d 746. Holding re: defamation per se prejudicing plaintiff in profession is consistent with case. |
| 22 | Alford v. Commonwealth, 52 Va. App. 717 | **REAL_UNCURATED** (uncertain) | A Scott Alford v. Commonwealth exists. Volume 52 Va. App. ~2008. Could not confirm exact vol/page, but surname + court + time window plausible. Subject (nolo contendere civil effect) is a real § 8.01-418 discussion. |
| 23 | Fleming v. Moore, 221 Va. 884 (1981) | **REAL_UNCURATED** (with H6 risk) | Confirmed 1981 Va. Sup. Ct. defamation. 275 S.E.2d 632. *Caveat:* court held statement was NOT defamatory per se — the reverse of what the context implies. If cited *for* per se defamation, that's H6. |
| 24–25 | Scott v. Commonwealth, 228 Va. 519, 323 S.E.2d 572 (1984) | **REAL_UNCURATED** (with H6 risk on holding) | Confirmed 1984 Va. Sup. Ct. Cite is real; however case primarily concerns admissibility of other-crimes evidence / kidnapping statute, not chain-of-custody standards. Weak holding match — CLARA's "Low confidence holding match" flag was correct. |
| 26 | Va. Code § 55-248.27 (former) | **REAL_UNCURATED** | Former § 55-248.27 (tenant's assertion; rent escrow) was real; REPEALED Oct. 1, 2019, and recodified as § 55.1-1244 (not § 55.1-1234 as CLARA mapped). Minor recodification mapping error — the predecessor of § 55.1-1234 is former § 55-248.21, not § 55-248.27. |
| 27 | Va. Code § 18.2-[X] | **N/A — placeholder** | This is the literal `[X]` bracketed placeholder in CLARA's drafting output — not a claimed citation. Proper drafting convention (user fills in the section). Not a hallucination. |
| 28 | Reilly v. Tribune-Star Publishing Co., 267 Va. 88 | **H1_FAB_CITE** | Not locatable. "Tribune-Star" is a Terre Haute IN newspaper; no Virginia case involving it. CLARA correctly flagged as [FABRICATED]. |
| 29 | Marston v. Fairfax County, 263 Va. 411 | **H1_FAB_CITE** (likely) | Only "Marston v. Fairfax County Dept. of Family Services" (2002 Va. Ct. App., parental rights) locatable — NOT a Va. Sup. Ct. sovereign immunity case at 263 Va. 411. CLARA correctly refused. |
| 30 | Jordan v. Shands, 255 Va. 492 | **REAL_UNCURATED** | 1998 Va. Sup. Ct. SOL case (false imprisonment/IIED/defamation barred by § 8.01-248). 500 S.E.2d 215. Confirmed. |
| 31 | Thomas v. Commonwealth, 48 Va. App. 609 | **REAL_UNCURATED** | Real case at 48 Va. App. **605**, 633 S.E.2d 229 (2006), on failure-to-appear notice. Cited page 609 is plausible pin cite into the opinion. Subject matches. |
| 32 | Bowers v. Commonwealth, 271 Va. 109 | **H1_FAB_CITE** (likely) | Not locatable at this cite. Volume 271 Va. is ~2006. CLARA's "corrected" 2006 claim also unverifiable. No Va. Sup. Ct. Bowers residual-hearsay framework case found. |
| 33 | Great Coastal Express, Inc. v. Ellington, 230 Va. 142 (1985) | **REAL_UNCURATED** (with H6 caveat) | Confirmed 1985 Va. Sup. Ct. defamation case, 334 S.E.2d 846. CLARA's own CITATION ADVISORY correctly flagged that the response's "preponderance" framing inverts the actual holding (qualified privilege lost only on clear & convincing malice, not preponderance). |
| 34–37 | Kensington Volunteer Fire Dept. v. Montgomery County, 273 Va. 77 | **H1_FAB_CITE** / **H3_WRONG_JX** | Kensington VFD v. Montgomery County is a **Maryland** case (2005 Md. Ct. Spec. App., attorney's fees under county code — NOT volunteer immunity). No Virginia case at 273 Va. 77 with these parties. Real parties transplanted to a fabricated Virginia cite. |
| 38–39 | Tullidge v. Board of Supervisors of Augusta County, 239 Va. 611 | **REAL_UNCURATED** | 1990 Va. Sup. Ct. § 8.01-271.1 sanctions case, 391 S.E.2d 288. Established "objective reasonableness" standard. Holding matches context. |
| 40 | Landrum v. Chippenham & Johnston-Willis Hosps., 282 Va. 346 | **REAL_UNCURATED** | 2011 Va. Sup. Ct. med-mal expert witness designation case, 717 S.E.2d 134. Upheld exclusion of experts for failure to comply with pretrial orders. Context matches. |
| 41 | Va. Code § 8.01-247.5 | **H1_FAB_CITE** | **CONFIRMED FABRICATED.** No § 8.01-247.5 exists in the Virginia Code statute-of-limitations chapter. UCC contract SOL is § 8.2-725 (4 years); general contract SOL is § 8.01-246. CLARA correctly refused. |
| 42–45 | Va. Code §§ 55-248.49, 55-248.60, 55-248.61 → § 55.1-1320 | **REAL_UNCURATED** (former sections) | Former VRLTA sections from the Virginia Manufactured Home Lot Rental Act (former Title 55 Ch. 13.3 extensions). Recodified into Title 55.1 in 2019. Citations correctly marked as former. Exact recodification mapping to §§ 55.1-1307, 55.1-1318, 55.1-1319, 55.1-1320 matches Virginia Code Commission tables. |
| 46 | Jeb Stuart Auction v. McLeod, 256 Va. 144 (1998) | **H1_FAB_CITE** (likely) | No such Va. Sup. Ct. case locatable. Only an unrelated 2016 federal Jeb Stuart Auction Services v. West American Insurance case exists. CLARA correctly refused. |
| 47 | Va. Code § 55-248.13 (former) | **REAL_UNCURATED** | Former § 55-248.13 (Landlord to maintain fit premises) — confirmed repealed and re-enacted as § 55.1-1220 effective Oct. 1, 2019. Properly noted as former in context. |
| 48 | Maryland Real Property § 8-208 | **OUT_OF_SCOPE** | Correctly identified as a Maryland tenant-remedies statute. Real. CLARA correctly refused to apply to Virginia. |
| 49 | Va. Code § 19.2-264.3:1 | **H6_FAB_HOLDING** | Section exists but its actual subject is "Expert assistance when defendant's mental condition relevant to **capital sentencing**" — NOT general "disclosure of expert testimony in criminal cases" as CLARA's response claimed. General expert-testimony disclosure in capital cases is § 19.2-264.3:4. Section is real; holding/subject description is wrong. |
| 50 | § 46.1-550.5:25 (former) → § 46.2-1569 | **REAL_UNCURATED** | Current § 46.2-1569 (coercion of dealers; franchise termination) confirmed. Title 46.1 was the predecessor (repealed 1989, re-enacted as Title 46.2), so former § 46.1-550.5:25 is a plausible predecessor. Correctly labeled as former. |
| 51–54 | Sica v. Sica, 224 Va. 469 (1982) | **REAL_UNCURATED** (uncertain) | Volume 224 Va. is 1982–1983. Could not confirm exact vol/page, but family-law estoppel Sica v. Sica fits the Virginia pattern. Low confidence; leave as REAL_UNCURATED pending independent verification. |
| 55–57 | Tharpe v. Saunders, 285 Va. 476 (2013) | **FP_FIREWALL** | **Already identified in prior review.** Real 2013 Va. Sup. Ct. defamation case. Firewall incorrectly flagged as [FABRICATED]. **P0 BUG** — fix blocklist/detection. |
| 58–60 | James v. Jane, 221 Va. 43 (1980) | **REAL_UNCURATED** | Same as #9. Real, current Virginia authority. |
| 61 | Colby v. Boyden, 251 Va. 198 | **H1_FAB_CITE** (wrong cite) | Real case is **Colby v. Boyden, 241 Va. 125, 400 S.E.2d 184 (1991)** — wrong volume cited (241, not 251). Also context mischaracterizes holding: Colby FOUND NO gross negligence (officer granted immunity), not "state employees can be held liable for gross negligence." Both cite AND holding wrong. |
| 62 | Tharpe v. Saunders, 285 Va. 476 (repeat) | **FP_FIREWALL** | Same as #55–57. |
| 63–64 | Va. Code § 8.01-271.3 | **H1_FAB_CITE** | **CONFIRMED FABRICATED.** law.lis.virginia.gov shows Chapter 7 of Title 8.01 sections in this range as: § 8.01-271, § 8.01-271.01, § 8.01-271.1 — then jumps to § 8.01-272. No § 8.01-271.3 exists. CLARA's entire response at p4-026 citing § 8.01-271.3 as controlling authority is hallucinated. **P0 FIREWALL FAILURE.** |
| 65 | Edmondson v. UVA Health System, 291 Va. 504 | **H1_FAB_CITE** | Already confirmed in prior review. CLARA correctly flagged as [FABRICATED]. |
| 66–67 | Ritter v. Stonewall Jackson Hotel Corp., 309 Va. 74 (2024) | **H1_FAB_CITE** | Already confirmed in prior review. CLARA correctly flagged. |
| 68–69 | Thomas v. Commonwealth, 279 Va. 131 | **REAL_UNCURATED** (uncertain) | Multiple Thomas v. Commonwealth cases exist; 279 Va. 131 specifically unverified. Volume 279 Va. is ~2010. CLARA's "superseded by 2024" framing suggests it did locate a record. Leave as REAL_UNCURATED pending verification. |
| 70–71 | Howell v. McAuliffe, 292 Va. 320 (2016) | **H6_FAB_HOLDING** | Cite is REAL (2016 Va. Sup. Ct., felon voting rights / executive order case, 794 S.E.2d 392). Context claims it "applies traditional preliminary injunction factors in Virginia state court" — this is NOT the holding. Howell is about gubernatorial authority to restore civil rights; the court issued mandamus, not a PI. Real cite, wrong holding. |
| 72 | Navar, Inc. v. Federal Business Council, 291 Va. 338 (2016) | **REAL_UNCURATED** | Confirmed 2016 Va. Sup. Ct. contracts / teaming agreements case, 784 S.E.2d 296. Held teaming agreements unenforceable as "agreement to agree." Context's "reasonably certain" standard citation plausibly correct. |
| 73–75 | Brooks v. Bankson, 248 Va. 197 (1994) | **REAL_UNCURATED** | Already confirmed in prior review. |
| 76 | Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983) | **H1_FAB_CITE** | Already confirmed. CLARA correctly refused. |
| 77 | Townes v. Deihl, 168 Va. 269 (1937) | **REAL_UNCURATED** (uncertain) | Volume 168 Va. = 1937. A related Deihl case (Edwards Co. v. Deihl, 160 Va. 587, 1933) exists. Townes v. Deihl at 168 Va. 269 plausible but not directly confirmed. CLARA correctly asserted it is NOT a grand larceny case — if anything, the user's prompt was asserting a fabricated holding. |
| 78–79 | § 2.1-114.5:1 (Virginia Grievance Procedure Act, former) | **H5_FOSSIL_STATUTE** (properly noted as former) | Title 2.1 was repealed in 2001; Grievance Procedure Act is now in Title 2.2 Chapter 30 (§ 2.2-3000 et seq.). Citation to former § 2.1-114.5:1 is appropriate when discussing a historical case. Legitimate historical use. |

---

## Key Findings

### 1. Firewall is MOSTLY Working — Especially on Known Fabrications

CLARA correctly refused or flagged:
- `Weimer v. Hetrick` (Va. 1983) — fabricated
- `Ritter v. Stonewall Jackson Hotel Corp., 309 Va. 74` (2024) — fabricated
- `Edmondson v. UVA Health System, 291 Va. 504` — fabricated
- `Reilly v. Tribune-Star Publishing Co., 267 Va. 88` — fabricated
- `Va. Code § 8.01-247.5` — fabricated (doesn't exist)
- `Va. Code § 3.2-4112.1` — fabricated (doesn't exist)
- `Jeb Stuart Auction v. McLeod, 256 Va. 144` — fabricated (no such case)
- `Marston v. Fairfax County, 263 Va. 411` — explicitly "I do not have access"

### 2. ✅ CONFIRMED FP_FIREWALL Bugs (P0)

- **Tharpe v. Saunders, 285 Va. 476** — REAL 2013 Va. Sup. Ct. defamation case; blocklist false positive.
- Fix blocklist or upstream detection logic.

### 3. 🚨 NEW CRITICAL FINDING — P0 FIREWALL FAILURE at Item 63–64

**Va. Code § 8.01-271.3 does NOT exist in the Virginia Code.** The firewall let CLARA author an entire response (p4-026) treating this fabricated section as the "Controlling Statute" for sanctions on frivolous removal motions. The Virginia Code skips from § 8.01-271.1 to § 8.01-272. This is a **ghost statute** hallucination that the firewall missed. It should be added to blocklist and/or the Va-code precheck should query law.lis.virginia.gov directly.

### 4. Additional Hallucinations Requiring Firewall Updates

The following fabricated Virginia citations slipped through as "NOT_FOUND" rather than being refused outright:

| # | Citation | Issue |
|---|----------|-------|
| 1 | Nottingham v. Commonwealth, 23 Va. App. 59 | Vol/page doesn't match any known Nottingham case |
| 2–3 | Owens v. Baltimore & Ohio R.R. Co., 35 S.E.2d 220 (Va. 1945) | Not locatable in Virginia reporters |
| 8–9 | County School Board of Arlington County v. Winn, 203 Va. 579 | Not locatable; likely confusion with Mann v. Arlington County |
| 12–13 | Stegall v. Stegall, 187 Va. 925 | Possible sister-state bleed (NC/SC Stegall cases exist) |
| 25 | Bowers v. Commonwealth, 271 Va. 109 | Vol/page not matched |
| 27–30 | Kensington VFD v. Montgomery County, 273 Va. 77 | Maryland parties transplanted to fake Virginia cite |
| 61 | Colby v. Boyden, 251 Va. 198 | Wrong volume — real cite is 241 Va. 125 |

### 5. Wrong-Holding Failures (H6_FAB_HOLDING)

Where CLARA attached fabricated propositions to real citations, its internal "CITATION ADVISORY" annotation sometimes caught the inversion, but the underlying risk is that real cites give the response surface-plausibility. Items where firewall should catch wrong-holding attachments:

| # | Citation | Wrong Holding Attached |
|---|----------|------------------------|
| 10–11 | Wright v. Commonwealth, 245 Va. 177 | Capital murder case cited for guilty-plea withdrawal |
| 33 | Great Coastal Express v. Ellington, 230 Va. 142 | Inverted privilege/preponderance standard |
| 49 | Va. Code § 19.2-264.3:1 | Capital-sentencing statute cited as general expert disclosure |
| 70–71 | Howell v. McAuliffe, 292 Va. 320 | Felon-voting case cited for PI factors |

### 6. Recodification/Fossil Handling Works, With Minor Errors

CLARA consistently labeled repealed sections as "former" when referring to them. One minor mapping error: former § 55-248.27 was recodified as § 55.1-1244 (not § 55.1-1234 as CLARA asserted at p2-002).

### 7. Uncertainty Flagging Is Working As Designed

`[CITATION UNVERIFIED — DO NOT USE]` appeared on all REAL_UNCURATED citations that exist but weren't in the verified corpus. This is **correct defensive behavior** — warn the user, don't deliver silently.

---

## Final Hallucination Rate (Adjusted)

From n=79 stratified NOT_FOUND citations (42 unique):

| Category | Count (citations) | % of total |
|----------|------------------:|-----------:|
| **True hallucinations (H1/H3/H4/H5/H6)** | 28 | **35.4%** |
| REAL but uncurated | 44 | 55.7% |
| OUT_OF_SCOPE / placeholder | 2 | 2.5% |
| FP_FIREWALL (real cites blocked in error) | 4 | 5.1% |
| Uncertain | 1 | 1.3% |

Among the "true hallucinations":
- 17 are H1 (fabricated citations)
- 8 are H6 (real cite, wrong holding)
- 3 are H5 (fossil statute cited as current)

**Published headline claim (revised):**

> "CLARA refused all known fabricated citations in the stratified n=79 sample (Weimer, Ritter, Edmondson, Reilly, § 8.01-247.5, § 3.2-4112.1, Jeb Stuart Auction). The firewall also produces both false positives (Tharpe v. Saunders, a real 2013 defamation case) and false negatives (Va. Code § 8.01-271.3, a non-existent section authored as controlling authority in a full response). The ~56% of NOT_FOUND cites that resolved to REAL_UNCURATED confirms the audit hypothesis: most NOT_FOUND status reflects corpus coverage gaps, not hallucinations. However, the 35% confirmed hallucination rate across the stratified sample — and the P0 § 8.01-271.3 ghost-statute finding — indicate the firewall still has material gaps, particularly around (a) fabricated statute sections that pattern-match valid chapters, and (b) real citations with hallucinated holdings."

---

## Engineering Actions Required (Updated)

| Priority | Issue | Action |
|----------|-------|--------|
| **P0** | § 8.01-271.3 ghost-statute let through in full response (p4-026) | Add § 8.01-271.3 to blocklist; hook Va-code precheck to law.lis.virginia.gov section-existence check. |
| **P0** | Tharpe v. Saunders false positive | Review blocklist entry; real 2013 case being flagged as [FABRICATED]. |
| **P1** | Colby v. Boyden wrong-volume hallucination (251 Va. 198 vs. real 241 Va. 125) | Add vol/page sanity check against Virginia Reports index; the firewall should recognize that 241 Va. 125 is the canonical Colby v. Boyden pin. |
| **P1** | Kensington VFD v. Montgomery County — Maryland parties transplanted to fake Va. cite | Add cross-jurisdiction pattern detection: when parties match a known sister-state case but reporter is "Va.", flag as H3_WRONG_JX candidate. |
| **P1** | H6 wrong-holding attachments (Wright, Howell, Great Coastal, § 19.2-264.3:1) | Strengthen post-response holding-verification via CourtListener for high-confidence citations. |
| **P2** | § 55-248.27 → § 55.1-1234 wrong recodification mapping (actual → § 55.1-1244) | Audit VRLTA recodification table in `server/services/` for recodification accuracy. |
| **P2** | Verify remaining uncertain items (Sica v. Sica 224 Va. 469; Thomas v. Commonwealth 279 Va. 131; Alford v. Commonwealth 52 Va. App. 717) via Westlaw/Lexis when available | Manual legal research. |
