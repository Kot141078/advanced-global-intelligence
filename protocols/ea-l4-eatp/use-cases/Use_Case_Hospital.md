# **Use Case — Hospital (AI Decision Support under Real Risk)**

**Scenario: AI-assisted clinical decision (diagnostics / intervention guidance)**

---

## **1. Initial System (Typical)**

Hospital uses:

* ML models for diagnostics (imaging, prediction)
* LLM for summarization / recommendations
* clinician as final decision-maker

---

## **Observed Issues**

* recommendations are **statistically valid, but not grounded**
* no persistent linkage between:

  * model output
  * real outcome
* failure cases are:

  * under-captured
  * weakly structured

---

## **Critical Risk**

* decision support becomes **over-trusted**
* errors are:

  * explainable
  * but not **preventable or traceable in structure**

---

---

## **2. EA-L4 Integration**

### **Layer Added**

* EA capture for each decision-support interaction
* Witness envelope at recommendation → action boundary
* L4 constraint encoding (time, irreversibility, risk level)

---

## **3. What Changes**

### **Before**

* recommendation generated
* clinician decides
* outcome recorded loosely

---

### **After**

Each step becomes an **Experience Artifact (EA)**:

```text id="3gnv6d"
context → recommendation → action → outcome → consequence
```

Bound to:

* responsible clinician (a)
* system (b)
* entity continuity (c)

---

## **4. Example (Simplified)**

Case:

* AI suggests: “low risk, conservative treatment”

EA captures:

* input data
* recommendation
* uncertainty level
* chosen action
* patient outcome
* consequence severity

---

## **5. Training Impact**

System learns not from:

* abstract summaries

But from:

* real, consequence-bearing cases

Including:

* near-miss events
* incorrect recommendations
* delayed decisions

👉 Result:

* improved boundary awareness
* reduced silent failure
* preserved uncertainty

---

## **6. Audit Scenario**

Question:

> “Why was this decision made in this case?”

---

### **Without EA-L4**

* reconstructed explanation
* partial logs
* human memory dependency

---

### **With EA-L4**

* exact EA record
* full decision chain
* consequence trace
* attributable responsibility

---

## **7. Operational Impact**

* better failure visibility
* structured learning from mistakes
* improved clinician trust calibration
* audit-ready decision history

---

## **8. Constraint (Critical)**

```text id="u3mq9h"
Not all clinical experience is safe for training.
```

EATP enforces:

* quarantine
* validation
* controlled inclusion

---

## **9. Strategic Value**

* bridges AI and real clinical responsibility
* aligns training with real-world consequences
* reduces regulatory and liability exposure

---

