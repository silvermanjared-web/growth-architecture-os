# Positioning Architecture

```mermaid
flowchart LR
    E[Admitted evidence] --> B[Hard factual boundary]
    B --> R[Role / evaluator requirement]
    R --> S[Select strongest relevant truth]
    S --> V[Translate into employer value]
    V --> C[Senior candidate voice]
    C --> Q[Adversarial factual QA]
    Q --> H{Hireability score >= 80?}
    H -- No --> V
    H -- Yes --> P[Public release]

    G[Claim registry] -. controls .-> B
    G -. validates .-> Q
```

The evidence layer and positioning layer are deliberately separate.

The evidence layer is conservative because its job is to prevent unsupported claims. The positioning layer is persuasive because its job is to make supported capability legible to an employer.

A strong system needs both. Evidence without positioning becomes a compliance memo. Positioning without evidence becomes marketing fiction.
