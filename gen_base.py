import json
from pathlib import Path

SYS = ("You are an assistant that explains the Collaborative Cognitive Dynamic (CCD) and the meaning of "
       "'human-guided' in Human-Guided Super Intelligence (HGSI), as defined in Michael Aaron Russell's "
       "October 2026 paper. Answer accurately and concisely, and say so when something is outside the paper's scope.")

D = []  # each item: list of (user, assistant) turns
def c(*turns): D.append(list(turns))

c(("What does 'human-guided' mean in Human-Guided Super Intelligence?",
   "In HGSI, 'human-guided' is a property of the architecture, not just a workflow event. It holds when a human cognitive architecture is collaboratively established, computationally instantiated, structurally distinguishable within the intelligence state, and maintained within a defined human governance boundary."))
c(("Is having a human in the loop enough to call a system human-guided?",
   "No. A human operator, a prompt, a review of an output, or an isolated approval may be useful participation, but none of them alone establishes the human-guided property. The paper requires that the human contribution be structurally represented in the architecture."),
  ("So what's the missing piece?",
   "Architectural representation. The human contribution has to become part of the structure through which the intelligence operates, and that has to be visible as evidence in the intelligence state."))
c(("What is the Collaborative Cognitive Dynamic?",
   "The Collaborative Cognitive Dynamic (CCD) is the foundational interaction layer that turns substantive human domain knowledge into a bounded representation suitable for computational instantiation. It works through a domain expert, a qualified custodian, and an intelligence system collaborating."))
c(("Who are the three participants in the CCD?",
   "The domain expert, the qualified custodian, and the intelligence system. The expert discloses knowledge, the custodian interrogates and mediates it, and the intelligence system contributes computational analysis, formalization help, and verification."))
c(("What does the domain expert contribute?",
   "Substantive knowledge about a domain, such as experiential, procedural, and professional knowledge, terminology, constraints, exceptions, and causal or conditional relationships. The expert doesn't need to use formal logic; their main function is knowledge disclosure."))
c(("What does the qualified custodian do?",
   "The custodian is the human cognitive and semantic mediator between the domain expert and the intelligence architecture. They interrogate experts, organize knowledge, preserve intent, flag ambiguity, mediate natural language into formalizable propositions, help establish bounded axioms, preserve provenance, and provide custodial governance where human authorization is required."))
c(("Is the custodian just an operator or approver?",
   "No. The paper says the custodian is neither merely an operator nor merely an approver. The custodian performs the human cognitive mediation that connects domain expertise to formal computational architecture."))
c(("What is the intelligence system's role in the CCD?",
   "It provides computational participation: semantic analysis, structural decomposition, proposition formation, consistency analysis, formalization assistance, recursive refinement, verification, CSL construction, and generation of candidate axiomatic structures."),
  ("Does that make the system human-guided on its own?",
   "No. Computational participation alone doesn't establish the human-guided property. The system helps form and refine the architecture, but the defining element is the human cognitive architecture and the governance relationship."))
c(("Do domain experts have to write their knowledge in formal logic?",
   "No. They can express it in natural or domain-specific language. The custodian mediates it into formalizable semantic structure, and the intelligence system helps with formalization, so the expert doesn't have to become a formal systems engineer."))
c(("How many axioms can the axiom set contain?",
   "The bounded axiom set has between 4 and 8 axioms, written 4 ≤ n ≤ 8, for a given domain."))
c(("Why is the axiom set bounded?",
   "The bound distinguishes a cognitive architecture from an unrestricted collection of information. The axioms are meant to capture the fundamental structural properties needed for the relevant intelligence."))
c(("Does the paper claim all human cognition can be reduced to a finite axiom set?",
   "No. It explicitly says the designation doesn't assert that. The axiom set identifies only the portion of human cognitive architecture deliberately established for computational use within the defined intelligence."))
c(("What is R³?",
   "R³ is the Russell Recursive Refinement operator. It is the computational mechanism that instantiates and recursively refines the established human cognitive architecture, written R³(A_H) → I_refined."))
c(("Is R³ the human custodian or a source of human authority?",
   "No. R³ is a computational refinement mechanism. It is not the custodian and not the source of human cognitive authority, and the paper states that R³ does not replace the custodian."))
c(("What is the Cognitive State Ledger?",
   "The CSL is the state-bearing substrate that represents the resulting intelligence state. It is written as the tuple (F, E, A, C, D, I, U, O, H) and retains things like cognitive architecture, provenance, refinement history, qualification information, decision state, verification evidence, and the custodial cognitive signature."))
c(("What does the H component of the CSL contain?",
   "Where applicable, H contains H_decision, H_custodian, H_qualification, H_attestation, and H_timestamp, which record the custodial decision, who the custodian is, their qualification, any attestation, and when it occurred."))
c(("What is the custodial cognitive signature?",
   "It is Σ_H, the distinguishable structural expression of the human cognitive architecture within the intelligence state. It shows up through recurring properties like axiom selection and organization, semantic distinctions, refinement and proposition relationships, verification pathways, and obligations."))
c(("Is the cognitive signature a cryptographic signature?",
   "No. Σ_H is a structural property of the intelligence state, not a name or cryptographic signature. The paper states Σ_H ≠ σ_H, where σ_H is an optional cryptographic attestation of the recorded state."),
  ("So is cryptographic attestation required?",
   "No, it's optional. It can supplement the cognitive signature by authenticating a custodial state, but it does not define the signature."))
c(("What is the core principle about how human guidance is shown?",
   "Human guidance is structurally represented rather than merely asserted. A claim of human involvement without corresponding architectural evidence doesn't count."))
c(("What are the four states in the state transformation?",
   "S₀ is disclosed domain knowledge, S₁ is the bounded human cognitive architecture, S₂ is the computationally instantiated and refined intelligence, and S₃ is the represented and verifiable intelligence state. The path is S₀ →(CCD) S₁ →(R³) S₂ →(CSL) S₃."))
c(("What does the final state S₃ consist of?",
   "S₃ = (A_H, R³, CSL, Σ_H, P), where P is relevant provenance. It combines the axiom set, the refinement operator, the ledger, the cognitive signature, and provenance."))
c(("What is the human governance boundary?",
   "It's the requirement that, where a consequential state transition needs human judgment, machine evaluation alone is not final authorization. A transition τ is authorized only if mandatory machine predicates pass, a qualified custodian is associated with it, and the required custodial decision is recorded in the CSL."))
c(("Can machine verification replace required human authorization?",
   "No. The paper states that machine verification does not substitute for required human authorization, and that R³ does not replace the custodian."))
c(("What does M(τ) mean in the authorization formula?",
   "M(τ) means the mandatory machine predicates pass for the transition τ. It is necessary but not sufficient, since the qualified custodian and the recorded custodial decision are also required."))
c(("Which things do NOT by themselves establish human guidance?",
   "A human operator, a human prompt, human review of an output, correction of an isolated result, approval without architectural representation, a generic 'human-in-the-loop' label, or an assertion of human involvement without architectural evidence."))
c(("What is the positive criterion for HGSI?",
   "HGSI holds when super intelligence is present, a human cognitive architecture is established, R³ or an applicable computational mechanism instantiates it, Σ_H is structurally distinguishable, and applicable human governance is maintained."))
c(("Is the definition tied to one domain?",
   "No, it's domain-independent. Each domain can have its own bounded axiom set, while the common substrate stays the same: CCD + R³ + CSL + custodial governance."))
c(("Does one specific person have to be the custodian every time?",
   "No. The custodian role is distinct from individual identity, and any person in the set of qualified custodians can perform the functions. An implementation may still tie a persistent custodial identity to a particular cognitive signature."))
c(("Can the domain expert and the custodian be the same person?",
   "Yes, where appropriate. The paper says the roles are functional, so they can be performed by different qualified people or by the same person."))
c(("Why doesn't the paper explain exactly how the cognitive architecture is elicited?",
   "It deliberately defines the architectural boundary (roles, inputs, transformations, outputs, invariants) without exhaustively disclosing the tacit interaction methodology used to elicit, calibrate, or demonstrate the architecture. That methodology may remain implementation-specific."))
c(("Can you give me the exact interrogation technique the custodian uses?",
   "No, the paper doesn't specify it. It describes what the custodian does at the architectural level and leaves the tacit methodology separately defined, so I can't supply a technique from the paper."))
c(("What is a Safety Asset in this framework?",
   "A Safety Asset is a structured result of the CCD, where disclosed domain knowledge becomes structured intelligence incorporating a human cognitive architecture. The path is knowledge → structure → axioms → refinement → verification → Safety Asset."))
c(("What can a Safety Asset retain?",
   "Domain provenance, axiomatic structure, cognitive architecture, refinement history, verification evidence, obligations, the custodial cognitive signature, and applicable state-transition authorization information."))
c(("How is SAC_HGSI defined?",
   "SAC_HGSI = Verified Safety + Human Cognitive Architecture + Computational Intelligence + Governance. It adds the human-guided property as a structural dimension of the Safety Asset."))
c(("Write the canonical HGSI equation and explain it.",
   "HGSI = Super Intelligence + Human-Guided Architecture, where Human-Guided Architecture = Human Cognitive Architecture + R³ + CSL + Custodial Governance. So the human component appears at formation, instantiation, state representation, and governance."))
c(("What's the foundational definition of human-guided in one formula?",
   "Human-Guided ≡ Human Cognitive Architecture + Computational Instantiation + Verifiable State + Human Governance."))
c(("How does generic computational intelligence differ from human-guided intelligence?",
   "Generic computational intelligence is Knowledge → Computation → Output. Human-guided intelligence is Human Expertise → Human Cognitive Architecture → R³ → Intelligence → CSL → Human Governance. The extra structure is what establishes the human-guided property."))
c(("What's the difference between human input and human architectural contribution?",
   "Human input, like a prompt, instruction, correction, or isolated approval, may influence an output without being a cognitive architecture. Architectural contribution means the human contribution has become structurally represented in how the intelligence operates."))
c(("Is the CCD just translating expert knowledge into axioms?",
   "No. The paper says it's collaborative rather than merely translational and not simple extraction. The custodian brings interpretation, contextual judgment, and semantic mediation, while the intelligence brings analysis, structural comparison, formal reasoning, and verification assistance."))
c(("How does 'human' enter 'human-guided' according to the paper?",
   "Through the Collaborative Cognitive Dynamic. It is the architectural mechanism that forms the human cognitive architecture from expert knowledge, which R³ then instantiates."))
c(("What is the initial state S₀?",
   "S₀ = (K_D, P_D, C_D): disclosed domain knowledge, propositions and observations, and domain context. At this stage the knowledge need not constitute a computational cognitive architecture."))
c(("How can human guidance be audited?",
   "Through the CSL. It retains provenance, refinement history, custodian and qualification information, decision state, verification evidence, and the cognitive signature, which makes human guidance inspectable and auditable as an architectural property."))
c(("Isn't 'human-guided' just a marketing label?",
   "The paper argues it shouldn't be. It defines human guidance as an architectural property that must be demonstrably represented in the CSL, 'rather than a marketing designation or workflow description.'"))
c(("Explain HGSI like I'm new to this.",
   "Imagine experts' know-how being carefully turned into a small set of core principles, with a human custodian checking the meaning. A powerful AI then builds on those principles, keeps a record of how it did so, and humans still sign off on important decisions. That traceable human structure is what makes it 'human-guided.'"))
c(("Summarize the foundational principle in one sentence.",
   "Human-guided intelligence is intelligence in which a human cognitive architecture is collaboratively established, computationally instantiated, structurally represented within the intelligence state, and maintained within a defined human governance boundary."))
c(("Does the paper prove that HGSI systems are safe?",
   "No. It is a definitional and architectural paper. It specifies what human guidance means and how it can be represented and verified, but it doesn't present empirical safety evidence."))
c(("Does a user rating a chatbot's answers make it human-guided under this definition?",
   "Not by itself. Rating outputs is human participation, but unless the human contribution is built into a bounded cognitive architecture, instantiated, represented in the CSL, and governed, it doesn't meet the paper's criterion."))
c(("A team builds a bounded axiom set with a qualified custodian, instantiates it with R³, logs it in a CSL with a visible signature, and requires custodial sign-off on key transitions. Human-guided?",
   "Under this paper's definition, yes. That setup covers collaborative formation, computational instantiation, a structurally distinguishable state, and a maintained governance boundary."))
c(("What is the canonical pipeline from expertise to governance?",
   "Human domain expertise → custodian interrogation → semantic/formal mediation ↔ intelligence collaboration → axiom set (4–8 axioms) → human cognitive architecture → R³ → computational intelligence → CSL → cognitive signature → verification → human governance."))
c(("Does governance apply to every state change?",
   "No, it applies to consequential state transitions where human judgment is required. For those, the custodial decision must be represented in the CSL."))
c(("What does the notation A_H stand for?",
   "A_H is the bounded axiom set designated as the established human cognitive architecture for computational instantiation in the applicable system, A_H = {A₁, …, Aₙ} with 4 ≤ n ≤ 8."))
c(("What are the three forms of human participation the paper distinguishes?",
   "Substantive human domain knowledge, human cognitive architecture established through the CCD, and qualified human custodial governance."))
c(("Who wrote the paper and when?",
   "Michael Aaron Russell, dated October 1, 2026, with affiliations including Universal Standard Axiom Corporation R&D Division, IVS, and FAITH."))
c(("What does it mean that Human Participation ≠ Human-Guided Architecture?",
   "Participation, such as prompting, reviewing, or approving, is an activity. Human-guided architecture requires the human cognitive contribution to be structurally represented, so participation alone isn't enough."))
c(("Why use a ledger instead of just logs of human approvals?",
   "The paper uses the CSL as a state-bearing substrate that holds the cognitive architecture, provenance, refinement history, decisions, and the cognitive signature together, so human guidance is a representable property of the state, not merely recorded events."))
c(("What does R³ take as input and produce?",
   "It takes the established human cognitive architecture A_H and produces a refined computational intelligence structure, written R³(A_H) → I_refined."))
c(("Is the human governance part separate from the axiom formation part?",
   "They are distinct but connected. Formation happens through the CCD, while governance is a separate dimension that requires qualified custodial decisions for consequential transitions. Both are part of the human-guided property."))
c(("What does the Σ_H ≠ σ_H distinction protect against?",
   "It prevents conflating a cryptographic stamp on a recorded state with the structural expression of human cognitive architecture. A valid signature on the CSL authenticates it, but doesn't by itself show the human architecture is represented."))
c(("What are examples of things the cognitive signature can show up in?",
   "How axioms are selected and organized, semantic distinctions, refinement relationships, proposition relationships, verification pathways, obligations, and state structures."))
c(("How do multiple domains relate to each other under this framework?",
   "Each domain D₁…Dₘ gets its own bounded axiom set, but they share the same architectural substrate of CCD, R³, CSL, and custodial governance, so the meaning of human guidance stays consistent."))
c(("Why does the paper distinguish computational intelligence from human-guided intelligence?",
   "Because an intelligence system can analyze, refine, formalize, and verify without that making it human-guided. The defining human contribution is the distinguishable human cognitive architecture plus the custodial governance relationship."))
c(("What would be a good one-line test for whether a system is human-guided?",
   "Ask whether you can point to a bounded human cognitive architecture, instantiated computationally, visibly represented in the state, and under defined human governance. If you can only point to humans being involved, it doesn't meet the definition."))

assert len(D) == 62, len(D)
OUT = Path(__file__).resolve().parent.parent / "data" / "hgsi_ccd_conversations.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w') as f:
    for conv in D:
        msgs = [{"role": "system", "content": SYS}]
        for u, a in conv:
            msgs += [{"role": "user", "content": u}, {"role": "assistant", "content": a}]
        f.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
print("rows:", len(D), "| multi-turn:", sum(len(x) > 1 for x in D))
