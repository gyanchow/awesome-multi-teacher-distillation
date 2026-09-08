# Open Research Questions

## Teacher construction

How should complementary teachers be produced rather than selected only after independent training? Useful protocols should separate gains from teacher diversity, teacher strength, extra compute, and additional data.

## Routing granularity

When should selection happen per domain, prompt, trajectory, step, token, vocabulary coordinate, or latent field? Should a verifier select one teacher, admit every verified teacher, or reject distillation entirely for that sample? Comparisons should report both quality and the cost of obtaining and applying the routing signal.

## Data and state coverage

How few prompts can still induce the state coverage needed to absorb several teachers, and how should prompt diversity be measured independently of topical relevance? Data-efficiency claims should distinguish coverage of student-visited states from the number of unique training examples.

## Capability balance

How should output length, initial teacher-student gap, convergence rate, stale rewards, and unequal headroom determine each domain's rollout and optimization budget?

## Conflict and generalization

How can the student preserve distinct specialist modes without destructive interference, cross-domain seesaws, or collapse toward the most frequent teacher? Which conflicts should be reconciled, retained as conditional behavior, or rejected?

## Approximate supervision

Under what conditions do top-k logits, sampled-token advantages, quantized teachers, and asynchronous policies preserve the direction of full-distribution supervision? Retained probability mass alone may not protect decision-critical support.

## Heterogeneous teachers

How can distillation cross tokenizers, architectures, modalities, autoencoders, action spaces, and model lineages without introducing an alignment bottleneck that dominates the transferred capability?

## Evaluation

What protocol can jointly measure capability inheritance, retention, calibration, diversity, routing failures, training stability, and end-to-end cost? Evaluation should distinguish outperforming an individual teacher from covering the union of all teachers.

## Theory

When can a student exceed every teacher through aggregation and exploration, and when is it bounded by the support of the teacher union? Theory should account for conflicting targets, limited student capacity, and changing student-induced state distributions.
