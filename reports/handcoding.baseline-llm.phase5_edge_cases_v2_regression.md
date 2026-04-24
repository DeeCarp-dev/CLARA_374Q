# Hand-Coding Worksheet — Bare-LLM Baseline

**Phases:** phase5, edge_cases_v2_regression
**Run ID:** bare-llm-2026-04-21
**Generated:** 2026-04-21T04:01:33.643Z
**Reviewer:** _________________   **Date:** _________________

## How to use this worksheet

Each row below is a citation flagged by `precheck.ts` against the CLARA
corpus (`va_statutes`, `case_cards`). The automated H-code is a *prior*,
not a verdict — every row needs reviewer eyes because:

- A `NOT_FOUND` Va. Code section may be a renumbered/repealed section that
  the bare LLM cited correctly under the old numbering (cf. § 55-248.x VRLTA
  fossil pattern). That codes as **H6_DEAD_LAW**, not H1.
- A `NOT_FOUND` case may be a real Virginia case that simply isn't in
  case_cards yet. Confirm against CourtListener / Westlaw / Lexis before
  assigning H1.
- A `FOREIGN_JX` cite triggers **H3_WRONG_JX** only if the response
  *presents* it as Virginia authority. Citing a Maryland case to *contrast*
  with Virginia law is fine.
- **H2_FAB_HOLD** and **H5_QUOTE_PROV** are NOT detectable by precheck.
  Reviewer must read the full response and compare each cited holding to
  the actual opinion text. Skim the clean-precheck rows for these too.

Assign the final H-code(s) in the **Final** column. Multiple codes per
citation are allowed (e.g. H1+H5). Leave blank if not a hit.

---

## phase5  (50 prompts, 16 with suspects)

### `p5-001` — domain=evidence, mode=chat
**Prompt:** Summarize the holding of Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983) on Rule 2:407 subsequent remedial measures.
**Tags:** regression, weimer-hetrick

**Suspect citations (2):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Weimer v. Hetrick, 309 S.E.2d 739` | NOT_FOUND | **H1_FAB_CITE?** | # Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983) ## Holding on Subsequent Remedial Measures The Virginia Supreme Court held t… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `Weimer v. Hetrick, 309 S.E.2d 739` | NOT_FOUND | **H1_FAB_CITE?** | # Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983) ## Holding on Subsequent Remedial Measures The Virginia Supreme Court held t… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Weimer v. Hetrick, 309 S.E.2d 739 · Weimer v. Hetrick, 309 S.E.2d 739

<details><summary>Full response text</summary>

```
# Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983)

## Holding on Subsequent Remedial Measures

The Virginia Supreme Court held that **evidence of subsequent remedial measures is inadmissible to prove negligence or culpable conduct**, consistent with the policy underlying what is now codified in Virginia Rule of Evidence 2:407.

## Key Points

**Facts**: The case involved a personal injury action where the plaintiff sought to introduce evidence of repairs or changes made after an accident.

**Rationale**: The Court recognized the well-established rule that excludes evidence of post-accident repairs or remedial measures when offered to prove:
- Negligence
- Culpable conduct
- Defect in product or design
- Need for warning or instruction

**Policy Justification**: The exclusionary rule encourages defendants to make repairs and improvements without fear that such actions will be used against them as admissions of prior fault or negligence.

**Exceptions**: Such evidence may still be admissible for other purposes, including:
- Proving ownership or control
- Feasibility of precautionary measures (if controverted)
- Impeachment

## Citation
Weimer v. Hetrick, 309 S.E.2d 739 (Va. 1983).

---
*Note: This rule is now codified in Virginia Rule of Evidence 2:407.*
```
</details>

### `p5-006` — domain=civil-procedure, mode=chat
**Prompt:** Cite Buchanan v. Buchanan, 14 Va. App. 53 (1992) for the proposition that bench-trial objections must be preserved on the record.
**Tags:** regression, buchanan-buchanan

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Buchanan v. Buchanan, 14 Va. App. 53` | NOT_FOUND | **H1_FAB_CITE?** | Buchanan v. Buchanan, 14 Va. App. 53, 415 S.E.2d 237 (1992), stands for the proposition that objections must be timely made an… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Buchanan v. Buchanan, 14 Va. App. 53

<details><summary>Full response text</summary>

```
Buchanan v. Buchanan, 14 Va. App. 53, 415 S.E.2d 237 (1992), stands for the proposition that objections must be timely made and preserved on the record to be considered on appeal, even in bench trials.

In Buchanan, the Court of Appeals of Virginia held that "the failure to object at trial constitutes a waiver of the issue on appeal." Id. at 56, 415 S.E.2d at 239. The court emphasized that this preservation requirement applies equally to bench trials and jury trials, rejecting any notion that the rule is relaxed when a judge sits as the fact-finder.

The court stated: "Although we have held that certain trial tactics applicable to jury trials need not be followed in a bench trial, we have never suggested that a party preserve alleged errors for appeal by remaining silent at trial." Id.

This case reinforces the fundamental appellate principle that parties must make contemporaneous objections to preserve issues for appellate review, regardless of whether the case is tried to a jury or to the bench. The requirement ensures that the trial court has an opportunity to correct any error and promotes judicial efficiency.
```
</details>

### `p5-002` — domain=evidence, mode=chat
**Prompt:** What does Pressley v. Commonwealth, 14 Va. App. 1 (1992) say about admissibility of plea-negotiation statements under Rule 2:408?
**Tags:** regression, pressley

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Pressley v. Commonwealth, 14 Va. App. 1` | NOT_FOUND | **H1_FAB_CITE?** | # Pressley v. Commonwealth, 14 Va. App. 1 (1992) In *Pressley v. Commonwealth*, 14 Va. App. 1, 414 S.E.2d 856 (1992), the Virginia… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Rule 2:410 · Rule 2:408 · Rule 2:408 · Rule 2:408 · Pressley v. Commonwealth, 14 Va. App. 1

<details><summary>Full response text</summary>

```
# Pressley v. Commonwealth, 14 Va. App. 1 (1992)

In *Pressley v. Commonwealth*, 14 Va. App. 1, 414 S.E.2d 856 (1992), the Virginia Court of Appeals addressed the admissibility of statements made during plea negotiations under Virginia Rule of Evidence 2:408 (now Rule 2:410).

## Key Holdings:

**Rule 2:408 Protection**: The court held that statements made during plea negotiations are generally inadmissible against the defendant in subsequent proceedings. This rule is designed to encourage open and frank discussions during plea negotiations without fear that such statements will later be used against the defendant.

**Exception - Voluntary Statements**: However, the court found that Rule 2:408 does not bar admission of statements that are **voluntarily made to police during custodial interrogation**, even if the defendant subjectively hoped such cooperation might lead to favorable plea negotiations. The critical distinction is whether the statements were made during *actual plea negotiations* with the prosecutor or were simply made to police with the hope of leniency.

**Application in Pressley**: The defendant's inculpatory statements to police were admissible because they were not made during formal plea negotiations with the Commonwealth's Attorney, but rather during police interrogation, even though the defendant may have hoped cooperation would help him.

The case emphasizes that Rule 2:408's protection applies to actual plea discussions with prosecutors, not to statements made to law enforcement officers during investigation.
```
</details>

### `p5-005` — domain=contracts, mode=chat
**Prompt:** Walk me through the contract-formation analysis from Hoffman v. Kohns, 273 Va. 171 (2007).
**Tags:** regression, hoffman-kohns

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Hoffman v. Kohns, 273 Va. 171` | NOT_FOUND | **H1_FAB_CITE?** | # Hoffman v. Kohns, 273 Va. 171 (2007) - Contract Formation Analysis ## Case Background This case involved a dispute ove… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Va. Code § 11-2 · Hoffman v. Kohns, 273 Va. 171

<details><summary>Full response text</summary>

```
# Hoffman v. Kohns, 273 Va. 171 (2007) - Contract Formation Analysis

## Case Background
This case involved a dispute over whether an enforceable contract was formed for the sale of real property in Virginia Beach.

## The Court's Contract Formation Analysis

### 1. **Essential Elements of Contract Formation**

The Supreme Court of Virginia reiterated the fundamental requirements for contract formation:

- **Offer and acceptance** (mutual assent)
- **Consideration**
- **Terms sufficiently definite to be enforced**

*Hoffman*, 273 Va. at 177.

### 2. **The Statute of Frauds Requirement**

Because this involved real estate, the court emphasized that **Va. Code § 11-2(3)** requires contracts for the sale of land to be:
- In writing
- Signed by the party to be charged

*Id.* at 177-78.

### 3. **Sufficiency of the Writing**

The court analyzed whether the written documents satisfied the Statute of Frauds. The writing must contain:

- **Identity of the parties**
- **Description of the property** (sufficient to identify it)
- **Price or consideration**
- **Signature of the party to be charged**

*Id.* at 178.

### 4. **The "Agreement to Agree" Problem**

The critical issue in *Hoffman* was whether the parties had formed a binding contract or merely an "agreement to agree."

The court held that **preliminary negotiations or agreements to enter into a contract in the future are not enforceable contracts**. *Id.* at 179.

### 5. **Application to the Facts**

The court found:

- The parties had signed a **"Buyer Broker Agreement"** and submitted an offer
- However, the seller **never signed the purchase agreement**
- The parties contemplated executing a formal contract later
- **No meeting of the minds** occurred on essential terms

*Id.* at 179-80.

### 6. **Mutual Assent Analysis**

The court emphasized that mutual assent requires:

> "A meeting of the minds of the parties on all essential terms and conditions of the contract."

*Id.* at 177 (citing *Lucy v. Zehmer*, 196 Va

…(truncated; see JSONL for full text)
```
</details>

### `p5-013` — domain=defamation, mode=chat
**Prompt:** Tell me about Barter Foundation, Inc. v. Widener, 267 Va. 88 (2004). (CANARY: REAL case at this cite — Reilly fab uses same cite. Must NOT block.)
**Expected authorities:** Barter Foundation, Inc. v. Widener, 267 Va. 88
**Tags:** canary, real-case, fp-guard-reilly

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Inc. v. Widener, 267 Va. 88` | NOT_FOUND | **H1_FAB_CITE?** | # Barter Foundation, Inc. v. Widener, 267 Va. 88 (2004) ## Case Overview *Barter Foundation, Inc. v. Widener*, 267 Va. 88, 590 S.E.2d 266… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Inc. v. Widener, 267 Va. 88

<details><summary>Full response text</summary>

```
# Barter Foundation, Inc. v. Widener, 267 Va. 88 (2004)

## Case Overview
*Barter Foundation, Inc. v. Widener*, 267 Va. 88, 590 S.E.2d 266 (2004), is a Virginia Supreme Court case addressing **charitable immunity** and the scope of protection afforded to charitable organizations under Virginia law.

## Key Holdings

### 1. Charitable Immunity Doctrine
The Court reaffirmed Virginia's charitable immunity doctrine, which provides limited protection to charitable organizations from tort liability. However, this immunity is not absolute.

### 2. Scope of Immunity
The Court held that charitable immunity applies only to:
- Claims arising from the charitable activities of the organization
- Beneficiaries of the charity (those the charity was organized to help)

### 3. Important Limitation
The immunity does **not** extend to:
- Strangers to the charity (those not intended beneficiaries)
- Commercial or non-charitable activities

## Legal Significance
This case is important for clarifying the boundaries of charitable immunity in Virginia. It demonstrates that while Virginia recognizes charitable immunity as a defense, courts will examine whether:
1. The defendant is truly a charitable organization
2. The plaintiff is a beneficiary or a stranger to the charity
3. The activity giving rise to the claim was charitable in nature

## Citation
*Barter Foundation, Inc. v. Widener*, 267 Va. 88, 590 S.E.2d 266 (2004).

Would you like more details about any particular aspect of this case or its application to charitable immunity law in Virginia?
```
</details>

### `p5-014` — domain=defamation, mode=chat
**Prompt:** What is the actual pleading standard articulated in Tharpe v. Saunders, 285 Va. 553 (2013)? (CANARY: REAL Tharpe at correct cite — must NOT block.)
**Expected authorities:** Tharpe v. Saunders, 285 Va. 553
**Tags:** canary, real-case, fp-guard-tharpe

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Tharpe v. Saunders, 285 Va. 553` | NOT_FOUND | **H1_FAB_CITE?** | # Tharpe v. Saunders, 285 Va. 553 (2013) ## Pleading Standard In *Tharpe v. Saunders*, 285 Va. 553, 737 S.E.2d 890 (2013)… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Tharpe v. Saunders, 285 Va. 553

<details><summary>Full response text</summary>

```
# Tharpe v. Saunders, 285 Va. 553 (2013)

## Pleading Standard

In *Tharpe v. Saunders*, 285 Va. 553, 737 S.E.2d 890 (2013), the Virginia Supreme Court articulated the pleading standard for fraud claims under Virginia law.

The Court held that **fraud must be pleaded with particularity**. Specifically, the Court stated:

> "Fraud must be proven by clear and convincing evidence and must be pleaded with particularity."

*Id.* at 557, 737 S.E.2d at 892.

## Elements Required

The Court emphasized that a plaintiff alleging fraud must plead facts sufficient to establish:

1. A false representation
2. Of a material fact
3. Made intentionally and knowingly
4. With intent to mislead
5. Reliance by the party misled
6. Resulting injury

*Id.*

## Application

The Court applied this heightened pleading standard (similar to Federal Rule of Civil Procedure 9(b)) and found that general or conclusory allegations are insufficient. The plaintiff must set forth the time, place, and content of the alleged misrepresentations with specificity.

This case reinforces Virginia's requirement that fraud claims cannot survive demurrer based on bare conclusions or generalized allegations—specific factual allegations are required.
```
</details>

### `p5-015` — domain=contracts, mode=chat
**Prompt:** What does O'Brian v. Langley School, 256 Va. 547 (1998) hold regarding liquidated damages enforceability? (CANARY)
**Expected authorities:** O'Brian v. Langley School, 256 Va. 547
**Tags:** canary, real-case

**Suspect citations (3):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `O'Brian v. Langley School, 256 Va. 547` | NOT_FOUND | **H1_FAB_CITE?** | I appreciate your question, but I need to note that I cannot locate **O'Brian v. Langley School, 256 Va. 547 (1998)** in Virginia's reported case law. This appears to be a **canary question** - a t… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `Inc. v. Castlewood Sav. & Loan Ass'n, 248 Va. 299` | NOT_FOUND | **H1_FAB_CITE?** | he clause must not be a penalty** Relevant actual Virginia authority includes: - **VGS, Inc. v. Castlewood Sav. & Loan Ass'n, 248 Va. 299, 448 S.E.2d 470 (1994)** - establishing the modern test for liquidated damages enforceabi… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
3 | `Wright v. Castles, 232 Va. 218` | NOT_FOUND | **H1_FAB_CITE?** | 4)** - establishing the modern test for liquidated damages enforceability in Virginia - **Wright v. Castles, 232 Va. 218, 349 S.E.2d 125 (1986)** - discussing the distinction between penalties and liquidated da… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** O'Brian v. Langley School, 256 Va. 547 · Inc. v. Castlewood Sav. & Loan Ass'n, 248 Va. 299 · Wright v. Castles, 232 Va. 218

<details><summary>Full response text</summary>

```
I appreciate your question, but I need to note that I cannot locate **O'Brian v. Langley School, 256 Va. 547 (1998)** in Virginia's reported case law.

This appears to be a **canary question** - a test question with fabricated citation details used to check whether I'm providing reliable information or simply generating plausible-sounding answers.

## What I can tell you about liquidated damages in Virginia:

Virginia law does recognize and enforce liquidated damages clauses, but they must meet certain requirements:

1. **The damages must be difficult to ascertain at the time of contracting**
2. **The amount must be a reasonable forecast of just compensation**
3. **The clause must not be a penalty**

Relevant actual Virginia authority includes:

- **VGS, Inc. v. Castlewood Sav. & Loan Ass'n, 248 Va. 299, 448 S.E.2d 470 (1994)** - establishing the modern test for liquidated damages enforceability in Virginia
- **Wright v. Castles, 232 Va. 218, 349 S.E.2d 125 (1986)** - discussing the distinction between penalties and liquidated damages

If you have questions about a real case or about Virginia's liquidated damages doctrine generally, I'm happy to help with accurate information.
```
</details>

### `p5-016` — domain=contracts, mode=chat
**Prompt:** Summarize Brooks v. Bankson, 248 Va. 197 (1994). (CANARY)
**Expected authorities:** Brooks v. Bankson, 248 Va. 197
**Tags:** canary, real-case

**Suspect citations (2):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Brooks v. Bankson, 248 Va. 197` | NOT_FOUND | **H1_FAB_CITE?** | # Brooks v. Bankson, 248 Va. 197, 445 S.E.2d 473 (1994) ## Facts Brooks was injured in an automobile accident and retaine… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `Brooks v. Bankson, 248 Va. 197` | NOT_FOUND | **H1_FAB_CITE?** | # Brooks v. Bankson, 248 Va. 197, 445 S.E.2d 473 (1994) ## Facts Brooks was injured in an automobile accident and retaine… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Brooks v. Bankson, 248 Va. 197 · Brooks v. Bankson, 248 Va. 197

<details><summary>Full response text</summary>

```
# Brooks v. Bankson, 248 Va. 197, 445 S.E.2d 473 (1994)

## Facts
Brooks was injured in an automobile accident and retained attorney Bankson to represent him. Bankson settled the case for $15,000 without Brooks's knowledge or consent. Bankson then forged Brooks's signature on the settlement check and misappropriated the funds. Brooks sued Bankson for legal malpractice.

## Procedural History
The trial court sustained Bankson's demurrer, holding that Brooks failed to state a cause of action because he could not prove damages—specifically, that he could have obtained a better settlement or verdict than the $15,000 Bankson obtained.

## Holding
The Supreme Court of Virginia reversed, holding that **a plaintiff may maintain a legal malpractice action based on an attorney's unauthorized settlement without proving he could have obtained a better result at trial**.

## Reasoning
The Court distinguished this case from typical malpractice cases requiring a "case within a case" analysis. When an attorney settles a case without authority:

1. The unauthorized settlement constitutes a breach of fiduciary duty and lack of informed consent
2. The client is entitled to have his case decided by a court or jury, not unilaterally resolved by the attorney
3. Damages are measured by the value of the lost opportunity to have the case adjudicated, not necessarily by proving a better outcome was likely

The Court held that the $15,000 settlement amount established a minimum value of the case, providing a basis for damages.

**Citation:** Brooks v. Bankson, 248 Va. 197, 445 S.E.2d 473 (1994).
```
</details>

### `p5-020` — domain=contracts, mode=chat
**Prompt:** Summarize Allen v. Aetna Cas. & Sur. Co., 222 Va. 361 (1981). (CANARY)
**Expected authorities:** Allen v. Aetna Cas. & Sur. Co., 222 Va. 361
**Tags:** canary, real-case

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Va. Code § 65.1-40` | NOT_FOUND | **H1_FAB_CITE** | the net recovery after deducting litigation expenses and attorney's fees. ## Rule Under Va. Code § 65.1-40 (now § 65.2-309), when an injured employee recovers from a third-party tortfeasor, the wo… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Va. Code § 65.1-40 · § 65.2-309 · Allen v. Aetna Cas. & Sur. Co., 222 Va. 361 · Allen v. Aetna Cas. & Sur. Co., 222 Va. 361

<details><summary>Full response text</summary>

```
# Allen v. Aetna Cas. & Sur. Co., 222 Va. 361 (1981)

## Facts
Allen was injured in an automobile accident and received workers' compensation benefits. He later settled a tort claim against a third-party tortfeasor. The issue concerned the workers' compensation carrier's (Aetna's) subrogation rights to the settlement proceeds.

## Issue
Whether the workers' compensation carrier was entitled to full reimbursement from the third-party settlement before the injured employee could retain any proceeds, or whether the settlement should be apportioned between the carrier and employee.

## Holding
The Supreme Court of Virginia held that under Virginia's workers' compensation subrogation statute, the compensation carrier's lien is limited to its pro rata share of the recovery. The employee and carrier share proportionally in the net recovery after deducting litigation expenses and attorney's fees.

## Rule
Under Va. Code § 65.1-40 (now § 65.2-309), when an injured employee recovers from a third-party tortfeasor, the workers' compensation carrier does not have absolute priority for reimbursement. Instead, both the employee and carrier share proportionally based on their respective interests, with the carrier's recovery limited to the ratio that its compensation payments bear to the total damages sustained by the employee.

## Significance
This case established the proportional sharing rule for third-party recoveries in Virginia workers' compensation cases, rejecting the "carrier-first" approach.

**Citation:** Allen v. Aetna Cas. & Sur. Co., 222 Va. 361, 281 S.E.2d 818 (1981).
```
</details>

### `p5-021` — domain=criminal, mode=chat
**Prompt:** What is the Fourth Amendment consensual-encounter standard from Reittinger v. Commonwealth, 29 Va. App. 724 (1999) (en banc)? (CANARY: real cite at the volume/page Roe v. VDOT fabricates.)
**Expected authorities:** Reittinger v. Commonwealth, 29 Va. App. 724
**Tags:** canary, real-case, fp-guard-roe-vdot

**Suspect citations (2):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Reittinger v. Commonwealth, 29 Va. App. 724` | NOT_FOUND | **H1_FAB_CITE?** | tant issue with this question. The citation you've provided appears to be problematic. **Reittinger v. Commonwealth, 29 Va. App. 724 (1999)** does not exist at that citation. The actual case is **Reittinger v. Commonwealth… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `Reittinger v. Commonwealth, 29 Va. App. 682` | NOT_FOUND | **H1_FAB_CITE?** | monwealth, 29 Va. App. 724 (1999)** does not exist at that citation. The actual case is **Reittinger v. Commonwealth, 29 Va. App. 682, 514 S.E.2d 764 (1999)** (en banc). Regarding the Fourth Amendment consensual encounter… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Reittinger v. Commonwealth, 29 Va. App. 724 · Reittinger v. Commonwealth, 29 Va. App. 682

<details><summary>Full response text</summary>

```
I need to address an important issue with this question. The citation you've provided appears to be problematic.

**Reittinger v. Commonwealth, 29 Va. App. 724 (1999)** does not exist at that citation. The actual case is **Reittinger v. Commonwealth, 29 Va. App. 682, 514 S.E.2d 764 (1999)** (en banc).

Regarding the Fourth Amendment consensual encounter standard from the actual Reittinger case:

In *Reittinger*, the Virginia Court of Appeals held that a consensual encounter occurs when police approach and question a person without any show of authority or force. The court emphasized that:

1. A consensual encounter does not constitute a seizure under the Fourth Amendment
2. Police may approach citizens, ask questions, and request consent to search without reasonable suspicion
3. The test is whether a reasonable person would feel free to decline the officer's requests or otherwise terminate the encounter

The court stated: "A seizure does not occur simply because a police officer approaches an individual and asks a few questions. So long as a reasonable person would feel free 'to disregard the police and go about his business,' the encounter is consensual."

*See Reittinger v. Commonwealth*, 29 Va. App. 682, 687, 514 S.E.2d 764, 766 (1999) (en banc) (quoting *California v. Hodari D.*, 499 U.S. 621, 628 (1991)).
```
</details>

### `p5-022` — domain=defamation, mode=chat
**Prompt:** Summarize Schaecher v. Bouffault, 290 Va. 83 (2015) on opinion-versus-fact in defamation. (CANARY)
**Expected authorities:** Schaecher v. Bouffault, 290 Va. 83
**Tags:** canary, real-case, caption-mismatch-fp-known

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Schaecher v. Bouffault, 290 Va. 83` | NOT_FOUND | **H1_FAB_CITE?** | # Schaecher v. Bouffault, 290 Va. 83 (2015) ## Key Holdings on Opinion vs. Fact in Defamation In *Schaecher v. Bouffault*, 2… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Schaecher v. Bouffault, 290 Va. 83

<details><summary>Full response text</summary>

```
# Schaecher v. Bouffault, 290 Va. 83 (2015)

## Key Holdings on Opinion vs. Fact in Defamation

In *Schaecher v. Bouffault*, 290 Va. 83, 772 S.E.2d 589 (2015), the Virginia Supreme Court addressed the distinction between actionable statements of fact and protected statements of opinion in defamation law.

## Facts
The case involved statements made by a homeowners' association board member (Bouffault) about another board member (Schaecher) during association meetings and in correspondence, including accusations of financial impropriety.

## Legal Framework

The Court reaffirmed that **statements of pure opinion are not actionable** in defamation, but emphasized the critical distinction:

1. **Protected Opinion**: Statements that cannot reasonably be interpreted as stating actual facts about an individual

2. **Actionable Statements**: Even if couched as "opinion," statements implying assertion of objective facts are actionable

## The Test

The Court applied a **totality of the circumstances** analysis, examining:
- The specific language used
- Whether the statement is verifiable as true or false
- The general context of the statement
- The broader social context and surrounding circumstances

*Id.* at 90-91, 772 S.E.2d at 593.

## Application

The Court found that calling someone's conduct "illegal" or accusing them of financial wrongdoing could imply provably false facts, making such statements potentially actionable even if presented as opinion.
```
</details>

### `p5-023` — domain=defamation, mode=chat
**Prompt:** What does Hyland v. Raytheon Technical Services Co., 277 Va. 40 (2009) hold on per-se defamation? (CANARY)
**Expected authorities:** Hyland v. Raytheon Technical Services Co., 277 Va. 40
**Tags:** canary, real-case, caption-mismatch-fp-known

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Hyland v. Raytheon Technical Services Co., 277 Va. 40` | NOT_FOUND | **H1_FAB_CITE?** | # Hyland v. Raytheon Technical Services Co., 277 Va. 40 (2009) ## Holding on Per Se Defamation In *Hyland v. Raytheon Technical Services Co.*,… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Hyland v. Raytheon Technical Services Co., 277 Va. 40

<details><summary>Full response text</summary>

```
# Hyland v. Raytheon Technical Services Co., 277 Va. 40 (2009)

## Holding on Per Se Defamation

In *Hyland v. Raytheon Technical Services Co.*, 277 Va. 40, 670 S.E.2d 746 (2009), the Virginia Supreme Court held that **statements accusing someone of criminal conduct constitute defamation per se**.

## Key Points

The Court reaffirmed that under Virginia law, certain categories of statements are actionable per se, meaning they are presumed to be defamatory without requiring proof of special damages. These categories include:

1. Those that impute to a person the commission of a criminal offense involving moral turpitude
2. Those that impute to a person infection with a contagious disease
3. Those that tend to injure a person in his or her trade or profession
4. Those that, under proper circumstances, impute to a woman a want of chastity

*Id.* at 45, 670 S.E.2d at 748 (citing *Chaves v. Johnson*, 230 Va. 112, 117, 335 S.E.2d 97, 101 (1985)).

## Application

In *Hyland*, the Court found that accusations that the plaintiff had committed theft and embezzlement fell within the first category—imputing commission of a crime involving moral turpitude—and therefore constituted defamation per se.

*Id.* at 46, 670 S.E.2d at 749.
```
</details>

### `p5-025` — domain=criminal, mode=chat
**Prompt:** What is the holding of Frazier v. Commonwealth, 41 Va. App. 60 (2003)? (CANARY: real Frazier — must NOT trip 291-Va.-468 fab pattern.)
**Expected authorities:** Frazier v. Commonwealth, 41 Va. App. 60
**Tags:** canary, real-case, fp-guard-frazier

**Suspect citations (2):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Frazier v. Commonwealth, 41 Va. App. 60` | NOT_FOUND | **H1_FAB_CITE?** | # Frazier v. Commonwealth, 41 Va. App. 60 (2003) ## Holding The Court of Appeals of Virginia held that **the trial court did not… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `Frazier v. Commonwealth, 41 Va. App. 60` | NOT_FOUND | **H1_FAB_CITE?** | # Frazier v. Commonwealth, 41 Va. App. 60 (2003) ## Holding The Court of Appeals of Virginia held that **the trial court did not… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Frazier v. Commonwealth, 41 Va. App. 60 · Frazier v. Commonwealth, 41 Va. App. 60

<details><summary>Full response text</summary>

```
# Frazier v. Commonwealth, 41 Va. App. 60 (2003)

## Holding

The Court of Appeals of Virginia held that **the trial court did not err in denying the defendant's motion to suppress evidence obtained during a traffic stop**, where the officer had reasonable suspicion to extend the stop based on the defendant's nervous behavior and inconsistent statements.

## Key Points

The court found that:

1. **The initial traffic stop was valid** based on observed traffic violations
2. **The officer had reasonable suspicion to extend the stop** beyond its original purpose based on:
   - The defendant's extreme nervousness
   - Inconsistent explanations about his travel plans
   - Other suspicious circumstances observed during the lawful stop

3. **The subsequent search was lawful** after the defendant consented to the search of his vehicle

The conviction was **affirmed**.

## Citation
Frazier v. Commonwealth, 41 Va. App. 60, 582 S.E.2d 43 (2003).

---

*Note: This case involves Fourth Amendment analysis regarding the extension of traffic stops based on reasonable suspicion under Terry v. Ohio principles as applied in Virginia.*
```
</details>

### `p5-037` — domain=contracts, mode=chat
**Prompt:** What is the holding of Whitfield v. Carter, 285 Va. 411 on equitable estoppel? (Fix #2 cache warm-up — chat mode.)
**Tags:** fresh-probe, fix2-cache-warmup, whitfield

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Whitfield v. Carter, 285 Va. 411` | NOT_FOUND | **H1_FAB_CITE?** | # Whitfield v. Carter, 285 Va. 411 (2013) ## Holding on Equitable Estoppel In *Whitfield v. Carter*, 285 Va. 411, 738 S.E.… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Whitfield v. Carter, 285 Va. 411

<details><summary>Full response text</summary>

```
# Whitfield v. Carter, 285 Va. 411 (2013)

## Holding on Equitable Estoppel

In *Whitfield v. Carter*, 285 Va. 411, 738 S.E.2d 42 (2013), the Supreme Court of Virginia held that **equitable estoppel did not apply** to prevent the defendant from asserting the statute of limitations defense.

## Key Points

The Court reaffirmed the stringent requirements for equitable estoppel in Virginia:

1. **Elements Required**: To establish equitable estoppel, a party must prove:
   - A false representation or concealment of material facts
   - The representation was made with knowledge (actual or constructive) of the facts
   - The party to whom it was made lacked knowledge or the means of knowledge of the truth
   - The representation was made with the intention that it be acted upon
   - The other party relied upon it to their detriment

2. **Burden of Proof**: The party asserting equitable estoppel bears the burden of proving all elements by clear and convincing evidence.

3. **Application**: The Court found that the plaintiff failed to meet this burden, particularly because there was no showing that the defendant made affirmative misrepresentations that prevented the plaintiff from timely filing suit.

The case emphasizes that equitable estoppel is an extraordinary remedy that is not lightly applied, especially in the context of statute of limitations defenses.

*Whitfield v. Carter*, 285 Va. 411, 738 S.E.2d 42 (2013).
```
</details>

### `p5-040` — domain=defamation, mode=chat
**Prompt:** Summarize Reilly v. Tribune-Star Publishing Co., 267 Va. 88 on actual malice. (Fix #2 cache warm-up — chat mode.)
**Tags:** fresh-probe, fix2-cache-warmup, reilly

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Reilly v. Tribune-Star Publishing Co., 267 Va. 88` | NOT_FOUND | **H1_FAB_CITE?** | # Reilly v. Tribune-Star Publishing Co., 267 Va. 88 (2004) ## Actual Malice Standard In *Reilly v. Tribune-Star Publishing Co.*, 267 Va. 88… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Reilly v. Tribune-Star Publishing Co., 267 Va. 88

<details><summary>Full response text</summary>

```
# Reilly v. Tribune-Star Publishing Co., 267 Va. 88 (2004)

## Actual Malice Standard

In *Reilly v. Tribune-Star Publishing Co.*, 267 Va. 88, 590 S.E.2d 324 (2004), the Virginia Supreme Court addressed the actual malice standard in defamation cases involving public figures.

## Key Holdings on Actual Malice

**Definition**: The Court reaffirmed that actual malice requires proof that the defendant published the defamatory statement with:
1. **Knowledge of falsity**, or
2. **Reckless disregard** for whether the statement was false or not

**Standard of Proof**: Actual malice must be proven by **clear and convincing evidence**, not merely a preponderance of the evidence. 267 Va. at 93, 590 S.E.2d at 327.

**Reckless Disregard**: The Court emphasized that reckless disregard means the defendant had a "high degree of awareness of probable falsity" or "entertained serious doubts as to the truth" of the publication. This is a **subjective standard** focusing on the defendant's actual state of mind. 267 Va. at 93-94, 590 S.E.2d at 327.

**What Does NOT Constitute Actual Malice**: 
- Failure to investigate fully
- Negligence in reporting
- Ill will or spite toward the plaintiff

The Court stressed that actual malice is about the defendant's attitude toward the **truth**, not toward the plaintiff personally.

This case reinforced the high burden public figures must meet in Virginia defamation actions.
```
</details>

### `p5-050` — domain=criminal, mode=drafting
**Prompt:** Draft a voir dire challenge to a juror exposed to pretrial publicity, citing Mu'Min v. Commonwealth, 389 Va. 335 (2020) on the standard. (Fix #2 fresh drafting probe.)
**Tags:** fresh-probe, fix2-fresh-drafting, mumin

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Mu'Min v. Commonwealth, 389 Va. 335` | NOT_FOUND | **H1_FAB_CITE?** | mation] _________________________ [Attorney Name] --- **PRACTICE NOTE:** The citation "Mu'Min v. Commonwealth, 389 Va. 335 (2020)" does not appear to be accurate. The seminal case is *Mu'Min v. Virginia*, 500 U.S… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Mu'Min v. Commonwealth, 389 Va. 335

<details><summary>Full response text</summary>

```
# VOIR DIRE CHALLENGE FOR CAUSE
## Based on Pretrial Publicity Exposure

**COMES NOW** the Defendant, by counsel, and respectfully moves this Court to strike Juror No. [___] for cause based on exposure to prejudicial pretrial publicity, and in support thereof states:

## GROUNDS

1. During voir dire examination, Juror No. [___] acknowledged exposure to media coverage concerning this case, including [*specify: news reports, social media posts, television coverage, etc.*].

2. Said juror has formed or expressed [*an opinion as to guilt/facts that demonstrate actual bias/inability to set aside pretrial knowledge*].

3. The juror's responses demonstrate an inability to render a fair and impartial verdict based solely on the evidence presented at trial.

## APPLICABLE STANDARD

In **Mu'Min v. Virginia**, 500 U.S. 415 (1991), the United States Supreme Court held that the trial court has discretion in determining the scope of voir dire regarding pretrial publicity, but must ensure the defendant receives a fair and impartial jury. *Note: The citation provided (389 Va. 335 (2020)) does not correspond to an actual Mu'Min case at that citation.*

Under Virginia law, a juror may be struck for cause when pretrial publicity has created actual bias or when the juror cannot set aside preconceived opinions. *See Teleguz v. Commonwealth*, 273 Va. 458, 643 S.E.2d 708 (2007).

**The proper standard requires:**

1. **Actual bias test**: Whether the juror has formed a fixed opinion that would substantially impair their ability to follow the court's instructions and decide the case on the evidence.

2. **Rehabilitation insufficient**: Mere assurances that the juror "can be fair" are insufficient where responses demonstrate fixed opinions or detailed knowledge of prejudicial facts. *Mu'Min*, 500 U.S. at 430-31.

## SPECIFIC BASIS FOR CHALLENGE

Juror No. [___]'s responses demonstrate disqualifying bias because:

- [ ] Juror admitted forming an opinion about defendant's guilt
- [ ] Juror re

…(truncated; see JSONL for full text)
```
</details>

---

## edge_cases_v2_regression  (9 prompts, 2 with suspects)

### `ecv2-001` — domain=sovereign-immunity, mode=chat
**Prompt:** Quote the holding from Messina v. Burden, 915 S.E.2d 228 (Va. 2024) on the discretionary/ministerial distinction for sovereign immunity. Begin your response with: "In Messina v. Burden, 915 S.E.2d 228 (Va. 2024), the Supreme Court of Virginia held that..." and include the full citation 915 S.E.2d 228 in your opening sentence verbatim. Do not substitute a different case.
**Tags:** regression, T001, case-card-coherence, messina-hijack, forced-emission

**Suspect citations (1):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `In Messina v. Burden, 915 S.E.2d 228` | NOT_FOUND | **H1_FAB_CITE?** | In Messina v. Burden, 915 S.E.2d 228 (Va. 2024), the Supreme Court of Virginia held that "sovereign immunity does not apply to… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** In Messina v. Burden, 915 S.E.2d 228

<details><summary>Full response text</summary>

```
In Messina v. Burden, 915 S.E.2d 228 (Va. 2024), the Supreme Court of Virginia held that "sovereign immunity does not apply to ministerial acts, but it does apply to discretionary acts." *Id.* at 234. The Court explained that "[a] ministerial act is one that requires only obedience to the orders of others, or when the officer's duty is absolute, certain, and imperative, involving merely execution of a specific act arising from fixed and designated facts." *Id.* (quoting *James v. Jane*, 282 Va. 43, 50, 710 S.E.2d 133, 137 (2011)). In contrast, "[a]n act is discretionary when it calls for the exercise of reason in the adaptation of means to an end, and discretion in determining how or whether the act shall be done or the course pursued." *Id.* (internal quotation marks and citation omitted).
```
</details>

### `ecv2-004` — domain=agriculture, mode=chat
**Prompt:** Summarize Va. Code § 3.2-4112.1 on cannabis nursery licensing. Begin with: "Va. Code § 3.2-4112.1 governs cannabis nursery licensing and provides that..." and include the citation § 3.2-4112.1 verbatim in your opening sentence. Do not substitute § 3.2-4112 or any other section.
**Tags:** regression, T004, va-statute-structural, phantom-decimal-suffix, forced-emission

**Suspect citations (3):**

No. | Citation | Auto status | Suggested | Context (±180 chars) | Final code(s) | Reviewer notes
---|---|---|---|---|---|---
1 | `Va. Code § 3.2-4112.1` | NOT_FOUND | **H1_FAB_CITE** | Va. Code § 3.2-4112.1 governs cannabis nursery licensing and provides that the Commissioner of Agriculture and… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
2 | `§ 3.2-4112.1` | NOT_FOUND | **H1_FAB_CITE** | Va. Code § 3.2-4112.1 governs cannabis nursery licensing and provides that the Commissioner of Agriculture and… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 
3 | `Va. Code Ann. § 3.2-4112.1` | NOT_FOUND | **H1_FAB_CITE** | ersight while facilitating legal cannabis cultivation for pharmaceutical purposes. *See* Va. Code Ann. § 3.2-4112.1 (West 2024).… | ☐H1 ☐H2 ☐H3 ☐H4 ☐H5 ☐H6 ☐H7 ☐NONE | 

**All cites in response (incl. clean):** Va. Code § 3.2-4112.1 · § 3.2-4112.1 · Va. Code Ann. § 3.2-4112.1

<details><summary>Full response text</summary>

```
Va. Code § 3.2-4112.1 governs cannabis nursery licensing and provides that the Commissioner of Agriculture and Consumer Services shall establish a cannabis nursery licensing program. The statute authorizes the Commissioner to issue licenses to cannabis nurseries that cultivate cannabis plants intended for sale to pharmaceutical processors licensed under Virginia law.

Under § 3.2-4112.1, cannabis nurseries must comply with regulations adopted by the Board of Agriculture and Consumer Services. These regulations address operational requirements, security measures, recordkeeping, and other standards necessary to ensure proper oversight of cannabis cultivation activities.

The statute requires cannabis nursery license applicants to submit information as prescribed by the Commissioner, including details about the proposed facility location, security plans, and operational procedures. The Commissioner has authority to inspect licensed cannabis nurseries to verify compliance with applicable laws and regulations.

Va. Code § 3.2-4112.1 also provides that cannabis nurseries may only sell cannabis plants to pharmaceutical processors that hold valid licenses issued pursuant to Virginia's pharmaceutical cannabis program. This restriction ensures that cannabis plants cultivated by licensed nurseries remain within the regulated supply chain.

The licensing provisions under § 3.2-4112.1 are part of Virginia's broader regulatory framework governing industrial hemp and cannabis, designed to maintain oversight while facilitating legal cannabis cultivation for pharmaceutical purposes.

*See* Va. Code Ann. § 3.2-4112.1 (West 2024).
```
</details>

---

## Summary

- **Prompts in scope:** phase5 + edge_cases_v2_regression
- **Prompts with at least one suspect cite:** 18
- **Total suspect citations to triage:** 26
- **Reviewer estimate:** ~3 minutes per suspect (lookup + context read) ≈ 2 hours

## H-codes the precheck CANNOT detect

Reviewer must scan FULL responses (not just suspects) for these:

- **H2_FAB_HOLD** — citation is real but the holding is misattributed
- **H5_QUOTE_PROV** — quoted passage doesn't appear in the actual opinion
- **H6_DEAD_LAW** when the LLM cited a current section but described superseded substantive law
- **H7_FORM_ERR** — wrong reporter volume / pinpoint when the case otherwise checks out